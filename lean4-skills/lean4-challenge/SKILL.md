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

Choose the **investigation direction** (specified or to be discovered) and **requested deliverable** (shortlist, bounded judgment, or comprehensive comparison) separately. An unspecified direction does not by itself imply a scout-only request.

- **Direction-finding requested:** scout a small, bounded set of distinct, plausible high-impact design questions. Rank them by evidence, potential impact, uncertainty, and cost of the next discriminating test; return the shortlist and recommended first direction without silently starting deep investigation.
- **Design assessment requested, no direction specified:** scout a bounded set of plausible consequential questions, rank them, then investigate the highest-value one only as deeply as needed for a defensible provisional judgment. Report remaining leads and uncertainty rather than exploring every direction or returning only a shortlist.
- **Direction specified:** investigate that decision directly; skip broad scouting. Delegate independent checks or counterarguments only when useful.
- **Comprehensive comparison explicitly requested:** investigate multiple consequential directions with bounded questions and experiments, and synthesize overlapping or conflicting evidence. Comprehensive does not mean exhaustive repository-wide exploration.

When intent is implicit, "find promising questions" calls for a shortlist; "assess/evaluate this design" calls for a bounded judgment. If no direction warrants deep testing, say why and retain the current design where supported. Parallelize independent work only when its expected benefit exceeds coordination cost. Use bounded sequential work if delegation is unavailable or not worthwhile; report material limits and never claim parallel work that did not occur.

## Explore consequential directions

Use the following **overlapping lenses** to discover design questions; they are search heuristics, not a checklist, mandatory coverage areas, or one subagent assignment per lens. For open requests, briefly scan plausible lenses and deepen only decision-changing leads. For named decisions, follow the relevant lens directly. Load a reference **when its investigative method is relevant**; do not load all five merely to establish coverage.

- **[Mathematical framing and representation](references/mathematical-framing.md):** trace local objects to generic mathematical owners, canonical notions, equivalent characterizations, and natural duals.
- **[Mathematical abstraction and reuse](references/abstraction-reuse.md):** compare shared invariants, assumptions, constructions, and conclusions; weigh existing results, local/public helpers, or no extraction.
- **[API expressivity and information](references/api-expressivity.md):** test whether interfaces preserve distinctions downstream theorems need, and weigh hypotheses, inference, and consumer costs.
- **[Proof architecture](references/proof-architecture.md):** compare mathematical proof mechanisms, not merely tactic length; probe conceptual directness and robustness.
- **[Theory organization and theorem placement](references/theory-organization.md):** follow generic ownership, representative import/dependency paths, and placement or migration tradeoffs.

Group candidate leads by the **underlying design decision and discriminating evidence**, not their lens labels. Multiple lenses may describe one issue. Before parallel delegation, give each subagent a bounded question and evidence target; merge substantially overlapping investigations, and sequence dependent questions. Parallel counterchecks of the same decision are valid when intentionally independent and worth the cost. The coordinator synthesizes cross-cutting findings; subagents need not explore every lens.

## Deep investigation

1. Establish the mathematical goal, intended users, constraints, artifact or proposal, and primary decision. Expand to adjacent decisions only if they could change that judgment.
2. Form credible alternatives through the relevant exploration lenses, following their search paths and discriminating probes where they could change the recommendation. Look past the most visible local symptom, but do not treat the lens list as required coverage or independent workstreams.
3. Prefer the smallest **discriminating experiment** to verbal plausibility: targeted local/mathlib search, `#check`, `#synth`, `#print`, isolated scratch examples or proofs, minimal imports, concrete instances, and one representative downstream consumer in the actual Lean/mathlib environment. Follow one uncertain composition path to closure or its lowest-level obstruction.
4. Challenge promising alternatives too: test a countervailing cost that might reverse the decision, such as inference burden, complexity, information loss, downstream compatibility, or maintenance. Feasibility is not superiority; failed proof search is not impossibility.
5. Stop when the decision is stable, a genuine tradeoff remains, or more experiments are unlikely to change the judgment. Do not manufacture novelty or expand into parallel implementation cases merely to produce more findings.

## Boundaries and completion

Production sources and other durable repository artifacts remain unchanged under this Skill, even if implementation is requested. Scratch experiments may test hypotheses but are not production changes. Recommend concrete follow-up work for the appropriate execution Skill without automatically invoking it. Distinguish checked Lean facts, mathematical reasoning, qualitative judgments, and unresolved hypotheses; report missing tools or specification instead of claiming verification.

For direction-finding only, return prioritized questions, their evidence and uncertainty, and the smallest next experiment. For a bounded design assessment, return a judgment on the leading decision supported by representative evidence, explicitly naming uninvestigated directions and limits. For directed or comprehensive investigation, return the design judgment(s), alternatives, actual experiment outcomes, comparative costs, unresolved tradeoffs, and the smallest justified next action (including retaining the current design).

If implementation is recommended, provide an actionable handoff: chosen option, checked evidence and limits, statement/trust invariants, affected declarations, consumers and import boundaries, smallest proposed edit or ordered edit stages, and verification gate. Name an execution Skill only where its scope fits (e.g. `lean4-optimize` for verified-proof refactoring, `lean4-formalize` for individual declaration design). When no single Skill owns a cross-module change, identify that gap and describe the bounded, explicitly authorized multi-step implementation path instead of inventing a Skill or declaring implementation impossible. If asked to implement within Challenge, state that execution must occur outside this advisory Skill; never edit, delegate, or grant execution authority automatically. A successful Challenge requires neither novelty nor an edit.
