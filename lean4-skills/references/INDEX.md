# Reference Map

`SKILL.md` owns shared behavior. Workflow files own task-specific behavior. The references below are loaded only when their knowledge changes the current task.

## Workflows

- `workflows/prove.md` — proof holes and proof failures
- `workflows/formalize.md` — statement design and informal-to-Lean formalization
- `workflows/disprove.md` — certified refutation and counterexample search
- `workflows/review.md` — read-only code review
- `workflows/optimize.md` — proof strategy, golfing, and performance improvement
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
- `proof-golfing.md` — local simplification of already-correct proofs
- `performance-optimization.md` — elaboration/performance diagnosis and targeted remedies
- `profiling-workflows.md` — Lean profiling facilities
- `simp-reference.md` — simp normal forms, simp-lemma hygiene, and simprocs

## Mathlib-focused knowledge

- `mathlib-review-taxonomy.md` — review vocabulary for upstream-oriented work
- `verso-docs.md` — Verso roles in Lean documentation

## Advanced Lean programming

- `lean4-custom-syntax.md` — notation, macros, elaborators, and DSL syntax
- `compiler-internals.md` — compiler attributes and pipeline diagnostics
- `ffi-interop.md` — Lean/C/C++ FFI boundaries
- `json-patterns.md` — Lean JSON construction and elaboration
- `linter-authoring.md` — project-specific Lean linters

Do not treat this index as a preload list. Start from the current task and load the smallest relevant reference.
