#!/usr/bin/env python3
"""Read-only mechanical triage for Windows LÖVE / Love2D artifacts."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

RE_REQUIRE = re.compile(r"\brequire\s*(?:\(\s*)?['\"]([^'\"]+)['\"]")
RE_CUSTOM_RUN = re.compile(r"\b(?:function\s+love\.run\b|love\.run\s*=)")
RE_RESOLUTION = re.compile(
    r"\blove\.filesystem\.(?:setRequirePath|setCRequirePath|mount|setIdentity)\s*\(|\bappendidentity\b"
)
RE_THREAD = re.compile(r"\blove\.thread\.(?:newThread|getChannel|newChannel)\s*\(")
RE_FFI = re.compile(r"\b(?:require\s*(?:\(\s*)?['\"]ffi['\"]|ffi\.(?:load|cdef)\b)")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_windows_pe(data: bytes) -> bool:
    if len(data) < 0x40 or not data.startswith(b"MZ"):
        return False
    offset = int.from_bytes(data[0x3C:0x40], "little")
    return 0 <= offset <= len(data) - 4 and data[offset : offset + 4] == b"PE\0\0"


def text(data: bytes) -> str | None:
    if b"\0" in data[:4096]:
        return None
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return None


def normalize(name: str) -> str:
    return str(PurePosixPath(name.replace("\\", "/")))


def inventory(lua_entries: dict[str, bytes], native_candidates: list[str]) -> dict[str, object]:
    require_hints: list[dict[str, str]] = []
    indicators = {
        "custom_love_run": [],
        "resolution_override": [],
        "thread_use": [],
        "ffi_native": [],
    }
    checks = {
        "custom_love_run": RE_CUSTOM_RUN,
        "resolution_override": RE_RESOLUTION,
        "thread_use": RE_THREAD,
        "ffi_native": RE_FFI,
    }

    for name, data in sorted(lua_entries.items()):
        source = text(data)
        if source is None:
            continue
        for module in RE_REQUIRE.findall(source):
            require_hints.append({"source": name, "module": module})
        for key, pattern in checks.items():
            if pattern.search(source):
                indicators[key].append(name)

    lua_files = sorted(lua_entries)
    return {
        "lua_files": lua_files,
        "config_files": [name for name in ("main.lua", "conf.lua") if name in lua_entries],
        "require_hints": require_hints,
        "indicators": indicators,
        "native_candidates": sorted(native_candidates),
    }


def directory_inputs(root: Path) -> tuple[dict[str, bytes], list[str]]:
    lua_entries: dict[str, bytes] = {}
    natives: list[str] = []
    for child in root.rglob("*"):
        if not child.is_file():
            continue
        rel = child.relative_to(root).as_posix()
        suffix = child.suffix.lower()
        if suffix == ".dll":
            natives.append(rel)
        elif suffix == ".lua":
            try:
                lua_entries[rel] = child.read_bytes()
            except OSError:
                pass
    return lua_entries, natives


def zip_inputs(raw: bytes) -> tuple[dict[str, bytes], list[str], bool]:
    lua_entries: dict[str, bytes] = {}
    natives: list[str] = []
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = [normalize(name) for name in archive.namelist() if not name.endswith("/")]
        for info in archive.infolist():
            if info.is_dir():
                continue
            name = normalize(info.filename)
            suffix = PurePosixPath(name).suffix.lower()
            if suffix == ".dll":
                natives.append(name)
            elif suffix == ".lua":
                try:
                    lua_entries[name] = archive.read(info)
                except (OSError, RuntimeError, zipfile.BadZipFile):
                    pass
    return lua_entries, natives, "main.lua" in names


def result(
    target: dict[str, object],
    classification: str,
    lua_entries: dict[str, bytes],
    natives: list[str],
    root_main: bool,
) -> dict[str, object]:
    output = {
        "target": target,
        "container": {"classification": classification},
        "love_evidence": {"root_main_lua": root_main},
    }
    output.update(inventory(lua_entries, natives))
    return output


def analyze_target(path: Path) -> dict[str, object]:
    if path.is_dir():
        lua_entries, natives = directory_inputs(path)
        root_main = "main.lua" in lua_entries
        return result(
            {"path": str(path.resolve()), "kind": "directory"},
            "source-directory" if root_main else "unknown-directory",
            lua_entries,
            natives,
            root_main,
        )

    if not path.is_file():
        raise FileNotFoundError(path)

    raw = path.read_bytes()
    target = {
        "path": str(path.resolve()),
        "kind": "file",
        "size": len(raw),
        "sha256": sha256(raw),
    }

    if zipfile.is_zipfile(io.BytesIO(raw)):
        lua_entries, natives, root_main = zip_inputs(raw)
        if is_windows_pe(raw):
            classification = "windows-fused-executable" if root_main else "windows-pe-with-zip"
        else:
            classification = "love-archive" if root_main else "zip-non-love"
        return result(target, classification, lua_entries, natives, root_main)

    return result(
        target,
        "unsupported-or-unknown-windows-executable" if is_windows_pe(raw) else "unsupported-or-unknown-file",
        {},
        [],
        False,
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only triage for Windows LÖVE source, .love, and fused PE artifacts."
    )
    parser.add_argument("target", type=Path)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
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
