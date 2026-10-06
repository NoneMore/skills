"""Deterministic helper for canonical game-logic project knowledge stores.

Paths carry analysis/target scope. The manifest carries content identity,
provenance, and graph relationships. Python 3.8+; standard library only.
"""

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
FINDING_ID_RE = re.compile(r"^- ID:\s*`([^`]+)`\s*$")
EVIDENCE_REF_RE = re.compile(r"^- `([^`]+)`:\s*(.*)$")
HEX64_RE = re.compile(r"^[0-9A-Fa-f]{64}$")
FINDING_STATUSES = {"confirmed", "working-hypothesis", "unknown", "superseded"}
ARTIFACT_STATUSES = {"active", "superseded"}
ANALYSES = "analyses"
TARGETS = "targets"
SHARED_ARTIFACTS = Path("shared") / "artifacts"


class StoreError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def atomic_json(path: Path, value: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def atomic_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(value, encoding="utf-8")
    temp.replace(path)


def manifest_path(root: Path) -> Path:
    return root / "artifacts" / "manifest.json"


def analysis_dir(root: Path, analysis_id: str) -> Path:
    return root / ANALYSES / analysis_id


def target_dir(root: Path, analysis_id: str, target_id: str) -> Path:
    return analysis_dir(root, analysis_id) / TARGETS / target_id


def finding_path(root: Path, analysis_id: str, target_id: str) -> Path:
    return target_dir(root, analysis_id, target_id) / "finding.md"


def require_id(value: str, label: str) -> None:
    if not ID_RE.fullmatch(value):
        raise StoreError("%s must be lowercase and filesystem-safe: %r" % (label, value))


def local_name(value: str) -> str:
    if not value or Path(value).name != value or value in (".", ".."):
        raise StoreError("local name must be one sibling filename: %r" % value)
    return value


def read_object(path: Path, label: str) -> Dict[str, object]:
    if not path.is_file():
        raise StoreError("%s not found: %s" % (label, path))
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StoreError("invalid %s JSON: %s" % (label, exc))
    if not isinstance(value, dict):
        raise StoreError("%s must be a JSON object" % label)
    return value


def load_manifest(root: Path) -> Dict[str, object]:
    return read_object(manifest_path(root), "manifest")


def records(manifest: Dict[str, object], key: str) -> List[Dict[str, object]]:
    value = manifest.get(key)
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise StoreError("manifest.%s must be an array of objects" % key)
    return value  # type: ignore[return-value]


def confined(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or any(part == ".." for part in rel.parts):
        raise StoreError("project path must be relative and confined: %s" % relative)
    candidate = (root / rel).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        raise StoreError("project path escapes root: %s" % relative)
    return candidate


def scope_target(root: Path, analysis_id: str, target_id: str) -> Dict[str, object]:
    require_id(analysis_id, "analysis id")
    require_id(target_id, "target id")
    path = target_dir(root, analysis_id, target_id) / "target.json"
    target = read_object(path, "target metadata")
    if target.get("id") != target_id:
        raise StoreError("target metadata id does not match directory: %s" % target_id)
    for key in ("game_version", "build_id", "platform", "distribution", "module", "module_sha256"):
        if not isinstance(target.get(key), str) or not target.get(key):
            raise StoreError("target metadata %s must be a non-empty string" % key)
    return target


def evidence_token(token: str) -> Tuple[str, str]:
    if token.startswith("source:"):
        return "source", token[7:]
    if token.startswith("artifact:"):
        return "artifact", token[9:]
    return "artifact", token


def ref_locator(value: str, label: str) -> Tuple[str, str]:
    if "=" not in value:
        raise StoreError("%s must use ID=LOCATOR syntax" % label)
    evidence_id, locator = value.split("=", 1)
    require_id(evidence_id, label + " id")
    if not locator.strip():
        raise StoreError("%s locator must be non-empty" % label)
    return evidence_id, locator


def parse_finding(root: Path, path: Path) -> Tuple[Optional[str], Set[Tuple[str, str]], List[str]]:
    finding_id: Optional[str] = None
    cited: Set[Tuple[str, str]] = set()
    errors: List[str] = []
    in_evidence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FINDING_ID_RE.match(line)
        if match and finding_id is None:
            finding_id = match.group(1)
        if line.startswith("## "):
            in_evidence = line.strip() == "## Evidence"
            continue
        if in_evidence:
            match = EVIDENCE_REF_RE.match(line)
            if match:
                kind, evidence_id = evidence_token(match.group(1))
                if ID_RE.fullmatch(evidence_id):
                    cited.add((kind, evidence_id))
                else:
                    errors.append("invalid evidence ref %r in %s" % (match.group(1), path.relative_to(root)))
    if finding_id is None:
        errors.append("finding missing '- ID: `...`': %s" % path.relative_to(root))
    elif not ID_RE.fullmatch(finding_id):
        errors.append("invalid finding id %r in %s" % (finding_id, path.relative_to(root)))
    return finding_id, cited, errors


def parse_findings(root: Path) -> Tuple[Dict[str, Path], Dict[str, Set[Tuple[str, str]]], List[str]]:
    ids: Dict[str, Path] = {}
    evidence: Dict[str, Set[Tuple[str, str]]] = {}
    errors: List[str] = []
    analyses = root / ANALYSES
    if not analyses.exists():
        return ids, evidence, errors

    paths = sorted(analyses.glob("*/targets/*/finding.md"))
    canonical = {path.resolve() for path in paths}
    for path in sorted(analyses.rglob("finding.md")):
        if path.resolve() not in canonical:
            errors.append("finding outside canonical target scope: %s" % path.relative_to(root))

    for path in paths:
        finding_id, cited, file_errors = parse_finding(root, path)
        errors.extend(file_errors)
        if finding_id is None or not ID_RE.fullmatch(finding_id):
            continue
        if finding_id in ids:
            errors.append(
                "duplicate finding id %s in %s and %s"
                % (finding_id, ids[finding_id].relative_to(root), path.relative_to(root))
            )
            continue
        ids[finding_id] = path
        evidence[finding_id] = cited
    return ids, evidence, errors


def find_finding(root: Path, finding_id: str) -> Path:
    ids, _, errors = parse_findings(root)
    if errors:
        raise StoreError("findings must be repaired first: " + "; ".join(errors))
    if finding_id not in ids:
        raise StoreError("finding id not found: %s" % finding_id)
    return ids[finding_id]


def upsert_evidence(path: Path, kind: str, evidence_id: str, locator: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("## Evidence")
    except ValueError:
        raise StoreError("finding has no '## Evidence' section: %s" % path)

    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    replacement = "- `%s:%s`: %s" % (kind, evidence_id, locator)
    existing: Optional[int] = None
    independent: Optional[int] = None
    for i in range(start + 1, end):
        if lines[i].startswith("- Independent check:") and independent is None:
            independent = i
        match = EVIDENCE_REF_RE.match(lines[i])
        if match and evidence_token(match.group(1)) == (kind, evidence_id):
            existing = i
            break

    if existing is not None:
        lines[existing] = replacement
    else:
        insert_at = independent if independent is not None else end
        while insert_at > start + 1 and lines[insert_at - 1] == "":
            insert_at -= 1
        lines.insert(insert_at, replacement)
    atomic_text(path, "\n".join(lines).rstrip() + "\n")


def link_evidence(root: Path, manifest: Dict[str, object], finding_id: str,
                  kind: str, evidence_id: str, locator: str) -> None:
    require_id(finding_id, "finding id")
    require_id(evidence_id, "%s id" % kind)
    path = find_finding(root, finding_id)
    items = records(manifest, "sources" if kind == "source" else "artifacts")
    item = next((entry for entry in items if entry.get("id") == evidence_id), None)
    if item is None:
        raise StoreError("%s id not found: %s" % (kind, evidence_id))
    refs = item.get("finding_refs")
    if not isinstance(refs, list):
        raise StoreError("%s %s finding_refs is not an array" % (kind, evidence_id))
    if finding_id not in refs:
        refs.append(finding_id)
    upsert_evidence(path, kind, evidence_id, locator)


def artifact_scope(path: str) -> Optional[Tuple[str, str]]:
    parts = Path(path).parts
    if len(parts) != 6 or parts[0] != ANALYSES or parts[2] != TARGETS or parts[4] != "artifacts":
        return None
    if not ID_RE.fullmatch(parts[1]) or not ID_RE.fullmatch(parts[3]):
        return None
    return parts[1], parts[3]


def validate_store(root: Path, manifest: Dict[str, object], verify_files: bool) -> List[str]:
    errors: List[str] = []
    if manifest.get("schema_version") != 3:
        errors.append("schema_version must equal 3")
    if not isinstance(manifest.get("project"), str) or not manifest.get("project"):
        errors.append("project must be a non-empty string")

    try:
        sources = records(manifest, "sources")
        artifacts = records(manifest, "artifacts")
    except StoreError as exc:
        return errors + [str(exc)]

    source_ids: Set[str] = set()
    source_paths: Set[str] = set()
    for item in sources:
        source_id = item.get("id")
        label = "source %r" % source_id
        if not isinstance(source_id, str) or not ID_RE.fullmatch(source_id):
            errors.append("invalid source id: %r" % source_id)
        elif source_id in source_ids:
            errors.append("duplicate source id: %s" % source_id)
        else:
            source_ids.add(source_id)
        path = item.get("path")
        if not isinstance(path, str) or not path:
            errors.append("%s has invalid path" % label)
            continue
        if path in source_paths:
            errors.append("duplicate source path: %s" % path)
        source_paths.add(path)
        if not isinstance(item.get("finding_refs"), list):
            errors.append("%s finding_refs must be an array" % label)
        if not isinstance(item.get("size"), int):
            errors.append("%s has invalid size" % label)
        digest = item.get("sha256")
        if not isinstance(digest, str) or not HEX64_RE.fullmatch(digest):
            errors.append("%s has invalid sha256" % label)
        if verify_files:
            full = Path(path).expanduser().resolve()
            if not full.is_file():
                errors.append("source file missing: %s" % path)
            else:
                if item.get("size") != full.stat().st_size:
                    errors.append("%s size mismatch" % label)
                if isinstance(digest, str) and digest.upper() != sha256_file(full):
                    errors.append("%s sha256 mismatch" % label)

    artifact_ids: Set[str] = set()
    artifact_paths: Set[str] = set()
    for item in artifacts:
        artifact_id = item.get("id")
        label = "artifact %r" % artifact_id
        if not isinstance(artifact_id, str) or not ID_RE.fullmatch(artifact_id):
            errors.append("invalid artifact id: %r" % artifact_id)
        elif artifact_id in artifact_ids:
            errors.append("duplicate artifact id: %s" % artifact_id)
        else:
            artifact_ids.add(artifact_id)

        relative = item.get("path")
        if not isinstance(relative, str) or not relative:
            errors.append("%s has invalid path" % label)
            continue
        if relative in artifact_paths:
            errors.append("duplicate artifact path: %s" % relative)
        artifact_paths.add(relative)
        scope = artifact_scope(relative)
        shared = len(Path(relative).parts) == 3 and Path(relative).parts[:2] == ("shared", "artifacts")
        if scope is None and not shared:
            errors.append("%s must use a target or shared artifact path" % label)
        if scope is not None:
            try:
                scope_target(root, *scope)
            except StoreError as exc:
                errors.append(str(exc))

        try:
            full = confined(root, relative)
        except StoreError as exc:
            errors.append(str(exc))
            continue

        status = item.get("status")
        if status not in ARTIFACT_STATUSES:
            errors.append("%s has invalid status: %r" % (label, status))
        successor = item.get("superseded_by")
        if status == "superseded" and not isinstance(successor, str):
            errors.append("superseded %s must name superseded_by" % label)
        if status != "superseded" and successor is not None:
            errors.append("%s has superseded_by while active" % label)
        for field in ("derived_from", "source_refs", "finding_refs", "consumes_finding_refs"):
            value = item.get(field)
            if not isinstance(value, list) or any(not isinstance(ref, str) for ref in value):
                errors.append("%s %s must be an array of strings" % (label, field))
        if not isinstance(item.get("size"), int):
            errors.append("%s has invalid size" % label)
        digest = item.get("sha256")
        if not isinstance(digest, str) or not HEX64_RE.fullmatch(digest):
            errors.append("%s has invalid sha256" % label)
        if verify_files:
            if not full.is_file():
                errors.append("artifact file missing: %s" % relative)
            else:
                if item.get("size") != full.stat().st_size:
                    errors.append("%s size mismatch" % label)
                if isinstance(digest, str) and digest.upper() != sha256_file(full):
                    errors.append("%s sha256 mismatch" % label)

    for item in artifacts:
        artifact_id = str(item.get("id"))
        successor = item.get("superseded_by")
        if isinstance(successor, str) and successor not in artifact_ids:
            errors.append("artifact %s superseded_by unknown artifact %s" % (artifact_id, successor))
        for ref in item.get("derived_from", []):
            if isinstance(ref, str) and ref not in artifact_ids:
                errors.append("artifact %s derived_from unknown artifact %s" % (artifact_id, ref))
        for ref in item.get("source_refs", []):
            if isinstance(ref, str) and ref not in source_ids:
                errors.append("artifact %s source_refs unknown source %s" % (artifact_id, ref))

    analyses = root / ANALYSES
    if not analyses.is_dir():
        errors.append("analyses directory is missing")
    else:
        for a_dir in sorted(path for path in analyses.iterdir() if path.is_dir()):
            if not ID_RE.fullmatch(a_dir.name):
                errors.append("invalid analysis id in path: %s" % a_dir.name)
                continue
            targets = a_dir / TARGETS
            if not targets.exists():
                continue
            for t_dir in sorted(path for path in targets.iterdir() if path.is_dir()):
                try:
                    scope_target(root, a_dir.name, t_dir.name)
                except StoreError as exc:
                    errors.append(str(exc))

    errors.extend(parse_findings(root)[2])
    return errors


def check_links(root: Path, manifest: Dict[str, object]) -> List[str]:
    errors: List[str] = []
    finding_ids, evidence, finding_errors = parse_findings(root)
    errors.extend(finding_errors)
    maps = {
        "artifact": {str(x.get("id")): x for x in records(manifest, "artifacts") if isinstance(x.get("id"), str)},
        "source": {str(x.get("id")): x for x in records(manifest, "sources") if isinstance(x.get("id"), str)},
    }

    for kind, mapping in maps.items():
        for evidence_id, item in mapping.items():
            refs = item.get("finding_refs", [])
            if not isinstance(refs, list):
                continue
            for finding_id in refs:
                if finding_id not in finding_ids:
                    errors.append("%s %s references missing finding %s" % (kind, evidence_id, finding_id))
                elif (kind, evidence_id) not in evidence.get(finding_id, set()):
                    errors.append("%s %s -> finding %s is not reciprocal" % (kind, evidence_id, finding_id))

    for finding_id, refs in evidence.items():
        for kind, evidence_id in refs:
            item = maps[kind].get(evidence_id)
            if item is None:
                errors.append("finding %s cites unknown %s %s" % (finding_id, kind, evidence_id))
            elif finding_id not in item.get("finding_refs", []):
                errors.append("finding %s -> %s %s is not reciprocal" % (finding_id, kind, evidence_id))

    for artifact_id, item in maps["artifact"].items():
        refs = item.get("consumes_finding_refs", [])
        if not isinstance(refs, list):
            continue
        for finding_id in refs:
            if finding_id not in finding_ids:
                errors.append("artifact %s consumes missing finding %s" % (artifact_id, finding_id))
            elif ("artifact", artifact_id) in evidence.get(finding_id, set()):
                errors.append("artifact %s both evidences and consumes finding %s" % (artifact_id, finding_id))
    return errors


def report(errors: Iterable[str]) -> int:
    items = list(errors)
    if not items:
        print("OK")
        return 0
    for item in items:
        print("ERROR: %s" % item)
    print("FAILED: %d error(s)" % len(items))
    return 1


def cmd_init(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    require_id(args.project, "project")
    path = manifest_path(root)
    if path.exists() and not args.force:
        raise StoreError("manifest already exists; use --force only for an intentional reset")
    (root / "artifacts").mkdir(parents=True, exist_ok=True)
    (root / ANALYSES).mkdir(parents=True, exist_ok=True)
    (root / SHARED_ARTIFACTS).mkdir(parents=True, exist_ok=True)
    atomic_json(path, {"schema_version": 3, "project": args.project, "sources": [], "artifacts": []})
    print("initialized %s" % path)
    return 0


def cmd_init_target(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    load_manifest(root)
    require_id(args.analysis_id, "analysis id")
    require_id(args.target_id, "target id")
    directory = target_dir(root, args.analysis_id, args.target_id)
    metadata = directory / "target.json"
    if metadata.exists() and not args.force:
        raise StoreError("target already exists: %s/%s" % (args.analysis_id, args.target_id))
    for role in ("artifacts", "reports", "scripts"):
        (directory / role).mkdir(parents=True, exist_ok=True)
    digest = args.module_sha256.upper() if HEX64_RE.fullmatch(args.module_sha256) else args.module_sha256
    atomic_json(metadata, {
        "id": args.target_id,
        "game_version": args.game_version,
        "build_id": args.build_id,
        "platform": args.platform,
        "distribution": args.distribution,
        "module": args.module,
        "module_sha256": digest,
    })
    print("initialized target %s/%s" % (args.analysis_id, args.target_id))
    return 0


def cmd_register_source(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    errors = validate_store(root, manifest, False)
    if errors:
        raise StoreError("store must be repaired first: " + "; ".join(errors))
    require_id(args.id, "source id")
    full = Path(args.path).expanduser().resolve()
    if not full.is_file():
        raise StoreError("source file not found: %s" % full)
    sources = records(manifest, "sources")
    stored_path = str(full)
    if any(item.get("id") == args.id for item in sources):
        raise StoreError("source id already exists: %s" % args.id)
    if any(item.get("path") == stored_path for item in sources):
        raise StoreError("source path already exists: %s" % stored_path)
    sources.append({
        "id": args.id,
        "path": stored_path,
        "kind": args.kind,
        "description": args.description,
        "size": full.stat().st_size,
        "sha256": sha256_file(full),
        "finding_refs": [],
    })
    atomic_json(manifest_path(root), manifest)
    print("registered source %s" % args.id)
    return 0


def cmd_add_artifact(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    require_id(args.id, "artifact id")
    if args.shared:
        if args.analysis_id or args.target_id:
            raise StoreError("--shared cannot be combined with target scope")
        relative = str(SHARED_ARTIFACTS / local_name(args.local_name))
    else:
        if not args.analysis_id or not args.target_id:
            raise StoreError("add-artifact requires target scope or --shared")
        scope_target(root, args.analysis_id, args.target_id)
        relative = str(
            Path(ANALYSES) / args.analysis_id / TARGETS / args.target_id
            / "artifacts" / local_name(args.local_name)
        )
    full = confined(root, relative)
    if not full.is_file():
        raise StoreError("artifact file not found: %s" % full)

    errors = validate_store(root, manifest, False)
    if errors:
        raise StoreError("store must be repaired first: " + "; ".join(errors))
    artifacts = records(manifest, "artifacts")
    if any(item.get("id") == args.id for item in artifacts):
        raise StoreError("artifact id already exists: %s" % args.id)
    if any(item.get("path") == relative for item in artifacts):
        raise StoreError("artifact path already exists: %s" % relative)

    artifact_ids = {str(item.get("id")) for item in artifacts}
    source_ids = {str(item.get("id")) for item in records(manifest, "sources")}
    for ref in args.derived_from:
        if ref not in artifact_ids:
            raise StoreError("derived_from artifact id not found: %s" % ref)
    for ref in args.source_ref:
        if ref not in source_ids:
            raise StoreError("source ref not found: %s" % ref)
    for finding_id in args.consumes_finding_ref:
        find_finding(root, finding_id)

    entry: Dict[str, object] = {
        "id": args.id,
        "path": relative,
        "kind": args.kind,
        "description": args.description,
        "size": full.stat().st_size,
        "sha256": sha256_file(full),
        "producer": {"tool": args.tool, "version": args.tool_version},
        "rva_or_range": args.rva_or_range,
        "derived_from": list(args.derived_from),
        "source_refs": list(args.source_ref),
        "finding_refs": [],
        "consumes_finding_refs": list(args.consumes_finding_ref),
        "status": "active",
        "superseded_by": None,
    }
    artifacts.append(entry)
    for finding_id in args.finding_ref:
        link_evidence(root, manifest, finding_id, "artifact", args.id, "registered artifact")
    atomic_json(manifest_path(root), manifest)
    print("added artifact %s" % args.id)
    return 0


def finding_text(args: argparse.Namespace) -> str:
    return (
        "# %s\n\n"
        "- ID: `%s`\n"
        "- Status: `%s`\n"
        "- Supersedes: %s\n"
        "- Superseded by: none\n\n"
        "## Claim\n\n%s\n\n"
        "## Evidence\n\n- Independent check: %s\n\n"
        "## Reusable detail\n\n%s\n\n"
        "## Dependencies\n\n%s\n\n"
        "## Validation and limitations\n\n%s\n"
        % (
            args.title, args.id, args.status, args.supersedes, args.claim,
            args.independent_check, args.reusable_detail, args.dependencies,
            args.limitations,
        )
    )


def cmd_add_finding(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    errors = validate_store(root, manifest, False)
    if errors:
        raise StoreError("store must be repaired first: " + "; ".join(errors))
    require_id(args.id, "finding id")
    scope_target(root, args.analysis_id, args.target_id)
    if args.id in parse_findings(root)[0]:
        raise StoreError("finding id already exists: %s" % args.id)
    path = finding_path(root, args.analysis_id, args.target_id)
    if path.exists():
        raise StoreError("target already has a primary finding: %s" % path.relative_to(root))
    atomic_text(path, finding_text(args))
    try:
        for spec in args.source_ref:
            evidence_id, locator = ref_locator(spec, "source ref")
            link_evidence(root, manifest, args.id, "source", evidence_id, locator)
        for spec in args.artifact_ref:
            evidence_id, locator = ref_locator(spec, "artifact ref")
            link_evidence(root, manifest, args.id, "artifact", evidence_id, locator)
    except Exception:
        path.unlink(missing_ok=True)
        raise
    atomic_json(manifest_path(root), manifest)
    print("added finding %s" % args.id)
    return 0


def cmd_link(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    errors = validate_store(root, manifest, False)
    if errors:
        raise StoreError("store must be repaired first: " + "; ".join(errors))
    kind, evidence_id = ("source", args.source_id) if args.source_id else ("artifact", args.artifact_id)
    link_evidence(root, manifest, args.finding_id, kind, evidence_id, args.locator)
    atomic_json(manifest_path(root), manifest)
    print("linked %s:%s -> finding %s" % (kind, evidence_id, args.finding_id))
    return 0


def cmd_supersede(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    artifacts = records(manifest, "artifacts")
    by_id = {str(item.get("id")): item for item in artifacts if isinstance(item.get("id"), str)}
    if args.old_id == args.new_id or args.old_id not in by_id or args.new_id not in by_id:
        raise StoreError("supersede requires two distinct existing artifact IDs")
    by_id[args.old_id]["status"] = "superseded"
    by_id[args.old_id]["superseded_by"] = args.new_id
    atomic_json(manifest_path(root), manifest)
    print("superseded %s -> %s" % (args.old_id, args.new_id))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    return report(validate_store(root, load_manifest(root), True))


def cmd_check_links(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    return report(validate_store(root, manifest, False) + check_links(root, manifest))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage canonical game-logic project knowledge stores")
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("init")
    p.add_argument("--root", required=True)
    p.add_argument("--project", required=True)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("init-target")
    p.add_argument("--root", required=True)
    p.add_argument("--analysis-id", required=True)
    p.add_argument("--target-id", required=True)
    p.add_argument("--game-version", default="unknown")
    p.add_argument("--build-id", default="unknown")
    p.add_argument("--platform", default="unknown")
    p.add_argument("--distribution", default="unknown")
    p.add_argument("--module", default="unknown")
    p.add_argument("--module-sha256", default="unknown")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init_target)

    p = sub.add_parser("register-source")
    p.add_argument("--root", required=True)
    p.add_argument("--id", required=True)
    p.add_argument("--path", required=True)
    p.add_argument("--kind", default="source-file")
    p.add_argument("--description", required=True)
    p.set_defaults(func=cmd_register_source)

    p = sub.add_parser("add-artifact")
    p.add_argument("--root", required=True)
    p.add_argument("--id", required=True)
    p.add_argument("--analysis-id")
    p.add_argument("--target-id")
    p.add_argument("--local-name", required=True)
    p.add_argument("--shared", action="store_true")
    p.add_argument("--kind", required=True)
    p.add_argument("--description", required=True)
    p.add_argument("--tool", required=True)
    p.add_argument("--tool-version", default="unknown")
    p.add_argument("--rva-or-range", default="not-applicable")
    p.add_argument("--derived-from", action="append", default=[])
    p.add_argument("--source-ref", action="append", default=[])
    p.add_argument("--finding-ref", action="append", default=[])
    p.add_argument("--consumes-finding-ref", action="append", default=[])
    p.set_defaults(func=cmd_add_artifact)

    p = sub.add_parser("add-finding")
    p.add_argument("--root", required=True)
    p.add_argument("--analysis-id", required=True)
    p.add_argument("--target-id", required=True)
    p.add_argument("--id", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--status", default="working-hypothesis", choices=sorted(FINDING_STATUSES))
    p.add_argument("--supersedes", default="none")
    p.add_argument("--claim", required=True)
    p.add_argument("--independent-check", default="not yet established")
    p.add_argument("--reusable-detail", default="none")
    p.add_argument("--dependencies", default="none")
    p.add_argument("--limitations", default="not yet fully validated")
    p.add_argument("--source-ref", action="append", default=[], metavar="ID=LOCATOR")
    p.add_argument("--artifact-ref", action="append", default=[], metavar="ID=LOCATOR")
    p.set_defaults(func=cmd_add_finding)

    p = sub.add_parser("link")
    p.add_argument("--root", required=True)
    p.add_argument("--finding-id", required=True)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--source-id")
    group.add_argument("--artifact-id")
    p.add_argument("--locator", required=True)
    p.set_defaults(func=cmd_link)

    p = sub.add_parser("verify")
    p.add_argument("--root", required=True)
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("check-links")
    p.add_argument("--root", required=True)
    p.set_defaults(func=cmd_check_links)

    p = sub.add_parser("supersede")
    p.add_argument("--root", required=True)
    p.add_argument("--old-id", required=True)
    p.add_argument("--new-id", required=True)
    p.set_defaults(func=cmd_supersede)
    return parser


def run_self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="project-store-test-") as tmp:
        base = Path(tmp)
        root = base / "analysis"
        cmd_init(argparse.Namespace(root=str(root), project="sample-game", force=False))
        cmd_init_target(argparse.Namespace(
            root=str(root), analysis_id="reload-timing", target_id="build-1",
            game_version="1.0", build_id="1", platform="pc", distribution="test",
            module="game.exe", module_sha256="unknown", force=False,
        ))

        source = base / "game.exe"
        source.write_text("source\n", encoding="utf-8")
        cmd_register_source(argparse.Namespace(
            root=str(root), id="game-source", path=str(source),
            kind="binary", description="source",
        ))

        artifact = target_dir(root, "reload-timing", "build-1") / "artifacts" / "static.txt"
        artifact.write_text("evidence\n", encoding="utf-8")
        cmd_add_artifact(argparse.Namespace(
            root=str(root), id="reload-static", analysis_id="reload-timing",
            target_id="build-1", local_name="static.txt", shared=False, kind="test",
            description="test", tool="self-test", tool_version="1",
            rva_or_range="not-applicable", derived_from=[], source_ref=["game-source"],
            finding_ref=[], consumes_finding_ref=[],
        ))
        cmd_add_finding(argparse.Namespace(
            root=str(root), analysis_id="reload-timing", target_id="build-1",
            id="reload-result", title="Reload result", status="confirmed",
            supersedes="none", claim="Sample.", independent_check="self-test",
            reusable_detail="none", dependencies="none", limitations="none",
            source_ref=[], artifact_ref=["reload-static=line 1"],
        ))

        shared = root / SHARED_ARTIFACTS / "common.txt"
        shared.write_text("shared\n", encoding="utf-8")
        cmd_add_artifact(argparse.Namespace(
            root=str(root), id="shared-common", analysis_id=None, target_id=None,
            local_name="common.txt", shared=True, kind="test",
            description="shared", tool="self-test", tool_version="1",
            rva_or_range="not-applicable", derived_from=[], source_ref=[],
            finding_ref=["reload-result"], consumes_finding_ref=[],
        ))

        artifact_record = next(
            item for item in records(load_manifest(root), "artifacts")
            if item.get("id") == "reload-static"
        )
        if any(key in artifact_record for key in ("target", "analysis_id", "target_id")):
            raise AssertionError("path-derived scope was redundantly stored")
        if cmd_verify(argparse.Namespace(root=str(root))) or cmd_check_links(argparse.Namespace(root=str(root))):
            raise AssertionError("store verification failed")
    print("project_store self-test: OK")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.self_test:
        run_self_test()
        return 0
    if not hasattr(args, "func"):
        parser.print_help()
        return 2
    try:
        return args.func(args)
    except StoreError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
