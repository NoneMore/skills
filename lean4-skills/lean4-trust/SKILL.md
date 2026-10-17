---
name: lean4-trust
description: "Use for Lean 4/mathlib when inspecting, explaining, or reducing the trust basis of a declaration: explicit axioms or assumptions, unresolved `sorry`/`admit` dependencies, `#print axioms`, or removal of unacceptable trust dependencies under an explicit policy. Do not infer trust properties merely from successful elaboration."
license: MIT
---

# Lean 4 Trust

## Workflow

1. Inspect the environment and, when relevant, `#print axioms <declaration>`. Distinguish project axioms, unresolved placeholders, transitive assumptions, and ordinary Lean/kernel principles; interpret them against the requested policy.
2. Trace each unwanted assumption through the target and its dependencies.
3. Search local and imported APIs for an accepted replacement; prove the smallest missing lemma when necessary.
4. Replace the dependency without strengthening the theorem statement or substituting another forbidden assumption.
5. Verify the edited scope and re-check the target's trust basis.

If the theorem is not derivable under the accepted policy, report the blocker instead of changing the statement or policy implicitly.

## Completion

Return the declaration checked, policy used, assumptions removed or still present, verification performed, and any material trust uncertainty. Successful elaboration alone is not a trust audit.
