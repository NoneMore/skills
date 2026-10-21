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

Question consequential mathematical design choices and return evidence-backed comparisons, including reasons to retain the current design. Unlike `lean4-review` (findings against relatively settled criteria for a specified artifact), Challenge investigates whether the design itself should differ. Proof, formalization, and optimization methods are experiments, not production deliverables.

## Select depth by requested outcome

Direction and deliverable are independent; an unspecified direction does not mean a scout-only answer.

- **Find directions:** scout a bounded set of plausible high-impact decisions, rank by evidence, impact, uncertainty, and next-test cost, then stop with a shortlist.
- **Assess a design without a named direction:** scout briefly, then test the leading decision enough for a bounded comparative judgment; report other leads as uninvestigated.
- **Investigate a named decision:** go directly to its alternatives and discriminating evidence.
- **Explicitly comprehensive assessment:** compare multiple material decisions with bounded experiments, not exhaustive repository coverage.

If no candidate merits deeper testing, explain why. Use subagents only for independent, bounded questions when their benefit exceeds coordination cost; otherwise work sequentially. Never claim delegation that did not occur.

## Discover the governing decision

These overlapping lenses are search heuristics, **not** required stages or one-subagent-per-lens assignments. Brief scouting uses the index; **read a selected reference before substantial investigation**, not all five for coverage.

- **[Mathematical framing](references/mathematical-framing.md):** generic owners, canonical notions, alternative characterizations and natural duals.
- **[Abstraction and reuse](references/abstraction-reuse.md):** shared mathematical invariants; reuse, local/public helper, or no extraction.
- **[API expressivity](references/api-expressivity.md):** assumptions, retained information, inference and downstream use.
- **[Proof architecture](references/proof-architecture.md):** competing mathematical mechanisms rather than tactic length.
- **[Theory organization](references/theory-organization.md):** theorem ownership, dependencies, imports and placement.

Group leads by the **underlying design decision and test**, not by lens. Merge overlapping questions; investigate prerequisites first and use independent counterchecks only when useful.

## Experiment, compare, stop

1. Establish the intended mathematics, representative consumers, constraints, and decision. Expand scope only if it could reverse the judgment.
2. Compare credible alternatives, including the status quo. Search existing local/mathlib APIs before proposing new ones.
3. Prefer the smallest discriminating Lean/mathlib probe (`#check`, `#synth`, `#print`, minimal imports, scratch proof or boundary case). If composition matters, trace one representative path to closure or its lowest-level obstruction.
4. Probe a plausible *cost against* the attractive option: stronger assumptions, information loss, inference, dependency, consumer fit, or maintenance. Elaboration proves feasibility, not superiority; failed search does not prove impossibility.
5. Stop when evidence distinguishes options, a genuine tradeoff remains, or further tests are unlikely to change the decision. Do not manufacture novelty or expand into parallel implementation work.

## Output and authority

Return the deliverable requested: for a scout, ranked questions and next tests; for an assessment, a supported judgment on the leading decision with other leads and limits; for directed/comprehensive work, alternatives, actual experiment results, comparative costs, uncertainty, and the smallest justified recommendation (including no change).

Separate checked Lean facts from mathematical reasoning, judgment, and untested hypotheses. Report missing tools and verification limits explicitly. **Never edit production source or other durable repository artifacts under Challenge, even if implementation is requested.** Scratch experiments are permitted. For a recommended change, explain its design implications, material affected surfaces/invariants, and what would need verification; **do not promise an implementation plan, execution owner, cross-module workflow, or successful migration**. Execution is a separate task governed by its own authorization and capabilities.
