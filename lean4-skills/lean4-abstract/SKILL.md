---
name: lean4-abstract
description: >-
  User-invoked Lean 4/mathlib study of suspected mathematical reuse within
  one proof or across declarations.
disable-model-invocation: true
license: MIT
---

# Lean 4 Abstract

Study a concrete mathematical reuse hypothesis, not tactic resemblance or
speculative repository-wide similarity.

## Workflow

1. Bound the hypothesis, representative sites, and edit authority.
2. Compare hypotheses, constructions, and conclusions; search the current
   proof, nearby code, and existing APIs before widening toward a specific match.
3. Choose an existing result, local/private helper, justified public theorem,
   or no extraction; weigh dependency direction, elaboration, and maintenance.
4. Check the candidate and representative uses in their Lean context. Do not
   weaken hypotheses, public statements, or trust to force a match.
5. Before authorized edits, record the verification baseline or its limits.
   Change only requested sites and verify affected consumers/imports; inspecting
   other consumers does not authorize migration.

## Completion

- **Assessment:** report evidence, tradeoffs, and recommendation without edits.
- **Implementation:** report the reused/extracted result, changed consumers, and
  verification performed; distinguish blockers or unchecked work from completion.
