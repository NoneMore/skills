from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "blueprint.py"
spec = importlib.util.spec_from_file_location("blueprint_tool", MODULE)
assert spec and spec.loader
bp = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = bp
spec.loader.exec_module(bp)


class Obj:
    def __init__(self, *, name="node", thm=None, parent=None, attrs=None, userdata=None, order=0, line=1):
        self.nodeName = name
        if thm is not None:
            self.thmName = thm
        self.parentNode = parent
        self.attributes = attrs or {}
        self.userdata = userdata or {}
        self._bp_order = order
        self._bp_file = "blueprint/src/content.tex"
        self._bp_line = line


class Context:
    def __init__(self, labels):
        self.labels = labels


class Document:
    def __init__(self, by_tag, labels):
        self.by_tag = by_tag
        self.context = Context(labels)

    def getElementsByTagName(self, tag):
        return list(self.by_tag.get(tag, []))


def command(name, owner, values=(), line=1):
    attrs = {}
    if name == "uses":
        attrs["labels"] = list(values)
    elif name == "lean":
        attrs["decls"] = list(values)
    elif name in ("proves", "label"):
        attrs["label"] = values[0] if values else ""
    return Obj(name=name, parent=owner, attrs=attrs, line=line)


def analysis(*, nodes, proofs=(), edges=(), proof_edges=(), commands=(), labels=None, assignments=()):
    by_tag = {}
    for item in commands:
        by_tag.setdefault(item.nodeName, []).append(item)
    by_tag["proof"] = list(proofs)
    doc = Document(by_tag, labels or {})
    return bp.Analysis(
        Path("/repo"),
        Path("/repo/blueprint/src/web.tex"),
        doc,
        set(nodes),
        list(proofs),
        set(edges),
        set(proof_edges),
        list(assignments),
    )


class BlueprintToolTests(unittest.TestCase):
    def test_valid_state_keeps_statement_and_proof_dependencies_separate(self):
        dep_s = Obj(thm="lemma", userdata={"leanok": True}, order=1, line=2)
        dep_p = Obj(thm="lemma", userdata={"leanok": True}, order=2, line=5)
        target = Obj(thm="theorem", userdata={"leandecls": ["Demo.main"]}, order=3, line=8)
        proof = Obj(name="proof", userdata={"proves": target, "leanok": True}, order=4, line=12)
        cmds = [
            command("uses", target, ["lem:statement"], 9),
            command("lean", target, ["Demo.main"], 10),
            command("uses", proof, ["lem:proof"], 13),
            command("leanok", proof, line=14),
        ]
        a = analysis(
            nodes=[dep_s, dep_p, target], proofs=[proof],
            edges=[(dep_s, target)], proof_edges=[(dep_p, target)],
            commands=cmds,
            labels={"lem:statement": dep_s, "lem:proof": dep_p, "thm:main": target},
            assignments=[("lem:statement", dep_s), ("lem:proof", dep_p), ("thm:main", target)],
        )
        self.assertEqual(bp.validate(a), [])
        state = bp.normalize(a)
        node = next(item for item in state["nodes"] if item["label"] == "thm:main")
        self.assertEqual(node["statement"]["uses"], ["lem:statement"])
        self.assertEqual(node["proof"]["uses"], ["lem:proof"])
        self.assertEqual(node["statement"]["lean"], ["Demo.main"])

    def test_repeated_uses_is_error_because_upstream_is_single_valued(self):
        dep = Obj(thm="lemma", order=1)
        target = Obj(thm="theorem", order=2)
        a = analysis(
            nodes=[dep, target],
            commands=[command("uses", target, ["lem:a"], 3), command("uses", target, ["lem:a"], 4)],
            labels={"lem:a": dep, "thm:t": target},
            assignments=[("lem:a", dep), ("thm:t", target)],
            edges=[(dep, target)],
        )
        self.assertIn("multiple-value-macro", {item.code for item in bp.validate(a)})

    def test_duplicate_label_across_nodes_is_error_but_aliases_are_allowed(self):
        a_node = Obj(thm="lemma", order=1)
        b_node = Obj(thm="lemma", order=2)
        ok = analysis(nodes=[a_node], labels={"a": a_node}, assignments=[("a", a_node), ("alias", a_node)])
        self.assertNotIn("duplicate-label", {item.code for item in bp.validate(ok)})
        bad = analysis(nodes=[a_node, b_node], labels={"a": b_node}, assignments=[("a", a_node), ("a", b_node)])
        self.assertIn("duplicate-label", {item.code for item in bp.validate(bad)})

    def test_unresolved_reference_is_error(self):
        target = Obj(thm="theorem", order=1)
        a = analysis(nodes=[target], commands=[command("uses", target, ["lem:missing"], 3)], assignments=[("thm:t", target)])
        self.assertIn("unresolved-reference", {item.code for item in bp.validate(a)})

    def test_cycle_and_conflicting_status_are_errors(self):
        a_node = Obj(thm="lemma", userdata={"notready": True, "leanok": True}, order=1)
        b_node = Obj(thm="lemma", order=2)
        cmds = [command("uses", a_node, ["b"], 3), command("uses", b_node, ["a"], 4)]
        a = analysis(
            nodes=[a_node, b_node], commands=cmds,
            labels={"a": a_node, "b": b_node}, assignments=[("a", a_node), ("b", b_node)],
            edges=[(b_node, a_node), (a_node, b_node)],
        )
        codes = {item.code for item in bp.validate(a)}
        self.assertIn("dependency-cycle", codes)
        self.assertIn("conflicting-status", codes)

    @unittest.skipUnless(
        all(importlib.util.find_spec(name) is not None for name in ("plasTeX", "leanblueprint", "plastexdepgraph", "pygraphviz")),
        "leanblueprint runtime is not installed",
    )
    def test_controlled_parse_integration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "blueprint" / "src"
            src.mkdir(parents=True)
            (src / "plastex.cfg").write_text(
                "[general]\nrenderer=HTML5\nplugins=plastexdepgraph leanblueprint\n\n[files]\ndirectory=../web/\n",
                encoding="utf-8",
            )
            (src / "web.tex").write_text(
                r"""\documentclass{article}
\usepackage{amsthm}
\usepackage{blueprint}
\newtheorem{lemma}{Lemma}
\begin{document}
\begin{lemma}\label{lem:a}A.\end{lemma}
\begin{lemma}\label{lem:b}\uses{lem:a}B.\end{lemma}
\end{document}
""",
                encoding="utf-8",
            )
            parsed = bp.parse_project(root)
            self.assertEqual(bp.validate(parsed), [])
            state = bp.normalize(parsed)
            by_label = {item["label"]: item for item in state["nodes"]}
            self.assertEqual(by_label["lem:b"]["statement"]["uses"], ["lem:a"])

    def test_diff_reports_structural_changes(self):
        before = {"schema_version": 1, "document": {"entrypoint": "x"}, "nodes": [{
            "label": "thm:a", "kind": "theorem", "title": None,
            "source": {"file": "a.tex", "line": 1},
            "statement": {"uses": [], "lean": [], "leanok": False, "mathlibok": False, "notready": False},
            "proof": None,
        }]}
        after = json.loads(json.dumps(before))
        after["nodes"][0]["statement"]["leanok"] = True
        payload = bp.diff_states(before, after)
        self.assertEqual(len(payload["changed"]), 1)
        self.assertIn("statement", payload["changed"][0]["changes"])


if __name__ == "__main__":
    unittest.main()
