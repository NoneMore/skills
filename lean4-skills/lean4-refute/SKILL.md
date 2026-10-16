---
name: lean4-refute
description: "Use for formal mathematics in Lean 4/mathlib when the requested outcome is to show a proposition is false or to find and Lean-certify a counterexample or proof of its negation. Do not treat failed proof search or exploratory counterexample probing alone as certified falsity."
license: MIT
---

# Lean 4 Refute

## Purpose

Produce a Lean-certified logical refutation of a target proposition while preserving the original target.

## Invariants

- Preserve the original declaration; encode witnesses or negations as separate checked results.
- Failure to prove a proposition is not evidence that it is false.
- Do not weaken the trust basis with new axioms, `sorry`, or `admit` to manufacture a refutation.

## Workflow

1. Resolve the exact proposition and inspect its logical shape.
2. Choose the cheapest promising bounded route: a concrete witness, a small decidable/finite search, contradiction with existing facts, or a direct proof of the negation.
3. Search local declarations and mathlib before building specialized machinery; use [mathlib search and integration](../references/mathlib-guide.md) when useful.
4. Encode the candidate witness or negation as a separate result and ask Lean to certify it.
5. Verify the checked result with the lightest gate that establishes the requested scope; use [verification guidance](../references/verification.md) when needed.

Keep search bounded. If the proposition instead needs redesign, use `lean4-formalize`; if the user wants to keep proving the fixed target, use `lean4-prove`. If the user is only exploring whether an assumption may be unnecessary or probing examples/counterexamples to understand the boundary, use `lean4-explore` until certified falsity becomes the requested outcome.

## Outcomes

- **REFUTED:** Lean typechecks a result that logically refutes the target under the agreed trust basis.
- **WITNESS_UNCERTIFIED:** a plausible witness or argument exists but Lean certification did not complete.
- **INCONCLUSIVE:** bounded search produced no certified refutation.

Only `REFUTED` is a certified disproof.
