#!/usr/bin/env python3
"""Read-only Unity player fingerprint probe with no third-party dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
from pathlib import Path
from typing import Any


UNITY_VERSION_RE = re.compile(rb"(?<!\d)((?:20\d{2}|[3-9])\.\d+\.\d+[abcfpx]\d+)(?!\d)")
LOADER_VERSION_RE = {
    "BepInEx": re.compile(r"\bBepInEx\s+(?:version\s+)?([0-9]+(?:\.[0-9A-Za-z-]+)+)", re.I),
    "MelonLoader": re.compile(r"\bMelonLoader\s+v?([0-9]+(?:\.[0-9A-Za-z-]+)+)", re.I),
}


def norm(path: Path) -> str:
    try:
        return str(path.resolve(strict=False))
    except OSError:
        return str(path.absolute())


def data_directories(root: Path) -> list[Path]:
    candidates: list[Path] = []
    if root.is_dir() and (root.name.endswith("_Data") or (root / "globalgamemanagers").is_file()):
        candidates.append(root)
    if root.is_dir():
        candidates.extend(path for path in root.glob("*_Data") if path.is_dir())
        mac_data = root / "Contents" / "Resources" / "Data"
        if mac_data.is_dir():
            candidates.append(mac_data)
        candidates.extend(
            path / "Contents" / "Resources" / "Data"
            for path in root.glob("*.app")
            if (path / "Contents" / "Resources" / "Data").is_dir()
        )
    seen: set[str] = set()
    result: list[Path] = []
    for path in candidates:
        key = norm(path)
        if key not in seen:
            seen.add(key)
            result.append(path)
    return result


def sha256(path: Path) -> str | None:
    try:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError:
        return None


def unity_version(data_dirs: list[Path]) -> tuple[str | None, str | None]:
    for data_dir in data_dirs:
        for name in ("globalgamemanagers", "data.unity3d"):
            path = data_dir / name
            if not path.is_file():
                continue
            try:
                with path.open("rb") as handle:
                    match = UNITY_VERSION_RE.search(handle.read(4 * 1024 * 1024))
                if match:
                    return match.group(1).decode("ascii"), norm(path)
            except OSError:
                continue
    return None, None


def binary_architecture(path: Path) -> str | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(4096)
        if len(header) >= 20 and header[:4] == b"\x7fELF":
            byte_order = {1: "<", 2: ">"}.get(header[5])
            if byte_order:
                machine = struct.unpack_from(f"{byte_order}H", header, 18)[0]
                return {
                    3: "x86",
                    40: "ARM",
                    62: "x64",
                    183: "ARM64",
                }.get(machine, f"ELF machine {machine}")
            return "ELF unknown"
        if len(header) >= 64 and header[:2] == b"MZ":
            pe_offset = struct.unpack_from("<I", header, 0x3C)[0]
            if pe_offset + 6 <= len(header) and header[pe_offset : pe_offset + 4] == b"PE\0\0":
                machine = struct.unpack_from("<H", header, pe_offset + 4)[0]
                return {
                    0x014C: "x86",
                    0x8664: "x64",
                    0x01C4: "ARM",
                    0xAA64: "ARM64",
                }.get(machine, f"PE machine 0x{machine:04x}")
        if len(header) >= 8:
            magic = header[:4]
            if magic in (b"\xca\xfe\xba\xbe", b"\xbe\xba\xfe\xca"):
                return "Mach-O universal"
            byte_order = {
                b"\xce\xfa\xed\xfe": "<",
                b"\xcf\xfa\xed\xfe": "<",
                b"\xfe\xed\xfa\xce": ">",
                b"\xfe\xed\xfa\xcf": ">",
            }.get(magic)
            if byte_order:
                cpu_type = struct.unpack_from(f"{byte_order}I", header, 4)[0]
                return {
                    7: "x86",
                    0x01000007: "x64",
                    12: "ARM",
                    0x0100000C: "ARM64",
                }.get(cpu_type, f"Mach-O CPU 0x{cpu_type:08x}")
    except (OSError, struct.error):
        return None
    return None


def executable_candidates(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    candidates: list[Path] = []
    for pattern in ("*.exe", "*.x86", "*.x86_64"):
        candidates.extend(path for path in root.glob(pattern) if path.is_file())
    for app in root.glob("*.app"):
        macos_dir = app / "Contents" / "MacOS"
        if macos_dir.is_dir():
            candidates.extend(path for path in macos_dir.iterdir() if path.is_file())
    return sorted(candidates, key=lambda path: ("unitycrashhandler" in path.name.lower(), path.name.lower()))


def detect_loader(root: Path) -> list[dict[str, Any]]:
    detected: list[dict[str, Any]] = []
    for name, folder, log_paths in (
        (
            "BepInEx",
            root / "BepInEx",
            (root / "BepInEx" / "LogOutput.log", root / "BepInEx" / "LogOutput.txt"),
        ),
        (
            "MelonLoader",
            root / "MelonLoader",
            tuple(sorted((root / "MelonLoader" / "Logs").glob("*.log"), reverse=True))
            if (root / "MelonLoader" / "Logs").is_dir()
            else (),
        ),
    ):
        if not folder.is_dir():
            continue
        version = None
        version_evidence = None
        for log_path in log_paths:
            if not log_path.is_file():
                continue
            try:
                text = log_path.read_text(encoding="utf-8", errors="replace")[:512_000]
            except OSError:
                continue
            match = LOADER_VERSION_RE[name].search(text)
            if match:
                version = match.group(1)
                version_evidence = norm(log_path)
                break
        detected.append(
            {
                "name": name,
                "version": version,
                "evidence": [norm(folder)] + ([version_evidence] if version_evidence else []),
            }
        )
    return detected


def inspect(root: Path) -> dict[str, Any]:
    root = root.resolve(strict=False)
    if not root.exists():
        raise FileNotFoundError(f"target does not exist: {root}")

    if root.is_file():
        scan_root = root.parent
    elif root.name.endswith("_Data"):
        scan_root = root.parent
    else:
        scan_root = root

    data_dirs = data_directories(root)
    for data_dir in data_directories(scan_root):
        if norm(data_dir) not in {norm(path) for path in data_dirs}:
            data_dirs.append(data_dir)
    mono_evidence: list[Path] = []
    il2cpp_evidence: list[Path] = []
    native_module: Path | None = None
    metadata: Path | None = None

    for data_dir in data_dirs:
        mono_evidence.extend(
            path
            for path in (
                data_dir / "Managed" / "Assembly-CSharp.dll",
                data_dir.parent / "MonoBleedingEdge",
                data_dir.parent / "Mono",
            )
            if path.exists()
        )
        metadata_candidate = data_dir / "il2cpp_data" / "Metadata" / "global-metadata.dat"
        if metadata_candidate.is_file():
            metadata = metadata or metadata_candidate
            il2cpp_evidence.append(metadata_candidate)

    native_roots = [scan_root] + [path.parent for path in data_dirs]
    for native_root in native_roots:
        for candidate in (
            native_root / "GameAssembly.dll",
            native_root / "GameAssembly.so",
            native_root / "libil2cpp.so",
            native_root / "UnityFramework",
            native_root / "Contents" / "Frameworks" / "UnityFramework.framework" / "UnityFramework",
        ):
            if candidate.is_file() and norm(candidate) not in {norm(path) for path in il2cpp_evidence}:
                native_module = native_module or candidate
                il2cpp_evidence.append(candidate)

    has_mono = any(path.name == "Assembly-CSharp.dll" for path in mono_evidence)
    has_il2cpp = metadata is not None and native_module is not None
    if has_mono and has_il2cpp:
        backend = "conflicting"
    elif has_il2cpp:
        backend = "IL2CPP"
    elif has_mono:
        backend = "Mono"
    else:
        backend = "unknown"

    executables = executable_candidates(root) if root.is_file() else executable_candidates(scan_root)
    arch_evidence = native_module or (executables[0] if executables else None)
    version, version_evidence = unity_version(data_dirs)

    warnings: list[str] = []
    if not data_dirs:
        warnings.append("No Unity data directory was found at the supplied level.")
    if backend == "conflicting":
        warnings.append("Mono and IL2CPP signals coexist; confirm with a loader log or loaded modules.")
    if backend == "unknown":
        warnings.append("Backend is unresolved; do not choose backend-specific references yet.")
    if version is None:
        warnings.append("Unity version was not found in the inspected data headers.")

    return {
        "root": norm(root),
        "backend": backend,
        "backend_evidence": {
            "mono": [norm(path) for path in mono_evidence],
            "il2cpp": [norm(path) for path in il2cpp_evidence],
        },
        "architecture": binary_architecture(arch_evidence) if arch_evidence else None,
        "architecture_evidence": norm(arch_evidence) if arch_evidence else None,
        "unity_version": version,
        "unity_version_evidence": version_evidence,
        "data_directories": [norm(path) for path in data_dirs],
        "executables": [norm(path) for path in executables],
        "loader": detect_loader(scan_root),
        "il2cpp_build_pair": {
            "native_module": norm(native_module) if native_module else None,
            "native_sha256": sha256(native_module) if native_module else None,
            "metadata": norm(metadata) if metadata else None,
            "metadata_sha256": sha256(metadata) if metadata else None,
        }
        if metadata or native_module
        else None,
        "warnings": warnings,
    }


def human_report(report: dict[str, Any]) -> str:
    lines = [
        f"Root: {report['root']}",
        f"Backend: {report['backend']}",
        f"Architecture: {report['architecture'] or 'unknown'}",
        f"Unity version: {report['unity_version'] or 'unknown'}",
    ]
    loaders = report["loader"]
    if loaders:
        lines.append("Loader: " + ", ".join(f"{item['name']} {item['version'] or '(version unknown)'}" for item in loaders))
    else:
        lines.append("Loader: none detected")
    if report["warnings"]:
        lines.append("Warnings:")
        lines.extend(f"  - {warning}" for warning in report["warnings"])
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect a Unity game directory without modifying it.")
    parser.add_argument("game_root", type=Path, help="Game root, .app bundle, *_Data directory, or executable")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        report = inspect(args.game_root)
    except (FileNotFoundError, PermissionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True) if args.json else human_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
