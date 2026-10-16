---
name: lean4-explore
description: "Use for formal mathematics in Lean 4/mathlib when multiple materially different formal-design directions remain plausible and choosing among them is itself the requested outcome. The uncertainty may concern the formal object, abstraction, API family, mathematical hypothesis boundary, generalization, dual formulation, or dependency strategy. Explore local project and mathlib evidence and use disposable Lean experiments when they discriminate between directions. Do not use for plain explanation, ordinary theorem lookup, or multiple proof strategies for a fixed concrete goal inside an already-owned task, or when the requested outcome is already a concrete proof completion, statement formalization, certified refutation, diagnostic repair, trust audit, code review, or optimization."
license: MIT
---

# Lean 4 Explore

## Purpose

Reduce uncertainty when multiple materially different formal-design directions remain plausible before committing to a durable Lean outcome. Compare only branches whose differences could change the chosen formal object, abstraction, API, assumptions, generality, symmetry, or dependency strategy.

## Invariants

- Production source is observational by default. Disposable scratch declarations, `example`s, `#check`, `#synth`, minimal test files, or temporary local edits are allowed when they materially test a branch, but do not silently turn exploratory candidates into durable project changes.
- When exploration supports another capability that owns the requested outcome, preserve that owner's stricter mutation, trust, scope, and verification invariants. Exploratory permission never broadens the primary owner's contract.
- Distinguish verified facts, working hypotheses, and material rejected or deferred branches. Do not preserve branch history that does not affect the decision.
- Search by mathematical meaning, type shape, structure, and neighborhood before guessing declaration names. Inspect local declarations and active imports before widening outward, and validate candidate declarations in the actual project context.
- Prefer Lean/project evidence over verbal plausibility when an inexpensive experiment can discriminate between branches.
- Diverge only while a branch is likely to reveal materially new information; prune branches once evidence makes them dominated, irrelevant, or outside scope.

For work aimed at upstream mathlib, consult current authoritative contribution policy and nearby current mathlib code in addition to this Skill.

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

1. State the exploration question, current constraints, and the decision or uncertainty the investigation should resolve.
2. Inspect the local declaration neighborhood and active imports before widening outward.
3. Generate a small number of materially different branches across the relevant directions above.
4. Test cheap discriminators first. Use disposable Lean experiments rather than argument-by-guess when possible.
5. Compare surviving branches by evidence, canonicality, generality, downstream leverage, implementation cost, and risk.
6. Converge when one direction is sufficiently supported, when several genuinely viable options remain with an explicit tradeoff, or when choosing among formal directions is no longer the primary uncertainty.

For claims that depend on actual elaboration, changed imports, or project integration, load [verification guidance](../references/verification.md) and use the lightest gate that establishes the claim. Exploration does not upgrade a scratch success into a project-level verification claim.

## Handoff

Stop exploring when choosing among formal directions is no longer the primary uncertainty. Carry the selected direction and material evidence into the capability that owns the next requested outcome. Common handoffs are `lean4-formalize` for a durable declaration, `lean4-prove` for a settled target that needs a proof, and `lean4-refute` for requested certified falsity.

## Completion

Return, in proportion to the task:

- the best-supported direction or the small set of remaining viable directions;
- the evidence that materially discriminates between them;
- rejected alternatives only when their rejection explains the choice, prevents repeated work, or preserves a material tradeoff;
- unresolved uncertainty only when it could still change the decision;
- the next concrete outcome or action once the investigation has converged enough to hand off.

Stop when further branching is unlikely to change the decision, or when the user-requested uncertainty has been reduced enough for the next bounded outcome.
