---
name: lean4-diagnose
description: "Use for Lean 4/Lake diagnostics arising in formal-mathematics or mathlib work when a concrete failure is the primary problem: type mismatches, instance synthesis, imports/namespaces, elaboration depth, heartbeat/timeouts, visibility, or build/integration failures. Diagnose before changing source, preserve the governing statement/trust contract, and hand ordinary proof search to lean4-prove once the diagnostic class is understood. Do not use for open-ended abstraction exploration or general Lean application/CLI/FFI development."
license: MIT
---

# Lean 4 Diagnose

## Purpose

Classify a concrete formal-mathematics Lean/Lake failure before editing, then make the smallest source change that tests the current diagnosis without weakening the governing task contract.

## First rule

Obtain the exact current diagnostic and nearby source context. Do not treat every elaboration failure as a proof-search problem.

## Invariants

- Preserve existing theorem statements, declaration signatures, and public API unless statement design is explicitly authorized. If diagnosis shows the statement itself is the blocker, surface that and hand authorized statement work to `lean4-formalize` rather than silently changing it.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to clear a diagnostic.
- Do not modify generated caches or dependency checkouts such as `.lake/packages` unless the requested diagnostic specifically concerns those artifacts.
- When diagnosis supports another capability that owns the requested outcome, preserve that owner's stricter mutation, trust, scope, and verification invariants.

## Triage

- **Type mismatch:** compare expected and actual types before adding coercions or `convert`; inspect implicit arguments, universes, equality direction, candidate signatures, and local instances.
- **Failed to synthesize instance:** first determine whether the instance is truly absent or its parameters still contain unresolved metavariables. Add the smallest useful annotations before manufacturing new evidence.
- **Recursion depth / heartbeat / timeout:** distinguish reduction/elaboration depth from excessive tactic or typeclass work. Narrow automation before raising limits; diagnose the bottleneck before turning the task into performance optimization.
- **Unknown identifier / invalid field / imports:** check spelling, namespace, active imports, visibility, and actual declaration signatures. Search local declarations and active imports before widening outward; do not guess API names.
- **Unsolved goals / tactic failed:** inspect the remaining goal. If the remaining problem is ordinary proof search, use `lean4-prove`.
- **No goals to be solved:** remove the redundant later tactic; an earlier tactic already closed the goal.

For upstream mathlib work, consult current authoritative contribution policy and nearby current mathlib code.

## Boundaries

If there is no concrete diagnostic and the main uncertainty is instead what formal abstraction, API, hypothesis boundary, or approach should be pursued, use `lean4-explore`. If diagnosis reduces the problem to a known proof obligation, hand off to `lean4-prove`. If the only viable repair would revise a fixed statement or trust basis, report that blocker and use the capability that owns the newly authorized outcome rather than broadening diagnosis implicitly.

## Verification and stop behavior

After each hypothesis-driven edit, re-read the diagnostic. When file-local, dependency-aware, or project-level scope matters, load [verification guidance](../references/verification.md) and report the gate that actually ran.

Do not broaden a local diagnostic into general architecture or application refactoring. If the task leaves formal mathematics and becomes general Lean application development, stop using this skill.

Done means the failure class is resolved enough that the requested code works under the required verification gate without violating the governing statement/trust contract, or the remaining blocker and next diagnostic action are explicit.
