---
name: lean4-diagnose
description: "Use for formal-mathematics Lean 4/Lake work when the task needs root-cause diagnosis of elaboration, module, import, dependency, toolchain, build, or integration failures, especially when several symptoms may share one cause or a migration path is needed. Do not use for general Lean application/CLI/FFI development."
license: MIT
---

# Lean 4 Diagnose

Identify the root cause of a Lean/Lake/module/dependency/integration failure and the smallest justified migration or repair path.

Start from the exact diagnostic, reproduction boundary, and nearby source. Prefer one cause that explains clustered symptoms over independent symptom patching.

## Triage

- **Clustered failures:** inspect shared imports, APIs, instances, toolchain changes, and build boundaries before patching files independently.
- **Type mismatch:** compare expected and actual types, including implicit arguments, universes, equality direction, changed signatures, and local instances.
- **Instance failure:** determine whether the instance is absent, moved, or blocked by unresolved metavariables before manufacturing local evidence.
- **Unknown identifier / field / import:** inspect spelling, namespace, visibility, active imports, and the current declaration signature.
- **Depth / heartbeat / timeout:** localize whether the cost is elaboration, reduction, tactic work, or typeclass search before raising limits.
- **Build mismatch:** distinguish source state from built artifacts and reproduce at the smallest boundary that exercises the suspected dependency path.

Prefer the smallest change that tests the root-cause hypothesis. Do not turn diagnosis into unrelated refactoring, silent API revision, or trust weakening.

## Completion

Re-run the command or repository gate that exercises the failing boundary and report what it establishes. A file-local pass is not enough when the suspected failure is in a changed dependency or integration boundary.

Done means the root cause is supported by reproducible evidence and either the requested failure is repaired at the relevant boundary or the smallest remaining migration/diagnostic action is explicit.
