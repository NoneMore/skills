---
name: lean4-trust
description: "Use for Lean 4/mathlib when inspecting, explaining, or reducing the trust basis of a declaration: explicit axioms or assumptions, unresolved `sorry`/`admit` dependencies, `#print axioms`, or removal of unacceptable trust dependencies under an explicit policy. Do not infer trust properties merely from successful elaboration."
license: MIT
---

# Lean 4 Trust

Inspect and, when requested, reduce a declaration's trust dependencies against an explicit task or project policy.

## Inspect

Use Lean's environment and, when relevant, `#print axioms <declaration>`. Distinguish project axioms, unresolved placeholders, transitive assumptions, and ordinary Lean/kernel principles; acceptability is determined by the requested policy, not by appearance in `#print axioms` alone.

## Cleanup

1. Trace each unwanted assumption through the target and its dependencies.
2. Search local code and active imports before widening to mathlib for an accepted replacement.
3. Prove the smallest missing lemma when necessary.
4. Replace the dependency without silently strengthening the theorem statement or substituting another forbidden assumption.
5. Re-run the semantic/integration gate required by the edited scope, then re-check the target's trust basis.

If the theorem is not derivable under the accepted policy, report the blocker instead of changing the statement or trust policy implicitly.

## Completion

Return the declaration checked, policy used, assumptions removed or still present, verification performed, and any material trust uncertainty. Successful elaboration alone is not a trust audit.
