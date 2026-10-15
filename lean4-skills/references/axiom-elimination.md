# Axiom and Trust-Basis Cleanup

Use when a task explicitly concerns unwanted axioms, assumptions, `sorry`/`admit`, or the trust basis of a declaration. This is not a rule that every project must avoid every kernel axiom; the acceptable trust basis is project- and task-specific.

## Inspect first

For a named declaration, use Lean's own environment to inspect its dependencies and, when relevant, `#print axioms <declaration>` in the project context. A successful theorem elaboration does not by itself mean that the theorem has the trust basis the user expects.

Distinguish:

- explicit project `axiom` declarations;
- unresolved `sorry`/`admit` placeholders;
- ordinary proved theorems that transitively depend on assumptions;
- Lean/kernel principles such as choice, propositional extensionality, or quotient soundness, whose acceptability depends on the project's policy.

Do not label a dependency "custom" or "unacceptable" merely because it appears in `#print axioms`; interpret the result against the requested policy.

## Elimination workflow

1. Identify the exact declaration whose trust basis matters.
2. Inspect the unwanted assumption and the declarations that depend on it.
3. Search local code and mathlib for an existing theorem that provides the needed fact without that assumption.
4. If none exists, prove the smallest missing lemma from accepted hypotheses.
5. Replace the dependency without strengthening the theorem statement or silently adding a different assumption.
6. Re-run the relevant elaboration/integration gate and re-check the target's trust basis.

Work bottom-up when several unwanted assumptions depend on one another.

## Statement problems

Sometimes elimination reveals that the theorem is actually too strong. Do not hide that by replacing one axiom with another or by weakening an existing statement silently. Hand statement design to the formalization workflow, or refutation to the disprove workflow when there is credible evidence of falsity.

## Completion

Report the declaration checked, the unwanted assumptions removed or still present, the verification gate that ran, and any remaining trust-policy uncertainty.
