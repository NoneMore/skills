# Reference Map

`SKILL.md` owns shared behavior. Workflow files own task-specific behavior. The references below are loaded only when their knowledge changes the current formalization task.

## Workflows

- `workflows/prove.md` — proof holes and proof failures
- `workflows/formalize.md` — statement design and informal-to-Lean formalization
- `workflows/disprove.md` — certified refutation and counterexample search
- `workflows/review.md` — read-only code review
- `workflows/optimize.md` — proof strategy, local simplification, and performance improvement
- `workflows/learn.md` — teaching and exploration

Treat one workflow as the current owner. A workflow may explicitly hand off when responsibility changes.

## Verification and project policy

- `verification.md` — live, file-local, dependency-aware, and project integration gates
- `branches/mathlib-upstream.md` — authoritative current mathlib contribution policy and upstream-only expectations

## Search, diagnostics, and trust

- `mathlib-guide.md` — finding and validating existing declarations before reproving them
- `compilation-errors.md` — diagnostic triage by failure class
- `axiom-elimination.md` — trust-basis inspection and removal of unwanted assumptions

## Proof quality and performance

- `proof-simplification.md` — strategy-level simplification and library leverage
- `performance-optimization.md` — elaboration/performance diagnosis, profiling, and targeted remedies
- `simp-reference.md` — simp normal forms, simp-lemma hygiene, and simprocs

## Mathlib-focused knowledge

- `mathlib-review-taxonomy.md` — review vocabulary for upstream-oriented work

Do not treat this index as a preload list. Start from the current task and load the smallest relevant reference.
