---
name: lean4-refute
description: "Use for formal mathematics in Lean 4/mathlib when the task is to show a proposition is false or to find and Lean-certify a counterexample or proof of its negation. Do not treat failed proof search or exploratory counterexample probing alone as certified falsity."
license: MIT
---

# Lean 4 Refute

Produce a Lean-certified logical refutation while preserving the original target.

## Contract

- Failed proof search is not evidence of falsity.
- Encode a witness or negation as a separate checked result; do not use the target declaration itself as evidence for its refutation.
- Do not introduce new axioms, `sorry`, or `admit` to manufacture a result.

## Workflow

1. Resolve the exact proposition and choose the cheapest bounded route: concrete witness, small decidable search, contradiction from accepted facts, or direct negation.
2. Search local declarations and active imports before widening to mathlib; validate candidates in the project context.
3. Encode the candidate as an independent result and ask Lean to certify it.
4. When the target or environment contains `sorry`/`admit`, custom axioms, or uncertain trust dependencies, inspect the refutation's trust basis (for example with `#print axioms`) and reject certification if it depends on the target, `sorryAx`, or another forbidden assumption.
5. Run the verification gate needed by the affected scope and report what ran.

A plausible witness remains uncertified evidence until Lean checks an independent refutation under the accepted trust policy.

## Outcomes

- **REFUTED:** an independent Lean result refutes the target under the accepted trust policy.
- **WITNESS_UNCERTIFIED:** a plausible witness or argument exists but required certification did not complete.
- **INCONCLUSIVE:** bounded search produced no certified refutation.

Only `REFUTED` is a certified disproof.
