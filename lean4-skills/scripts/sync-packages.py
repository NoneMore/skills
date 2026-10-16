#!/usr/bin/env python3
"""Vendor shared Lean 4 reference material into independently installable Skills."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "references"

PACKAGE_REFERENCES = {
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
    "lean4-review": ["mathlib-guide.md", "simp-reference.md", "branches/mathlib-upstream.md"],
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


def expected_files(package: str):
    for rel in PACKAGE_REFERENCES[package]:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()

    errors: list[str] = []
    for package in PACKAGE_REFERENCES:
        errors.extend(validate_name(package))
        for src, dst in expected_files(package):
            if not src.exists():
                errors.append(f"missing canonical source {src.relative_to(ROOT)}")
                continue
            if args.check:
                if not dst.exists() or dst.read_bytes() != src.read_bytes():
                    errors.append(f"vendored copy drift: {dst.relative_to(ROOT)}")
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
