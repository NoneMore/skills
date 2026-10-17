#!/usr/bin/env python3
"""Read-only triage for Windows LÖVE / Love2D game artifacts.

The helper classifies source directories, .love ZIP archives, and standard fused
Windows executables with an appended ZIP payload. It reports mechanical evidence
only; it does not execute the game, interpret gameplay semantics, inspect ambient
save directories, or modify target files.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import struct
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable


LUA_SUFFIXES = {".lua"}
CONFIG_NAMES = {"main.lua", "conf.lua"}
NATIVE_SUFFIXES = {".dll"}

RE_REQUIRE = re.compile(r"\brequire\s*(?:\(\s*)?['\"]([^'\"]+)['\"]")
RE_CUSTOM_RUN = re.compile(r"\b(?:function\s+love\.run\b|love\.run\s*=)")
RE_THREAD = re.compile(r"\blove\.thread\.newThread\s*\(")
RE_CHANNEL = re.compile(r"\b(?:love\.thread\.getChannel|love\.thread\.newChannel)\s*\(")
RE_SET_REQUIRE_PATH = re.compile(r"\blove\.filesystem\.setRequirePath\s*\(")
RE_SET_C_REQUIRE_PATH = re.compile(r"\blove\.filesystem\.setCRequirePath\s*\(")
RE_MOUNT = re.compile(r"\blove\.filesystem\.mount\s*\(")
RE_SET_IDENTITY = re.compile(r"\blove\.filesystem\.setIdentity\s*\(")
RE_APPEND_IDENTITY = re.compile(r"\bappendidentity\b")
RE_FFI = re.compile(r"\b(?:require\s*(?:\(\s*)?['\"]ffi['\"]|ffi\.(?:load|cdef)\b)")
RE_RANDOM = re.compile(r"\b(?:math\.random|love\.math\.(?:random|newRandomGenerator)|RandomGenerator)\b")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_directory(path: Path) -> str:
    """Hash a directory deterministically from relative paths + file hashes."""
    digest = hashlib.sha256()
    for child in sorted((p for p in path.rglob("*") if p.is_file()), key=lambda p: p.as_posix().lower()):
        rel = child.relative_to(path).as_posix().encode("utf-8", errors="surrogateescape")
        digest.update(struct.pack("<I", len(rel)))
        digest.update(rel)
        digest.update(bytes.fromhex(sha256_file(child)))
    return digest.hexdigest()


def read_text_bytes(data: bytes) -> str | None:
    if b"\x00" in data[:4096]:
        return None
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def normalize_zip_name(name: str) -> str:
    return str(PurePosixPath(name.replace("\\", "/")))


def zip_root_has_main(names: Iterable[str]) -> bool:
    normalized = {normalize_zip_name(name) for name in names if not name.endswith("/")}
    return "main.lua" in normalized


def locate_fused_zip(path: Path) -> tuple[int, bytes] | None:
    """Locate a valid appended ZIP by walking EOCD candidates from the end.

    A standard fused LÖVE executable is a PE followed by a .love ZIP. We avoid
    accepting the first local-file signature and instead require a parseable ZIP
    whose recovered root contains main.lua.
    """
    data = path.read_bytes()
    if not data.startswith(b"MZ"):
        return None

    eocd_sig = b"PK\x05\x06"
    search_end = len(data)
    while True:
        eocd = data.rfind(eocd_sig, 0, search_end)
        if eocd < 0:
            return None
        if eocd + 22 <= len(data):
            comment_len = int.from_bytes(data[eocd + 20 : eocd + 22], "little")
            zip_end = eocd + 22 + comment_len
            if zip_end <= len(data):
                # The ZIP start can be recovered from the central-directory offset.
                cd_size = int.from_bytes(data[eocd + 12 : eocd + 16], "little")
                cd_offset = int.from_bytes(data[eocd + 16 : eocd + 20], "little")
                zip_start = eocd - cd_size - cd_offset
                if 0 <= zip_start < eocd:
                    payload = data[zip_start:zip_end]
                    try:
                        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                            if zip_root_has_main(archive.namelist()):
                                return zip_start, payload
                    except (zipfile.BadZipFile, OSError):
                        pass
        search_end = eocd


def inventory_entries(entries: dict[str, bytes]) -> dict[str, object]:
    lua_files: list[str] = []
    config_files: list[str] = []
    native_candidates: list[str] = []
    require_edges: list[dict[str, str]] = []
    indicators: dict[str, list[str]] = {
        "custom_love_run": [],
        "thread_creation": [],
        "channel_use": [],
        "set_require_path": [],
        "set_c_require_path": [],
        "mount": [],
        "set_identity": [],
        "appendidentity": [],
        "rng": [],
        "ffi_native": [],
    }

    for name, data in sorted(entries.items()):
        norm = normalize_zip_name(name)
        suffix = PurePosixPath(norm).suffix.lower()
        if suffix in NATIVE_SUFFIXES:
            native_candidates.append(norm)
        if suffix not in LUA_SUFFIXES:
            continue

        lua_files.append(norm)
        if PurePosixPath(norm).name in CONFIG_NAMES and "/" not in norm:
            config_files.append(norm)

        text = read_text_bytes(data)
        if text is None:
            continue

        for module in RE_REQUIRE.findall(text):
            require_edges.append({"source": norm, "module": module})

        checks = {
            "custom_love_run": RE_CUSTOM_RUN,
            "thread_creation": RE_THREAD,
            "channel_use": RE_CHANNEL,
            "set_require_path": RE_SET_REQUIRE_PATH,
            "set_c_require_path": RE_SET_C_REQUIRE_PATH,
            "mount": RE_MOUNT,
            "set_identity": RE_SET_IDENTITY,
            "appendidentity": RE_APPEND_IDENTITY,
            "rng": RE_RANDOM,
            "ffi_native": RE_FFI,
        }
        for key, pattern in checks.items():
            if pattern.search(text):
                indicators[key].append(norm)

    return {
        "lua_files": lua_files,
        "config_files": config_files,
        "require_hints": require_edges,
        "indicators": indicators,
        "native_candidates": native_candidates,
    }


def entries_from_directory(root: Path) -> dict[str, bytes]:
    entries: dict[str, bytes] = {}
    for child in root.rglob("*"):
        if not child.is_file():
            continue
        rel = child.relative_to(root).as_posix()
        suffix = child.suffix.lower()
        if suffix in LUA_SUFFIXES or suffix in NATIVE_SUFFIXES:
            try:
                entries[rel] = child.read_bytes()
            except OSError:
                continue
    return entries


def entries_from_zip_bytes(payload: bytes) -> dict[str, bytes]:
    entries: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            norm = normalize_zip_name(info.filename)
            suffix = PurePosixPath(norm).suffix.lower()
            if suffix not in LUA_SUFFIXES and suffix not in NATIVE_SUFFIXES:
                continue
            try:
                entries[norm] = archive.read(info)
            except (OSError, RuntimeError, zipfile.BadZipFile):
                continue
    return entries


def analyze_target(path: Path) -> dict[str, object]:
    if path.is_dir():
        entries = entries_from_directory(path)
        classification = "source-directory" if "main.lua" in entries else "unknown-directory"
        result: dict[str, object] = {
            "target": {
                "path": str(path.resolve()),
                "kind": "directory",
                "sha256": sha256_directory(path),
            },
            "container": {"classification": classification},
            "love_evidence": {"root_main_lua": "main.lua" in entries},
        }
        result.update(inventory_entries(entries))
        return result

    if not path.is_file():
        raise FileNotFoundError(path)

    raw = path.read_bytes()
    target = {
        "path": str(path.resolve()),
        "kind": "file",
        "size": len(raw),
        "sha256": sha256_file(path),
    }

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            root_main = zip_root_has_main(archive.namelist())
            entries = entries_from_zip_bytes(raw)
        classification = "love-archive" if root_main else "zip-non-love"
        result = {
            "target": target,
            "container": {"classification": classification},
            "love_evidence": {"root_main_lua": root_main},
        }
        result.update(inventory_entries(entries))
        return result

    fused = locate_fused_zip(path)
    if fused is not None:
        offset, payload = fused
        entries = entries_from_zip_bytes(payload)
        result = {
            "target": target,
            "container": {
                "classification": "windows-fused-executable",
                "appended_love_offset": offset,
                "appended_love_size": len(payload),
                "appended_love_sha256": hashlib.sha256(payload).hexdigest(),
            },
            "love_evidence": {"root_main_lua": "main.lua" in entries},
        }
        result.update(inventory_entries(entries))
        return result

    classification = "unsupported-or-unknown-windows-executable" if raw.startswith(b"MZ") else "unsupported-or-unknown-file"
    return {
        "target": target,
        "container": {"classification": classification},
        "love_evidence": {"root_main_lua": False},
        "lua_files": [],
        "config_files": [],
        "require_hints": [],
        "indicators": {},
        "native_candidates": [],
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only triage for Windows LÖVE source directories, .love archives, and fused executables."
    )
    parser.add_argument("target", type=Path, help="Game directory, .love archive, or Windows executable")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result = analyze_target(args.target)
    except (OSError, zipfile.BadZipFile) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
