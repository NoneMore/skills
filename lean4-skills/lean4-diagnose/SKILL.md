---
name: lean4-diagnose
description: "Use for formal-mathematics Lean 4/mathlib/Lake root-cause diagnosis or migration planning, or to repair shared/cross-boundary elaboration, module, import, dependency, toolchain, build, or integration failures. Routine local proof repair stays in lean4-prove; no mandatory handoff. Excludes general Lean application/CLI/FFI work."
license: MIT
---

# Lean 4 Diagnose

Start from the exact diagnostic, reproduction boundary, and nearby source. Prefer one cause that explains clustered symptoms over independent symptom patching.

## Triage

- **Shared boundary:** for clustered failures or build mismatches, inspect common imports, APIs, toolchain changes, and source-versus-artifact state before patching files independently.
- **Elaboration:** for type, instance, identifier, field, or import failures, compare expected/actual types and signatures, implicits, universes, namespaces, active imports, and available instances. For dependent-index mismatches, distinguish definitional equality, required transport, and genuine statement mismatch with a minimal diagnostic experiment.
- **Resource limits:** localize elaboration, reduction, tactic, or typeclass-search cost before raising limits.

Test the root-cause hypothesis with the smallest justified change. Do not turn diagnosis into unrelated refactoring, silent API revision, or trust weakening.

## Completion

Re-run the failing command or repository gate; a file-local pass is insufficient across changed dependency or integration boundaries. Completion requires reproducible root-cause evidence and the requested outcome: diagnosis-only tasks identify the cause and smallest useful next action; repair tasks fix the failure and pass the affected verification gate. If repair is blocked, report the blocker and next action without claiming completion.
