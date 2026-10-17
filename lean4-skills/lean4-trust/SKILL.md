---
name: lean4-trust
description: "Use for Lean 4/mathlib when inspecting, explaining, or reducing the trust basis of a declaration: explicit axioms or assumptions, unresolved `sorry`/`admit` dependencies, `#print axioms`, or removal of unacceptable trust dependencies under an explicit policy. Do not infer trust properties merely from successful elaboration."
license: MIT
---

# Lean 4 Trust

## Purpose

Inspect and, when requested, reduce a declaration's trust dependencies against an explicit project/task policy.

## Inspect first

For a named declaration, use Lean's own environment to inspect dependencies and, when relevant, `#print axioms <declaration>` in the project context. Successful elaboration alone does not establish the trust basis the user expects.

Distinguish:

- explicit project `axiom` declarations;
- unresolved `sorry`/`admit` placeholders as trust dependencies;
- ordinary proved theorems that transitively depend on assumptions;
- Lean/kernel principles such as choice, propositional extensionality, or quotient soundness, whose acceptability depends on project policy.

Do not label a dependency unacceptable merely because it appears in `#print axioms`; interpret it against the requested policy.

## Cleanup

1. Trace each unwanted assumption through the target and dependent declarations.
2. Search local code and active imports before widening to mathlib for an accepted replacement; validate candidate declarations in the actual project context.
3. If necessary, prove the smallest missing lemma from accepted hypotheses.
4. Replace the dependency without strengthening the theorem statement or silently introducing another unacceptable assumption.
5. Re-run the semantic or integration gate required for the edited scope, then re-check the target's trust basis with `#print axioms` or the equivalent inspection. Successful elaboration alone is not a trust result; if cleanup changes dependency files, use a repository gate that rebuilds the affected dependency boundary before concluding the cleanup holds.

Work bottom-up when unwanted assumptions depend on one another.

## Completion

If cleanup shows that the theorem is not derivable under the accepted trust policy, report that blocker rather than replacing one unacceptable assumption with another or silently revising the statement.

Return the declaration checked, the policy used, assumptions removed or still present, verification gate that ran, and any remaining trust-policy uncertainty.
