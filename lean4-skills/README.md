# Lean 4 Skills

A jointly installed family of eight outcome-oriented capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Install all eight `lean4-*` Skills together. They are independently discoverable so the runtime can activate the narrow capability whose behavioral contract and references match the requested outcome; they are not intended to be deployed as unrelated standalone products.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `lean4-explore` — choose among multiple materially different Lean/mathlib formal directions when that choice is itself the requested outcome.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is the requested outcome.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — diagnose Lean/Lake failures in formal-mathematics work when the primary problem is a concrete diagnostic rather than ordinary proof search.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies when the trust basis itself is the requested outcome.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

## Routing and composition

Choose the primary capability by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, and explanatory substeps normally remain inside the capability that already owns the task.

`lean4-explore` is not a generic preflight or fallback for every non-editing Lean question. Different proof strategies for a fixed concrete goal remain `lean4-prove` work. An ordinary proof hole remains `lean4-prove` work even when the source contains `sorry` or `admit`; use `lean4-trust` when the trust basis itself is the requested outcome.

When capabilities compose, the primary outcome owner keeps the governing mutation, trust, scope, and verification contract. A supporting capability may gather evidence or resolve a bounded subproblem, but it must not broaden that contract.

Each capability is directly discoverable from its own metadata. There is no family router or compatibility Skill. Cross-skill composition happens only when the requested outcome genuinely crosses a boundary.

## Knowledge placement

Keep knowledge at the lowest level where it materially improves execution or verification.

The family has one shared runtime reference: [verification guidance](references/verification.md). It captures Lean/Lake verification semantics that are easy to get materially wrong, including the difference between file-local and dependency-aware checks after changed imports.

Load shared references on demand rather than preloading them for every Skill. In a composed task, the primary outcome owner owns shared-reference loading; supporting capabilities reuse guidance already established for the active task instead of reloading duplicate copies.

Specialized optimization knowledge stays with `lean4-optimize`:

- `lean4-optimize/references/proof-simplification.md` — simplify an already-correct proof strategy;
- `lean4-optimize/references/simplification.md` — `simp`, simp-lemma, and simproc design;
- `lean4-optimize/references/performance.md` — measured elaboration/build performance work.

There is no standalone shared mathlib-search document. Search behavior is small enough to keep local to the owning Skill: inspect local declarations and active imports, search by meaning/type rather than guessed names, and validate candidates in the actual project context.

Current upstream mathlib policy is live external state. For upstream-targeted work, consult the current authoritative contribution guidance and nearby current mathlib code instead of relying on a cached family document.

Installations of this family should preserve the collection layout so relative references remain available. If a target runtime requires physically self-contained Skill packages, materialize reference copies as generated distribution artifacts rather than committing mirrors back into the authoring tree.

Collection-level upstream provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
