---
name: lean4-abstract
description: >-
  Use for Lean 4/mathlib when concrete evidence suggests reusable mathematical
  structure within one proof, across declarations, or in existing library code,
  and the task is to investigate, validate, or extract that reuse.
  Not for routine proof completion, local cleanup, or isolated statement design.
license: MIT
---

# Lean 4 Abstract

Recognize and evaluate reusable *mathematical* structure: repeated subarguments
inside a large proof, similarities to earlier declarations, or a known library
construction. Multiple top-level theorems are not required. Shared tactic syntax
alone is not evidence of a shared mathematical argument.

## Workflow

1. Identify the concrete reuse signal and representative sites, whether the task
   requests assessment or implementation, and the applicable verification gate.
   A signal may be repeated invariants within one proof or a plausible match to
   earlier work. Ordinary proof work does not justify speculative repository-wide
   similarity searches.
2. Compare the smallest relevant sites and their constructions, hypotheses,
   invariants, and conclusions. Search within the active proof and nearby code,
   then local and imported APIs; widen to targeted repository/mathlib search only
   when a specific construction, theorem family, or plausible owner motivates it.
3. Compare the smallest useful outcomes: apply an existing result, factor a local
   or private helper, introduce a reusable declaration, or make no change.
   Distinguish mathematical generality from elaboration convenience; do not
   create public API just because a helper is long or private.
4. Validate candidate statements and representative applications in the actual
   Lean context (including repeated local uses in a single proof). Check
   hypotheses, universes, coercions, and typeclass inference. Place any new
   declaration at an appropriate mathematical layer without introducing
   unnecessary imports or reversing dependency direction.
5. Separate investigation from modification authority. Reading earlier consumers
   to assess reuse does not authorize editing or migrating them. If implementation
   was requested, change only authorized sites, verify the affected integration
   scope, and preserve public statements, accepted trust, and unrelated work.

## Acceptance and stopping

Accept extraction only when checked reuse, clarity, or a stable mathematical
boundary outweighs indirection, parameters, inference/search burden, and
maintenance cost. Prefer existing APIs to parallel implementations. A local
helper can be the correct endpoint; publication and migration are optional.

Reject superficial similarity and incompatible special cases. Stop when the
same structural blocker repeats, a helper chain stops making progress, or
broader search becomes speculative. Report possible wider redesign separately;
open-ended semantic reconnaissance belongs to user-invoked `lean4-recon`.

Do not add axioms, `sorry`, or `admit` to manufacture success. Do not claim
dependency-aware verification from file-local checks against stale imports.

## Completion

- **Assessment:** identify candidate reuse or explain why not to extract it;
  give representative sites, evidence, tradeoffs, and next action. Do not edit
  production sources on an assessment-only request.
- **Implementation:** identify the reused or extracted abstraction, authorized
  consumers changed, concrete benefit, verification actually performed, and
  limitations. If candidate uses or the required gate cannot be checked,
  report the result as partial.

Do not commit or push unless authorized by the current task. Prompt guidance
does not replace runtime/tool authorization enforcement.
