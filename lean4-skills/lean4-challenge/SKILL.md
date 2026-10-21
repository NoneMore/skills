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

Question whether consequential mathematical design choices should be retained or revised. Unlike `lean4-review`, which assesses a specified artifact against relatively settled criteria, Challenge investigates open comparative decisions, including whether the framing itself is right. Formalization, proof, and optimization techniques are available as investigative tools, not implementation deliverables.

## Choose investigation depth

- **No direction specified:** scout a small, bounded set of distinct, plausible high-impact design questions. Parallelize independent scouting questions only when the expected benefit justifies coordination cost. Synthesize and rank directions by supporting evidence, potential impact, uncertainty, and cost of the next discriminating test. Return the shortlist and recommended first direction; do not silently turn reconnaissance into deep investigation.
- **Direction specified:** investigate that decision directly; skip broad scouting. Delegate independent checks or counterarguments only when useful.
- **Comprehensive depth explicitly requested:** investigate multiple consequential directions with bounded questions and experiments; parallelize independent deep investigations when beneficial, and synthesize overlapping and conflicting evidence. Comprehensive does not mean exhaustive repository-wide exploration.

Investigation scope and depth follow the user's intent; parallelism is an execution choice based on independent work, runtime support, and expected value versus cost. Use bounded sequential work when delegation is unavailable or not worthwhile; report material limits and do not claim parallel work that did not occur.

## Deep investigation

1. Establish the mathematical goal, intended users, constraints, artifact or proposal, and primary decision. Expand to adjacent decisions only if they could change that judgment.
2. Form credible alternatives where they could change the recommendation: framing/representation, hypotheses, proof mechanism, mathematical reuse, API information or ergonomics, theorem placement, or module dependencies. Follow the local construction toward its canonical mathematical owner where relevant.
3. Prefer the smallest **discriminating experiment** to verbal plausibility: targeted local/mathlib search, `#check`, `#synth`, `#print`, isolated scratch examples or proofs, minimal imports, concrete instances, and one representative downstream consumer in the actual Lean/mathlib environment. Follow one uncertain composition path to closure or its lowest-level obstruction.
4. Challenge promising alternatives too: test a countervailing cost that might reverse the decision, such as inference burden, complexity, information loss, downstream compatibility, or maintenance. Feasibility is not superiority; failed proof search is not impossibility.
5. Stop when the decision is stable, a genuine tradeoff remains, or more experiments are unlikely to change the judgment. Do not manufacture novelty or expand into parallel implementation cases merely to produce more findings.

## Boundaries and completion

Production sources and other durable repository artifacts remain unchanged under this Skill, even if implementation is requested. Scratch experiments may test hypotheses but are not production changes. Recommend concrete follow-up work for the appropriate execution Skill without automatically invoking it. Distinguish checked Lean facts, mathematical reasoning, qualitative judgments, and unresolved hypotheses; report missing tools or specification instead of claiming verification.

For reconnaissance, return a prioritized set of consequential questions, the evidence and uncertainty behind each, and the smallest next experiment. For deep investigation, return the principal design judgment, alternatives and actual experiment outcomes, comparative costs, unresolved tradeoffs, and the smallest justified next action (including retaining the current design). If implementation is recommended, hand off the chosen option, checked evidence and limits, statement/trust invariants, affected declarations or consumers, smallest proposed edit, and verification gate. Name an execution Skill only when its scope fits (e.g. `lean4-optimize` for verified-proof refactoring, `lean4-formalize` for declaration design); otherwise identify the ownership gap. Never delegate or authorize edits automatically. A successful Challenge requires neither novelty nor an edit.
