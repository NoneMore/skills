---
name: lean4-challenge
description: >-
  Explicitly user-invoked, advisory investigation of consequential Lean 4/mathlib
  mathematical design choices. Question the current framing, abstractions,
  proof mechanisms, APIs, or theory organization using focused evidence.
disable-model-invocation: true
license: MIT
---

# Lean 4 Challenge

Question consequential mathematical design choices and return evidence-backed comparisons, including reasons to retain the current design. Unlike `lean4-review` (findings against criteria for a specified artifact), Challenge asks whether the design itself should differ. Proof, formalization, and optimization are investigative techniques, not production deliverables.

## Investigation

Follow the user's requested outcome. If they only ask for promising directions, return a prioritized shortlist with discriminating next checks. Otherwise, investigate relevant design alternatives far enough to reach a supported judgment. For open-ended requests, identify consequential decisions from the mathematics and downstream uses without requiring the user to name a direction. Scope work to what could change the judgment, not a fixed depth mode or an exhaustive repository survey.

Use the following **optional, non-exhaustive** lenses when their specialized guidance helps; they are neither a checklist nor the limits of the design space:

- **[Mathematical framing](references/mathematical-framing.md):** generic owners, canonical notions, alternative characterizations and duals.
- **[Abstraction and reuse](references/abstraction-reuse.md):** shared mathematical invariants; existing result, helper, or no extraction.
- **[API expressivity](references/api-expressivity.md):** assumptions, information retained and downstream use.
- **[Proof architecture](references/proof-architecture.md):** competing mathematical mechanisms rather than tactic length.
- **[Theory organization](references/theory-organization.md):** theorem ownership, imports and dependency placement.

Group overlapping symptoms by the underlying decision, not by lens. Parallelize substantive independent investigations when useful and supported; otherwise work directly.

## Compare with evidence

1. Recover the intended mathematics, relevant consumers, and alternatives, including the current design.
2. Prefer the smallest discriminating check: targeted mathlib search, `#check`/`#synth`, scratch Lean examples, boundary cases, minimal imports, or a representative downstream composition path.
3. Test a potential drawback of promising alternatives (assumptions, information loss, inference, dependencies, consumer fit, maintenance). Elaboration shows feasibility, not superiority.
4. Stop when further investigation is unlikely to change the judgment. Do not force novelty.

## Outcome and scope

Return the requested shortlist or comparative judgment with actual evidence, costs, unresolved questions, and next verification needs. Distinguish checked Lean facts from unverified reasoning; report missing tools or limits. **Do not edit production source or durable repository artifacts under Challenge, even if asked to implement.** Scratch experiments are allowed. Describe implications of recommended changes without promising an implementation plan, execution owner, or migration workflow.
