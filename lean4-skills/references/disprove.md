# Refutation Workflow

Use to show a Lean proposition is false or to find a Lean-certified counterexample.

## Contract

1. Resolve the exact proposition and preserve the original declaration.
2. Inspect its logical shape and look for the cheapest promising refutation route: a concrete witness, a small decidable/finite search, contradiction with existing facts, or a direct proof of the negation.
3. Search local declarations and mathlib before building specialized machinery.
4. Encode a candidate witness or negation as a separate result and ask Lean to certify it.
5. Keep the search bounded. Failure to find a counterexample is not evidence that the original proposition is true.

## Outcomes

- **REFUTED:** Lean typechecks a result that logically refutes the target under the agreed trust basis.
- **WITNESS_UNCERTIFIED:** a plausible witness or argument exists but Lean certification did not complete.
- **INCONCLUSIVE:** the bounded search produced no certified refutation.

Only `REFUTED` is a certified disproof.
