---
name: lean4-recon
description: "Use for open-ended formal-mathematics investigation in Lean 4/mathlib when the requested outcome is to challenge or improve the current problem framing before committing to a durable implementation. Deliberately widen semantic and repository context to discover whether a local definition, theorem, hypothesis set, or API is better understood through an existing generic abstraction, canonical construction, broader theorem, dual formulation, historical design, or dependency strategy. No alternative direction needs to be known in advance. Search needed only to finish an already-settled declaration, proof, review, optimization, or upstream-readiness task stays with that owning Skill."
license: MIT
---

# Lean 4 Recon

## Purpose

Deliberately widen the semantic and repository context around a Lean/mathlib problem before committing to a durable design. Test whether the apparent local formulation is actually an instance of a more canonical abstraction, existing API, broader theorem, fixed-point or universal construction, dual formulation, weaker hypothesis boundary, or previously explored design.

Recon may begin with no known alternative. Discovering whether a materially better framing exists is part of the task.

## Context-loading mode

This Skill uses a deliberately divergent context policy. Outcome-completion Skills should normally read and search only as far as needed to deliver their already-owned artifact. Recon instead tests whether that local framing is itself the wrong boundary.

Do not stop expanding context merely because the local theorem, definition, or implementation could already be completed. Expand across a semantic boundary only while the next boundary has a credible chance of changing the abstraction, statement, assumptions, API placement, dependency strategy, or downstream design.

Useful expansion directions include:

- **Follow the implementation downward:** inspect the definitions and operators that actually drive the local construction.
- **Find the owning abstraction upward:** trace those definitions to their generic namespace, structure, or theorem family and inspect the API there rather than searching only with application-domain vocabulary.
- **Look for canonical characterizations:** ask whether a new object is already a fixed point, least/greatest solution, closure/interior/hull/kernel, range or membership condition, `iInf`/`iSup`, or another existing universal construction.
- **Check symmetry and duality:** inspect natural dual, converse, complement, opposite, additive/multiplicative, least/greatest, or left/right counterparts when they could change the right API.
- **Pressure-test assumptions:** use cheap examples, standard counterexamples, finite cases, or scratch Lean declarations to test whether nontrivial hypotheses are genuinely needed.
- **Revisit history when constraints changed:** inspect earlier implementations, abandoned branches, PR discussion, or review feedback only when they can explain a live constraint or reveal that a previously rejected design has become viable.
- **Look forward to leverage:** ask whether a small generic theorem or lower-level API would eliminate repeated local machinery or substantially simplify downstream work.

Load [the recon playbook](references/recon-playbook.md) when a task benefits from a more explicit semantic-expansion procedure.

## Invariants

- Production source is observational by default. Disposable `example`s, `#check`, `#synth`, minimal test files, or temporary local edits are allowed when they materially test a possible reframe, but do not silently promote experiments into production changes.
- Search by mathematical meaning, type shape, implementation structure, and owning namespace before relying on guessed declaration names. Inspect local declarations and active imports before widening outward, then validate material candidate APIs in the actual project context.
- Before adding a new predicate, wrapper, or helper theorem, try to express it using the canonical structure already governing the construction. A local concept may be ordinary fixed-point membership, an existing order construction, or a specialization of a generic theorem.
- Prefer Lean/project evidence over verbal plausibility when an inexpensive experiment can distinguish a material framing question.
- Distinguish verified facts, working hypotheses, and material unresolved alternatives. Do not preserve branch history that no longer affects the decision.
- Do not force a reframe merely to justify Recon. A bounded investigation that finds no material reason to change the current framing is a valid outcome.

## Reviewer questions

Use these as prompts for judgment, not an exhaustive checklist:

1. What generic construction actually drives this local definition or proof?
2. Is a new predicate, wrapper, or helper merely a restatement of an existing canonical notion?
3. Does the essential argument use less structure than the local statement, so that the useful theorem belongs in a more general API?
4. Is the new object equal or equivalent to an existing canonical construction or universal characterization?
5. Are the nontrivial hypotheses necessary, and what cheap example or counterexample would test the boundary?
6. Is there a natural dual or symmetric result whose existence changes the API design?

## Workflow

1. State the local framing, current constraints, and what kind of design commitment would follow if the framing were accepted unchanged.
2. Inspect the local declaration neighborhood and the definitions/operators that implement the construction.
3. Cross the smallest promising semantic boundary: owning generic namespace, canonical characterization, dual API, assumption boundary, relevant history, or downstream reuse.
4. Use cheap discriminators first: `#check`, `#synth`, `#print`, scratch `example`s, minimal imports, concrete instances, or focused repository search.
5. If a materially better framing appears, test enough of it to establish that the difference is real rather than merely aesthetically plausible.
6. Converge when further expansion is unlikely to change the design decision, when a better framing is supported well enough to hand off, or when the bounded investigation supports retaining the current framing.

For claims based on actual elaboration, report the check that ran and the scope it establishes. Scratch or file-local success answers only the local question it exercised; if the design comparison materially depends on changed imports or project integration, use a gate that exercises that boundary.

## Boundaries

Recon owns deliberate context expansion whose requested purpose is to test or improve the current framing. It does not own ordinary theorem lookup, API search, proof-strategy comparison, local diagnostics, or small experiments when those are merely bounded means to an already-settled formalization, proof, refutation, review, optimization, or upstream-readiness outcome.

When Recon converges on a concrete declaration, proof, refutation, repair, optimization, trust cleanup, review, or upstream contribution task, stop expanding context and let that outcome's contract govern durable work unless the user explicitly asked to carry both outcomes through.

## Completion

Return, in proportion to the task:

- any material discovery that changed the problem framing, especially an existing abstraction, canonical characterization, broader theorem, duality, assumption boundary, or historical constraint;
- the best-supported direction when the evidence favors one, or the small set of remaining options when a real tradeoff remains;
- the evidence that materially supports the reframe or supports keeping the current framing;
- unresolved uncertainty only when it could still change the design decision;
- the next concrete outcome once reconnaissance has converged enough to proceed.

A result that finds no material reframe is complete when the most plausible semantic expansion paths were checked proportionately and further widening is unlikely to change the decision.