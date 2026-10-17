# Lean 4 Skills

A jointly installed family of nine capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Install all nine `lean4-*` Skills together. Seven are model-discoverable and intentionally allow compatible overlap; two are user-invoked modes for work whose broader scope should be an explicit choice. There is no family router or requirement that discovery select exactly one Skill.

The split is motivated by observed agent behavior: task-specific branch references under a broad Skill were not loaded reliably enough in practice, and routing distinctions encoded only after activation did not consistently affect discovery. The model-discoverable Skills therefore favor reliable loading of useful task guidance over mutually exclusive classification. Reading an additional compatible Skill is acceptable when its contract does not conflict with the requested work.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Model-discoverable capabilities

- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration, including choices of canonical types, hypotheses, and generality.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — identify the root cause and migration path for Lean/Lake/module/dependency/toolchain/build/integration failures.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

Discovery is recall-oriented. A task may load more than one compatible capability when their descriptions match; evaluation should care that materially useful guidance is available and that no conflicting behavior results, not that one unique owner wins classification.

## User-invoked capabilities

- `lean4-recon` — deliberately widen Lean/mathlib semantic and repository context to challenge the current framing before committing to implementation. This is an explicit request to spend context divergently rather than merely complete the local artifact.
- `lean4-mathlib-contribute` — assess or adapt an existing Lean artifact specifically for upstream mathlib contribution readiness using current upstream policy and nearby current mathlib code.

These Skills set `disable-model-invocation: true`. Their broader search/review bars should not be inferred from ordinary Lean work: the user chooses when to invoke them.

`lean4-recon` addresses an observed failure mode where a locally convergent task-completion strategy can finish a Lean artifact without crossing the semantic boundary needed to discover a more canonical mathlib abstraction. Explicit invocation authorizes a different context-loading policy: follow implementations into owning abstractions, inspect canonical characterizations and dualities, pressure-test hypotheses, and revisit relevant history when it can change the design decision.

`lean4-mathlib-contribute` is user-invoked because upstream readiness is a distinct review/adaptation bar with live external policy and can justify API-shape changes that ordinary library use should not silently impose.

## Knowledge placement

Keep knowledge at the lowest level where it materially improves execution or verification.

Runtime guidance is self-contained within each Skill where locality materially improves reliability. Repeated rules should earn their cost by changing that Skill's behavior or completion claim; compatible Skills do not need pairwise exclusion doctrine merely to keep discovery mutually exclusive.

Specialized optimization knowledge stays with `lean4-optimize`:

- `lean4-optimize/references/proof-simplification.md` — simplify an already-correct proof strategy;
- `lean4-optimize/references/simplification.md` — `simp`, simp-lemma, and simproc design;
- `lean4-optimize/references/performance.md` — measured elaboration/build performance work.

There is no standalone shared mathlib-search document. Search behavior is small enough to keep local to Skills that use it: inspect local declarations and active imports, search by meaning/type rather than guessed names, and validate candidates in the actual project context.

Current upstream mathlib contribution policy is live external state owned by the user-invoked `lean4-mathlib-contribute` Skill. It consults current authoritative contribution guidance and nearby current mathlib code at execution time instead of relying on a cached family document.

Collection-level upstream provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
