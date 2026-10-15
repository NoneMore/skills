# Reference Map

`SKILL.md` owns shared behavior. Workflow files own task-specific behavior. The references below are loaded only when their knowledge changes the current formalization task.

## Workflows

- `references/prove.md` — proof holes and proof failures
- `references/formalize.md` — statement design and informal-to-Lean formalization
- `references/disprove.md` — certified refutation and counterexample search
- `references/repair.md` — non-proof diagnostics and explicit trust-basis repair
- `references/review.md` — read-only code review
- `references/optimize.md` — proof strategy, local simplification, and performance improvement
- `references/learn.md` — teaching and exploration

Treat one workflow as the current owner. A workflow may explicitly hand off when responsibility changes.

## Verification and project policy

- `references/verification.md` — live, file-local, dependency-aware, and project integration gates
- `references/branches/mathlib-upstream.md` — authoritative current mathlib contribution policy and upstream-only expectations

## Search, diagnostics, and trust

- `references/mathlib-guide.md` — finding and validating existing declarations before reproving them
- `references/compilation-errors.md` — diagnostic triage by failure class
- `references/axiom-elimination.md` — trust-basis inspection and removal of unwanted assumptions

## Proof quality and performance

- `references/proof-simplification.md` — strategy-level simplification and library leverage
- `references/performance-optimization.md` — elaboration/performance diagnosis, profiling, and targeted remedies
- `references/simp-reference.md` — simp normal forms, simp-lemma hygiene, and simprocs

## Mathlib-focused knowledge

- `references/mathlib-review-taxonomy.md` — review vocabulary for upstream-oriented work

Do not treat this index as a preload list. Start from the current task and load the smallest relevant reference.
