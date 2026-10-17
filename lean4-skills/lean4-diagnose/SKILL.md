---
name: lean4-diagnose
description: "Use for formal-mathematics Lean 4/Lake work when the task needs root-cause diagnosis of elaboration, module, import, dependency, toolchain, build, or integration failures, especially when several symptoms may share one cause or a migration path is needed. Do not use for general Lean application/CLI/FFI development."
license: MIT
---

# Lean 4 Diagnose

## Purpose

Identify the root cause of a Lean/Lake/module/dependency/integration failure and the smallest justified migration or repair path.

## First rule

Obtain the exact current diagnostic, reproduction boundary, and nearby source context before editing. Prefer a root-cause hypothesis that explains the observed symptoms over independent symptom patching.

## Useful diagnosis targets

- several declarations or files failing after the same dependency or toolchain change;
- imports, namespaces, visibility, generated artifacts, or module boundaries behaving inconsistently;
- Lake targets, package resolution, build configuration, or repository integration failures;
- upstream API movement or signature changes that require identifying a common migration;
- a single diagnostic when explaining its cause is material to the requested work.

## Triage

- **Cluster before patching:** when several failures appear together, identify shared imports, APIs, instances, toolchain changes, or build boundaries before fixing symptoms independently.
- **Type mismatch:** compare expected and actual types; inspect implicit arguments, universes, equality direction, changed signatures, and local instances before adding coercions or `convert`.
- **Failed to synthesize instance:** determine whether the instance is absent, moved, or blocked by unresolved metavariables before manufacturing local evidence.
- **Unknown identifier / invalid field / imports:** check spelling, namespace, active imports, visibility, and the actual current declaration signature. Search local declarations and active imports before widening outward.
- **Recursion depth / heartbeat / timeout:** distinguish elaboration/reduction depth from tactic or typeclass work. Localize the bottleneck before raising limits or calling it a performance problem.
- **Build/integration mismatch:** distinguish source state from built artifacts and reproduce at the smallest boundary that exercises the suspected dependency or build path.

## Repair discipline

Prefer the smallest change that tests the current root-cause hypothesis. Do not widen a migration into unrelated refactoring, silently revise public statements, or weaken the trust basis with new axioms, `sorry`, or `admit`.

If the requested work includes a bounded fix after the cause is established, keep the repair tied to that evidence rather than broadening into unrelated cleanup.

## Verification and completion

Re-run the command or repository gate that exercises the failing boundary. A passing file-local `lake env lean` check is not evidence that changed imports or a build/integration boundary is fixed; use a dependency-aware or repository-configured gate when that boundary is material, and report what actually ran.

Done means the root cause is supported by reproducible evidence and either the requested failure is repaired under the appropriate gate or the smallest remaining migration/diagnostic action is explicit. Do not claim a boundary is fixed from a weaker check that does not exercise it.
