---
name: lean4-diagnose
description: "Use for formal-mathematics Lean 4/Lake work when the requested outcome is root-cause diagnosis of a failure that is not naturally owned by one declaration or proof task, especially breakage across module, import, dependency, toolchain, build, or integration boundaries. Also use when diagnosis itself is explicitly requested. Local diagnostics encountered while delivering another concrete outcome stay with that owning Skill. Do not use for general Lean application/CLI/FFI development."
license: MIT
---

# Lean 4 Diagnose

## Purpose

Identify the root cause of a Lean/Lake/module/dependency/integration failure and the smallest justified migration or repair path when no single declaration or proof task naturally owns the problem, or when diagnosis itself is the requested result.

## First rule

Obtain the exact current diagnostic, reproduction boundary, and nearby source context before editing. First decide whether this is an artifact-owned failure or a boundary-owned/root-cause investigation.

## Ownership

Artifact-owned failures stay with the Skill that owns the requested artifact outcome. A type mismatch, instance failure, unknown identifier, or tactic failure encountered while formalizing a declaration, repairing a fixed proof, certifying a refutation, reviewing code, optimizing a proof, or adapting an upstream contribution remains an internal substep of that work.

Use this Skill when diagnosis itself is the deliverable or when the failure crosses a boundary such as:

- several declarations or files failing after the same dependency or toolchain change;
- imports, namespaces, visibility, generated artifacts, or module boundaries behaving inconsistently;
- Lake targets, package resolution, build configuration, or repository integration failures;
- upstream API movement or signature changes that require identifying a common migration rather than repairing one owned proof;
- symptoms whose common cause must be isolated before any artifact-specific repair is justified.

## Triage

- **Cluster before patching:** when several failures appear together, identify shared imports, APIs, instances, toolchain changes, or build boundaries before fixing symptoms independently.
- **Type mismatch:** compare expected and actual types; inspect implicit arguments, universes, equality direction, changed signatures, and local instances before adding coercions or `convert`.
- **Failed to synthesize instance:** determine whether the instance is absent, moved, or blocked by unresolved metavariables before manufacturing local evidence.
- **Unknown identifier / invalid field / imports:** check spelling, namespace, active imports, visibility, and the actual current declaration signature. Search local declarations and active imports before widening outward.
- **Recursion depth / heartbeat / timeout:** distinguish elaboration/reduction depth from tactic or typeclass work. Localize the bottleneck before raising limits or calling it a performance problem.
- **Build/integration mismatch:** distinguish source state from built artifacts and reproduce at the smallest boundary that exercises the suspected dependency or build path.

## Repair discipline

Prefer the smallest change that tests the current root-cause hypothesis. Do not widen a migration into unrelated refactoring, silently revise public statements, or weaken the trust basis with new axioms, `sorry`, or `admit`.

When the investigation converges to one owned artifact, return that root cause and let the owning outcome govern the actual repair unless the user explicitly asked this Skill to carry the bounded fix through.

## Verification and completion

Re-run the command or repository gate that exercises the failing boundary. A passing file-local `lake env lean` check is not evidence that changed imports or a build/integration boundary is fixed; use a dependency-aware or repository-configured gate when that boundary is material, and report what actually ran.

Done means the root cause is supported by reproducible evidence and either the requested boundary failure is repaired under the appropriate gate or the smallest remaining migration/diagnostic action is explicit. Do not claim a boundary is fixed from a weaker check that does not exercise it.
