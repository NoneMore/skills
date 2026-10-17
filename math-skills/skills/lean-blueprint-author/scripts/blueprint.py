#!/usr/bin/env python3
"""Read-only mechanical projection/check/diff tooling for leanblueprint projects."""

from __future__ import annotations

import argparse
import contextlib
import glob
import json
import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Sequence

SCHEMA_VERSION = 1
CALLBACK_CUTOFF = 110  # current upstream graph construction completes here


class ProviderError(RuntimeError):
    pass


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    file: str | None = None
    line: int | None = None
    subject: dict[str, Any] | None = None

    def json(self) -> dict[str, Any]:
        out: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.file is not None or self.line is not None:
            out["source"] = {"file": self.file, "line": self.line}
        if self.subject:
            out["subject"] = self.subject
        return out


@dataclass
class Analysis:
    root: Path
    entrypoint: Path
    document: Any
    nodes: set[Any]
    proofs: list[Any]
    statement_edges: set[tuple[Any, Any]]
    proof_edges: set[tuple[Any, Any]]
    label_assignments: list[tuple[str, Any]]


def _source(obj: Any) -> tuple[str | None, int | None]:
    return getattr(obj, "_bp_file", None), getattr(obj, "_bp_line", None)


def _order(obj: Any) -> int:
    return int(getattr(obj, "_bp_order", 10**12))


def _text(value: Any) -> str:
    if value is None:
        return ""
    return str(getattr(value, "textContent", value)).strip()


def _values(obj: Any, macro: str) -> list[str]:
    attrs = getattr(obj, "attributes", {})
    key = {"label": "label", "lean": "decls", "uses": "labels", "proves": "label"}.get(macro)
    if key is None:
        return []
    value = attrs.get(key)
    if value is None:
        return []
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    try:
        items = list(value)
    except TypeError:
        items = [value]
    return [text for item in items if (text := _text(item))]


def _rel(path: str | None, root: Path) -> str | None:
    if not path:
        return None
    p = Path(path)
    try:
        return p.resolve().relative_to(root.resolve()).as_posix()
    except (OSError, ValueError):
        return p.as_posix()


@contextlib.contextmanager
def _cwd(path: Path) -> Iterator[None]:
    old = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


@contextlib.contextmanager
def _instrument(root: Path) -> Iterator[list[tuple[str, Any]]]:
    try:
        from plasTeX import Macro
        from plasTeX.Context import Context
    except ImportError as exc:
        raise ProviderError("plasTeX is not installed") from exc

    old_invoke, old_label = Macro.invoke, Context.label
    assignments: list[tuple[str, Any]] = []
    counter = 0

    def invoke(self: Any, tex: Any) -> Any:
        nonlocal counter
        if getattr(self, "macroMode", None) != Macro.MODE_END and not hasattr(self, "_bp_order"):
            counter += 1
            self._bp_order = counter
            try:
                self._bp_file = _rel(tex.filename, root)
                self._bp_line = int(tex.lineNumber)
            except Exception:
                self._bp_file, self._bp_line = None, None
        return old_invoke(self, tex)

    def label(self: Any, name: str, node: Any = None) -> Any:
        target = node if node is not None else getattr(self, "currentlabel", None)
        if name and str(name).strip() and target is not None:
            assignments.append((str(name).strip(), target))
        return old_label(self, name, node)

    Macro.invoke, Context.label = invoke, label
    try:
        yield assignments
    finally:
        Macro.invoke, Context.label = old_invoke, old_label


def _config(path: Path) -> Any:
    try:
        from plasTeX.Config import defaultConfig
        from plasTeX.client import collect_renderer_config
    except ImportError as exc:
        raise ProviderError("plasTeX is not installed") from exc
    cfg = defaultConfig()
    collect_renderer_config(cfg)
    if path.is_file():
        cfg.read([str(path)])
    return cfg


def parse_project(root: Path, entrypoint: Path | None = None, config: Path | None = None) -> Analysis:
    """Drive upstream plasTeX only through graph construction; skip mutating status callbacks."""
    try:
        import plasTeX
        from plasTeX.TeX import TeX
    except ImportError as exc:
        raise ProviderError("plasTeX is not installed") from exc

    root = root.resolve()
    entrypoint = (entrypoint or root / "blueprint/src/web.tex").resolve()
    config = (config or entrypoint.parent / "plastex.cfg").resolve()
    if not entrypoint.is_file():
        raise ProviderError(f"entrypoint not found: {entrypoint}")

    with _cwd(entrypoint.parent):
        document = plasTeX.TeXDocument(config=_config(config))
        tex = TeX(document, file=entrypoint.name)
        tex.toplevel = False  # do not auto-run all post-parse callbacks
        document.userdata["jobname"] = tex.jobname
        document.userdata["working-dir"] = os.getcwd()

        renderer = document.config["general"]["renderer"]
        pauxname = f"{tex.jobname}.paux"
        for dirname in [os.getcwd()] + list(document.config["general"]["paux-dirs"]):
            for fname in glob.glob(os.path.join(dirname, "*.paux")):
                if os.path.basename(fname) != pauxname:
                    document.context.restore(fname, renderer)

        with _instrument(root) as labels:
            tex.parse()

        names = {
            getattr(cb, "__name__", "")
            for cbs in document.postParseCallbacks.values()
            for cb in cbs
        }
        if "make_lean_data" not in names:
            raise ProviderError("unsupported leanblueprint runtime: make_lean_data callback not found")

        for order in sorted(document.postParseCallbacks):
            if order <= CALLBACK_CUTOFF:
                for callback in list(document.postParseCallbacks[order]):
                    callback()

        graphs = document.userdata.get("dep_graph", {}).get("graphs")
        if not graphs:
            raise ProviderError("dependency graph was not produced before the analysis boundary")

        nodes: set[Any] = set()
        statement_edges: set[tuple[Any, Any]] = set()
        proof_edges: set[tuple[Any, Any]] = set()
        for graph in graphs.values():
            nodes.update(graph.nodes)
            statement_edges.update(graph.edges)
            proof_edges.update(graph.proof_edges)

        return Analysis(
            root,
            entrypoint,
            document,
            nodes,
            list(document.getElementsByTagName("proof")),
            statement_edges,
            proof_edges,
            list(labels),
        )


def _items(a: Analysis, macro: str) -> list[Any]:
    return list(a.document.getElementsByTagName(macro))


def _labels_by_node(a: Analysis) -> dict[Any, list[str]]:
    out: dict[Any, list[str]] = defaultdict(list)
    for label, target in a.label_assignments:
        if target in a.nodes and label not in out[target]:
            out[target].append(label)
    return out


def _primary_labels(a: Analysis) -> dict[Any, str | None]:
    labels = _labels_by_node(a)
    return {node: labels.get(node, [None])[0] for node in a.nodes}


def _name(a: Analysis, obj: Any) -> str:
    labels = _primary_labels(a)
    if obj in a.nodes:
        return labels[obj] or f"<unlabelled:{getattr(obj, 'thmName', obj.nodeName)}>"
    if obj in a.proofs:
        target = obj.userdata.get("proves")
        return f"proof of {_name(a, target)}" if target in a.nodes else "<unassociated proof>"
    return "<non-blueprint owner>"


def validate(a: Analysis) -> list[Diagnostic]:
    d: list[Diagnostic] = []

    # A repeated label on the same object is harmless; reuse across objects is not.
    assigned: dict[str, set[Any]] = defaultdict(set)
    for label, target in a.label_assignments:
        assigned[label].add(target)
    label_source = {v[0]: _source(item) for item in _items(a, "label") if (v := _values(item, "label"))}
    for label, targets in assigned.items():
        if len(targets) > 1:
            file, line = label_source.get(label, (None, None))
            d.append(Diagnostic("duplicate-label", f"label {label!r} is assigned to multiple objects", file, line, {"label": label}))

    # These macros are single-valued in upstream userdata; repetition silently overwrites.
    for macro in ("uses", "lean", "proves"):
        owners: dict[Any, list[Any]] = defaultdict(list)
        for item in _items(a, macro):
            owners[item.parentNode].append(item)
        for owner, items in owners.items():
            if len(items) > 1:
                file, line = _source(items[1])
                d.append(Diagnostic("multiple-value-macro", f"multiple \\{macro} occurrences share one owner", file, line, {"macro": macro, "owner": _name(a, owner)}))

    allowed = {
        "lean": lambda owner: owner in a.nodes,
        "uses": lambda owner: owner in a.nodes or owner in a.proofs,
        "leanok": lambda owner: owner in a.nodes or owner in a.proofs,
        "mathlibok": lambda owner: owner in a.nodes,
        "notready": lambda owner: owner in a.nodes,
        "proves": lambda owner: owner in a.proofs,
    }
    for macro, predicate in allowed.items():
        for item in _items(a, macro):
            if not predicate(item.parentNode):
                file, line = _source(item)
                d.append(Diagnostic("invalid-macro-owner", f"\\{macro} is not attached to an expected blueprint node/proof", file, line, {"macro": macro}))

    graph_targets = set(a.nodes)
    for macro in ("uses", "proves"):
        for item in _items(a, macro):
            for label in _values(item, macro):
                if label not in a.document.context.labels:
                    file, line = _source(item)
                    d.append(Diagnostic("unresolved-reference", f"\\{macro} references unknown label {label!r}", file, line, {"macro": macro, "label": label}))
                elif a.document.context.labels[label] not in graph_targets:
                    file, line = _source(item)
                    d.append(Diagnostic("invalid-reference-target", f"\\{macro} label {label!r} does not resolve to a dependency-graph node", file, line, {"macro": macro, "label": label}))

    # Proof metadata is meaningful only after upstream associates the proof.
    for proof in a.proofs:
        metadata = [item for macro in ("uses", "leanok") for item in _items(a, macro) if item.parentNode is proof]
        if metadata and proof.userdata.get("proves") not in a.nodes:
            file, line = _source(metadata[0])
            d.append(Diagnostic("unassociated-proof", "proof has blueprint metadata but no tracked statement target", file, line))

    by_target: dict[Any, list[Any]] = defaultdict(list)
    for proof in a.proofs:
        target = proof.userdata.get("proves")
        if target in a.nodes:
            by_target[target].append(proof)
    for target, proofs in by_target.items():
        if len(proofs) > 1:
            file, line = _source(proofs[1])
            d.append(Diagnostic("proof-association-conflict", f"multiple proofs are associated with {_name(a, target)}", file, line, {"target": _name(a, target)}))

    for node in a.nodes:
        if node.userdata.get("notready") and (node.userdata.get("leanok") or node.userdata.get("mathlibok")):
            file, line = _source(node)
            d.append(Diagnostic("conflicting-status", f"{_name(a, node)} is both notready and formalized", file, line, {"node": _name(a, node)}))

    edges = a.statement_edges | a.proof_edges
    for dep, target in edges:
        if dep is target:
            file, line = _source(target)
            d.append(Diagnostic("self-dependency", f"{_name(a, target)} depends on itself", file, line, {"node": _name(a, target)}))

    dependencies = {node: set() for node in a.nodes}
    for dep, target in edges:
        if dep in a.nodes and target in a.nodes:
            dependencies[target].add(dep)
    state, stack, reported = {node: 0 for node in a.nodes}, [], set()

    def visit(node: Any) -> None:
        state[node] = 1
        stack.append(node)
        for dep in dependencies[node]:
            if state[dep] == 0:
                visit(dep)
            elif state[dep] == 1:
                cycle = stack[stack.index(dep):] + [dep]
                key = frozenset(cycle)
                if key not in reported:
                    reported.add(key)
                    file, line = _source(node)
                    d.append(Diagnostic("dependency-cycle", "dependency cycle: " + " -> ".join(_name(a, x) for x in cycle), file, line))
        stack.pop()
        state[node] = 2

    for node in a.nodes:
        if state[node] == 0:
            visit(node)

    # With valid single-value references, raw \uses must agree with upstream edges.
    blockers = {"multiple-value-macro", "invalid-macro-owner", "unresolved-reference", "invalid-reference-target", "unassociated-proof", "proof-association-conflict"}
    if not any(item.code in blockers for item in d):
        expected_statement: set[tuple[Any, Any]] = set()
        expected_proof: set[tuple[Any, Any]] = set()
        for item in _items(a, "uses"):
            owner = item.parentNode
            targets = [a.document.context.labels[label] for label in _values(item, "uses")]
            if owner in a.nodes:
                expected_statement.update((dep, owner) for dep in targets)
            elif owner in a.proofs:
                target = owner.userdata.get("proves")
                expected_proof.update((dep, target) for dep in targets)
        if expected_statement != a.statement_edges or expected_proof != a.proof_edges:
            d.append(Diagnostic("projection-mismatch", "raw \\uses occurrences and upstream graph edges disagree"))

        for node in a.nodes:
            occurrences = [item for item in _items(a, "lean") if item.parentNode is node]
            raw = _values(occurrences[0], "lean") if occurrences else []
            stored = [str(x).strip() for x in node.userdata.get("leandecls", [])]
            if raw != stored:
                file, line = _source(node)
                d.append(Diagnostic("projection-mismatch", f"raw \\lean mapping and upstream mapping disagree for {_name(a, node)}", file, line))

    d.sort(key=lambda x: (x.file or "", x.line or 10**12, x.code, x.message))
    return d


def normalize(a: Analysis) -> dict[str, Any]:
    errors = validate(a)
    if errors:
        raise ValueError("cannot normalize an invalid projection")
    labels = _primary_labels(a)
    proof_for = {p.userdata.get("proves"): p for p in a.proofs if p.userdata.get("proves") in a.nodes}

    def deps(edges: set[tuple[Any, Any]], target: Any) -> list[str]:
        nodes = sorted((dep for dep, dst in edges if dst is target), key=lambda n: (_order(n), labels[n] or ""))
        return [labels[node] for node in nodes if labels[node] is not None]

    out = []
    for node in sorted(a.nodes, key=lambda n: (_order(n), labels[n] or "")):
        file, line = _source(node)
        proof = proof_for.get(node)
        proof_json = None
        if proof is not None:
            pfile, pline = _source(proof)
            proof_json = {"source": {"file": pfile, "line": pline}, "uses": deps(a.proof_edges, node), "leanok": bool(proof.userdata.get("leanok"))}
        title = _text(getattr(node, "attributes", {}).get("title")) or None
        out.append({
            "label": labels[node],
            "kind": str(getattr(node, "thmName", getattr(node, "nodeName", "node"))),
            "title": title,
            "source": {"file": file, "line": line},
            "statement": {
                "uses": deps(a.statement_edges, node),
                "lean": [str(x).strip() for x in node.userdata.get("leandecls", [])],
                "leanok": bool(node.userdata.get("leanok")),
                "mathlibok": bool(node.userdata.get("mathlibok")),
                "notready": bool(node.userdata.get("notready")),
            },
            "proof": proof_json,
        })
    return {"schema_version": SCHEMA_VERSION, "document": {"entrypoint": a.entrypoint.relative_to(a.root).as_posix()}, "nodes": out}


def _state(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION or not isinstance(data.get("nodes"), list):
        raise ProviderError(f"expected blueprint state schema_version={SCHEMA_VERSION}")
    return data


def _identity(node: dict[str, Any]) -> str:
    if node.get("label"):
        return f"label:{node['label']}"
    src = node.get("source") or {}
    return f"source:{src.get('file')}:{src.get('line')}:{node.get('kind')}"


def diff_states(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    old = {_identity(n): n for n in _state(before)["nodes"]}
    new = {_identity(n): n for n in _state(after)["nodes"]}
    changed = []
    for key in sorted(old.keys() & new.keys()):
        if old[key] != new[key]:
            fields = {field: {"before": old[key].get(field), "after": new[key].get(field)} for field in ("kind", "title", "source", "statement", "proof") if old[key].get(field) != new[key].get(field)}
            changed.append({"label": new[key].get("label"), "changes": fields})
    return {
        "schema_version": SCHEMA_VERSION,
        "added": [new[k] for k in sorted(new.keys() - old.keys())],
        "removed": [old[k] for k in sorted(old.keys() - new.keys())],
        "changed": changed,
    }


def _json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def _project_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--entrypoint", type=Path)
    parser.add_argument("--config", type=Path)


def _resolve(args: argparse.Namespace) -> tuple[Path, Path | None, Path | None]:
    root = args.project_root.resolve()
    entry = args.entrypoint if args.entrypoint is None or args.entrypoint.is_absolute() else root / args.entrypoint
    config = args.config if args.config is None or args.config.is_absolute() else root / args.config
    return root, entry, config


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only leanblueprint mechanical tooling; JSON output only.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "check"):
        _project_args(sub.add_parser(name))
    diff = sub.add_parser("diff")
    diff.add_argument("before", type=Path)
    diff.add_argument("after", type=Path)
    args = parser.parse_args(argv)

    if args.command == "diff":
        try:
            _json(diff_states(json.loads(args.before.read_text()), json.loads(args.after.read_text())))
            return 0
        except (OSError, json.JSONDecodeError, ProviderError) as exc:
            _json({"schema_version": SCHEMA_VERSION, "ok": False, "error": {"code": "provider-unavailable", "message": str(exc)}})
            return 2

    try:
        analysis = parse_project(*_resolve(args))
    except (ProviderError, OSError, RuntimeError, ImportError) as exc:
        _json({"schema_version": SCHEMA_VERSION, "ok": False, "error": {"code": "provider-unavailable", "message": str(exc)}})
        return 2

    errors = validate(analysis)
    if args.command == "check" or errors:
        _json({"schema_version": SCHEMA_VERSION, "ok": not errors, "diagnostics": [e.json() for e in errors]})
        return 0 if not errors else 1

    _json(normalize(analysis))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
