#!/usr/bin/env python3
"""Read-only mechanical triage for Windows LÖVE / Love2D artifacts."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable

RE_REQUIRE = re.compile(r"\brequire\s*(?:\(\s*)?['\"]([^'\"]+)['\"]")
INDICATORS = {
    "custom_love_run": re.compile(r"\b(?:function\s+love\.run\b|love\.run\s*=)"),
    "resolution_override": re.compile(
        r"\blove\.filesystem\.(?:setRequirePath|setCRequirePath|mount|setIdentity)\s*\(|\bappendidentity\b"
    ),
    "thread_use": re.compile(r"\blove\.thread\.(?:newThread|getChannel|newChannel)\s*\("),
    "ffi_native": re.compile(r"\b(?:require\s*(?:\(\s*)?['\"]ffi['\"]|ffi\.(?:load|cdef)\b)"),
}


def normalize(name: str) -> str:
    return str(PurePosixPath(name.replace("\\", "/")))


def is_windows_pe(data: bytes) -> bool:
    if len(data) < 0x40 or not data.startswith(b"MZ"):
        return False
    offset = int.from_bytes(data[0x3C:0x40], "little")
    if offset > len(data) - 24 or data[offset : offset + 4] != b"PE\0\0":
        return False

    coff = offset + 4
    machine = int.from_bytes(data[coff : coff + 2], "little")
    section_count = int.from_bytes(data[coff + 2 : coff + 4], "little")
    optional_size = int.from_bytes(data[coff + 16 : coff + 18], "little")
    optional = coff + 20
    if machine == 0 or section_count == 0 or optional_size < 2:
        return False
    if optional + optional_size + section_count * 40 > len(data):
        return False
    return int.from_bytes(data[optional : optional + 2], "little") in {0x10B, 0x20B}


def decode_lua(data: bytes) -> str | None:
    if b"\0" in data[:4096]:
        return None
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def scan(entries: Iterable[tuple[str, bytes | None]]) -> dict[str, object]:
    lua_files: list[str] = []
    natives: list[str] = []
    require_hints: list[dict[str, str]] = []
    indicators: dict[str, list[str]] = {key: [] for key in INDICATORS}

    for raw_name, data in entries:
        name = normalize(raw_name)
        suffix = PurePosixPath(name).suffix.lower()
        if suffix == ".dll":
            natives.append(name)
            continue
        if suffix != ".lua" or data is None:
            continue

        lua_files.append(name)
        source = decode_lua(data)
        if source is None:
            continue
        require_hints.extend({"source": name, "module": module} for module in RE_REQUIRE.findall(source))
        for key, pattern in INDICATORS.items():
            if pattern.search(source):
                indicators[key].append(name)

    lua_files.sort()
    return {
        "lua_files": lua_files,
        "config_files": [name for name in ("main.lua", "conf.lua") if name in lua_files],
        "require_hints": require_hints,
        "indicators": indicators,
        "native_candidates": sorted(natives),
    }


def directory_entries(root: Path) -> Iterable[tuple[str, bytes | None]]:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".lua", ".dll"}:
            continue
        name = path.relative_to(root).as_posix()
        if path.suffix.lower() == ".dll":
            yield name, None
            continue
        try:
            yield name, path.read_bytes()
        except OSError:
            continue


def zip_entries(raw: bytes) -> Iterable[tuple[str, bytes | None]]:
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            name = normalize(info.filename)
            suffix = PurePosixPath(name).suffix.lower()
            if suffix == ".dll":
                yield name, None
            elif suffix == ".lua":
                try:
                    yield name, archive.read(info)
                except (OSError, RuntimeError, zipfile.BadZipFile):
                    continue


def build_result(
    target: dict[str, object], classification: str, inventory: dict[str, object]
) -> dict[str, object]:
    root_main = "main.lua" in inventory["lua_files"]
    return {
        "target": target,
        "container": {"classification": classification},
        "love_evidence": {"root_main_lua": root_main},
        **inventory,
    }


def analyze_target(path: Path) -> dict[str, object]:
    if path.is_dir():
        inventory = scan(directory_entries(path))
        classification = "source-directory" if "main.lua" in inventory["lua_files"] else "unknown-directory"
        return build_result({"path": str(path.resolve()), "kind": "directory"}, classification, inventory)

    if not path.is_file():
        raise FileNotFoundError(path)

    raw = path.read_bytes()
    target = {
        "path": str(path.resolve()),
        "kind": "file",
        "size": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }

    if zipfile.is_zipfile(io.BytesIO(raw)):
        inventory = scan(zip_entries(raw))
        has_main = "main.lua" in inventory["lua_files"]
        is_pe = is_windows_pe(raw)
        classification = (
            "windows-fused-executable" if is_pe and has_main
            else "windows-pe-with-zip" if is_pe
            else "love-archive" if has_main and path.suffix.lower() == ".love"
            else "zip-with-root-main-lua" if has_main
            else "zip-non-love"
        )
        return build_result(target, classification, inventory)

    return build_result(
        target,
        "unsupported-or-unknown-windows-executable" if is_windows_pe(raw) else "unsupported-or-unknown-file",
        scan(()),
    )


def _self_test_zip() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("main.lua", "function love.update(dt) require('rules') end\n")
        archive.writestr("rules.lua", "return {}\n")
    return buffer.getvalue()


def _self_test_pe() -> bytes:
    data = bytearray(0x200)
    data[:2] = b"MZ"
    data[0x3C:0x40] = (0x80).to_bytes(4, "little")
    data[0x80:0x84] = b"PE\0\0"
    coff = 0x84
    data[coff : coff + 2] = (0x14C).to_bytes(2, "little")
    data[coff + 2 : coff + 4] = (1).to_bytes(2, "little")
    data[coff + 16 : coff + 18] = (0xE0).to_bytes(2, "little")
    data[coff + 20 : coff + 22] = (0x10B).to_bytes(2, "little")
    return bytes(data)


def run_self_test() -> int:
    payload = _self_test_zip()
    valid_pe = _self_test_pe()
    fake_pe = bytearray(0x100)
    fake_pe[:2] = b"MZ"
    fake_pe[0x3C:0x40] = (0x80).to_bytes(4, "little")
    fake_pe[0x80:0x84] = b"PE\0\0"

    assert is_windows_pe(valid_pe)
    assert not is_windows_pe(bytes(fake_pe))

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        love = root / "game.love"
        generic = root / "game.zip"
        fused = root / "game.exe"
        fake_fused = root / "fake.exe"
        love.write_bytes(payload)
        generic.write_bytes(payload)
        fused.write_bytes(valid_pe + payload)
        fake_fused.write_bytes(bytes(fake_pe) + payload)

        assert analyze_target(love)["container"]["classification"] == "love-archive"
        assert analyze_target(generic)["container"]["classification"] == "zip-with-root-main-lua"
        assert analyze_target(fused)["container"]["classification"] == "windows-fused-executable"
        assert analyze_target(fake_fused)["container"]["classification"] != "windows-fused-executable"

    print("love2d_triage self-test: OK")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only triage for Windows LÖVE source, .love, and fused PE artifacts."
    )
    parser.add_argument("target", type=Path, nargs="?")
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        if args.target is not None:
            parser.error("--self-test does not accept a target")
    elif args.target is None:
        parser.error("target is required unless --self-test is used")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return run_self_test()
    assert args.target is not None
    try:
        output = analyze_target(args.target)
    except (OSError, zipfile.BadZipFile) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
