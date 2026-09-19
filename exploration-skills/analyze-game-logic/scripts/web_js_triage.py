"""Mechanical Web/JavaScript reverse-engineering triage.

The helper never edits source inputs or source maps. It inventories one or more
Web/JavaScript files/directories and records reproducibility/provenance metadata.
Lean retention stages generated output temporarily, promotes only selected
canonical views, formats those views in place, and removes verified raw staging
copies. All retention preserves the prior parallel raw + formatted-copy behavior.

Third-party tools process untrusted syntax. Prefer a constrained analysis
container/VM with no credentials and no network access when the input is not
trusted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple
from urllib.parse import unquote, urlsplit


PINNED = {
    "webcrack": ("webcrack", "webcrack", "2.16.0"),
    "wakaru": ("wakaru", "@wakaru/cli", "1.10.0"),
    "prettier": ("prettier", "prettier", "3.9.6"),
}

CODE_SUFFIXES = {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
WEB_ARTIFACT_SUFFIXES = CODE_SUFFIXES | {
    ".map", ".html", ".htm", ".json", ".wasm", ".asar"
}
FORMAT_SUFFIXES = CODE_SUFFIXES | {".json"}
HELPER_VERSION = "v4.4.1"
MANIFEST_SCHEMA = 2
SOURCE_MAPPING_LINE_RE = re.compile(
    r"(?m)^[ \t]*//[#@][ \t]*sourceMappingURL[ \t]*=[ \t]*([^\r\n]+?)[ \t]*$"
)
SOURCE_MAPPING_BLOCK_RE = re.compile(
    r"/\*[#@]\s*sourceMappingURL\s*=\s*([^*\r\n]+?)\s*\*/"
)
WINDOWS_DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")
SKIPPED_DIRECTORY_NAMES = {".git", "node_modules"}
OBFUSCATED_IDENTIFIER_RE = re.compile(r"\b_0x[0-9A-Fa-f]{4,}\b")
ENCODED_ESCAPE_RE = re.compile(r"\\(?:x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4})")
PACKER_RE = re.compile(r"eval\s*\(\s*function\s*\(\s*p\s*,\s*a\s*,\s*c\s*,\s*k", re.I)
DYNAMIC_DECODER_RE = re.compile(r"(?:String\.fromCharCode|atob\s*\(|decodeURIComponent\s*\()")
MANAGED_TOP_LEVEL = {
    ".staging",
    "logs",
    "webcrack",
    "wakaru",
    "wakaru-source-aware",
    "sourcemap-sources",
    "pretty",
    "triage-manifest.json",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def command_text(argv: Sequence[str]) -> str:
    # Reproducibility display only. subprocess is always invoked without shell.
    return " ".join(json.dumps(part) for part in argv)


def workspace_bin_dirs(workspace: Path) -> List[Path]:
    """Return nearest-first workspace/ancestor node_modules/.bin directories."""
    resolved = workspace.expanduser().resolve()
    dirs: List[Path] = []
    seen: Set[Path] = set()
    for base in (resolved,) + tuple(resolved.parents):
        candidate = base / "node_modules" / ".bin"
        if candidate.is_dir() and candidate not in seen:
            seen.add(candidate)
            dirs.append(candidate)
    return dirs


def resolve_tool(
    name: str,
    allow_npx: bool,
    local_bin_dirs: Sequence[Path] = (),
) -> Optional[List[str]]:
    """Resolve workspace-local, PATH-installed, then optionally pinned npx tools."""
    binary, package, version = PINNED[name]
    for bin_dir in local_bin_dirs:
        found = shutil.which(binary, path=str(bin_dir))
        if found:
            return [found]
    found = shutil.which(binary)
    if found:
        return [found]
    if allow_npx:
        npx = shutil.which("npx")
        if npx:
            return [npx, "--yes", "%s@%s" % (package, version)]
    return None


def is_npx_prefix(prefix: Sequence[str]) -> bool:
    if not prefix:
        return False
    return Path(prefix[0]).name.lower() in {"npx", "npx.cmd", "npx.exe"}


def tool_version(prefix: Sequence[str], timeout: int) -> Optional[str]:
    for flag in ("--version", "-V"):
        try:
            proc = subprocess.run(
                list(prefix) + [flag],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=timeout,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            continue
        text = (proc.stdout or "").strip()
        if proc.returncode == 0 and text:
            return text.splitlines()[0][:200]
    return None


def node_version(timeout: int) -> Optional[str]:
    node = shutil.which("node")
    if not node:
        return None
    return tool_version([node], timeout)


def run_step(
    name: str,
    argv: Sequence[str],
    cwd: Path,
    logs: Path,
    timeout: int,
    dry_run: bool,
    metadata: Optional[Mapping[str, object]] = None,
    retain_success_log: bool = True,
) -> Dict[str, object]:
    record: Dict[str, object] = {
        "name": name,
        "command": list(argv),
        "command_display": command_text(argv),
        "started_unix": int(time.time()),
    }
    if metadata:
        record.update(metadata)
    print("[%s] %s" % (name, record["command_display"]))
    if dry_run:
        record.update({"status": "dry-run", "returncode": None})
        return record

    logs.mkdir(parents=True, exist_ok=True)
    log_path = logs / (name.replace("/", "_") + ".log")
    try:
        with log_path.open("w", encoding="utf-8", errors="replace") as log:
            proc = subprocess.run(
                list(argv),
                cwd=str(cwd),
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                check=False,
                text=True,
            )
        status = "ok" if proc.returncode == 0 else "failed"
        record.update({"status": status, "returncode": proc.returncode})
        if status == "ok" and not retain_success_log:
            try:
                log_path.unlink()
                record["log_retained"] = False
            except OSError as exc:
                record.update(
                    {
                        "log": str(log_path),
                        "log_retained": True,
                        "log_cleanup_error": str(exc),
                    }
                )
        else:
            record.update({"log": str(log_path), "log_retained": True})
    except subprocess.TimeoutExpired:
        record.update(
            {
                "status": "timeout",
                "returncode": None,
                "log": str(log_path),
                "log_retained": True,
            }
        )
    except OSError as exc:
        record.update({"status": "error", "returncode": None, "error": str(exc)})
        if log_path.exists():
            record.update({"log": str(log_path), "log_retained": True})
    record["finished_unix"] = int(time.time())
    return record


def copy_generated_tree(
    src: Path,
    dst: Path,
    skipped_symlinks: Optional[List[str]] = None,
) -> int:
    """Copy regular generated files without dereferencing symlinks."""
    if not src.exists() and not src.is_symlink():
        return 0
    if src.is_symlink():
        if skipped_symlinks is not None:
            skipped_symlinks.append(str(src))
        return 0
    count = 0
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return 1
    for path in src.rglob("*"):
        if path.is_symlink():
            if skipped_symlinks is not None:
                skipped_symlinks.append(str(path))
            continue
        if not path.is_file():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        count += 1
    return count


def regular_file_inventory(root: Path) -> Dict[str, Tuple[int, str]]:
    """Return relative-path -> (size, sha256) for regular files, ignoring symlinks."""
    if not root.exists() or root.is_symlink():
        return {}
    if root.is_file():
        return {".": (root.stat().st_size, sha256_file(root))}
    records: Dict[str, Tuple[int, str]] = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        records[str(path.relative_to(root))] = (path.stat().st_size, sha256_file(path))
    return records


def verify_generated_copy(src: Path, dst: Path) -> bool:
    return regular_file_inventory(src) == regular_file_inventory(dst)


def remove_generated_path(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        return
    if path.is_symlink() or path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


def detect_obvious_obfuscation(path: Path) -> Dict[str, object]:
    """Cheap signal check used only to decide whether lean mode should add webcrack."""
    sample_limit = 1024 * 1024
    try:
        size = path.stat().st_size
        with path.open("rb") as handle:
            if size <= sample_limit:
                data = handle.read()
            else:
                half = sample_limit // 2
                head = handle.read(half)
                handle.seek(max(0, size - half))
                data = head + b"\n" + handle.read(half)
    except OSError as exc:
        return {"obvious": False, "signals": [], "error": str(exc)}

    text = data.decode("utf-8", errors="replace")
    signals: List[str] = []
    obfuscated_ids = len(OBFUSCATED_IDENTIFIER_RE.findall(text))
    encoded_escapes = len(ENCODED_ESCAPE_RE.findall(text))
    dynamic_decoders = len(DYNAMIC_DECODER_RE.findall(text))

    if "javascript-obfuscator" in text.lower():
        signals.append("javascript-obfuscator-marker")
    if PACKER_RE.search(text):
        signals.append("packer-eval-wrapper")
    if obfuscated_ids >= 8:
        signals.append("many-_0x-identifiers")
    if encoded_escapes >= 40 and dynamic_decoders >= 2:
        signals.append("dense-encoded-strings-with-decoders")
    if obfuscated_ids >= 4 and encoded_escapes >= 20:
        signals.append("mixed-obfuscated-identifiers-and-encoded-strings")

    return {
        "obvious": bool(signals),
        "signals": signals,
        "sampled_bytes": len(data),
        "file_size": size,
        "counts": {
            "obfuscated_identifiers": obfuscated_ids,
            "encoded_escapes": encoded_escapes,
            "dynamic_decoders": dynamic_decoders,
        },
    }


def unique_format_candidates(paths: Sequence[Path]) -> List[Path]:
    seen: Set[Path] = set()
    result: List[Path] = []
    for root in paths:
        candidates = [root] if root.is_file() else format_candidates(root)
        for path in candidates:
            if path.is_symlink() or not path.is_file() or path.suffix.lower() not in FORMAT_SUFFIXES:
                continue
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                result.append(resolved)
    return sorted(result)


def format_candidates(root: Path) -> List[Path]:
    if not root.exists() or root.is_symlink():
        return []
    return [
        p
        for p in sorted(root.rglob("*"))
        if not p.is_symlink() and p.is_file() and p.suffix.lower() in FORMAT_SUFFIXES
    ]


def command_arg_length(argv: Sequence[str]) -> int:
    """Estimate command-line size using platform-appropriate quoting."""
    if os.name == "nt":
        return len(subprocess.list2cmdline(list(argv))) + 1
    return sum(len(os.fsencode(arg)) + 1 for arg in argv)


def prettier_command_budget() -> int:
    # Keep ample headroom for Windows cmd/npm shims and POSIX environment/ARG_MAX.
    if os.name == "nt":
        return 7000
    return 100_000


def relative_command_path(path: Path, cwd: Path) -> str:
    try:
        return os.path.relpath(str(path), str(cwd))
    except ValueError:
        # Different Windows drive: relative paths are impossible.
        return str(path)


def command_path_batches(
    paths: Sequence[Path],
    base_argv: Sequence[str],
    cwd: Path,
    budget: Optional[int] = None,
) -> Iterable[List[str]]:
    """Batch path arguments by encoded command size instead of file count."""
    limit = prettier_command_budget() if budget is None else budget
    if limit <= command_arg_length(base_argv):
        raise ValueError("command budget is too small for the fixed command arguments")
    current: List[str] = []
    for path in paths:
        arg = relative_command_path(path, cwd)
        proposed = current + [arg]
        if current and command_arg_length(list(base_argv) + proposed) > limit:
            yield current
            current = [arg]
        else:
            current = proposed
    if current:
        yield current


def safe_slug(path: Path) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", path.name).strip("-.") or "input"
    digest = hashlib.sha256(str(path).encode("utf-8", errors="surrogatepass")).hexdigest()[:10]
    return "%s-%s" % (stem[:80], digest)


def is_web_artifact(path: Path) -> bool:
    if path.name.lower() in {"package.json", "manifest.json"}:
        return True
    return path.suffix.lower() in WEB_ARTIFACT_SUFFIXES


def artifact_role(path: Path) -> str:
    suffix = path.suffix.lower()
    name = path.name.lower()
    if suffix in CODE_SUFFIXES:
        return "code"
    if suffix == ".map":
        return "source-map"
    if suffix in {".html", ".htm"}:
        return "bootstrap-html"
    if suffix == ".wasm":
        return "webassembly"
    if suffix == ".asar" or name == "app.asar":
        return "electron-asar"
    if suffix == ".json":
        return "config-or-manifest"
    return "supporting"


def collect_inputs(paths: Sequence[Path]) -> Tuple[List[Path], List[Path], List[Path]]:
    """Collect regular web artifacts while preserving explicit input/source order."""
    roots: List[Path] = []
    inventory: List[Path] = []
    code: List[Path] = []
    inventory_seen: Set[Path] = set()
    code_seen: Set[Path] = set()

    def add_candidate(candidate: Path) -> None:
        if candidate.is_symlink() or not candidate.is_file() or not is_web_artifact(candidate):
            return
        resolved = candidate.resolve()
        if resolved not in inventory_seen:
            inventory_seen.add(resolved)
            inventory.append(resolved)
        if resolved.suffix.lower() in CODE_SUFFIXES and resolved not in code_seen:
            code_seen.add(resolved)
            code.append(resolved)

    for raw in paths:
        expanded = raw.expanduser()
        if expanded.is_symlink():
            raise ValueError("input symlinks are not allowed: %s" % expanded)
        path = expanded.resolve()
        if not path.exists():
            raise ValueError("input does not exist: %s" % path)
        roots.append(path)
        if path.is_file():
            add_candidate(path)
            continue
        if not path.is_dir():
            raise ValueError("input must be a file or directory: %s" % path)

        for current, dirnames, filenames in os.walk(path, topdown=True, followlinks=False):
            current_path = Path(current)
            kept_dirs: List[str] = []
            for dirname in sorted(dirnames):
                child = current_path / dirname
                if dirname.lower() in SKIPPED_DIRECTORY_NAMES or child.is_symlink():
                    continue
                kept_dirs.append(dirname)
            dirnames[:] = kept_dirs
            for filename in sorted(filenames):
                add_candidate(current_path / filename)

    return roots, inventory, code


def source_mapping_url(path: Path) -> Optional[str]:
    try:
        size = path.stat().st_size
        with path.open("rb") as handle:
            truncated = size > 256 * 1024
            if truncated:
                handle.seek(size - 256 * 1024)
            text = handle.read().decode("utf-8", errors="replace")
    except OSError:
        return None

    if truncated:
        # Do not treat the first partial line in the tail buffer as a directive.
        newline = text.find("\n")
        text = text[newline + 1 :] if newline >= 0 else ""

    matches: List[Tuple[int, str]] = []
    for regex in (SOURCE_MAPPING_LINE_RE, SOURCE_MAPPING_BLOCK_RE):
        for match in regex.finditer(text):
            value = match.group(1).strip().strip('"\'')
            if value:
                matches.append((match.start(), value))
    if not matches:
        return None
    return max(matches, key=lambda item: item[0])[1]


def source_map_metadata(path: Path) -> Dict[str, object]:
    result: Dict[str, object] = {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError) as exc:
        result["parse_error"] = str(exc)
        return result
    if not isinstance(data, dict):
        result["parse_error"] = "top-level source map value is not an object"
        return result
    result["version"] = data.get("version")
    result["file"] = data.get("file")
    sources = data.get("sources")
    sources_content = data.get("sourcesContent")
    names = data.get("names")
    result["source_count"] = len(sources) if isinstance(sources, list) else None
    result["sources_content_count"] = (
        len(sources_content) if isinstance(sources_content, list) else None
    )
    result["name_count"] = len(names) if isinstance(names, list) else None
    return result


def local_mapping_url_path(source: Path, url: str) -> Optional[Path]:
    value = url.strip().strip('"\'')
    lowered = value.lower()
    if lowered.startswith("data:"):
        return None

    if WINDOWS_DRIVE_RE.match(value) or value.startswith("\\\\"):
        if os.name != "nt":
            return None
        candidate = Path(value)
    else:
        parts = urlsplit(value)
        if parts.scheme not in ("", "file"):
            return None
        raw_path = unquote(parts.path)
        if parts.scheme == "file":
            if os.name == "nt":
                if parts.netloc and parts.netloc.lower() != "localhost":
                    raw_path = "//%s%s" % (parts.netloc, raw_path)
                elif re.match(r"^/[A-Za-z]:/", raw_path):
                    raw_path = raw_path[1:]
            elif parts.netloc and parts.netloc.lower() != "localhost":
                return None
        if not raw_path:
            return None
        candidate = Path(raw_path)
        if not candidate.is_absolute():
            candidate = source.parent / candidate
    # Keep the final path component unresolved so callers can detect/reject symlinks.
    return candidate.absolute()


def path_within(path: Path, roots: Sequence[Path]) -> bool:
    if not roots:
        return True
    resolved = path.resolve()
    for root in roots:
        base = root.resolve()
        if resolved == base or base in resolved.parents:
            return True
    return False


def map_match_score(
    source: Path,
    map_path: Path,
    metadata: Mapping[str, object],
) -> Tuple[int, str]:
    same_parent = map_path.parent == source.parent
    declared = metadata.get("file")
    if isinstance(declared, str) and re.split(r"[\\/]", declared)[-1] == source.name:
        return (95 if same_parent else 90), "source-map-file-field-match"
    if map_path.name == source.name + ".map":
        return (
            (85 if same_parent else 80),
            "adjacent-name-match" if same_parent else "name-match",
        )
    return 0, "unverified"


def associate_source_maps(
    sources: Sequence[Path],
    explicit_maps: Sequence[Path],
    inventory_maps: Sequence[Path],
    explicit_bindings: Optional[Mapping[Path, Path]] = None,
    allow_pairwise_explicit: bool = False,
    automatic_map_roots: Sequence[Path] = (),
) -> Dict[Path, Dict[str, object]]:
    explicit_bindings = explicit_bindings or {}
    explicit: List[Path] = []
    inventory: List[Path] = []
    seen_explicit: Set[Path] = set()
    seen_inventory: Set[Path] = set()
    for raw in explicit_maps:
        resolved = raw.expanduser().resolve()
        if resolved not in seen_explicit:
            seen_explicit.add(resolved)
            explicit.append(resolved)
    for raw in inventory_maps:
        resolved = raw.expanduser().resolve()
        if resolved not in seen_inventory and resolved not in seen_explicit:
            seen_inventory.add(resolved)
            inventory.append(resolved)

    metadata_cache: Dict[Path, Dict[str, object]] = {}
    detail_cache: Dict[Path, Dict[str, object]] = {}

    def metadata(path: Path) -> Dict[str, object]:
        if path not in metadata_cache:
            metadata_cache[path] = source_map_metadata(path)
        return metadata_cache[path]

    def details(path: Path) -> Dict[str, object]:
        if path not in detail_cache:
            detail_cache[path] = {
                "path": str(path),
                "size": path.stat().st_size,
                "sha256": sha256_file(path),
                "metadata": metadata(path),
            }
        return dict(detail_cache[path])

    def selected(path: Path, association: str, url: Optional[str]) -> Dict[str, object]:
        record: Dict[str, object] = {
            "association": association,
            "source_mapping_url": url,
        }
        record.update(details(path))
        return record

    def best_candidate(
        source: Path,
        pool: Sequence[Path],
        origin: str,
        url: Optional[str],
    ) -> Optional[Dict[str, object]]:
        scored: List[Tuple[int, str, Path]] = []
        for map_path in pool:
            if not map_path.is_file() or map_path.is_symlink():
                continue
            score, status = map_match_score(source, map_path, metadata(map_path))
            if score:
                scored.append((score, status, map_path))
        if not scored:
            return None
        top_score = max(item[0] for item in scored)
        top = [item for item in scored if item[0] == top_score]
        if len(top) > 1:
            return {
                "association": "ambiguous-%s" % origin,
                "source_mapping_url": url,
                "path": None,
                "candidates": [
                    str(item[2]) for item in sorted(top, key=lambda item: str(item[2]))
                ],
            }
        _, status, chosen = top[0]
        return selected(chosen, "%s-%s" % (origin, status), url)

    normalized_bindings: Dict[Path, Path] = {
        source.expanduser().resolve(): map_path.expanduser().resolve()
        for source, map_path in explicit_bindings.items()
    }
    pairwise = (
        allow_pairwise_explicit
        and not normalized_bindings
        and len(sources) == len(explicit)
        and len(sources) > 1
    )
    single_explicit = len(sources) == 1 and len(explicit) == 1

    result: Dict[Path, Dict[str, object]] = {}
    for index, raw_source in enumerate(sources):
        source = raw_source.expanduser().resolve()
        url = source_mapping_url(source)

        if source in normalized_bindings:
            result[raw_source] = selected(
                normalized_bindings[source], "explicit-source-binding", url
            )
            continue
        if pairwise:
            result[raw_source] = selected(explicit[index], "explicit-pairwise", url)
            continue
        if single_explicit:
            result[raw_source] = selected(explicit[0], "explicit-single-source", url)
            continue

        if url and url.lower().startswith("data:"):
            result[raw_source] = {
                "association": "inline-data-uri",
                "source_mapping_url": url[:200],
                "path": None,
            }
            continue

        explicit_match = best_candidate(source, explicit, "explicit", url)
        if explicit_match is not None:
            result[raw_source] = explicit_match
            continue

        linked = local_mapping_url_path(source, url) if url else None
        linked_rejection: Optional[Dict[str, object]] = None
        if linked is not None:
            if linked.is_symlink():
                linked_rejection = {
                    "association": "linked-map-symlink-rejected",
                    "source_mapping_url": url,
                    "path": str(linked),
                }
            elif not path_within(linked, automatic_map_roots):
                linked_rejection = {
                    "association": "linked-map-outside-input-root",
                    "source_mapping_url": url,
                    "path": str(linked),
                }
            elif linked.is_file():
                result[raw_source] = selected(
                    linked, "linked-by-sourceMappingURL", url
                )
                continue

        inventory_match = best_candidate(source, inventory, "inventory", url)
        if inventory_match is not None:
            result[raw_source] = inventory_match
            continue

        if linked_rejection is not None:
            result[raw_source] = linked_rejection
            continue
        if linked is not None and not linked.is_file():
            result[raw_source] = {
                "association": (
                    "linked-map-not-file" if linked.exists() else "linked-map-missing"
                ),
                "source_mapping_url": url,
                "path": str(linked),
            }
            continue

        result[raw_source] = {
            "association": "none",
            "source_mapping_url": url,
            "path": None,
        }
    return result


def remove_managed_path(out: Path, name: str) -> None:
    if name not in MANAGED_TOP_LEVEL:
        raise ValueError("refusing to remove unmanaged path: %s" % name)
    target = out / name
    if not target.exists() and not target.is_symlink():
        return
    if target.is_symlink() or target.is_file():
        target.unlink()
    else:
        shutil.rmtree(target)


def recognizable_prior_manifest(out: Path) -> bool:
    manifest = out / "triage-manifest.json"
    if not manifest.is_file():
        return False
    try:
        data = json.loads(manifest.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return False
    if not isinstance(data, dict):
        return False
    if data.get("schema") == MANIFEST_SCHEMA and data.get("helper_version") in {
        "v4.3.1", "v4.4.0", HELPER_VERSION
    }:
        return True
    # Backward-compatible recognition of the v4.3 helper manifest.
    return data.get("schema") == 1 and "tools" in data and "steps" in data and "source" in data


def validate_managed_cleanup(out: Path) -> None:
    ambiguous = [
        name
        for name in MANAGED_TOP_LEVEL - {"triage-manifest.json"}
        if (out / name).exists() or (out / name).is_symlink()
    ]
    if ambiguous and not recognizable_prior_manifest(out):
        raise ValueError(
            "refusing --force cleanup because helper-managed names already exist "
            "without a recognizable prior triage manifest: %s"
            % ", ".join(sorted(ambiguous))
        )


def clean_managed_outputs(out: Path) -> None:
    validate_managed_cleanup(out)
    for name in sorted(MANAGED_TOP_LEVEL):
        remove_managed_path(out, name)


def generated_provenance(path: Path, out: Path) -> str:
    try:
        rel = path.relative_to(out)
    except ValueError:
        return "generated"
    top = rel.parts[0] if rel.parts else ""
    return {
        ".staging": "temporary-staging",
        "logs": "tool-log",
        "webcrack": "webcrack-generated-view",
        "wakaru": "wakaru-generated-view",
        "wakaru-source-aware": "wakaru-source-map-generated-view",
        "sourcemap-sources": "source-map-extracted-source",
        "pretty": "prettier-formatted-copy",
    }.get(top, "generated")


def generated_artifact_inventory(out: Path) -> List[Dict[str, object]]:
    records: List[Dict[str, object]] = []
    if not out.exists() or out.is_symlink():
        return records
    for name in sorted(MANAGED_TOP_LEVEL - {"triage-manifest.json"}):
        root = out / name
        if root.is_symlink():
            continue
        if root.is_file():
            paths = [root]
        elif root.is_dir():
            paths = [
                path
                for path in sorted(root.rglob("*"))
                if not path.is_symlink() and path.is_file()
            ]
        else:
            paths = []
        for path in paths:
            records.append(
                {
                    "path": str(path.relative_to(out)),
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                    "provenance": generated_provenance(path, out),
                }
            )
    return records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Inventory and run reproducible webcrack/Wakaru/Prettier triage on "
            "one or more Web/JavaScript files or directories"
        )
    )
    parser.add_argument(
        "input",
        nargs="*",
        type=Path,
        help="source JS/TS file, bundle/chunk, or directory to inventory",
    )
    parser.add_argument(
        "--source-map",
        type=Path,
        action="append",
        default=[],
        help=(
            "unbound source map candidate (repeatable); when all inputs are direct code files "
            "and counts match, values are paired in command-line order"
        ),
    )
    parser.add_argument(
        "--source-map-for",
        action="append",
        default=[],
        metavar="SOURCE=MAP",
        help="explicitly bind one source file to one source map (repeatable)",
    )
    parser.add_argument("--out", type=Path, help="artifact output directory")
    parser.add_argument(
        "--workspace",
        type=Path,
        help="workspace used to resolve node_modules/.bin tools (default: current directory)",
    )
    parser.add_argument(
        "--wakaru-mode",
        choices=("inspect", "strict", "normal"),
        default="inspect",
        help="bundle unpack mode (default: inspect; inspection output may not preserve init order)",
    )
    parser.add_argument(
        "--retention",
        choices=("lean", "all"),
        default="lean",
        help=(
            "generated-output retention policy (default: lean; all preserves the prior "
            "parallel raw + formatted-copy behavior)"
        ),
    )
    parser.add_argument(
        "--force-webcrack",
        action="store_true",
        help="run and retain webcrack for every code input in lean mode",
    )
    parser.add_argument("--skip-webcrack", action="store_true")
    parser.add_argument("--skip-wakaru", action="store_true")
    parser.add_argument("--skip-prettier", action="store_true")
    parser.add_argument(
        "--allow-npx",
        action="store_true",
        help="download/use pinned npm packages with npx when workspace/PATH tools are absent",
    )
    parser.add_argument(
        "--require-tools",
        action="store_true",
        help="fail if any requested tool cannot be resolved",
    )
    parser.add_argument(
        "--timeout", type=int, default=300, help="seconds per tool invocation"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show planned tool invocations without creating, deleting, copying, or writing files",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="reuse a non-empty output directory after clearing helper-managed artifacts",
    )
    parser.add_argument("--self-test", action="store_true")
    return parser


def parse_source_map_bindings(values: Sequence[str]) -> Dict[Path, Path]:
    bindings: Dict[Path, Path] = {}
    for value in values:
        if "=" not in value:
            raise ValueError("--source-map-for must use SOURCE=MAP syntax: %s" % value)
        source_text, map_text = value.rsplit("=", 1)
        if not source_text or not map_text:
            raise ValueError(
                "--source-map-for must use non-empty SOURCE=MAP syntax: %s" % value
            )
        source = Path(source_text).expanduser()
        map_path = Path(map_text).expanduser()
        if source.is_symlink():
            raise ValueError(
                "source-map binding source symlinks are not allowed: %s" % source
            )
        if map_path.is_symlink():
            raise ValueError(
                "source-map binding map symlinks are not allowed: %s" % map_path
            )
        source = source.resolve()
        map_path = map_path.resolve()
        if source in bindings:
            raise ValueError("duplicate --source-map-for binding for: %s" % source)
        bindings[source] = map_path
    return bindings


def self_test() -> int:
    import contextlib
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "input.js"
        source.write_text(
            "const x=1;\n//# sourceMappingURL=input.js.map\n", encoding="utf-8"
        )
        source_map = root / "input.js.map"
        source_map.write_text(
            json.dumps(
                {"version": 3, "file": "input.js", "sources": ["src.ts"], "names": []}
            ),
            encoding="utf-8",
        )
        assert len(sha256_file(source)) == 64
        assert source_mapping_url(source) == "input.js.map"
        # Linked maps are discovered even when a single-file input did not inventory the .map.
        assoc = associate_source_maps(
            [source], [], [], automatic_map_roots=[source.parent]
        )
        assert assoc[source]["association"] == "linked-by-sourceMappingURL"

        fake = root / "fake.js"
        fake.write_text(
            'const s = "sourceMappingURL=not-a-map.map";\n', encoding="utf-8"
        )
        assert source_mapping_url(fake) is None

        plain = root / "plain.js"
        plain.write_text("const answer = () => 42;\n", encoding="utf-8")
        assert detect_obvious_obfuscation(plain)["obvious"] is False
        obfuscated = root / "obfuscated.js"
        obfuscated.write_text(
            "var _0x1234=['\\x61','\\x62'];"
            + ";".join("_0x%04x=_0x1234[0]" % i for i in range(16)),
            encoding="utf-8",
        )
        assert detect_obvious_obfuscation(obfuscated)["obvious"] is True

        lean_logs = root / "lean-logs"
        step = run_step(
            "success-log-test",
            [sys.executable, "-c", "print('ok')"],
            root,
            lean_logs,
            30,
            False,
            retain_success_log=False,
        )
        assert step["status"] == "ok" and step.get("log_retained") is False
        assert not any(lean_logs.glob("*.log"))

        # Explicit direct-file pairing follows CLI/source order rather than sorted path order.
        b_source = root / "b.js"
        a_source = root / "a.js"
        b_source.write_text("", encoding="utf-8")
        a_source.write_text("", encoding="utf-8")
        b_map = root / "b.custom.map"
        a_map = root / "a.custom.map"
        for map_path, file_name in ((b_map, "b.js"), (a_map, "a.js")):
            map_path.write_text(
                json.dumps({"version": 3, "file": file_name}), encoding="utf-8"
            )
        _, _, ordered_code = collect_inputs([b_source, a_source])
        assert ordered_code == [b_source.resolve(), a_source.resolve()]
        paired = associate_source_maps(
            ordered_code, [b_map, a_map], [], allow_pairwise_explicit=True
        )
        assert paired[b_source.resolve()]["path"] == str(b_map.resolve())
        assert paired[a_source.resolve()]["path"] == str(a_map.resolve())

        # Equal-score heuristic matches are surfaced as ambiguous instead of guessed.
        ambiguous_source = root / "ambiguous.js"
        ambiguous_source.write_text("const ambiguous = true;\n", encoding="utf-8")
        maps1 = root / "maps1"
        maps2 = root / "maps2"
        maps1.mkdir()
        maps2.mkdir()
        m1 = maps1 / "x.map"
        m2 = maps2 / "y.map"
        for p in (m1, m2):
            p.write_text(
                json.dumps({"version": 3, "file": "ambiguous.js"}), encoding="utf-8"
            )
        ambiguous = associate_source_maps([ambiguous_source], [], [m1, m2])
        assert ambiguous[ambiguous_source]["association"] == "ambiguous-inventory"
        assert ambiguous[ambiguous_source]["path"] is None

        generated = root / "generated"
        (generated / "nested").mkdir(parents=True)
        (generated / "a.js").write_text("let a=1", encoding="utf-8")
        (generated / "nested" / "b.json").write_text("{}", encoding="utf-8")
        pretty = root / "pretty"
        skipped_symlinks: List[str] = []
        assert copy_generated_tree(generated, pretty, skipped_symlinks) == 2
        candidates = format_candidates(pretty)
        assert [p.name for p in candidates] == ["a.js", "b.json"]

        outside = root / "outside.js"
        outside.write_text("outside", encoding="utf-8")
        link = generated / "external.js"
        try:
            link.symlink_to(outside)
        except OSError:
            pass
        else:
            pretty2 = root / "pretty2"
            skipped: List[str] = []
            assert copy_generated_tree(generated, pretty2, skipped) == 2
            assert not (pretty2 / "external.js").exists()
            assert str(link) in skipped

        inputs = root / "web"
        inputs.mkdir()
        (inputs / "main.js").write_text("", encoding="utf-8")
        (inputs / "lazy.js").write_text("", encoding="utf-8")
        (inputs / "index.html").write_text("", encoding="utf-8")
        (inputs / "app.asar").write_bytes(b"asar")
        (inputs / "node_modules" / "pkg").mkdir(parents=True)
        (inputs / "node_modules" / "pkg" / "ignored.js").write_text(
            "", encoding="utf-8"
        )
        (inputs / ".git").mkdir()
        (inputs / ".git" / "ignored.js").write_text("", encoding="utf-8")
        roots, inventory, code = collect_inputs([inputs])
        assert roots == [inputs.resolve()]
        assert {p.name for p in code} == {"main.js", "lazy.js"}
        assert {artifact_role(p) for p in inventory} >= {
            "code",
            "bootstrap-html",
            "electron-asar",
        }
        assert not any(
            "node_modules" in p.parts or ".git" in p.parts for p in inventory
        )

        # Workspace-local node_modules/.bin takes precedence over PATH.
        workspace = root / "workspace"
        local_bin = workspace / "node_modules" / ".bin"
        local_bin.mkdir(parents=True)
        if os.name == "nt":
            local_tool = local_bin / "prettier.cmd"
            local_tool.write_text("@echo off\r\n", encoding="utf-8")
        else:
            local_tool = local_bin / "prettier"
            local_tool.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            local_tool.chmod(0o755)
        resolved_tool = resolve_tool(
            "prettier", False, workspace_bin_dirs(workspace)
        )
        assert resolved_tool
        assert Path(resolved_tool[0]).resolve() == local_tool.resolve()

        # Prettier batching uses relative paths and command-length budgets.
        long_paths: List[Path] = []
        for index in range(12):
            p = pretty / (("very-long-name-" * 6) + str(index) + ".js")
            p.write_text("", encoding="utf-8")
            long_paths.append(p)
        base = ["prettier", "--write", "--no-config", "--no-editorconfig"]
        batches = list(command_path_batches(long_paths, base, root, budget=420))
        assert len(batches) > 1
        assert all(not os.path.isabs(arg) for batch in batches for arg in batch)
        assert all(
            command_arg_length(base + batch) <= 420 or len(batch) == 1
            for batch in batches
        )

        out = root / "out"
        (out / "webcrack" / "old").mkdir(parents=True)
        (out / "webcrack" / "old" / "x.js").write_text("x", encoding="utf-8")
        (out / "keep.txt").write_text("keep", encoding="utf-8")
        (out / "triage-manifest.json").write_text(
            json.dumps({"schema": MANIFEST_SCHEMA, "helper_version": "v4.3.1"}),
            encoding="utf-8",
        )
        clean_managed_outputs(out)
        assert not (out / "webcrack").exists()
        assert (out / "keep.txt").is_file()

        # --dry-run --force must not remove or write anything.
        dry_out = root / "dry-out"
        (dry_out / "webcrack").mkdir(parents=True)
        (dry_out / "webcrack" / "old.js").write_text("old", encoding="utf-8")
        (dry_out / "triage-manifest.json").write_text(
            json.dumps({"schema": MANIFEST_SCHEMA, "helper_version": HELPER_VERSION}),
            encoding="utf-8",
        )
        before = {
            str(p.relative_to(dry_out)): p.read_bytes()
            for p in dry_out.rglob("*")
            if p.is_file() and not p.is_symlink()
        }
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ):
            dry_rc = main(
                [
                    str(source),
                    "--out",
                    str(dry_out),
                    "--force",
                    "--dry-run",
                    "--skip-webcrack",
                    "--skip-wakaru",
                    "--skip-prettier",
                ]
            )
        assert dry_rc == 2
        after = {
            str(p.relative_to(dry_out)): p.read_bytes()
            for p in dry_out.rglob("*")
            if p.is_file() and not p.is_symlink()
        }
        assert before == after

    print("web_js_triage self-test: OK")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.input or args.out is None:
        parser.error("at least one input and --out are required unless --self-test is used")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    if args.skip_webcrack and args.force_webcrack:
        parser.error("--skip-webcrack and --force-webcrack are mutually exclusive")

    out = args.out.expanduser().resolve()
    try:
        roots, inventory_files, sources = collect_inputs(args.input)
        bound_maps = parse_source_map_bindings(args.source_map_for)
    except ValueError as exc:
        parser.error(str(exc))

    explicit_maps: List[Path] = []
    for raw in args.source_map:
        expanded = raw.expanduser()
        if expanded.is_symlink():
            parser.error("source map symlinks are not allowed: %s" % expanded)
        source_map = expanded.resolve()
        if not source_map.is_file():
            parser.error("source map is not an existing file: %s" % source_map)
        explicit_maps.append(source_map)

    source_set = set(sources)
    for bound_source, bound_map in bound_maps.items():
        if bound_source not in source_set:
            parser.error(
                "--source-map-for source is not one of the analyzed code files: %s"
                % bound_source
            )
        if not bound_map.is_file():
            parser.error("source-map binding map is not an existing file: %s" % bound_map)

    workspace = (args.workspace or Path.cwd()).expanduser().resolve()
    if not workspace.is_dir():
        parser.error("--workspace must be an existing directory: %s" % workspace)
    local_bin_dirs = workspace_bin_dirs(workspace)

    filesystem_root = Path(out.anchor).resolve()
    if out == filesystem_root or out == Path.home().resolve():
        parser.error(
            "--out must be a dedicated analysis directory, not a filesystem root or home directory"
        )
    if out.exists() and not out.is_dir():
        parser.error("--out must be a directory path: %s" % out)

    protected_inputs = list(roots) + explicit_maps + list(bound_maps.values())
    for protected in protected_inputs:
        if protected.is_dir():
            overlaps = (
                out == protected or out in protected.parents or protected in out.parents
            )
        else:
            overlaps = out == protected or out in protected.parents
        if overlaps:
            parser.error("--out must not overlap an input/source-map tree: %s" % protected)

    if not sources:
        parser.error("no JS/TS code files found in the supplied inputs")

    out_nonempty = out.exists() and any(out.iterdir())
    if out_nonempty and not args.force:
        parser.error("output directory is not empty; use a fresh path or --force")
    if args.force and out.exists():
        try:
            if args.dry_run:
                validate_managed_cleanup(out)
            else:
                clean_managed_outputs(out)
        except ValueError as exc:
            parser.error(str(exc))
    if not args.dry_run:
        out.mkdir(parents=True, exist_ok=True)

    logs = out / "logs"
    generation_root = out / ".staging" if args.retention == "lean" else out
    if not args.dry_run:
        logs.mkdir(parents=True, exist_ok=True)
        if args.retention == "lean":
            generation_root.mkdir(parents=True, exist_ok=True)

    obfuscation = {source: detect_obvious_obfuscation(source) for source in sources}
    webcrack_sources: Dict[Path, bool] = {
        source: (
            not args.skip_webcrack
            and (
                args.retention == "all"
                or args.force_webcrack
                or bool(obfuscation[source].get("obvious"))
            )
        )
        for source in sources
    }
    requested = {
        "webcrack": any(webcrack_sources.values()),
        "wakaru": not args.skip_wakaru,
        "prettier": not args.skip_prettier,
    }
    tools: Dict[str, Optional[List[str]]] = {
        name: resolve_tool(name, args.allow_npx, local_bin_dirs) if enabled else None
        for name, enabled in requested.items()
    }
    missing = [
        name for name, enabled in requested.items() if enabled and not tools[name]
    ]
    if missing and args.require_tools:
        parser.error("missing requested tools: %s" % ", ".join(missing))

    inventory_maps = [
        path for path in inventory_files if path.suffix.lower() == ".map"
    ]
    direct_file_inputs = (
        len(args.input) == len(sources)
        and len(sources) > 1
        and all(
            raw.expanduser().exists()
            and not raw.expanduser().is_symlink()
            and raw.expanduser().is_file()
            and raw.expanduser().suffix.lower() in CODE_SUFFIXES
            for raw in args.input
        )
    )
    automatic_map_roots = [root if root.is_dir() else root.parent for root in roots]
    source_maps = associate_source_maps(
        sources,
        explicit_maps,
        inventory_maps,
        explicit_bindings=bound_maps,
        allow_pairwise_explicit=direct_file_inputs,
        automatic_map_roots=automatic_map_roots,
    )

    input_records = [
        {
            "path": str(path),
            "role": artifact_role(path),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in inventory_files
    ]
    source_records: List[Dict[str, object]] = []
    source_ids: Dict[Path, str] = {}
    for path in sources:
        source_id = safe_slug(path)
        source_ids[path] = source_id
        source_records.append(
            {
                "id": source_id,
                "path": str(path),
                "size": path.stat().st_size,
                "sha256": sha256_file(path),
                "source_map": source_maps[path],
                "obfuscation_triage": obfuscation[path],
                "webcrack_selected": webcrack_sources[path],
                "webcrack_selection_reason": (
                    "retention-all"
                    if args.retention == "all" and not args.skip_webcrack
                    else "forced"
                    if args.force_webcrack
                    else "obvious-obfuscation"
                    if bool(obfuscation[path].get("obvious")) and not args.skip_webcrack
                    else "not-selected"
                ),
            }
        )

    manifest: Dict[str, object] = {
        "schema": MANIFEST_SCHEMA,
        "helper_version": HELPER_VERSION,
        "dry_run": bool(args.dry_run),
        "workspace": str(workspace),
        "workspace_node_bin_dirs": [str(path) for path in local_bin_dirs],
        "input_roots": [str(path) for path in roots],
        "input_inventory": input_records,
        "analysis_sources": source_records,
        "explicit_source_maps": [str(path) for path in explicit_maps],
        "explicit_source_map_bindings": {
            str(source): str(map_path) for source, map_path in bound_maps.items()
        },
        "pinned_npx_reference_versions": {
            name: spec[2] for name, spec in PINNED.items()
        },
        "allow_npx": bool(args.allow_npx),
        "retention": args.retention,
        "force_webcrack": bool(args.force_webcrack),
        "wakaru_mode": args.wakaru_mode,
        "node_version": node_version(min(args.timeout, 30))
        if not args.dry_run
        else None,
        "tools": {},
        "steps": [],
        "notes": [
            "Original inputs/maps are never modified by this helper.",
            "Directory inventory excludes node_modules, .git, and symlinks by default.",
            "Workspace-local node_modules/.bin tools are preferred over PATH tools; npx remains opt-in.",
            "webcrack and Wakaru are tool-generated views of the same input; agreement is corroboration, not independent semantic evidence.",
            "Lean retention treats parallel tool views as staging, promotes selected canonical views, and retains webcrack only for obvious obfuscation or explicit request.",
            "All retention preserves parallel raw outputs and separate Prettier-formatted copies for tool comparison/debugging.",
            "Wakaru --unpack=inspect is an inspection-oriented decomposition and may not preserve executable initialization order.",
            "Lean-mode successful logs are summarized in step records and deleted; failure/timeout logs are retained.",
        ],
    }

    for name, prefix in tools.items():
        if prefix and is_npx_prefix(prefix):
            version = "pinned-npx:%s" % PINNED[name][2]
        elif prefix and not args.dry_run:
            version = tool_version(prefix, min(args.timeout, 30))
        else:
            version = None
        tool_record = {
            "requested": requested[name],
            "resolved": prefix,
            "version": version,
        }
        if name == "webcrack":
            tool_record["selected_source_ids"] = [
                source_ids[source] for source in sources if webcrack_sources[source]
            ]
            tool_record["policy_enabled"] = not args.skip_webcrack
        manifest["tools"][name] = tool_record  # type: ignore[index]

    steps: List[Dict[str, object]] = manifest["steps"]  # type: ignore[assignment]
    analyzer_steps = 0

    for source in sources:
        source_id = source_ids[source]
        cwd = source.parent

        if webcrack_sources[source] and tools["webcrack"]:
            # Important: do not pre-create the leaf output directory. webcrack
            # rejects an existing -o directory unless its own --force is used.
            webcrack_parent = generation_root / "webcrack"
            if not args.dry_run:
                webcrack_parent.mkdir(parents=True, exist_ok=True)
            webcrack_out = webcrack_parent / source_id
            cmd = list(tools["webcrack"] or []) + [
                str(source),
                "-o",
                str(webcrack_out),
            ]
            steps.append(
                run_step(
                    "webcrack-%s" % source_id,
                    cmd,
                    cwd,
                    logs,
                    args.timeout,
                    args.dry_run,
                    {
                        "tool": "webcrack",
                        "source_id": source_id,
                        "output": str(webcrack_out),
                    },
                    retain_success_log=args.retention == "all",
                )
            )
            analyzer_steps += 1

        if requested["wakaru"] and tools["wakaru"]:
            wakaru_parent = generation_root / "wakaru"
            if not args.dry_run:
                wakaru_parent.mkdir(parents=True, exist_ok=True)
            wakaru_out = wakaru_parent / source_id
            unpack = (
                "--unpack"
                if args.wakaru_mode == "normal"
                else "--unpack=%s" % args.wakaru_mode
            )
            cmd = list(tools["wakaru"] or []) + [
                str(source),
                unpack,
                "-o",
                str(wakaru_out),
            ]
            steps.append(
                run_step(
                    "wakaru-unpack-%s" % source_id,
                    cmd,
                    cwd,
                    logs,
                    args.timeout,
                    args.dry_run,
                    {
                        "tool": "wakaru",
                        "source_id": source_id,
                        "output": str(wakaru_out),
                    },
                    retain_success_log=args.retention == "all",
                )
            )
            analyzer_steps += 1

            map_record = source_maps[source]
            map_value = map_record.get("path")
            if isinstance(map_value, str) and Path(map_value).is_file():
                source_aware_parent = generation_root / "wakaru-source-aware"
                if not args.dry_run:
                    source_aware_parent.mkdir(parents=True, exist_ok=True)
                source_aware = source_aware_parent / (source_id + ".js")
                cmd = list(tools["wakaru"] or []) + [
                    str(source),
                    "--source-map",
                    map_value,
                    "-o",
                    str(source_aware),
                ]
                steps.append(
                    run_step(
                        "wakaru-source-map-%s" % source_id,
                        cmd,
                        cwd,
                        logs,
                        args.timeout,
                        args.dry_run,
                        {
                            "tool": "wakaru",
                            "source_id": source_id,
                            "source_map_association": map_record.get("association"),
                            "output": str(source_aware),
                        },
                        retain_success_log=args.retention == "all",
                    )
                )

    if requested["wakaru"] and tools["wakaru"]:
        extracted_maps: Set[Path] = set()
        for source in sources:
            map_value = source_maps[source].get("path")
            if not isinstance(map_value, str):
                continue
            map_path = Path(map_value)
            if (
                not map_path.is_file()
                or map_path.is_symlink()
                or map_path in extracted_maps
            ):
                continue
            extracted_maps.add(map_path)
            map_id = safe_slug(map_path)
            extract_parent = generation_root / "sourcemap-sources"
            if not args.dry_run:
                extract_parent.mkdir(parents=True, exist_ok=True)
            extracted = extract_parent / map_id
            cmd = list(tools["wakaru"] or []) + [
                "extract",
                str(map_path),
                "-o",
                str(extracted),
            ]
            steps.append(
                run_step(
                    "wakaru-extract-map-%s" % map_id,
                    cmd,
                    map_path.parent,
                    logs,
                    args.timeout,
                    args.dry_run,
                    {
                        "tool": "wakaru",
                        "source_map": str(map_path),
                        "output": str(extracted),
                    },
                    retain_success_log=args.retention == "all",
                )
            )

    promoted_pairs: List[Tuple[Path, Path]] = []
    promotion_errors: List[str] = []
    skipped_generated_symlinks: List[str] = []
    formatting_verified: Optional[bool] = None

    if args.retention == "lean" and not args.dry_run:
        for step in list(steps):
            if step.get("status") != "ok" or step.get("tool") not in {"webcrack", "wakaru"}:
                continue
            output_value = step.get("output")
            if not isinstance(output_value, str):
                continue
            staged = Path(output_value)
            try:
                relative = staged.relative_to(generation_root)
            except ValueError:
                promotion_errors.append("output is outside lean staging: %s" % staged)
                continue
            durable = out / relative
            try:
                remove_generated_path(durable)
                copied = copy_generated_tree(staged, durable, skipped_generated_symlinks)
                if copied == 0 or not verify_generated_copy(staged, durable):
                    raise ValueError("copy verification failed")
                promoted_pairs.append((staged, durable))
            except (OSError, ValueError) as exc:
                promotion_errors.append("%s -> %s: %s" % (staged, durable, exc))

        if promotion_errors:
            steps.append(
                {
                    "name": "lean-promotion",
                    "status": "failed",
                    "returncode": None,
                    "errors": promotion_errors,
                }
            )
        else:
            steps.append(
                {
                    "name": "lean-promotion",
                    "status": "ok",
                    "returncode": 0,
                    "promoted_outputs": [str(dst) for _, dst in promoted_pairs],
                    "log_retained": False,
                }
            )

        manifest["promoted_outputs"] = [str(dst.relative_to(out)) for _, dst in promoted_pairs]
        if skipped_generated_symlinks:
            unique_skipped = sorted(set(skipped_generated_symlinks))
            manifest["skipped_generated_symlinks"] = unique_skipped
            print(
                "warning: skipped %d generated symlink(s) during lean promotion"
                % len(unique_skipped),
                file=sys.stderr,
            )

        if requested["prettier"] and tools["prettier"] and not promotion_errors:
            candidates = unique_format_candidates([dst for _, dst in promoted_pairs])
            manifest["prettier_candidate_count"] = len(candidates)
            write_base = list(tools["prettier"] or []) + [
                "--write",
                "--no-config",
                "--no-editorconfig",
            ]
            write_steps: List[Dict[str, object]] = []
            for index, path_args in enumerate(
                command_path_batches(candidates, write_base, out), start=1
            ):
                cmd = write_base + path_args
                record = run_step(
                    "prettier-%03d" % index,
                    cmd,
                    out,
                    logs,
                    args.timeout,
                    False,
                    {
                        "tool": "prettier",
                        "phase": "write",
                        "candidate_count": len(path_args),
                        "estimated_command_length": command_arg_length(cmd),
                    },
                    retain_success_log=False,
                )
                steps.append(record)
                write_steps.append(record)

            writes_ok = all(step.get("status") == "ok" for step in write_steps)
            check_steps: List[Dict[str, object]] = []
            if writes_ok:
                check_base = list(tools["prettier"] or []) + [
                    "--check",
                    "--no-config",
                    "--no-editorconfig",
                ]
                for index, path_args in enumerate(
                    command_path_batches(candidates, check_base, out), start=1
                ):
                    cmd = check_base + path_args
                    record = run_step(
                        "prettier-check-%03d" % index,
                        cmd,
                        out,
                        logs,
                        args.timeout,
                        False,
                        {
                            "tool": "prettier",
                            "phase": "check",
                            "candidate_count": len(path_args),
                            "estimated_command_length": command_arg_length(cmd),
                        },
                        retain_success_log=False,
                    )
                    steps.append(record)
                    check_steps.append(record)
            formatting_verified = writes_ok and all(
                step.get("status") == "ok" for step in check_steps
            )
            # With zero candidates, there is nothing to format and the promoted copy
            # itself is already verified.
            if not candidates:
                formatting_verified = True

            if not formatting_verified:
                # Do not leave a partially formatted canonical tree. Restore it from
                # verified raw staging and retain staging for diagnosis/recovery.
                restore_errors: List[str] = []
                for staged, durable in promoted_pairs:
                    try:
                        remove_generated_path(durable)
                        copy_generated_tree(staged, durable)
                        if not verify_generated_copy(staged, durable):
                            raise ValueError("restore verification failed")
                    except (OSError, ValueError) as exc:
                        restore_errors.append("%s: %s" % (durable, exc))
                if restore_errors:
                    steps.append(
                        {
                            "name": "lean-restore-raw",
                            "status": "failed",
                            "returncode": None,
                            "errors": restore_errors,
                        }
                    )
        elif requested["prettier"] and tools["prettier"] and promotion_errors:
            formatting_verified = False
        else:
            # Prettier was skipped or unresolved: the verified promoted raw output is
            # the canonical retained view; no duplicate staging copy is needed after
            # a successful run.
            formatting_verified = None

    elif args.retention == "all" and requested["prettier"] and tools["prettier"] and not args.dry_run:
        pretty_root = out / "pretty"
        copied = 0
        skipped_generated_symlinks = []
        for name in (
            "webcrack",
            "wakaru",
            "wakaru-source-aware",
            "sourcemap-sources",
        ):
            generated = out / name
            if generated.exists() or generated.is_symlink():
                copied += copy_generated_tree(
                    generated,
                    pretty_root / name,
                    skipped_generated_symlinks,
                )

        manifest["prettier_copy_count"] = copied
        if skipped_generated_symlinks:
            unique_skipped = sorted(set(skipped_generated_symlinks))
            manifest["skipped_generated_symlinks"] = unique_skipped
            print(
                "warning: skipped %d generated symlink(s) before Prettier"
                % len(unique_skipped),
                file=sys.stderr,
            )
        candidates = format_candidates(pretty_root)
        prettier_base = list(tools["prettier"] or []) + [
            "--write",
            "--no-config",
            "--no-editorconfig",
        ]
        for index, path_args in enumerate(
            command_path_batches(candidates, prettier_base, out), start=1
        ):
            cmd = prettier_base + path_args
            steps.append(
                run_step(
                    "prettier-%03d" % index,
                    cmd,
                    out,
                    logs,
                    args.timeout,
                    False,
                    {
                        "tool": "prettier",
                        "candidate_count": len(path_args),
                        "estimated_command_length": command_arg_length(cmd),
                    },
                    retain_success_log=True,
                )
            )
    elif requested["prettier"] and tools["prettier"] and args.dry_run:
        print(
            "[prettier] dry-run: formatting is deferred until generated files exist"
        )

    manifest["formatting_verified"] = formatting_verified

    failed = [
        step for step in steps if step.get("status") not in ("ok", "dry-run")
    ]
    if failed:
        overall_status = "failed"
    elif analyzer_steps == 0:
        overall_status = "no-analysis"
    elif missing:
        overall_status = "partial"
    elif args.dry_run:
        overall_status = "dry-run"
    else:
        overall_status = "ok"

    manifest["overall_status"] = overall_status

    if args.retention == "lean" and not args.dry_run:
        if not failed and not promotion_errors and formatting_verified is not False:
            remove_generated_path(generation_root)
            manifest["staging_retained"] = False
        else:
            manifest["staging_retained"] = generation_root.exists()
        if logs.is_dir() and not any(logs.iterdir()):
            logs.rmdir()
    else:
        manifest["staging_retained"] = False

    if args.dry_run:
        manifest["generated_artifacts"] = []
        manifest["generated_paths"] = []
    else:
        manifest["generated_artifacts"] = generated_artifact_inventory(out)
        manifest["generated_paths"] = [
            name
            for name in sorted(MANAGED_TOP_LEVEL)
            if name != "triage-manifest.json" and (out / name).exists()
        ]

    manifest_path = out / "triage-manifest.json"
    if args.dry_run:
        print("manifest (dry-run, not written): %s" % manifest_path)
    else:
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print("manifest: %s" % manifest_path)

    if missing:
        print("unresolved tools (skipped): %s" % ", ".join(missing), file=sys.stderr)
    if failed:
        print(
            "%d tool step(s) failed; inspect logs and manifest" % len(failed),
            file=sys.stderr,
        )
        return 1
    if analyzer_steps == 0:
        print(
            "no analysis tool step could run; inspect tool resolution in the manifest",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
