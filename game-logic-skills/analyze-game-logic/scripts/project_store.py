"""Canonical hierarchy front-end for the game-logic project knowledge store.

New stores organize durable work by analysis and target scope while preserving
compatibility with legacy ``notes/findings`` stores. The legacy helper remains
the implementation source for manifest hashing/provenance and evidence links;
this module adds canonical scope/path rules and structural validation.
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

try:
    import project_store_legacy as _legacy
except ModuleNotFoundError:  # pragma: no cover - package import compatibility
    from . import project_store_legacy as _legacy  # type: ignore


StoreError = _legacy.StoreError
ID_RE = _legacy.ID_RE
FINDING_ID_RE = _legacy.FINDING_ID_RE
EVIDENCE_REF_RE = _legacy.EVIDENCE_REF_RE
manifest_path = _legacy.manifest_path
load_manifest = _legacy.load_manifest
atomic_write_json = _legacy.atomic_write_json
atomic_write_text = _legacy.atomic_write_text
artifacts_list = _legacy.artifacts_list
require_id = _legacy.require_id
parse_evidence_token = _legacy.parse_evidence_token
parse_ref_locator = _legacy.parse_ref_locator
link_evidence = _legacy.link_evidence
report_errors = _legacy.report_errors

_ORIGINAL_VALIDATE_MANIFEST_SHAPE = _legacy.validate_manifest_shape
_ORIGINAL_CMD_INIT = _legacy.cmd_init
_ORIGINAL_CMD_ADD_ARTIFACT = _legacy.cmd_add_artifact
_ORIGINAL_CMD_ADD_FINDING = _legacy.cmd_add_finding
_ORIGINAL_BUILD_PARSER = _legacy.build_parser

ANALYSES_DIR = "analyses"
TARGETS_DIR = "targets"
SHARED_ARTIFACTS = Path("shared") / "artifacts"
CANONICAL_ROLES = {"artifacts", "scripts", "reports"}


def analysis_dir(root: Path, analysis_id: str) -> Path:
    return root / ANALYSES_DIR / analysis_id


def target_dir(root: Path, analysis_id: str, target_id: str) -> Path:
    return analysis_dir(root, analysis_id) / TARGETS_DIR / target_id


def legacy_finding_dir(root: Path) -> Path:
    return root / "notes" / "findings"


def canonical_finding_path(root: Path, analysis_id: str, target_id: str) -> Path:
    return target_dir(root, analysis_id, target_id) / "finding.md"


def _local_name(name: str) -> str:
    candidate = Path(name)
    if candidate.name != name or name in ("", ".", ".."):
        raise StoreError("local name must be one filesystem-safe sibling name: %r" % name)
    return name


def _read_json_object(path: Path, label: str) -> Dict[str, object]:
    if not path.is_file():
        raise StoreError("%s not found: %s" % (label, path))
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StoreError("invalid %s JSON: %s" % (label, exc))
    if not isinstance(value, dict):
        raise StoreError("%s must be a JSON object: %s" % (label, path))
    return value


def _scope_target(root: Path, analysis_id: str, target_id: str) -> Dict[str, object]:
    require_id(analysis_id, "analysis id")
    require_id(target_id, "target id")
    target = _read_json_object(
        target_dir(root, analysis_id, target_id) / "target.json",
        "target metadata",
    )
    if target.get("id") != target_id:
        raise StoreError("target metadata id does not match directory: %s" % target_id)
    return target


def _parse_finding_file(root: Path, path: Path) -> Tuple[Optional[str], Set[Tuple[str, str]], List[str]]:
    errors: List[str] = []
    text = path.read_text(encoding="utf-8")
    finding_id: Optional[str] = None
    cited: Set[Tuple[str, str]] = set()
    in_evidence = False
    for line in text.splitlines():
        match = FINDING_ID_RE.match(line)
        if match and finding_id is None:
            finding_id = match.group(1)
        if line.startswith("## "):
            in_evidence = line.strip() == "## Evidence"
            continue
        if in_evidence:
            match = EVIDENCE_REF_RE.match(line)
            if not match:
                continue
            token = match.group(1)
            kind, evidence_id = parse_evidence_token(token)
            if not ID_RE.fullmatch(evidence_id):
                errors.append("invalid evidence ref %r in %s" % (token, path.relative_to(root)))
            else:
                cited.add((kind, evidence_id))
    if finding_id is None:
        errors.append("finding missing '- ID: `...`': %s" % path.relative_to(root))
    elif not ID_RE.fullmatch(finding_id):
        errors.append("invalid finding id %r in %s" % (finding_id, path.relative_to(root)))
    return finding_id, cited, errors


def parse_findings(root: Path) -> Tuple[Dict[str, Path], Dict[str, Set[Tuple[str, str]]], List[str]]:
    """Discover exact canonical findings plus the legacy recursive layout."""
    ids: Dict[str, Path] = {}
    evidence: Dict[str, Set[Tuple[str, str]]] = {}
    errors: List[str] = []
    candidates: List[Path] = []

    analyses = root / ANALYSES_DIR
    if analyses.exists():
        candidates.extend(sorted(analyses.glob("*/targets/*/finding.md")))
        canonical = {path.resolve() for path in candidates}
        for path in sorted(analyses.rglob("finding.md")):
            if path.resolve() not in canonical:
                errors.append("finding is outside canonical analysis/target location: %s" % path.relative_to(root))

    legacy = legacy_finding_dir(root)
    if legacy.exists():
        candidates.extend(sorted(legacy.rglob("*.md")))

    for path in candidates:
        finding_id, cited, file_errors = _parse_finding_file(root, path)
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


def find_finding_path(root: Path, finding_id: str) -> Path:
    ids, _, errors = parse_findings(root)
    if errors:
        raise StoreError("findings must be repaired first: " + "; ".join(errors))
    path = ids.get(finding_id)
    if path is None:
        raise StoreError("finding id not found: %s" % finding_id)
    return path


def _canonical_artifact_context(relative: str) -> Optional[Tuple[str, str]]:
    parts = Path(relative).parts
    if len(parts) < 6 or parts[0] != ANALYSES_DIR or parts[2] != TARGETS_DIR or parts[4] != "artifacts":
        return None
    if not ID_RE.fullmatch(parts[1]) or not ID_RE.fullmatch(parts[3]):
        return None
    return parts[1], parts[3]


def validate_canonical_structure(root: Path, manifest: Dict[str, object]) -> List[str]:
    errors: List[str] = []
    analyses = root / ANALYSES_DIR
    if analyses.exists():
        for a_dir in sorted(path for path in analyses.iterdir() if path.is_dir()):
            analysis_id = a_dir.name
            if not ID_RE.fullmatch(analysis_id):
                errors.append("invalid canonical analysis id in path: %s" % analysis_id)
                continue
            targets = a_dir / TARGETS_DIR
            if not targets.exists():
                continue
            for t_dir in sorted(path for path in targets.iterdir() if path.is_dir()):
                target_id = t_dir.name
                if not ID_RE.fullmatch(target_id):
                    errors.append("invalid canonical target id in path: %s" % target_id)
                    continue
                metadata = t_dir / "target.json"
                if not metadata.is_file():
                    errors.append("canonical target is missing target.json: %s" % t_dir.relative_to(root))
                    continue
                try:
                    target = _read_json_object(metadata, "target metadata")
                    if target.get("id") != target_id:
                        errors.append("target metadata id mismatch: %s" % metadata.relative_to(root))
                except StoreError as exc:
                    errors.append(str(exc))

        for path in sorted(analyses.rglob("finding.md")):
            parts = path.relative_to(root).parts
            if len(parts) != 5 or parts[0] != ANALYSES_DIR or parts[2] != TARGETS_DIR or parts[4] != "finding.md":
                errors.append("finding is outside canonical analysis/target location: %s" % path.relative_to(root))

    try:
        artifacts = artifacts_list(manifest)
    except StoreError as exc:
        return errors + [str(exc)]
    for item in artifacts:
        relative = item.get("path")
        if not isinstance(relative, str):
            continue
        context = _canonical_artifact_context(relative)
        if context is not None:
            analysis_id, target_id = context
            target_path = target_dir(root, analysis_id, target_id) / "target.json"
            if not target_path.is_file():
                errors.append("artifact %s references canonical target without target.json" % item.get("id"))
                continue
            try:
                target_meta = _read_json_object(target_path, "target metadata")
            except StoreError as exc:
                errors.append(str(exc))
                continue
            recorded_target = item.get("target")
            if isinstance(recorded_target, dict):
                for key in ("game_version", "build_id", "module", "module_sha256"):
                    scoped = target_meta.get(key)
                    recorded = recorded_target.get(key)
                    if isinstance(scoped, str) and scoped and recorded != scoped:
                        errors.append("artifact %s target.%s disagrees with target.json" % (item.get("id"), key))
        elif relative.startswith(ANALYSES_DIR + "/"):
            errors.append("artifact %s uses non-canonical analyses path: %s" % (item.get("id"), relative))
        elif relative.startswith("shared/") and not relative.startswith("shared/artifacts/"):
            errors.append("shared artifact %s must be under shared/artifacts/: %s" % (item.get("id"), relative))
    return errors


def validate_manifest_shape(root: Path, manifest: Dict[str, object], verify_files: bool) -> List[str]:
    return _ORIGINAL_VALIDATE_MANIFEST_SHAPE(root, manifest, verify_files) + validate_canonical_structure(root, manifest)


def cmd_init(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    require_id(args.project, "project")
    path = manifest_path(root)
    if path.exists() and not args.force:
        raise StoreError("manifest already exists; use --force only for an intentional reset")
    (root / "artifacts").mkdir(parents=True, exist_ok=True)
    (root / ANALYSES_DIR).mkdir(parents=True, exist_ok=True)
    (root / SHARED_ARTIFACTS).mkdir(parents=True, exist_ok=True)
    atomic_write_json(path, {"schema_version": 2, "project": args.project, "sources": [], "artifacts": []})
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
    for role in sorted(CANONICAL_ROLES):
        (directory / role).mkdir(parents=True, exist_ok=True)
    module_hash = args.module_sha256.upper() if _legacy.HEX64_RE.fullmatch(args.module_sha256) else args.module_sha256
    atomic_write_json(metadata, {
        "id": args.target_id,
        "game_version": args.game_version,
        "build_id": args.build_id,
        "platform": args.platform,
        "distribution": args.distribution,
        "module": args.module,
        "module_sha256": module_hash,
    })
    print("initialized target %s/%s" % (args.analysis_id, args.target_id))
    return 0


def _apply_target_scope(args: argparse.Namespace, target: Dict[str, object]) -> None:
    for attr in ("game_version", "build_id", "module", "module_sha256"):
        scoped = target.get(attr)
        setattr(args, attr, scoped if isinstance(scoped, str) and scoped else "unknown")


def cmd_add_artifact(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    canonical = bool(args.analysis_id or args.target_id or args.local_name)
    if args.shared:
        if args.analysis_id or args.target_id:
            raise StoreError("--shared cannot be combined with --analysis-id/--target-id")
        if args.path:
            raise StoreError("use --local-name instead of --path with --shared")
        if not args.local_name:
            raise StoreError("--shared requires --local-name")
        args.path = str(SHARED_ARTIFACTS / _local_name(args.local_name))
    elif canonical:
        if not args.analysis_id or not args.target_id or not args.local_name:
            raise StoreError("canonical artifacts require --analysis-id, --target-id, and --local-name")
        if args.path:
            raise StoreError("use --local-name instead of --path for canonical artifacts")
        target = _scope_target(root, args.analysis_id, args.target_id)
        args.path = str(
            Path(ANALYSES_DIR) / args.analysis_id / TARGETS_DIR / args.target_id
            / "artifacts" / _local_name(args.local_name)
        )
        _apply_target_scope(args, target)
    elif (root / ANALYSES_DIR).is_dir():
        raise StoreError("canonical stores require scope arguments or --shared for add-artifact")
    elif not args.path:
        raise StoreError("add-artifact requires --path, or canonical scope arguments")

    return _ORIGINAL_CMD_ADD_ARTIFACT(args)


def _finding_text(args: argparse.Namespace) -> str:
    return (
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
        % (args.title, args.id, args.status, args.target, args.scope, args.supersedes,
           args.claim, args.independent_check, args.reusable_detail, args.dependencies,
           args.limitations)
    )


def cmd_add_finding(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not args.analysis_id and not args.target_id:
        if (root / ANALYSES_DIR).is_dir():
            raise StoreError("canonical stores require --analysis-id and --target-id for add-finding")
        return _ORIGINAL_CMD_ADD_FINDING(args)
    if not args.analysis_id or not args.target_id:
        raise StoreError("add-finding requires both --analysis-id and --target-id")

    manifest = load_manifest(root)
    pre_errors = validate_manifest_shape(root, manifest, verify_files=False)
    if pre_errors:
        raise StoreError("manifest must be repaired before adding findings: " + "; ".join(pre_errors))
    require_id(args.id, "finding id")
    _scope_target(root, args.analysis_id, args.target_id)
    ids, _, finding_errors = parse_findings(root)
    if finding_errors:
        raise StoreError("findings must be repaired before adding another: " + "; ".join(finding_errors))
    if args.id in ids:
        raise StoreError("finding id already exists: %s" % args.id)
    path = canonical_finding_path(root, args.analysis_id, args.target_id)
    if path.exists():
        raise StoreError("canonical target already has a primary finding: %s" % path.relative_to(root))
    atomic_write_text(path, _finding_text(args))
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


def cmd_verify(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    _, _, finding_errors = parse_findings(root)
    return report_errors(validate_manifest_shape(root, manifest, verify_files=True) + finding_errors)


def cmd_check_links(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    manifest = load_manifest(root)
    base_errors = validate_manifest_shape(root, manifest, verify_files=False)
    return report_errors(base_errors + _legacy.check_links(root, manifest))


def _subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction:
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action
    raise AssertionError("legacy parser has no subparsers")


def build_parser() -> argparse.ArgumentParser:
    parser = _ORIGINAL_BUILD_PARSER()
    sub = _subparsers(parser)

    p_init = sub.choices["init"]
    p_init.set_defaults(func=cmd_init)
    for choice in sub._choices_actions:
        if choice.dest == "init":
            choice.help = "initialize the canonical analysis/target project layout"

    p_add = sub.choices["add-artifact"]
    for action in p_add._actions:
        if "--path" in action.option_strings:
            action.required = False
            action.help = "legacy project-relative path; canonical stores use scope args"
            break
    p_add.add_argument("--analysis-id")
    p_add.add_argument("--target-id")
    p_add.add_argument("--local-name", help="sibling-local artifact filename for canonical/shared storage")
    p_add.add_argument("--shared", action="store_true", help="store under shared/artifacts instead of one analysis target")
    p_add.set_defaults(func=cmd_add_artifact)

    p_finding = sub.choices["add-finding"]
    p_finding.add_argument("--analysis-id")
    p_finding.add_argument("--target-id")
    p_finding.set_defaults(func=cmd_add_finding)

    p_verify = sub.choices["verify"]
    p_verify.set_defaults(func=cmd_verify)
    p_links = sub.choices["check-links"]
    p_links.set_defaults(func=cmd_check_links)

    p_target = sub.add_parser("init-target", help="create one analysis/target scope")
    p_target.add_argument("--root", required=True)
    p_target.add_argument("--analysis-id", required=True)
    p_target.add_argument("--target-id", required=True)
    p_target.add_argument("--game-version", default="unknown")
    p_target.add_argument("--build-id", default="unknown")
    p_target.add_argument("--platform", default="unknown")
    p_target.add_argument("--distribution", default="unknown")
    p_target.add_argument("--module", default="unknown")
    p_target.add_argument("--module-sha256", default="unknown")
    p_target.add_argument("--force", action="store_true")
    p_target.set_defaults(func=cmd_init_target)
    return parser


def run_self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="project-store-hierarchy-test-") as tmp:
        root = Path(tmp) / "analysis"
        cmd_init(argparse.Namespace(root=str(root), project="sample-game", force=False))
        if (root / "notes" / "findings").exists():
            raise AssertionError("new init unexpectedly created legacy notes/findings")

        cmd_init_target(argparse.Namespace(
            root=str(root), analysis_id="reload-timing", target_id="build-1",
            game_version="1.0", build_id="1", platform="pc", distribution="test",
            module="game.exe", module_sha256="unknown", force=False,
        ))
        artifact = target_dir(root, "reload-timing", "build-1") / "artifacts" / "static.txt"
        artifact.write_text("evidence\n", encoding="utf-8")
        cmd_add_artifact(argparse.Namespace(
            root=str(root), id="reload-static", path=None, analysis_id="reload-timing",
            target_id="build-1", local_name="static.txt", shared=False, kind="test",
            description="test", tool="self-test", tool_version="1", game_version="wrong",
            build_id="wrong", module="wrong", module_sha256="wrong", rva_or_range="not-applicable",
            derived_from=[], source_ref=[], finding_ref=[], consumes_finding_ref=[],
        ))
        cmd_add_finding(argparse.Namespace(
            root=str(root), id="reload-result", title="Reload result", status="confirmed",
            target="build-1", scope="reload timing", supersedes="none", claim="Sample.",
            independent_check="self-test", reusable_detail="none", dependencies="none",
            limitations="none", source_ref=[], artifact_ref=["reload-static=line 1"],
            analysis_id="reload-timing", target_id="build-1",
        ))

        shared_file = root / SHARED_ARTIFACTS / "common.txt"
        shared_file.write_text("shared evidence\n", encoding="utf-8")
        cmd_add_artifact(argparse.Namespace(
            root=str(root), id="shared-common", path=None, analysis_id=None, target_id=None,
            local_name="common.txt", shared=True, kind="test", description="shared evidence",
            tool="self-test", tool_version="1", game_version="unknown", build_id="unknown",
            module="unknown", module_sha256="unknown", rva_or_range="not-applicable",
            derived_from=[], source_ref=[], finding_ref=[], consumes_finding_ref=[],
        ))

        manifest = load_manifest(root)
        item = next(entry for entry in artifacts_list(manifest) if entry.get("id") == "reload-static")
        expected = str(Path("analyses") / "reload-timing" / "targets" / "build-1" / "artifacts" / "static.txt")
        if item.get("path") != expected:
            raise AssertionError("canonical artifact path mismatch")
        if "analysis_id" in item or "target_id" in item:
            raise AssertionError("canonical path context was redundantly copied into the manifest")
        target = item.get("target")
        if not isinstance(target, dict) or target.get("game_version") != "1.0" or target.get("build_id") != "1":
            raise AssertionError("target scope was not inherited by the canonical artifact")

        errors = validate_manifest_shape(root, manifest, verify_files=True)
        errors.extend(_legacy.check_links(root, manifest))
        if errors:
            raise AssertionError("; ".join(errors))

        legacy = legacy_finding_dir(root)
        legacy.mkdir(parents=True, exist_ok=True)
        (legacy / "duplicate.md").write_text(
            "# Duplicate\n\n- ID: `reload-result`\n\n## Evidence\n\n- Independent check: none\n",
            encoding="utf-8",
        )
        _, _, duplicate_errors = parse_findings(root)
        if not any("duplicate finding id reload-result" in item for item in duplicate_errors):
            raise AssertionError("duplicate ID across canonical/legacy layouts was not rejected")
    print("project_store hierarchy self-test: OK")


def _install_legacy_hooks() -> None:
    _legacy.parse_findings = parse_findings
    _legacy.find_finding_path = find_finding_path
    _legacy.validate_manifest_shape = validate_manifest_shape


_install_legacy_hooks()


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
