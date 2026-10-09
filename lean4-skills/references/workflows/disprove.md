# Refutation Workflow

Use when the goal is to show a Lean statement is false or to find a certified counterexample. Refutation has a different success condition from proving and should not be hidden inside the normal proving path.

## Contract

1. Resolve the exact proposition and preserve the original declaration.
2. Inspect whether the goal is decidable, finite, or admits a natural concrete witness search.
3. Search for the cheapest promising counterexample method before broad proof search.
4. When a witness is found, encode a separate counterexample/negation result and ask Lean to certify it.
5. Do not replace the original theorem statement merely because evidence suggests it is false.

Prefer an append-only artifact such as `T_counterexample` or a separate negation theorem when editing a file that already contains the original claim.

## Outcomes

- **REFUTED:** Lean typechecks a result that logically refutes the target.
- **WITNESS_UNCERTIFIED:** a plausible witness was found but Lean certification did not complete.
- **INCONCLUSIVE:** the bounded search found no certified refutation.

Only the first outcome is a certified disproof. For specialized method registries or artifact machinery, consult `../disprove-engine.md` on demand.