"""Deterministic helper for analyze-game-logic project knowledge stores.

The helper manages source registrations, retained artifacts, finding files, and
reciprocal evidence links. It never interprets game semantics and never modifies
analyzed source/binary targets. Python 3.8+; standard library only.
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
VALID_ARTIFACT_STATUSES = {"active", "superseded", "missing"}
VALID_SOURCE_STATUSES = {"active", "missing"}
VALID_FINDING_STATUSES = {"confirmed", "working-hypothesis", "unknown", "superseded"}


class StoreError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def atomic_write_json(path: Path, data: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(payload, encoding="utf-8")
    temp.replace(path)


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(text, encoding="utf-8")
    temp.replace(path)


def manifest_path(root: Path) -> Path:
    return root / "artifacts" / "manifest.json"


def load_manifest(root: Path) -> Dict[str, object]:
    path = manifest_path(root)
    if not path.is_file():
        raise StoreError("manifest not found: %s" % path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StoreError("invalid manifest JSON: %s" % exc)
    if not isinstance(data, dict):
        raise StoreError("manifest root must be a JSON object")
    return data


def require_id(value: str, label: str) -> None:
    if not ID_RE.fullmatch(value):
        raise StoreError("%s must be lowercase and filesystem-safe: %r" % (label, value))


def confined_path(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute():
        raise StoreError("artifact path must be relative: %s" % relative)
    if any(part == ".." for part in rel.parts):
        raise StoreError("artifact path must not contain '..': %s" % relative)
    root_resolved = root.resolve()
    candidate = (root / rel).resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError:
        raise StoreError("artifact path escapes analysis root: %s" % relative)
    return candidate


def resolve_source_path(stored_path: str) -> Path:
    return Path(stored_path).expanduser().resolve()


def artifacts_list(manifest: Dict[str, object]) -> List[Dict[str, object]]:
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise StoreError("manifest.artifacts must be an array")
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            raise StoreError("manifest.artifacts[%d] must be an object" % index)
    return artifacts  # type: ignore[return-value]


def sources_list(manifest: Dict[str, object]) -> List[Dict[str, object]]:
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        raise StoreError("manifest.sources must be an array")
    for index, item in enumerate(sources):
        if not isinstance(item, dict):
            raise StoreError("manifest.sources[%d] must be an object" % index)
    return sources  # type: ignore[return-value]


def ensure_schema_v2(manifest: Dict[str, object]) -> None:
    version = manifest.get("schema_version")
    if version == 1:
        manifest["schema_version"] = 2
        manifest.setdefault("sources", [])
    elif version == 2:
        manifest.setdefault("sources", [])
    else:
        raise StoreError("unsupported schema_version: %r" % version)


def validate_target(target: object, label: str, errors: List[str]) -> None:
    if not isinstance(target, dict):
        errors.append("%s target must be an object" % label)
        return
    for key in ("game_version", "build_id", "module", "module_sha256", "rva_or_range"):
        value = target.get(key)
        if not isinstance(value, str) or not value:
            errors.append("%s target.%s must be a non-empty string" % (label, key))


def validate_finding_refs(item: Dict[str, object], label: str, errors: List[str]) -> None:
    refs = item.get("finding_refs")
    if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs):
        errors.append("%s finding_refs must be an array of strings" % label)
    elif len(refs) != len(set(refs)):
        errors.append("%s finding_refs contains duplicates" % label)


def validate_manifest_shape(root: Path, manifest: Dict[str, object], verify_files: bool) -> List[str]:
    errors: List[str] = []
    schema = manifest.get("schema_version")
    if schema not in (1, 2):
        errors.append("schema_version must equal 1 or 2")
    if not isinstance(manifest.get("project"), str) or not manifest.get("project"):
        errors.append("project must be a non-empty string")

    try:
        artifacts = artifacts_list(manifest)
        sources = sources_list(manifest)
    except StoreError as exc:
        return errors + [str(exc)]

    if schema == 1 and "sources" in manifest and sources:
        errors.append("schema_version 1 must not contain registered sources; upgrade to schema_version 2")

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

        stored_path = item.get("path")
        if not isinstance(stored_path, str) or not stored_path:
            errors.append("%s has invalid path" % label)
            continue
        if stored_path in source_paths:
            errors.append("duplicate source path: %s" % stored_path)
        source_paths.add(stored_path)

        if item.get("status") not in VALID_SOURCE_STATUSES:
            errors.append("%s has invalid status: %r" % (label, item.get("status")))
        validate_finding_refs(item, label, errors)
        validate_target(item.get("target"), label, errors)

        stored_size = item.get("size")
        stored_hash = item.get("sha256")
        if not isinstance(stored_size, int) or stored_size < 0:
            errors.append("%s has invalid size" % label)
        if not isinstance(stored_hash, str) or not HEX64_RE.fullmatch(stored_hash):
            errors.append("%s has invalid sha256" % label)

        if verify_files:
            full = resolve_source_path(stored_path)
            if not full.is_file():
                if item.get("status") != "missing":
                    errors.append("source file missing: %s" % stored_path)
            else:
                actual_size = full.stat().st_size
                actual_hash = sha256_file(full)
                if isinstance(stored_size, int) and stored_size != actual_size:
                    errors.append("%s size mismatch: manifest=%s actual=%s" % (label, stored_size, actual_size))
                if isinstance(stored_hash, str) and stored_hash.upper() != actual_hash:
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
        try:
            full = confined_path(root, relative)
        except StoreError as exc:
            errors.append(str(exc))
            continue

        status = item.get("status")
        if status not in VALID_ARTIFACT_STATUSES:
            errors.append("%s has invalid status: %r" % (label, status))

        superseded_by = item.get("superseded_by")
        if status == "superseded" and not isinstance(superseded_by, str):
            errors.append("superseded %s must name superseded_by" % label)
        if status != "superseded" and superseded_by is not None:
            errors.append("%s has superseded_by but status is %r" % (label, status))

        validate_finding_refs(item, label, errors)
        validate_target(item.get("target"), label, errors)

        derived = item.get("derived_from")
        if not isinstance(derived, list) or any(not isinstance(x, str) for x in derived):
            errors.append("%s derived_from must be an array of artifact IDs" % label)
        source_refs = item.get("source_refs", [])
        if not isinstance(source_refs, list) or any(not isinstance(x, str) for x in source_refs):
            errors.append("%s source_refs must be an array of source IDs" % label)

        stored_size = item.get("size")
        stored_hash = item.get("sha256")
        if not isinstance(stored_size, int) or stored_size < 0:
            errors.append("%s has invalid size" % label)
        if not isinstance(stored_hash, str) or not HEX64_RE.fullmatch(stored_hash):
            errors.append("%s has invalid sha256" % label)

        if verify_files:
            if not full.is_file():
                if status != "missing":
                    errors.append("artifact file missing: %s" % relative)
            else:
                actual_size = full.stat().st_size
                actual_hash = sha256_file(full)
                if isinstance(stored_size, int) and stored_size != actual_size:
                    errors.append("%s size mismatch: manifest=%s actual=%s" % (label, stored_size, actual_size))
                if isinstance(stored_hash, str) and stored_hash.upper() != actual_hash:
                    errors.append("%s sha256 mismatch" % label)

    for item in artifacts:
        artifact_id = str(item.get("id"))
        target = item.get("superseded_by")
        if isinstance(target, str) and target not in artifact_ids:
            errors.append("artifact %s superseded_by unknown artifact %s" % (artifact_id, target))
        derived = item.get("derived_from", [])
        if isinstance(derived, list):
            for ref in derived:
                if isinstance(ref, str) and ref not in artifact_ids:
                    errors.append("artifact %s derived_from unknown artifact %s" % (artifact_id, ref))
        source_refs = item.get("source_refs", [])
        if isinstance(source_refs, list):
            for ref in source_refs:
                if isinstance(ref, str) and ref not in source_ids:
                    errors.append("artifact %s source_refs unknown source %s" % (artifact_id, ref))

    return errors


def finding_dir(root: Path) -> Path:
    return root / "notes" / "findings"


def parse_evidence_token(token: str) -> Tuple[str, str]:
    if token.startswith("source:"):
        return "source", token[len("source:"):]
    if token.startswith("artifact:"):
        return "artifact", token[len("artifact:"):]
    return "artifact", token  # v4.1 compatibility


def canonical_evidence_token(kind: str, evidence_id: str) -> str:
    return "%s:%s" % (kind, evidence_id)


def parse_findings(root: Path) -> Tuple[Dict[str, Path], Dict[str, Set[Tuple[str, str]]], List[str]]:
    ids: Dict[str, Path] = {}
    evidence: Dict[str, Set[Tuple[str, str]]] = {}
    errors: List[str] = []
    directory = finding_dir(root)
    if not directory.exists():
        return ids, evidence, errors

    for path in sorted(directory.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        finding_id: Optional[str] = None
        in_evidence = False
        cited: Set[Tuple[str, str]] = set()
        for line in text.splitlines():
            match = FINDING_ID_RE.match(line)
            if match and finding_id is None:
                finding_id = match.group(1)
            if line.startswith("## "):
                in_evidence = line.strip() == "## Evidence"
                continue
            if in_evidence:
                em = EVIDENCE_REF_RE.match(line)
                if em:
                    token = em.group(1)
                    if token == "Independent check":
                        continue
                    kind, evidence_id = parse_evidence_token(token)
                    if not ID_RE.fullmatch(evidence_id):
                        errors.append("invalid evidence ref %r in %s" % (token, path.relative_to(root)))
                    else:
                        cited.add((kind, evidence_id))

        if finding_id is None:
            errors.append("finding missing '- ID: `...`': %s" % path.relative_to(root))
            continue
        if not ID_RE.fullmatch(finding_id):
            errors.append("invalid finding id %r in %s" % (finding_id, path.relative_to(root)))
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


def check_links(root: Path, manifest: Dict[str, object]) -> List[str]:
    errors: List[str] = []
    finding_ids, evidence, finding_errors = parse_findings(root)
    errors.extend(finding_errors)
    artifacts = artifacts_list(manifest)
    sources = sources_list(manifest)
    artifact_map = {str(item.get("id")): item for item in artifacts if isinstance(item.get("id"), str)}
    source_map = {str(item.get("id")): item for item in sources if isinstance(item.get("id"), str)}

    for kind, mapping in (("artifact", artifact_map), ("source", source_map)):
        for evidence_id, item in mapping.items():
            refs = item.get("finding_refs", [])
            if not isinstance(refs, list):
                continue
            for finding_id in refs:
                if finding_id not in finding_ids:
                    errors.append("%s %s references missing finding %s" % (kind, evidence_id, finding_id))
                elif (kind, evidence_id) not in evidence.get(finding_id, set()):
                    errors.append(
                        "%s %s -> finding %s is not reciprocated in the finding Evidence section"
                        % (kind, evidence_id, finding_id)
                    )

    for finding_id, refs in evidence.items():
        for kind, evidence_id in refs:
            mapping = source_map if kind == "source" else artifact_map
            item = mapping.get(evidence_id)
            if item is None:
                errors.append("finding %s cites unknown %s %s" % (finding_id, kind, evidence_id))
                continue
            finding_refs = item.get("finding_refs", [])
            if not isinstance(finding_refs, list) or finding_id not in finding_refs:
                errors.append(
                    "finding %s -> %s %s is not reciprocated in manifest finding_refs"
                    % (finding_id, kind, evidence_id)
                )
    return errors


def find_finding_path(root: Path, finding_id: str) -> Path:
    ids, _, errors = parse_findings(root)
    if errors:
        raise StoreError("findings must be repaired first: " + "; ".join(errors))
    path = ids.get(finding_id)
    if path is None:
        raise StoreError("finding id not found: %s" % finding_id)
    return path


def upsert_finding_evidence(path: Path, kind: str, evidence_id: str, locator: str) -> None:
    token = canonical_evidence_token(kind, evidence_id)
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("## Evidence")
    except ValueError:
        raise StoreError("finding has no '## Evidence' section: %s" % path)
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break

    replacement = "- `%s`: %s" % (token, locator)
    existing_index: Optional[int] = None
    independent_index: Optional[int] = None
    for index in range(start + 1, end):
        if lines[index].startswith("- Independent check:") and independent_index is None:
            independent_index = index
        match = EVIDENCE_REF_RE.match(lines[index])
        if not match:
            continue
        existing_kind, existing_id = parse_evidence_token(match.group(1))
        if existing_kind == kind and existing_id == evidence_id:
            existing_index = index
            break

    if existing_index is not None:
        lines[existing_index] = replacement
    else:
        insert_at = independent_index if independent_index is not None else end
        while insert_at > start + 1 and lines[insert_at - 1] == "":
            insert_at -= 1
        lines.insert(insert_at, replacement)

    atomic_write_text(path, "\n".join(lines).rstrip() + "\n")


def link_evidence(root: Path, manifest: Dict[str, object], finding_id: str, kind: str,
                  evidence_id: str, locator: str) -> None:
    require_id(finding_id, "finding id")
    require_id(evidence_id, "%s id" % kind)
    if not locator.strip():
        raise StoreError("evidence locator must be non-empty")
    path = find_finding_path(root, finding_id)
    mapping = sources_list(manifest) if kind == "source" else artifacts_list(manifest)
    item = next((entry for entry in mapping if entry.get("id") == evidence_id), None)
    if item is None:
        raise StoreError("%s id not found: %s" % (kind, evidence_id))
    refs = item.setdefault("finding_refs", [])
    if not isinstance(refs, list):
        raise StoreError("%s %s finding_refs is not an array" % (kind, evidence_id))
    if finding_id not in refs:
        refs.append(finding_id)
    upsert_finding_evidence(path, kind, evidence_id, locator)


def parse_ref_locator(value: str, label: str) -> Tuple[str, str]:
    if "=" not in value:
        raise StoreError("%s must use ID=LOCATOR syntax: %r" % (label, value))
    evidence_id, locator = value.split("=", 1)
    require_id(evidence_id, label + " id")
    if not locator.strip():
        raise StoreError("%s locator must be non-empty" % label)
    return evidence_id, locator


def default_report(project: str) -> str:
    return (
        "# Analysis Report\n\n"
        "- Project: `%s`\n"
        "- Status: in progress\n\n"
        "## Research question\n\n<Describe the concrete game-logic question.>\n\n"
        "## Baseline\n\n<Record target version/build/hash and implementation boundary.>\n\n"
        "## Conclusions\n\n<Summarize conclusions with finding/evidence references.>\n\n"
        "## Validation\n\n<Record dynamic/static validation and limitations.>\n\n"
        "## Unresolved next step\n\n<Record the highest-value unresolved step.>\n" % project
    )


def cmd_init(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    require_id(args.project, "project")
    path = manifest_path(root)
    if path.exists() and not args.force:
        raise StoreError("manifest already exists; use --force only for an intentional reset")
    (root / "artifacts").mkdir(parents=True, exist_ok=True)
    (root / "notes" / "findings").mkdir(parents=True, exist_ok=True)
    (root / "reports").mkdir(parents=True, exist_ok=True)
    atomic_write_json(path, {"schema_version": 2, "project": args.project, "sources": [], "artifacts": []})
    report = root / "reports" / "analysis.md"
    if not report.exists():
        atomic_write_text(report, default_report(args.project))
    print("initialized %s" % path)
    print("report %s" % report)
    return 0


def target_from_args(args: argparse.Namespace) -> Dict[str, str]:
    module_hash = args.module_sha256
    if HEX64_RE.fullmatch(module_hash):
        module_hash = module_hash.upper()
    return {
        "game_version": args.game_version,
        "build_id": args.build_id,
        "module": args.module,
        "module_sha256": module_hash,
        "rva_or_range": args.rva_or_range,
    }


def cmd_register_source(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    pre_errors = validate_manifest_shape(root, manifest, verify_files=False)
    if pre_errors:
        raise StoreError("manifest must be repaired before registering sources: " + "; ".join(pre_errors))
    ensure_schema_v2(manifest)
    require_id(args.id, "source id")
    full = Path(args.path).expanduser().resolve()
    if not full.is_file():
        raise StoreError("source file not found: %s" % full)
    sources = sources_list(manifest)
    if any(item.get("id") == args.id for item in sources):
        raise StoreError("source id already exists: %s" % args.id)
    stored_path = str(full)
    if any(item.get("path") == stored_path for item in sources):
        raise StoreError("source path already exists in manifest: %s" % stored_path)
    source_hash = sha256_file(full)
    target = target_from_args(args)
    if target["module"] == "unknown":
        target["module"] = full.name
    if target["module_sha256"] == "unknown":
        target["module_sha256"] = source_hash
    entry: Dict[str, object] = {
        "id": args.id,
        "path": stored_path,
        "kind": args.kind,
        "description": args.description,
        "size": full.stat().st_size,
        "sha256": source_hash,
        "target": target,
        "finding_refs": [],
        "status": "active",
    }
    for finding_id in args.finding_ref:
        require_id(finding_id, "finding ref")
        find_finding_path(root, finding_id)
    sources.append(entry)
    for finding_id in args.finding_ref:
        link_evidence(root, manifest, finding_id, "source", args.id, "registered source; add a more specific locator if needed")
    atomic_write_json(manifest_path(root), manifest)
    print("registered source %s (%d bytes)" % (args.id, entry["size"]))
    return 0


def cmd_add_artifact(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    require_id(args.id, "artifact id")
    full = confined_path(root, args.path)
    if not full.is_file():
        raise StoreError("artifact file not found: %s" % full)

    pre_errors = validate_manifest_shape(root, manifest, verify_files=False)
    if pre_errors:
        raise StoreError("manifest must be repaired before adding artifacts: " + "; ".join(pre_errors))
    artifacts = artifacts_list(manifest)
    if any(item.get("id") == args.id for item in artifacts):
        raise StoreError("artifact id already exists: %s" % args.id)
    if any(item.get("path") == args.path for item in artifacts):
        raise StoreError("artifact path already exists in manifest: %s" % args.path)

    artifact_ids = {str(item.get("id")) for item in artifacts}
    source_ids = {str(item.get("id")) for item in sources_list(manifest)}
    for ref in args.derived_from:
        require_id(ref, "derived_from id")
        if ref not in artifact_ids:
            raise StoreError("derived_from artifact id not found: %s" % ref)
    for ref in args.source_ref:
        require_id(ref, "source ref")
        if ref not in source_ids:
            raise StoreError("source ref not found: %s" % ref)

    entry: Dict[str, object] = {
        "id": args.id,
        "path": args.path,
        "kind": args.kind,
        "description": args.description,
        "size": full.stat().st_size,
        "sha256": sha256_file(full),
        "producer": {"tool": args.tool, "version": args.tool_version},
        "target": target_from_args(args),
        "derived_from": list(args.derived_from),
        "source_refs": list(args.source_ref),
        "finding_refs": [],
        "status": "active",
        "superseded_by": None,
    }
    for finding_id in args.finding_ref:
        require_id(finding_id, "finding ref")
        find_finding_path(root, finding_id)
    artifacts.append(entry)
    for finding_id in args.finding_ref:
        link_evidence(root, manifest, finding_id, "artifact", args.id, "registered artifact; add a more specific locator if needed")
    atomic_write_json(manifest_path(root), manifest)
    print("added artifact %s (%d bytes)" % (args.id, entry["size"]))
    return 0


def cmd_add_finding(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    pre_errors = validate_manifest_shape(root, manifest, verify_files=False)
    if pre_errors:
        raise StoreError("manifest must be repaired before adding findings: " + "; ".join(pre_errors))
    require_id(args.id, "finding id")
    if args.status not in VALID_FINDING_STATUSES:
        raise StoreError("invalid finding status: %s" % args.status)
    ids, _, finding_errors = parse_findings(root)
    if finding_errors:
        raise StoreError("findings must be repaired before adding another: " + "; ".join(finding_errors))
    if args.id in ids:
        raise StoreError("finding id already exists: %s" % args.id)
    path = finding_dir(root) / (args.id + ".md")
    text = (
        "# %s\n\n"
        "- ID: `%s`\n"
        "- Status: `%s`\n"
        "- Target: %s\n"
        "- Scope: %s\n"
        "- Supersedes: %s\n"
        "- Superseded by: none\n\n"
        "## Claim\n\n%s\n\n"
        "## Evidence\n\n"
        "- Independent check: %s\n\n"
        "## Reusable detail\n\n%s\n\n"
        "## Dependencies\n\n%s\n\n"
        "## Validation and limitations\n\n%s\n"
        % (
            args.title, args.id, args.status, args.target, args.scope, args.supersedes,
            args.claim, args.independent_check, args.reusable_detail, args.dependencies,
            args.limitations,
        )
    )
    atomic_write_text(path, text)
    try:
        for spec in args.source_ref:
            evidence_id, locator = parse_ref_locator(spec, "source ref")
            link_evidence(root, manifest, args.id, "source", evidence_id, locator)
        for spec in args.artifact_ref:
            evidence_id, locator = parse_ref_locator(spec, "artifact ref")
            link_evidence(root, manifest, args.id, "artifact", evidence_id, locator)
    except Exception:
        if path.exists():
            path.unlink()
        raise
    atomic_write_json(manifest_path(root), manifest)
    print("added finding %s" % args.id)
    return 0


def cmd_link(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    pre_errors = validate_manifest_shape(root, manifest, verify_files=False)
    if pre_errors:
        raise StoreError("manifest must be repaired before linking: " + "; ".join(pre_errors))
    if args.source_id:
        kind, evidence_id = "source", args.source_id
    else:
        kind, evidence_id = "artifact", args.artifact_id
    link_evidence(root, manifest, args.finding_id, kind, evidence_id, args.locator)
    atomic_write_json(manifest_path(root), manifest)
    print("linked %s:%s -> finding %s" % (kind, evidence_id, args.finding_id))
    return 0


def report_errors(errors: Iterable[str]) -> int:
    items = list(errors)
    if not items:
        print("OK")
        return 0
    for item in items:
        print("ERROR: %s" % item)
    print("FAILED: %d error(s)" % len(items))
    return 1


def cmd_verify(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    return report_errors(validate_manifest_shape(root, manifest, verify_files=True))


def cmd_check_links(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    base_errors = validate_manifest_shape(root, manifest, verify_files=False)
    return report_errors(base_errors + check_links(root, manifest))


def cmd_supersede(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    if args.old_id == args.new_id:
        raise StoreError("old and new artifact IDs must differ")
    artifacts = artifacts_list(manifest)
    by_id = {str(item.get("id")): item for item in artifacts if isinstance(item.get("id"), str)}
    if args.old_id not in by_id:
        raise StoreError("old artifact id not found: %s" % args.old_id)
    if args.new_id not in by_id:
        raise StoreError("new artifact id not found: %s" % args.new_id)
    old = by_id[args.old_id]
    old["status"] = "superseded"
    old["superseded_by"] = args.new_id
    atomic_write_json(manifest_path(root), manifest)
    print("superseded %s -> %s" % (args.old_id, args.new_id))
    return 0


def run_self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="project-store-test-") as tmp:
        base = Path(tmp)
        source = base / "source.js"
        source.write_text("function roll(){ return Math.random(); }\n", encoding="utf-8")
        root = base / "analysis"
        cmd_init(argparse.Namespace(root=str(root), project="sample-game", force=False))
        report = root / "reports" / "analysis.md"
        if not report.is_file():
            raise AssertionError("init did not create reports/analysis.md")

        manifest = load_manifest(root)
        ensure_schema_v2(manifest)
        source_entry: Dict[str, object] = {
            "id": "game-source",
            "path": str(source.resolve()),
            "kind": "source-code",
            "description": "self-test source",
            "size": source.stat().st_size,
            "sha256": sha256_file(source),
            "target": {
                "game_version": "unknown", "build_id": "unknown", "module": "source.js",
                "module_sha256": sha256_file(source), "rva_or_range": "not-applicable",
            },
            "finding_refs": [], "status": "active",
        }
        sources_list(manifest).append(source_entry)

        artifact = root / "artifacts" / "sample.txt"
        artifact.write_text("evidence\n", encoding="utf-8")
        artifact_entry: Dict[str, object] = {
            "id": "sample-artifact", "path": "artifacts/sample.txt", "kind": "test",
            "description": "self-test artifact", "size": artifact.stat().st_size,
            "sha256": sha256_file(artifact), "producer": {"tool": "self-test", "version": "1"},
            "target": {
                "game_version": "unknown", "build_id": "unknown", "module": "source.js",
                "module_sha256": sha256_file(source), "rva_or_range": "not-applicable",
            },
            "derived_from": [], "source_refs": ["game-source"], "finding_refs": [],
            "status": "active", "superseded_by": None,
        }
        artifacts_list(manifest).append(artifact_entry)
        atomic_write_json(manifest_path(root), manifest)

        finding = finding_dir(root) / "sample-finding.md"
        finding.write_text(
            "# Sample\n\n- ID: `sample-finding`\n- Status: `confirmed`\n\n"
            "## Claim\n\nSample.\n\n## Evidence\n\n- Independent check: self-test\n\n"
            "## Reusable detail\n\nnone\n\n## Dependencies\n\nnone\n\n"
            "## Validation and limitations\n\nnone\n",
            encoding="utf-8",
        )
        link_evidence(root, manifest, "sample-finding", "source", "game-source", "roll() definition")
        link_evidence(root, manifest, "sample-finding", "artifact", "sample-artifact", "line 1")
        atomic_write_json(manifest_path(root), manifest)
        errors = validate_manifest_shape(root, manifest, verify_files=True)
        errors.extend(check_links(root, manifest))
        if errors:
            raise AssertionError("; ".join(errors))
    print("project_store self-test: OK")


def add_target_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--game-version", default="unknown")
    parser.add_argument("--build-id", default="unknown")
    parser.add_argument("--module", default="unknown")
    parser.add_argument("--module-sha256", default="unknown")
    parser.add_argument("--rva-or-range", default="not-applicable")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage analyze-game-logic project knowledge stores")
    parser.add_argument("--self-test", action="store_true", help="run pure-Python integrity tests")
    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init", help="initialize manifest, directories, and reports/analysis.md")
    p_init.add_argument("--root", required=True)
    p_init.add_argument("--project", required=True)
    p_init.add_argument("--force", action="store_true")
    p_init.set_defaults(func=cmd_init)

    p_source = sub.add_parser("register-source", help="register an external read-only source file")
    p_source.add_argument("--root", required=True)
    p_source.add_argument("--id", required=True)
    p_source.add_argument("--path", required=True, help="source path; stored as an absolute read-only reference")
    p_source.add_argument("--kind", default="source-file")
    p_source.add_argument("--description", required=True)
    p_source.add_argument("--finding-ref", action="append", default=[], help="existing finding ID; reciprocal link is added")
    add_target_args(p_source)
    p_source.set_defaults(func=cmd_register_source)

    p_add = sub.add_parser("add-artifact", help="hash and add one retained artifact under the analysis root")
    p_add.add_argument("--root", required=True)
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--path", required=True, help="artifact path relative to analysis root")
    p_add.add_argument("--kind", required=True)
    p_add.add_argument("--description", required=True)
    p_add.add_argument("--tool", required=True)
    p_add.add_argument("--tool-version", default="unknown")
    add_target_args(p_add)
    p_add.add_argument("--derived-from", action="append", default=[], help="artifact ID")
    p_add.add_argument("--source-ref", action="append", default=[], help="registered source ID")
    p_add.add_argument("--finding-ref", action="append", default=[], help="existing finding ID; reciprocal link is added")
    p_add.set_defaults(func=cmd_add_artifact)

    p_finding = sub.add_parser("add-finding", help="create a reusable finding and optionally link evidence atomically")
    p_finding.add_argument("--root", required=True)
    p_finding.add_argument("--id", required=True)
    p_finding.add_argument("--title", required=True)
    p_finding.add_argument("--status", default="working-hypothesis", choices=sorted(VALID_FINDING_STATUSES))
    p_finding.add_argument("--target", default="unknown")
    p_finding.add_argument("--scope", default="unknown")
    p_finding.add_argument("--supersedes", default="none")
    p_finding.add_argument("--claim", required=True)
    p_finding.add_argument("--independent-check", default="not yet established")
    p_finding.add_argument("--reusable-detail", default="none")
    p_finding.add_argument("--dependencies", default="none")
    p_finding.add_argument("--limitations", default="not yet fully validated")
    p_finding.add_argument("--source-ref", action="append", default=[], metavar="ID=LOCATOR")
    p_finding.add_argument("--artifact-ref", action="append", default=[], metavar="ID=LOCATOR")
    p_finding.set_defaults(func=cmd_add_finding)

    p_link = sub.add_parser("link", help="link one registered source/artifact to an existing finding on both sides")
    p_link.add_argument("--root", required=True)
    p_link.add_argument("--finding-id", required=True)
    group = p_link.add_mutually_exclusive_group(required=True)
    group.add_argument("--source-id")
    group.add_argument("--artifact-id")
    p_link.add_argument("--locator", required=True)
    p_link.set_defaults(func=cmd_link)

    p_verify = sub.add_parser("verify", help="verify manifest structure and source/artifact integrity")
    p_verify.add_argument("--root", required=True)
    p_verify.set_defaults(func=cmd_verify)

    p_links = sub.add_parser("check-links", help="verify source/artifact/finding reciprocal links")
    p_links.add_argument("--root", required=True)
    p_links.set_defaults(func=cmd_check_links)

    p_sup = sub.add_parser("supersede", help="mark one artifact superseded by another")
    p_sup.add_argument("--root", required=True)
    p_sup.add_argument("--old-id", required=True)
    p_sup.add_argument("--new-id", required=True)
    p_sup.set_defaults(func=cmd_supersede)
    return parser


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
