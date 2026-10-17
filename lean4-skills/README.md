# Lean 4 Skills

A jointly installed family of nine outcome-oriented capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Install all nine `lean4-*` Skills together. They are independently discoverable so the runtime can activate the narrow capability whose behavioral contract and references match the requested outcome; they are not intended to be deployed as unrelated standalone products.

The split is motivated by observed agent behavior: task-specific branch references under a broad Skill were not loaded reliably enough in practice, and routing distinctions encoded only after activation did not consistently affect discovery. Independent Skills move behaviorally distinct context-loading policies into discovery metadata while keeping specialized context out of unrelated tasks.

`lean4-recon` also addresses a separate observed failure mode: a convergent task-completion strategy can successfully finish a local Lean artifact while never crossing the semantic boundary needed to discover a more canonical mathlib abstraction. Recon therefore deliberately spends context differently from artifact-completion Skills: it widens the semantic neighborhood to test the framing before committing to implementation.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `lean4-recon` — deliberately widen Lean/mathlib semantic and repository context to test whether the current local framing misses a more canonical abstraction, construction, general theorem, duality, assumption boundary, or design direction before committing to implementation.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is the requested outcome.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal, including local elaboration diagnostics encountered while repairing it.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — identify the root cause and migration path for Lean/Lake/module/dependency/integration failures that are not naturally owned by one declaration or proof task, or when diagnosis itself is the requested outcome.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies when the trust basis itself is the requested outcome.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.
- `lean4-mathlib-contribute` — assess or adapt an existing Lean artifact specifically for upstream mathlib contribution readiness.

## Routing

Choose a Skill by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, helper proofs, and local diagnostic work stay inside the selected Skill when they are merely bounded means to that outcome.

`lean4-recon` is different because deliberate context expansion is itself the requested work. Use it when the task asks whether the current framing should be challenged before implementation: follow local definitions into their owning abstractions, inspect canonical characterizations and nearby generic APIs, pressure-test hypotheses, or reopen a design boundary that ordinary task-completion search would have no reason to cross. No alternative direction needs to be known in advance. Do not select Recon merely because an already-owned formalization, proof, review, optimization, refutation, or upstream-readiness task needs ordinary search or proof-strategy comparison.

Artifact-owned failures stay with the artifact owner: diagnostics encountered while formalizing a declaration, repairing a fixed proof, certifying a refutation, reviewing code, optimizing a proof, or adapting an upstream contribution remain internal to that Skill. Use `lean4-diagnose` when root-cause investigation is itself requested or when the failure spans a module, dependency, toolchain, build, or integration boundary rather than one owned artifact.

Use more than one Skill only when the request itself contains multiple independently meaningful outcomes that no single Skill owns.

An ordinary proof hole remains `lean4-prove` work even when the source contains `sorry` or `admit`; use `lean4-trust` when the trust basis itself is the requested outcome.

Using mathlib as a library does not by itself select `lean4-mathlib-contribute`. That Skill is for an explicit upstream-contribution outcome on an existing artifact: determining or improving whether the artifact is suitable for submission to mathlib under current upstream expectations.

Each capability is directly discoverable from its own metadata. There is no family router or compatibility Skill.

## Knowledge placement

Keep knowledge at the lowest level where it materially improves execution or verification.

Runtime guidance is self-contained within each routable Skill. Verification rules are repeated locally only where they materially change that Skill's evidence or completion contract; the family does not require cross-Skill runtime references.

Self-contained placement is intentional because the split exists partly to make specialized context reliably available at activation time. That is not a reason to duplicate doctrine that does not materially change a Skill's behavior or completion claim.

Specialized optimization knowledge stays with `lean4-optimize`:

- `lean4-optimize/references/proof-simplification.md` — simplify an already-correct proof strategy;
- `lean4-optimize/references/simplification.md` — `simp`, simp-lemma, and simproc design;
- `lean4-optimize/references/performance.md` — measured elaboration/build performance work.

There is no standalone shared mathlib-search document. Search behavior is small enough to keep local to Skills that use it: inspect local declarations and active imports, search by meaning/type rather than guessed names, and validate candidates in the actual project context. Recon adds a different policy only when the requested outcome is to widen context beyond what completion of a settled artifact would require.

Current upstream mathlib contribution policy is live external state owned by `lean4-mathlib-contribute`. That Skill should consult current authoritative contribution guidance and nearby current mathlib code at execution time instead of relying on a cached family document. The general Lean Skills should not independently acquire an upstream-contribution review bar merely because they use mathlib APIs.

Collection-level upstream provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
