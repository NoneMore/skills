---
name: lean4-challenge
description: >-
  Explicitly user-invoked, advisory investigation of consequential Lean 4/mathlib
  mathematical design choices. Scout promising questions or experimentally
  compare framing, abstractions, proof mechanisms, APIs, and theory organization.
disable-model-invocation: true
license: MIT
---

# Lean 4 Challenge

Question consequential mathematical design choices and return evidence-backed comparisons, including reasons to retain the current design. Unlike `lean4-review` (findings against criteria for a specified artifact), Challenge asks whether the design itself should differ. Proof, formalization, and optimization are investigative techniques, not production deliverables.

## Match the requested depth

- **Find directions:** scout plausible consequential decisions and return a ranked shortlist with next tests; do not silently investigate them in depth.
- **Assess a design without a named direction:** scout briefly, then test the leading decision enough for a bounded judgment.
- **Investigate a named decision:** compare it directly without broad scouting.
- **Explicitly comprehensive assessment:** compare several material decisions, not the whole repository exhaustively.

When multiple **substantive, independent** investigations are valuable, actively delegate bounded questions to parallel subagents if available; synthesize their evidence. Do not delegate trivial or overlapping questions. Otherwise work sequentially.

## Find the governing decision

These overlapping lenses are optional search aids, not mandatory stages. Use the index to scout; **a named direction does not require reading a reference**. Consult a reference only when its specialized guidance would help.

- **[Mathematical framing](references/mathematical-framing.md):** generic owners, canonical notions, alternative characterizations and duals.
- **[Abstraction and reuse](references/abstraction-reuse.md):** shared mathematical invariants; existing result, helper, or no extraction.
- **[API expressivity](references/api-expressivity.md):** assumptions, information retained and downstream use.
- **[Proof architecture](references/proof-architecture.md):** competing mathematical mechanisms rather than tactic length.
- **[Theory organization](references/theory-organization.md):** theorem ownership, imports and dependency placement.

Group overlapping symptoms by the **underlying decision**, not the lens label.

## Compare with evidence

1. Recover the intended mathematics, relevant consumers, and alternatives, including the current design.
2. Prefer the smallest discriminating check: targeted mathlib search, `#check`/`#synth`, scratch Lean examples, boundary cases, minimal imports, or a representative downstream composition path.
3. Test a potential drawback of promising alternatives (assumptions, information loss, inference, dependencies, consumer fit, maintenance). Elaboration shows feasibility, not superiority.
4. Stop when further investigation is unlikely to change the judgment. Do not force novelty.

## Outcome and scope

Return the requested shortlist or comparative judgment with actual evidence, costs, unresolved questions, and next verification needs. Distinguish checked Lean facts from unverified reasoning; report missing tools or limits. **Do not edit production source or durable repository artifacts under Challenge, even if asked to implement.** Scratch experiments are allowed. Describe implications of recommended changes without promising an implementation plan, execution owner, or migration workflow.
