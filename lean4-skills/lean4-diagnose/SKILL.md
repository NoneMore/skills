---
name: lean4-diagnose
description: "Use for Lean 4/Lake diagnostics arising in formal-mathematics or mathlib work when a concrete failure is the primary problem: type mismatches, instance synthesis, imports/namespaces, elaboration depth, heartbeat/timeouts, visibility, or build/integration failures. Do not use for ordinary proof search, open-ended abstraction exploration, or general Lean application/CLI/FFI development."
license: MIT
---

# Lean 4 Diagnose

## Purpose

Classify a concrete formal-mathematics Lean/Lake failure before editing, then make the smallest source change that tests the current diagnosis.

## First rule

Obtain the exact current diagnostic and nearby source context. Do not treat every elaboration failure as a proof-search problem.

## Triage

- **Type mismatch:** compare expected and actual types before adding coercions or `convert`; inspect implicit arguments, universes, equality direction, candidate signatures, and local instances.
- **Failed to synthesize instance:** first determine whether the instance is truly absent or its parameters still contain unresolved metavariables. Add the smallest useful annotations before manufacturing new evidence.
- **Recursion depth / heartbeat / timeout:** distinguish reduction/elaboration depth from excessive tactic or typeclass work. Narrow automation before raising limits; load [performance guidance](references/performance-optimization.md) when the failure is performance-driven.
- **Unknown identifier / invalid field / imports:** check spelling, namespace, active imports, visibility, and actual declaration signatures. Search rather than guessing API names; use [mathlib search guidance](references/mathlib-guide.md) when relevant.
- **Unsolved goals / tactic failed:** inspect the remaining goal. If the remaining problem is ordinary proof search, use `lean4-prove`.
- **No goals to be solved:** remove the redundant later tactic; an earlier tactic already closed the goal.

For upstream mathlib work, also load [upstream guidance](references/branches/mathlib-upstream.md).

## Boundaries

If there is no concrete diagnostic and the main uncertainty is instead what formal abstraction, API, hypothesis boundary, or approach should be pursued, use `lean4-explore`. If diagnosis reduces the problem to a known proof obligation, hand off to `lean4-prove`.

## Verification and stop behavior

After each hypothesis-driven edit, re-read the diagnostic. Distinguish file-local from dependency-aware and project-level checks using [verification guidance](references/verification.md).

Do not broaden a local diagnostic into general architecture or application refactoring. If the task leaves formal mathematics and becomes general Lean application development, stop using this skill.

Done means the failure class is resolved enough that the requested code works under the required verification gate, or the remaining blocker and next diagnostic action are explicit.
