#!/usr/bin/env python3
"""Minimal stdlib smoke tests for love2d_triage.py."""

from __future__ import annotations

import importlib.util
import io
import tempfile
import zipfile
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("love2d_triage.py")
SPEC = importlib.util.spec_from_file_location("love2d_triage", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def love_payload() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("main.lua", "function love.update(dt) require('rules') end\n")
        archive.writestr("rules.lua", "return {}\n")
    return buffer.getvalue()


def test_love_archive(tmp: Path) -> None:
    path = tmp / "game.love"
    path.write_bytes(love_payload())
    result = MODULE.analyze_target(path)
    assert result["container"]["classification"] == "love-archive"
    assert result["love_evidence"]["root_main_lua"] is True
    assert {edge["module"] for edge in result["require_hints"]} == {"rules"}


def test_fused_pe(tmp: Path) -> None:
    path = tmp / "game.exe"
    prefix = b"MZ" + b"\x00" * 254
    payload = love_payload()
    path.write_bytes(prefix + payload)
    result = MODULE.analyze_target(path)
    assert result["container"]["classification"] == "windows-fused-executable"
    assert result["container"]["appended_love_offset"] == len(prefix)
    assert result["love_evidence"]["root_main_lua"] is True


def test_non_love_zip(tmp: Path) -> None:
    path = tmp / "not-love.zip"
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("data.txt", "no main")
    path.write_bytes(buffer.getvalue())
    result = MODULE.analyze_target(path)
    assert result["container"]["classification"] == "zip-non-love"


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        tmp = Path(directory)
        test_love_archive(tmp)
        test_fused_pe(tmp)
        test_non_love_zip(tmp)
    print("love2d_triage smoke tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
