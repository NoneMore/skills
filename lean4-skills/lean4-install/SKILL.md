---
name: lean4-install
description: "Use only when the user explicitly invokes this Skill to install or update reusable Lean 4/mathlib agent guidance as ordinary documentation in the current repository. Inspect and follow the repository's existing documentation conventions; if none apply, use docs/lean/. Do not select this Skill implicitly for proving, formalizing, diagnosing, reviewing, optimizing, or other Lean work."
license: MIT
---

# Lean 4 Documentation Installer

## Purpose

Materialize reusable Lean/mathlib guidance into the current repository's normal documentation tree so later work can consume it as project knowledge rather than as a runtime Skill dependency.

This Skill is user-invoked only. Other Lean Skills do not call it, depend on it at runtime, or gain permission to install documentation merely because the documentation would be useful.

## Installation outcome

Install the documentation bundle from `assets/docs/` into one coherent repository documentation directory while preserving the repository's own information architecture.

The bundle contains these stable filenames:

- `mathlib-search.md`
- `verification.md`
- `simplification.md`
- `performance.md`
- `upstream-mathlib.md`

Keep the bundle together so its relative links remain valid.

## Choose the destination

Inspect the repository before writing:

1. Read applicable workspace instructions and documentation conventions.
2. Inspect existing `docs/`, `documentation/`, contributor/development docs, and any established Lean-specific documentation area.
3. Prefer an existing location whose audience and ownership match reusable development guidance.
4. Do not invent a hidden agent-only documentation tree when the repository already has a normal documentation convention.
5. If no applicable convention exists, use `docs/lean/`.

The destination is a project-documentation decision, not a fixed path baked into the routable Skills.

## Existing files and updates

Treat existing repository documentation as user-owned state.

- If a target file is absent, create it from the corresponding asset.
- If it already matches the installer payload, leave it unchanged.
- If it contains the installer marker and local project additions, update the reusable guidance while preserving compatible project-specific additions.
- If an unmarked file already occupies the intended path, do not overwrite it blindly. Integrate the material into the repository's existing structure or choose the nearest convention-compatible subdirectory.
- Do not delete unrelated documentation merely to make the bundle layout cleaner.

Repository-specific policy outranks generic installed guidance. Preserve stronger local requirements rather than replacing them with generic defaults.

## Workflow

1. Resolve the documentation destination from repository evidence.
2. Read all files in `assets/docs/` before writing so cross-links and scope are understood.
3. Compare the bundle with existing target documentation.
4. Create or update only the documentation needed for this installation outcome.
5. If the repository maintains an explicit docs index or navigation file, update it only when that convention requires newly installed docs to be registered.
6. Verify that all installed relative Markdown links resolve and that the files are placed under the repository's intended documentation scope.
7. Report the destination, files created/updated/left unchanged, conflicts preserved, and any repository-specific guidance that overrides the generic bundle.

## Boundaries

This Skill installs documentation. It does not install or invoke the other Lean Skills, modify Lean source, rewrite theorem statements, edit build configuration, change CI, or provision external tools unless the user separately requests that outcome.

Do not turn installation into a general repository cleanup. Make the smallest coherent documentation change that establishes the reusable project knowledge.

## Completion

Installation is complete when the reusable guidance is present in a convention-compatible project documentation location, its internal links are valid, pre-existing project policy has been preserved, and the resulting paths are reported to the user.
