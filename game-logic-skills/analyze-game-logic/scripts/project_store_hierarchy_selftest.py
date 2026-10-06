"""Regression coverage for canonical and legacy project-store layouts."""

import argparse
import tempfile
from pathlib import Path

import project_store as store


def add_scope(root: Path, analysis_id: str, target_id: str, game_version: str,
              build_id: str, local_name: str, artifact_id: str, finding_id: str) -> None:
    store.cmd_init_analysis(argparse.Namespace(root=str(root), id=analysis_id, title=None, force=False))
    store.cmd_init_target(argparse.Namespace(
        root=str(root), analysis_id=analysis_id, target_id=target_id,
        game_version=game_version, build_id=build_id, platform="pc", distribution="test",
        module="game.exe", module_sha256="unknown", force=False,
    ))
    artifact = store.target_dir(root, analysis_id, target_id) / "artifacts" / local_name
    artifact.write_text("evidence\n", encoding="utf-8")
    store.cmd_add_artifact(argparse.Namespace(
        root=str(root), id=artifact_id, path=None, analysis_id=analysis_id,
        target_id=target_id, local_name=local_name, shared=False, kind="self-test",
        description="hierarchy self-test", tool="self-test", tool_version="1",
        game_version="unknown", build_id="unknown", module="unknown",
        module_sha256="unknown", rva_or_range="not-applicable", derived_from=[],
        source_ref=[], finding_ref=[], consumes_finding_ref=[],
    ))
    store.cmd_add_finding(argparse.Namespace(
        root=str(root), id=finding_id, title=finding_id, status="confirmed",
        target=target_id, scope=analysis_id, supersedes="none", claim="Sample.",
        independent_check="self-test", reusable_detail="none", dependencies="none",
        limitations="none", source_ref=[], artifact_ref=[artifact_id + "=line 1"],
        analysis_id=analysis_id, target_id=target_id,
    ))


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="project-store-hierarchy-regression-") as tmp:
        base = Path(tmp)
        root = base / "canonical"
        store.cmd_init(argparse.Namespace(root=str(root), project="sample-game", force=False))
        assert not (root / "notes" / "findings").exists()
        assert (root / "reports" / "index.md").is_file()

        scopes = [
            ("reload-timing", "build-1", "1.0", "1", "static.txt", "reload-static", "reload-result"),
            ("offline-accuracy", "build-2", "2.0", "2", "runtime.txt", "accuracy-runtime", "accuracy-result"),
        ]
        for scope in scopes:
            add_scope(root, *scope)

        shared_file = root / "shared" / "artifacts" / "common.txt"
        shared_file.write_text("shared evidence\n", encoding="utf-8")
        store.cmd_add_artifact(argparse.Namespace(
            root=str(root), id="shared-common", path=None, analysis_id=None, target_id=None,
            local_name="common.txt", shared=True, kind="self-test", description="shared evidence",
            tool="self-test", tool_version="1", game_version="unknown", build_id="unknown",
            module="unknown", module_sha256="unknown", rva_or_range="not-applicable",
            derived_from=[], source_ref=[], finding_ref=[], consumes_finding_ref=[],
        ))

        manifest = store.load_manifest(root)
        for analysis_id, target_id, game_version, build_id, local_name, artifact_id, _ in scopes:
            item = next(entry for entry in store.artifacts_list(manifest) if entry.get("id") == artifact_id)
            expected = str(Path("analyses") / analysis_id / "targets" / target_id / "artifacts" / local_name)
            assert item.get("path") == expected
            assert item.get("analysis_id") == analysis_id
            assert item.get("target_id") == target_id
            target = item.get("target")
            assert isinstance(target, dict)
            assert target.get("game_version") == game_version
            assert target.get("build_id") == build_id
            assert game_version not in local_name and build_id not in local_name and target_id not in local_name

        shared = next(entry for entry in store.artifacts_list(manifest) if entry.get("id") == "shared-common")
        assert shared.get("path") == "shared/artifacts/common.txt"
        assert shared.get("analysis_id") is None and shared.get("target_id") is None
        assert store.cmd_verify(argparse.Namespace(root=str(root))) == 0
        assert store.cmd_check_links(argparse.Namespace(root=str(root))) == 0

        legacy_dir = root / "notes" / "findings"
        legacy_dir.mkdir(parents=True, exist_ok=True)
        (legacy_dir / "duplicate.md").write_text(
            "# Duplicate\n\n- ID: `reload-result`\n\n## Evidence\n\n- Independent check: none\n",
            encoding="utf-8",
        )
        assert any("duplicate finding id reload-result" in error for error in store.parse_findings(root)[2])

        legacy_root = base / "legacy"
        store._ORIGINAL_CMD_INIT(argparse.Namespace(root=str(legacy_root), project="legacy-game", force=False))
        legacy_finding = legacy_root / "notes" / "findings" / "legacy-result.md"
        legacy_finding.write_text(
            "# Legacy result\n\n- ID: `legacy-result`\n- Status: `confirmed`\n\n"
            "## Claim\n\nSample.\n\n## Evidence\n\n- Independent check: self-test\n\n"
            "## Reusable detail\n\nnone\n\n## Dependencies\n\nnone\n\n"
            "## Validation and limitations\n\nnone\n",
            encoding="utf-8",
        )
        assert store.cmd_verify(argparse.Namespace(root=str(legacy_root))) == 0
        assert store.cmd_check_links(argparse.Namespace(root=str(legacy_root))) == 0

    print("project_store hierarchy regression self-test: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
