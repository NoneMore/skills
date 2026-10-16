# Lean 4 Skills

A Lean 4 capability family for formal mathematics in Lean 4 and mathlib. Eight outcome-oriented Skills are model-routable; `lean4-install` is a separate user-invoked installer for durable repository documentation.

Install the eight routable `lean4-*` capabilities together. They are not stages in a required workflow and are not intended to be unrelated standalone products. The installer is optional at runtime and must never be selected implicitly.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Routable capabilities

- `lean4-explore` — choose among multiple materially different Lean/mathlib formal directions when that choice is itself the requested outcome.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is the requested outcome.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — diagnose Lean/Lake failures in formal-mathematics work when the primary problem is a concrete diagnostic rather than ordinary proof search.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies when the trust basis itself is the requested outcome.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

## Explicit installer

`lean4-install` is user-invoked only. Its outcome is to materialize reusable Lean/mathlib guidance as ordinary documentation inside the target repository, following that repository's documentation conventions. It is not a router, support capability, runtime dependency, or prerequisite that other Skills call.

The installer carries a documentation bundle for:

- mathlib search and integration;
- verification gates and claim strength;
- simplification and simp-lemma design;
- measured Lean performance work;
- additional guidance for upstream mathlib contributions.

It prefers an existing repository documentation location. If the repository has no applicable convention, it defaults to `docs/lean/`. Once installed, these files are project knowledge: the routable Skills may follow them when present, just as they follow any other applicable repository documentation.

A repository does not need the installer to invoke the eight behavioral Skills. If the shared documentation is absent, each Skill still owns its core behavioral contract and must not pretend that project guidance exists.

## Routing and composition

Choose the primary routable capability by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, and explanatory substeps normally remain inside the capability that already owns the task.

`lean4-explore` is not a generic preflight or fallback for every non-editing Lean question. Different proof strategies for a fixed concrete goal remain `lean4-prove` work. An ordinary proof hole remains `lean4-prove` work even when the source contains `sorry` or `admit`; use `lean4-trust` when the trust basis itself is the requested outcome.

When capabilities compose, the primary outcome owner keeps the governing mutation, trust, scope, and verification contract. A supporting capability cannot broaden it.

`lean4-install` does not participate in this composition model. Installing or updating repository documentation is a separate explicit user outcome.

## Knowledge placement

Generic reusable Lean knowledge is not committed as shared runtime references beside the routable Skills and is not vendored into them. The source templates live under `lean4-install/assets/docs/` because their purpose is to become durable project documentation when the user asks for installation.

Only genuinely Skill-specific reference material stays with a routable Skill, such as `lean4-explore/references/exploration-playbook.md` and `lean4-optimize/references/proof-simplification.md`.

Collection-level upstream provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
