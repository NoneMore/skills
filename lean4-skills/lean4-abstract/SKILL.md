---
name: lean4-abstract
description: >-
  Use for Lean 4/mathlib formal mathematics when multiple existing proofs or
  declarations may share mathematical structure and the task is to discover,
  extract, generalize, and integrate a reusable abstraction across them.
  Not for isolated statement design or ordinary single-proof cleanup.
license: MIT
---

# Lean 4 Abstract

Find reusable *mathematical* structure across multiple existing Lean proofs or declarations,
then decide whether an abstraction improves their design. Shared tactic syntax alone is not
evidence of a shared mathematical argument.

## Workflow

1. Determine the requested proof/declaration set and whether the user asks for an assessment
   or implementation. Establish the current statements, proof status, and applicable
   repository verification gate. Limit investigation to those consumers and relevant
   dependencies or plausible abstraction owners.
2. Compare representative sites: identify common constructions, hypotheses, invariants,
   and conclusions, as well as differences that may obstruct generalization. Search local
   and imported APIs before broader mathlib for an existing result or canonical structure.
3. Compare the smallest plausible outcomes: reuse an existing API, extract a private helper,
   introduce a genuinely reusable declaration, or leave the proofs independent. Distinguish
   mathematical generality from convenience wrappers or elaboration boundaries. Do not
   promote helpers to public API merely because they are long or private.
4. Test a candidate declaration and its intended applications in the actual Lean context
   before migrating consumers. Check that differing hypotheses, universes, coercions, and
   typeclass inference do not make the abstraction misleading or harder to use.
5. If implementation is requested, make one coherent change at a time, migrate only
   affected consumers, and verify the affected dependency/integration scope. Preserve
   existing public statements, accepted trust basis, and unrelated work unless explicitly
   authorized otherwise.

## Acceptance and stopping

Accept an abstraction only when its verified reuse, mathematical clarity, or stable
integration boundary outweighs added parameters, indirection, inference/search burden,
and maintenance cost. Prefer existing library APIs to parallel implementations.

Reject superficial similarity or a candidate requiring incompatible special cases.
Stop when attempts repeat the same structural blocker, a new helper spawns an unresolved
helper chain, or further generalization becomes speculative. Report broader architectural
possibilities separately; do not silently widen into open-ended reconnaissance.

Do not add axioms, `sorry`, or `admit` to manufacture success. Do not claim
dependency-aware verification from a file-local check against stale imported artifacts.

## Completion

- **Assessment:** report the proposed abstraction or reason not to extract one, the
  representative consumers and evidence, tradeoffs, and the next useful action. Do not
  modify production source for an assessment-only request.
- **Implementation:** report the abstraction added or reused, consumers migrated,
  concrete benefit over the baseline, verification actually performed, and limitations.
  If representative uses or a required gate cannot be checked, report the work as partial.

Do not commit or push unless authorized by the current task. Prompt-level guidance
does not replace runtime or tool-level authorization enforcement.
