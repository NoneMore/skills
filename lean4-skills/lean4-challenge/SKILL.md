---
name: lean4-challenge
description: >-
  User-invoked, experiment-driven challenge of consequential mathematical design
  choices in proposed or existing Lean 4/mathlib formalizations, proofs, APIs,
  and theory/module organization. Compare framing, abstractions, reuse and proof
  strategies using focused counterfactual Lean experiments.
disable-model-invocation: true
license: MIT
---

# Lean 4 Challenge

Investigate whether consequential mathematical design choices should be retained or revised. Judge the quality of an existing or proposed formal development, not merely whether it elaborates or has reviewable correctness defects.

## Investigation

1. Establish the mathematical goal, artifact or proposal, intended users, constraints, and authorized scope. Identify design choices that could materially affect quality; do not apply an exhaustive checklist.
2. Form credible alternatives only where they might change the decision. As relevant, challenge the mathematical framing or representation, theorem hypotheses/generality, proof mechanism, reusable abstraction, API information and ergonomics, or theorem/module placement. Follow a local construction toward its canonical mathematical owner when that matters.
3. Prefer the smallest **discriminating experiment** over verbal plausibility: focused local/mathlib search, `#check`, `#synth`, `#print`, scratch declarations or proofs, minimal imports, concrete instances, and representative consumers in the project's actual Lean/mathlib environment. Compare hypotheses, conclusions, dependency direction, and information retained. If composition across an abstraction boundary is uncertain, follow one representative path until it closes or reveals the lowest-level obstruction.
4. Challenge promising alternatives as well as the existing design. Probe a plausible countervailing cost when it could reverse the recommendation: inference/search burden, proof complexity, lost information, downstream usage, maintenance, or a new abstraction boundary. Feasibility does not establish superiority; failed proof search does not establish impossibility.
5. Compare the material evidence and tradeoffs, then stop when the design decision is stable, a genuine tradeoff remains, or further experiments are unlikely to change the judgment. Do not expand into parallel cases or repository-wide discovery merely to produce more criticism.

## Boundaries

Assessment is read-only for production source; prefer isolated scratch experiments. Never treat a speculative alternative or an unchecked scratch statement as a verified improvement. Distinguish direct Lean checks, mathematical reasoning, qualitative judgments, and unresolved hypotheses. If necessary tools or the intended mathematical specification are unavailable, report the resulting limits instead of claiming verification.

For explicitly authorized implementation or extraction, establish the existing verification baseline or its limits first. Make only evidence-backed changes to requested sites, preserve public statements and the accepted trust basis unless their revision is expressly authorized, and verify affected consumers/imports with a gate covering the changed boundaries. Inspecting additional context does not authorize its migration.

Do not turn a challenge into routine proof repair, open-ended refutation, tactic golf, mathlib upstream readiness review, or automatic multi-Skill orchestration. Existing canonical APIs, a local helper, a justified public abstraction, and no change are all valid outcomes.

## Completion

Return the principal design judgment, the consequential alternatives investigated, decision-changing experiments and their actual outcomes, comparison of mathematical and engineering costs, and the smallest justified next action (including retaining the current design). State unresolved tradeoffs, rejected candidates, unchecked claims, and verification limits. A successful challenge need not produce novelty or a source edit.
