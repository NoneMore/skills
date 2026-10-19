---
name: lean4-diagnose
description: "Use when root-cause diagnosis or a migration plan is the requested Lean 4/mathlib/Lake outcome, especially for shared elaboration, module, import, dependency, toolchain, build, or integration failures. Routine local proof repair belongs to the proving task, not a required diagnostic handoff. Not for general Lean application/FFI work."
license: MIT
---

# Lean 4 Diagnose

Start from the exact diagnostic, reproduction boundary, and nearby source. Prefer one cause that explains clustered symptoms over independent symptom patching.

## Triage

- **Shared boundary:** for clustered failures or build mismatches, inspect common imports, APIs, toolchain changes, and source-versus-artifact state before patching files independently.
- **Elaboration:** for type, instance, identifier, field, or import failures, compare expected and actual types/signatures, implicits, universes, namespaces, active imports, and instance availability.
- **Resource limits:** localize elaboration, reduction, tactic, or typeclass-search cost before raising limits.

Test the root-cause hypothesis with the smallest justified change. Do not turn diagnosis into unrelated refactoring, silent API revision, or trust weakening.

## Completion

Re-run the command or repository gate that exercises the failing boundary; a file-local pass is insufficient when the suspected cause crosses a changed dependency or integration boundary. Done means the root cause has reproducible support and either the requested failure is repaired or the smallest remaining migration/diagnostic action is explicit.
