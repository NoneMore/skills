"""Explicit installer for the project-local game-logic store (Python 3.8+)."""

import argparse
import hashlib
import json
import tempfile
from pathlib import Path
from typing import Optional, Sequence

import project_store as store


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temp = destination.with_name(destination.name + ".tmp")
    temp.write_bytes(source.read_bytes())
    temp.replace(destination)


def bootstrap(args: argparse.Namespace) -> None:
    root = Path(args.root).resolve()
    store.require_id(args.project, "project")
    kit = Path(__file__).resolve().parent.parent
    source_tool = kit / "scripts" / "project_store.py"
    source_rules = kit / "assets" / "STORE.md"
    install = root / ".game-logic"
    tool = install / "bin" / "project_store.py"
    rules = install / "STORE.md"
    stamp = install / "bootstrap.json"
    manifest_path = store.manifest_path(root)

    manifest = None
    if manifest_path.exists():
        manifest = store.load_manifest(root)
        if manifest.get("project") != args.project:
            raise store.StoreError("project ID differs from existing manifest")
        version = manifest.get("schema_version")
        if version == 3 and not args.upgrade:
            raise store.StoreError("schema-3 migration requires explicit --upgrade")
        if version not in (3, store.SCHEMA_VERSION):
            raise store.StoreError("unsupported existing store schema")
        errors = store.validate_store(root, manifest, True)
        if not errors:
            errors.extend(store.check_links(root, manifest))
        if errors:
            raise store.StoreError("existing store must be repaired first: " + "; ".join(errors))

    stamp_data = None
    if stamp.exists():
        stamp_data = store.read_object(stamp, "bootstrap metadata")
        if stamp_data.get("project") != args.project:
            raise store.StoreError("bootstrap metadata refers to another project")
    for dest, source, key in (
        (tool, source_tool, "tool_sha256"),
        (rules, source_rules, "rules_sha256"),
    ):
        if not dest.exists():
            continue
        if not dest.is_file():
            raise store.StoreError("project kit destination is not a file: %s" % dest)
        current = digest(dest)
        if stamp_data is not None and stamp_data.get(key) != current:
            raise store.StoreError("locally modified project kit file; reconcile before upgrading: %s" % dest)
        if current != digest(source):
            if not args.upgrade:
                raise store.StoreError("project kit version differs; explicitly request --upgrade")
            if stamp_data is None:
                raise store.StoreError("unmanaged project kit file must not be overwritten: %s" % dest)

    if stamp_data is not None and not args.upgrade:
        if stamp_data.get("tool_sha256") != digest(source_tool) or stamp_data.get("rules_sha256") != digest(source_rules):
            raise store.StoreError("project kit metadata differs; explicitly request --upgrade")

    atomic_copy(source_tool, tool)
    atomic_copy(source_rules, rules)
    if manifest is None:
        store.cmd_init(argparse.Namespace(root=str(root), project=args.project, force=False))
    elif manifest.get("schema_version") == 3:
        store.cmd_migrate(argparse.Namespace(root=str(root)))
    if store.cmd_verify(argparse.Namespace(root=str(root))) != 0:
        raise store.StoreError("installed store verification failed")
    if store.cmd_check_links(argparse.Namespace(root=str(root))) != 0:
        raise store.StoreError("installed store link verification failed")
    store.atomic_json(stamp, {
        "kit_schema_version": 1,
        "project": args.project,
        "store_schema_version": store.SCHEMA_VERSION,
        "tool_sha256": digest(tool),
        "rules_sha256": digest(rules),
    })
    print("project kit ready at %s" % install)


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="game-logic-bootstrap-") as tmp:
        base = Path(tmp)
        root = base / "fresh"
        arguments = argparse.Namespace(root=str(root), project="example", upgrade=False)
        bootstrap(arguments)
        bootstrap(arguments)
        if store.load_manifest(root)["schema_version"] != store.SCHEMA_VERSION:
            raise AssertionError("fresh store not initialized")

        tool = root / ".game-logic" / "bin" / "project_store.py"
        tool.write_text("edited\n", encoding="utf-8")
        try:
            bootstrap(arguments)
        except store.StoreError:
            pass
        else:
            raise AssertionError("modified local tool was silently overwritten")

        legacy = base / "legacy"
        store.cmd_init(argparse.Namespace(root=str(legacy), project="legacy", force=False))
        data = store.load_manifest(legacy)
        data["schema_version"] = 3
        store.atomic_json(store.manifest_path(legacy), data)
        (legacy / store.APPLICATIONS).rmdir()
        upgrade = argparse.Namespace(root=str(legacy), project="legacy", upgrade=False)
        try:
            bootstrap(upgrade)
        except store.StoreError:
            pass
        else:
            raise AssertionError("legacy store was migrated without explicit upgrade")
        upgrade.upgrade = True
        bootstrap(upgrade)
        if store.load_manifest(legacy)["schema_version"] != store.SCHEMA_VERSION:
            raise AssertionError("legacy store migration failed")
    print("bootstrap self-test: OK")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Install or explicitly upgrade a project-local game-logic store")
    parser.add_argument("--root", help="Project root; must not be the installed game directory")
    parser.add_argument("--project", help="Filesystem-safe project ID")
    parser.add_argument("--upgrade", action="store_true", help="Explicitly upgrade installed kit or legacy store")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    if not args.root or not args.project:
        parser.error("--root and --project are required")
    try:
        bootstrap(args)
        return 0
    except (store.StoreError, OSError) as exc:
        parser.exit(1, "ERROR: %s\n" % exc)


if __name__ == "__main__":
    raise SystemExit(main())
