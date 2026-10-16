---
name: lean4-trust
description: "Use for Lean 4/mathlib when the requested outcome is to inspect, explain, or reduce the trust basis of a declaration: explicit axioms or assumptions, unresolved `sorry`/`admit` as trust dependencies, `#print axioms`, or removal of unacceptable trust dependencies under an explicit policy. Do not use merely because a fixed theorem currently contains a proof hole or `sorry`/`admit` when the requested outcome is ordinary proof completion; use lean4-prove for that. Do not infer trust properties merely from successful elaboration."
license: MIT
---

# Lean 4 Trust

## Purpose

Inspect and, when requested, reduce a declaration's trust dependencies against an explicit project/task policy.

## Inspect first

For a named declaration, use Lean's own environment to inspect dependencies and, when relevant, `#print axioms <declaration>` in the project context. Successful elaboration alone does not establish the trust basis the user expects.

Distinguish:

- explicit project `axiom` declarations;
- unresolved `sorry`/`admit` placeholders when the task is auditing or cleaning the trust basis rather than merely completing an ordinary proof;
- ordinary proved theorems that transitively depend on assumptions;
- Lean/kernel principles such as choice, propositional extensionality, or quotient soundness, whose acceptability depends on project policy.

Do not label a dependency unacceptable merely because it appears in `#print axioms`; interpret it against the requested policy.

## Cleanup

1. Trace each unwanted assumption through the target and dependent declarations.
2. Search local code and active imports before widening to mathlib for an accepted replacement; validate candidate declarations in the actual project context.
3. If necessary, prove the smallest missing lemma from accepted hypotheses.
4. Replace the dependency without strengthening the theorem statement or silently introducing another unacceptable assumption.
5. Re-run the relevant semantic/integration gate. Load [verification guidance](../references/verification.md) when dependency or project scope matters, then re-check the target's trust basis.

Work bottom-up when unwanted assumptions depend on one another.

## Boundaries and completion

An ordinary request to fill a proof hole in an already-fixed declaration belongs to `lean4-prove`, even if the current source spells that hole as `sorry` or `admit`. This skill owns the task when the user is asking what the declaration trusts, whether a placeholder or axiom contaminates that trust basis, or how to remove an unacceptable dependency under a stated policy. Trust cleanup may compose with `lean4-prove`, but the audit/cleanup outcome remains the reason this skill was selected.

If cleanup reveals that the theorem is too strong, use `lean4-formalize` for authorized statement design or `lean4-refute` when there is credible evidence of falsity; do not swap one unacceptable assumption for another.

Return the declaration checked, the policy used, assumptions removed or still present, verification gate that ran, and any remaining trust-policy uncertainty.
