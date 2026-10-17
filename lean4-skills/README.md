# Lean 4 Skills

A jointly installed family of nine outcome-oriented capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Install all nine `lean4-*` Skills together. They are independently discoverable so the runtime can activate the narrow capability whose behavioral contract and references match the requested outcome; they are not intended to be deployed as unrelated standalone products.

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
- `lean4-mathlib-contribute` — assess or adapt an existing Lean artifact specifically for upstream mathlib contribution readiness.

## Routing

Choose a Skill by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, helper proofs, and local diagnostic work stay inside the selected Skill when they are merely means to that outcome.

Do not select another Skill just because the task uses behavior associated with it. Use more than one Skill only when the request itself contains multiple independently meaningful outcomes that no single Skill owns.

`lean4-explore` is not a generic preflight or fallback for every non-editing Lean question. Different proof strategies for a fixed concrete goal remain `lean4-prove` work. An ordinary proof hole remains `lean4-prove` work even when the source contains `sorry` or `admit`; use `lean4-trust` when the trust basis itself is the requested outcome.

Using mathlib as a library does not by itself select `lean4-mathlib-contribute`. That Skill is for an explicit upstream-contribution outcome on an existing artifact: determining or improving whether the artifact is suitable for submission to mathlib under current upstream expectations.

Each capability is directly discoverable from its own metadata. There is no family router or compatibility Skill.

## Knowledge placement

Keep knowledge at the lowest level where it materially improves execution or verification.

Runtime guidance is self-contained within each routable Skill. Verification rules are repeated locally only where they materially change that Skill's evidence or completion contract; the family does not require cross-Skill runtime references.

Specialized optimization knowledge stays with `lean4-optimize`:

- `lean4-optimize/references/proof-simplification.md` — simplify an already-correct proof strategy;
- `lean4-optimize/references/simplification.md` — `simp`, simp-lemma, and simproc design;
- `lean4-optimize/references/performance.md` — measured elaboration/build performance work.

There is no standalone shared mathlib-search document. Search behavior is small enough to keep local to the owning Skill: inspect local declarations and active imports, search by meaning/type rather than guessed names, and validate candidates in the actual project context.

Current upstream mathlib contribution policy is live external state owned by `lean4-mathlib-contribute`. That Skill should consult current authoritative contribution guidance and nearby current mathlib code at execution time instead of relying on a cached family document. The general Lean Skills should not independently acquire an upstream-contribution review bar merely because they use mathlib APIs.

Collection-level upstream provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
