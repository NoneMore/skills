---
name: lean4-refute
description: "Use for formal mathematics in Lean 4/mathlib when the task is to show a proposition is false or to find and Lean-certify a counterexample or proof of its negation. Do not treat failed proof search or exploratory counterexample probing alone as certified falsity."
license: MIT
---

# Lean 4 Refute

## Workflow

1. Resolve the exact proposition and choose the cheapest bounded route: concrete witness, small decidable search, contradiction from accepted facts, or direct negation.
2. Search local and imported APIs before broader mathlib; validate candidates in context.
3. Encode the witness or negation as a separate result and ask Lean to certify it. Failed proof search is not evidence of falsity, and the target declaration itself must not serve as evidence for its refutation.
4. If the target or environment contains `sorry`/`admit`, custom axioms, or uncertain trust dependencies, inspect the refutation's trust basis and reject certification if it depends on the target, `sorryAx`, or another forbidden assumption.
5. Verify the affected scope and report what ran. Do not introduce new axioms, `sorry`, or `admit` to manufacture a result.

## Outcomes

- **REFUTED:** an independent Lean result refutes the target under the accepted trust policy.
- **WITNESS_UNCERTIFIED:** a plausible witness or argument exists but required certification did not complete.
- **INCONCLUSIVE:** bounded search produced no certified refutation.

Only `REFUTED` is a certified disproof.
