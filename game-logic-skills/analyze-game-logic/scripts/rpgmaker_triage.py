#!/usr/bin/env python3
"""Read-only, standard-library-only RPG Maker MV/MZ project triage.

Never executes project JavaScript, modifies game files, or unpacks game assets.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT_SUFFIXES = ("", "www", "Game/www", "assets/www", "resources/app", "app.nw", "package.nw")
EVENT_CODES = {
    111: "conditional_branch", 117: "common_event", 121: "switches",
    122: "variables", 123: "self_switch", 355: "script_start",
    655: "script_continuation", 356: "mv_plugin_command",
    357: "mz_plugin_command",
}
MAX_JSON_BYTES = 32 * 1024 * 1024


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def signals(path):
    mv_core = (path / "js/rpg_core.js").is_file()
    mz_core = (path / "js/rmmz_core.js").is_file()
    system = (path / "data/System.json").is_file()
    plugins = (path / "js/plugins.js").is_file()
    mv_project = any(path.glob("*.rpgproject"))
    mz_project = any(path.glob("*.rmmzproject"))
    sigs = {"mv_core": mv_core, "mz_core": mz_core, "system_json": system,
            "plugins_js": plugins, "mv_project": mv_project, "mz_project": mz_project}
    if mv_core and mz_core:
        engine, confidence = "ambiguous", "mixed core files"
    elif (mv_core and mz_project) or (mz_core and mv_project) or (mv_project and mz_project):
        engine, confidence = "ambiguous", "conflicting project markers"
    elif mv_core:
        engine, confidence = "MV", "high" if system else "medium"
    elif mz_core:
        engine, confidence = "MZ", "high" if system else "medium"
    elif mv_project:
        engine, confidence = "MV", "medium" if system else "low"
    elif mz_project:
        engine, confidence = "MZ", "medium" if system else "low"
    else:
        engine, confidence = "unknown", "none"
    return engine, confidence, sigs


def discover_root(root):
    candidates = []
    for suffix in ROOT_SUFFIXES:
        p = root / suffix
        if p.is_dir():
            engine, confidence, evidence = signals(p)
            candidates.append((p, engine, confidence, evidence))
    if not candidates:
        raise ValueError(f"Directory does not exist: {root}")
    identified = [c for c in candidates if c[1] != "unknown"]
    rank = {"high": 3, "medium": 2, "low": 1}
    chosen = max(identified, key=lambda c: rank.get(c[2], 0)) if identified else candidates[0]
    editions = {c[1] for c in identified}
    conflicts = [f"{c[0]}: {c[1]}" for c in identified] if len(editions) > 1 or "ambiguous" in editions else []
    p, engine, confidence, evidence = chosen
    if conflicts:
        engine, confidence = "ambiguous", "conflicting candidate roots"
    return p, engine, confidence, evidence, conflicts


def read_json(path):
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError("JSON file exceeds size cap")
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def read_plugins(path):
    """Decode the common generated var $plugins = [JSON] form without JS eval.

    Projects with JavaScript expressions in the manifest are reported as
    unparsed; never execute or interpret these expressions.
    """
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError("Plugin manifest exceeds size cap")
    raw = path.read_text(encoding="utf-8-sig")
    match = re.search(r"(?m)^[ \t]*(?:var|let|const)\s+\$plugins\s*=\s*(?=\[)", raw)
    if not match:
        raise ValueError("No recognized $plugins array assignment")
    literal = raw[match.end():].lstrip()
    parsed, end = json.JSONDecoder().raw_decode(literal)
    if not isinstance(parsed, list) or literal[end:].strip() not in ("", ";"):
        raise ValueError("$plugins is not a standalone JSON-literal array")
    return parsed


def events_from_json(filename, data):
    if re.fullmatch(r"Map[0-9]+\.json", filename) and isinstance(data, dict):
        for event in data.get("events", []) or []:
            if isinstance(event, dict):
                for page_number, page in enumerate(event.get("pages", []) or [], 1):
                    if isinstance(page, dict):
                        yield f"event:{event.get('id', '?')}/page:{page_number}", page.get("list", [])
    elif filename == "CommonEvents.json" and isinstance(data, list):
        for event in data:
            if isinstance(event, dict):
                yield f"common-event:{event.get('id', '?')}", event.get("list", [])
    elif filename == "Troops.json" and isinstance(data, list):
        for troop in data:
            if isinstance(troop, dict):
                for page_number, page in enumerate(troop.get("pages", []) or [], 1):
                    if isinstance(page, dict):
                        yield f"troop:{troop.get('id', '?')}/page:{page_number}", page.get("list", [])


def inspect_events(root, warnings, max_files=500):
    data_dir = root / "data"
    maps = sorted(data_dir.glob("Map[0-9]*.json"))
    truncated = len(maps) > max_files
    if truncated:
        warnings.append(f"Map scan truncated at {max_files} of {len(maps)} maps")
    filenames = maps[:max_files]
    filenames += [data_dir / x for x in ("CommonEvents.json", "Troops.json") if (data_dir / x).is_file()]
    totals = Counter()
    examples = []
    for path in filenames:
        try:
            data = read_json(path)
            for locator, commands in events_from_json(path.name, data):
                if not isinstance(commands, list):
                    continue
                for index, command in enumerate(commands):
                    if not isinstance(command, dict):
                        continue
                    code = command.get("code")
                    if isinstance(code, int) and code in EVENT_CODES:
                        totals[EVENT_CODES[code]] += 1
                        if len(examples) < 30:
                            examples.append({"file": str(path.relative_to(root)), "locator": locator,
                                             "command_index": index, "code": code})
        except (OSError, ValueError, UnicodeError) as e:
            warnings.append(f"Could not inspect {path.name}: {e}")
    return {"scanned_files": len(filenames), "truncated": truncated,
            "code_counts": dict(totals), "sample_locators": examples}


def scan_hooks(root, ordered_plugins, warnings):
    hits = []
    # Indicators only; regex may match comments or inactive branches.
    pattern = re.compile(r"\b(?:[A-Za-z_$][\w$]*\.)?([A-Za-z_$][\w$]*)\.prototype\.([\w$]+)\s*=")
    for item in ordered_plugins:
        if not item.get("enabled"):
            continue
        name = item["name"]
        # Restrict lookup to literal local JS basenames, not manifest-supplied paths.
        if name in (".", "..") or "/" in name or "\\" in name or not name:
            warnings.append(f"Skipping unsafe plugin name: {name!r}")
            continue
        plugin_file = root / "js/plugins" / (name + ".js")
        if not plugin_file.is_file():
            warnings.append(f"Enabled plugin missing locally: {name}")
            continue
        if plugin_file.stat().st_size > 5 * 1024 * 1024:
            warnings.append(f"Skipping oversized plugin: {plugin_file.name}")
            continue
        text = plugin_file.read_text(encoding="utf-8-sig", errors="replace")
        for m in pattern.finditer(text):
            hits.append({"plugin": name, "class": m.group(1), "method": m.group(2),
                         "line": text.count("\n", 0, m.start()) + 1})
        if "PluginManager.registerCommand" in text:
            hits.append({"plugin": name, "indicator": "registerCommand"})
        if "Game_Interpreter.prototype.pluginCommand" in text:
            hits.append({"plugin": name, "indicator": "MV-style pluginCommand"})
    return {"warning": "Heuristic search, not proof of effective override, execution order, or authority",
            "truncated": len(hits) > 1000, "indicators": hits[:1000]}


def triage(given_root, with_events=False, with_hooks=False):
    root, engine, confidence, evidence, conflicts = discover_root(given_root)
    warnings = []
    if conflicts:
        warnings.append("Conflicting candidate roots: " + ", ".join(conflicts))
    result = {"root": str(root), "engine": engine, "confidence": confidence,
              "signals": evidence, "hashes": {}, "plugins": [], "warnings": warnings}
    for relative in ("js/rpg_core.js", "js/rmmz_core.js", "js/plugins.js", "data/System.json"):
        file = root / relative
        if file.is_file():
            result["hashes"][relative] = sha256_file(file)
    manifest = root / "js/plugins.js"
    if manifest.is_file():
        try:
            plugins = read_plugins(manifest)
            result["plugins"] = [
                {"position": i, "name": p.get("name", ""), "enabled": p.get("status") is True,
                 "parameters_count": len(p.get("parameters", {})) if isinstance(p.get("parameters", {}), dict) else None}
                for i, p in enumerate(plugins) if isinstance(p, dict) and isinstance(p.get("name"), str)
            ]
        except (OSError, ValueError, UnicodeError) as e:
            warnings.append(f"Cannot parse generated plugins.js as JSON literal: {e}")
    if with_events:
        result["event_inventory"] = inspect_events(root, warnings)
    if with_hooks:
        result["hook_inventory"] = scan_hooks(root, result["plugins"], warnings)
    if engine == "ambiguous":
        warnings.append("Conflicting MV/MZ markers; do not choose engine automatically")
    if engine == "unknown":
        warnings.append("Insufficient engine markers; inspect pack/container without running JS")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Local RPG Maker project/deployment directory")
    parser.add_argument("--events", action="store_true", help="Count targeted event commands")
    parser.add_argument("--hooks", action="store_true", help="Heuristic enabled-plugin method indexing")
    parser.add_argument("--out", type=Path, help="Optional report path; keep OUTSIDE the project")
    args = parser.parse_args()
    root = args.project.expanduser().resolve()
    result = triage(root, args.events, args.hooks)
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        out = args.out.expanduser().resolve()
        if out == root or root in out.parents:
            parser.error("--out must be outside the supplied project tree")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
