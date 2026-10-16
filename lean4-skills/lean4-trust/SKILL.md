---
name: lean4-trust
description: "Use for Lean 4/mathlib tasks explicitly about axioms, assumptions, `sorry`/`admit`, `#print axioms`, or the trust basis of a declaration, including removing unwanted trust dependencies. Do not infer trust properties merely from successful elaboration."
license: MIT
---

# Lean 4 Trust

## Purpose

Inspect and, when requested, reduce a declaration's trust dependencies against an explicit project/task policy.

## Inspect first

For a named declaration, use Lean's own environment to inspect dependencies and, when relevant, `#print axioms <declaration>` in the project context. Successful elaboration alone does not establish the trust basis the user expects.

Distinguish:

- explicit project `axiom` declarations;
- unresolved `sorry`/`admit` placeholders;
- ordinary proved theorems that transitively depend on assumptions;
- Lean/kernel principles such as choice, propositional extensionality, or quotient soundness, whose acceptability depends on project policy.

Do not label a dependency unacceptable merely because it appears in `#print axioms`; interpret it against the requested policy.

## Cleanup

1. Trace each unwanted assumption through the target and dependent declarations.
2. Search local code and mathlib for an accepted replacement; use [mathlib search guidance](references/mathlib-guide.md) when useful.
3. If necessary, prove the smallest missing lemma from accepted hypotheses.
4. Replace the dependency without strengthening the theorem statement or silently introducing another unacceptable assumption.
5. Re-run the relevant semantic/integration gate using [verification guidance](references/verification.md), then re-check the target's trust basis.

Work bottom-up when unwanted assumptions depend on one another.

## Boundaries and completion

If cleanup reveals that the theorem is too strong, use `lean4-formalize` for authorized statement design or `lean4-refute` when there is credible evidence of falsity; do not swap one unacceptable assumption for another.

Return the declaration checked, the policy used, assumptions removed or still present, verification gate that ran, and any remaining trust-policy uncertainty.
