---
name: lean4-explore
description: "Use for formal mathematics in Lean 4/mathlib when the main uncertainty is what formal object, abstraction, existing API, theorem, assumption boundary, generalization, dual formulation, or implementation approach should be pursued. Explore the local project and mathlib, run disposable Lean experiments, compare plausible branches, and return evidence-backed directions. Do not use when the requested outcome is already a concrete proof completion, statement formalization, certified refutation, diagnostic repair, trust audit, code review, or optimization."
license: MIT
---

# Lean 4 Explore

## Purpose

Reduce uncertainty about the right formal direction before committing to a durable Lean change. Build and prune a small evidence-backed search tree rather than stopping at the first plausible theorem name or implementation.

Use this skill when the question is primarily **what should we pursue?**, not merely **how do we execute an already-known Lean task?**

## Invariants

- Production source is observational by default. Disposable scratch declarations, `example`s, `#check`, `#synth`, minimal test files, or temporary local edits are allowed when they materially test a branch, but do not silently turn exploratory candidates into durable project changes.
- Distinguish verified facts, working hypotheses, rejected branches, and deferred follow-ups.
- Search by mathematical meaning, type shape, structure, and neighborhood before guessing declaration names. Use [mathlib search and integration](references/mathlib-guide.md) when useful.
- Prefer Lean/project evidence over verbal plausibility when an inexpensive experiment can discriminate between branches.
- Diverge only while a branch is likely to reveal materially new information; prune branches once evidence makes them dominated, irrelevant, or outside scope.

For work aimed at upstream mathlib, load [upstream guidance](references/branches/mathlib-upstream.md) as an additional constraint on canonical API and contribution boundaries.

## Exploration directions

Start from the concrete question and expand only along useful dimensions:

- **Downward to examples:** test small instances, edge cases, counterexamples, explicit witnesses, and scratch declarations to pressure-test assumptions and conjectures.
- **Sideways through the library:** inspect nearby declarations, equivalent formulations, alternative representations, namespaces, imports, and canonical APIs.
- **Upward in abstraction:** ask whether a local theorem or predicate is really an instance of a more general order, lattice, fixed-point, algebraic, topological, or other structural fact.
- **Across symmetry:** look for dual, converse, complement, opposite, additive/multiplicative, or otherwise paired formulations whose existence changes the right API.
- **Backward through history:** inspect earlier implementations or abandoned approaches when they explain a constraint; reconsider them if the constraint has changed.
- **Forward to leverage:** ask whether a small general-purpose lemma or upstream API would remove repeated local machinery and simplify downstream work.

Load [the exploration playbook](references/exploration-playbook.md) when the task benefits from a more explicit branch-and-prune procedure.

## Workflow

1. State the exploration question, current constraints, and what decision or uncertainty the investigation should resolve.
2. Inspect the local declaration neighborhood and active imports before widening outward.
3. Generate a small number of materially different branches across the relevant directions above.
4. Test cheap discriminators first. Use disposable Lean experiments rather than argument-by-guess when possible.
5. Compare surviving branches by evidence, canonicality, generality, downstream leverage, implementation cost, and risk.
6. Converge when one direction is sufficiently supported, when several genuinely viable options remain with an explicit tradeoff, or when the next uncertainty belongs to a more outcome-specific skill.

Use [verification guidance](references/verification.md) for claims that depend on actual elaboration, imports, or project integration. Exploration does not upgrade a scratch success into a project-level verification claim.

## Handoffs

- Use `lean4-formalize` when the exploration has selected the mathematical encoding and the requested next outcome is a durable Lean declaration.
- Use `lean4-prove` when a concrete declaration/goal and proof obligation are settled.
- Use `lean4-refute` when the requested outcome becomes a Lean-certified counterexample or negation; exploratory counterexample probing alone does not require that skill.
- Use `lean4-diagnose` when a concrete Lean/Lake diagnostic becomes the primary blocker.
- Use `lean4-trust`, `lean4-review`, or `lean4-optimize` when the requested outcome becomes respectively a trust audit, independent evaluation, or durable improvement of already-correct code.

Ordinary theorem lookup needed to finish a known proof remains part of `lean4-prove`; do not invoke exploration merely because search is useful.

## Completion

Return:

- the best-supported direction or the small set of remaining viable directions;
- the evidence that discriminates between them;
- important branches rejected and why;
- unresolved uncertainties and non-blocking follow-ups;
- the next skill or concrete action if the investigation has converged enough to hand off.

Stop when further branching is unlikely to change the decision, or when the user-requested uncertainty has been reduced enough for the next bounded outcome.
