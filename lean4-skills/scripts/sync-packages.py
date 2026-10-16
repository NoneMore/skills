#!/usr/bin/env python3
"""Vendor shared Lean 4 reference material into the jointly installed Skill family."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "references"

# These are behavioral entry points, not complete dependency lists. Shared
# Markdown references may link to other shared references; package_references()
# follows those links transitively so an activated Skill can traverse its local
# reference graph without falling back to the collection root.
PACKAGE_REFERENCE_SEEDS = {
    "lean4-explore": ["mathlib-guide.md", "verification.md", "branches/mathlib-upstream.md"],
    "lean4-formalize": ["mathlib-guide.md", "verification.md", "branches/mathlib-upstream.md"],
    "lean4-prove": [
        "mathlib-guide.md",
        "verification.md",
        "performance-optimization.md",
        "simp-reference.md",
        "branches/mathlib-upstream.md",
    ],
    "lean4-refute": ["mathlib-guide.md", "verification.md", "branches/mathlib-upstream.md"],
    "lean4-diagnose": [
        "mathlib-guide.md",
        "verification.md",
        "performance-optimization.md",
        "branches/mathlib-upstream.md",
    ],
    "lean4-trust": ["mathlib-guide.md", "verification.md", "branches/mathlib-upstream.md"],
    "lean4-review": [
        "mathlib-guide.md",
        "verification.md",
        "simp-reference.md",
        "branches/mathlib-upstream.md",
    ],
    "lean4-optimize": [
        "mathlib-guide.md",
        "verification.md",
        "performance-optimization.md",
        "simp-reference.md",
        "branches/mathlib-upstream.md",
    ],
}

PROVENANCE = ["UPSTREAM.md", "THIRD_PARTY_NOTICES.md"]
NAME_RE = re.compile(r"(?m)^name:\s*([a-z0-9-]+)\s*$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
URI_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def local_link_target(raw_target: str) -> str | None:
    """Return the path part of a local Markdown link, or None for non-local links."""
    target = raw_target.strip()
    if target.startswith("<"):
        closing = target.find(">")
        if closing != -1:
            target = target[1:closing]
    else:
        # Markdown permits an optional title after the destination.
        target = target.split(maxsplit=1)[0]

    target = target.split("#", 1)[0]
    if not target or target.startswith("#") or URI_RE.match(target):
        return None
    return target


def markdown_local_links(path: Path):
    for raw_target in MARKDOWN_LINK_RE.findall(path.read_text(encoding="utf-8")):
        target = local_link_target(raw_target)
        if target is not None:
            yield target


def package_references(package: str) -> list[Path]:
    """Return the transitive shared-reference closure for one Skill."""
    pending = [Path(rel) for rel in PACKAGE_REFERENCE_SEEDS[package]]
    seen: set[Path] = set()
    shared_root = SHARED.resolve()

    while pending:
        rel = pending.pop()
        if rel in seen:
            continue
        seen.add(rel)

        src = SHARED / rel
        if not src.exists():
            # main() reports the missing canonical source with the package name.
            continue

        for target in markdown_local_links(src):
            resolved = (src.parent / target).resolve()
            try:
                dependency = resolved.relative_to(shared_root)
            except ValueError:
                # Links outside the canonical shared-reference tree are not
                # vendored dependencies. validate_local_links() will still
                # reject them if they become runtime-local package links.
                continue
            if dependency.suffix == ".md" and dependency not in seen:
                pending.append(dependency)

    return sorted(seen, key=lambda path: path.as_posix())


def expected_files(package: str):
    for rel in package_references(package):
        yield SHARED / rel, ROOT / package / "references" / rel
    for rel in PROVENANCE:
        yield ROOT / rel, ROOT / package / rel


def validate_name(package: str) -> list[str]:
    skill = ROOT / package / "SKILL.md"
    if not skill.exists():
        return [f"missing {skill.relative_to(ROOT)}"]
    match = NAME_RE.search(skill.read_text(encoding="utf-8"))
    if not match:
        return [f"missing frontmatter name in {skill.relative_to(ROOT)}"]
    if match.group(1) != package:
        return [f"directory/name mismatch: {package} != {match.group(1)}"]
    return []


def validate_local_links(package: str) -> list[str]:
    """Reject broken runtime-local Markdown links in a Skill package."""
    errors: list[str] = []
    package_root = (ROOT / package).resolve()

    for doc in sorted(package_root.rglob("*.md")):
        for target in markdown_local_links(doc):
            resolved = (doc.parent / target).resolve()
            try:
                resolved.relative_to(package_root)
            except ValueError:
                errors.append(
                    f"package-local link escapes {package}: "
                    f"{doc.relative_to(ROOT)} -> {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken package-local link: {doc.relative_to(ROOT)} -> {target}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()

    errors: list[str] = []
    for package in PACKAGE_REFERENCE_SEEDS:
        errors.extend(validate_name(package))
        for src, dst in expected_files(package):
            if not src.exists():
                errors.append(f"missing canonical source for {package}: {src.relative_to(ROOT)}")
                continue
            if args.check:
                if not dst.exists() or dst.read_bytes() != src.read_bytes():
                    errors.append(f"vendored copy drift: {dst.relative_to(ROOT)}")
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)

        # Validate after writing in sync mode so newly discovered transitive
        # dependencies are present before their links are checked.
        errors.extend(validate_local_links(package))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
