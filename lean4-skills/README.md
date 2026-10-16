# Lean 4 Skills

Independent, outcome-oriented capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `lean4-explore` — investigate an open Lean/mathlib design or research question when choosing among plausible abstractions, APIs, mathematical hypotheses, generalizations, or approaches is itself the requested outcome.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is the requested outcome.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — diagnose Lean/Lake failures in formal-mathematics work when the primary problem is a concrete diagnostic rather than ordinary proof search.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

## Routing and composition

Choose the primary capability by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, and explanatory substeps normally remain inside the capability that already owns the task.

`lean4-explore` is not a generic preflight or fallback for every non-editing Lean question. Compose it only when choosing among multiple plausible formal directions becomes a distinct requested outcome. A standalone explanation of existing code with no evaluation request and no open formal-design decision does not require a specialized Lean 4 Skill.

When a real outcome boundary is crossed, hand off explicitly: exploration may settle an encoding for formalization, diagnosis may reduce to ordinary proof search, review may identify a change owned by proof/trust/optimization, and exploration may support an optimization decision without owning the durable edit.

Each capability is directly discoverable from its own metadata. There is no family router or compatibility Skill. Cross-skill composition happens only when the requested outcome genuinely crosses a boundary.

## Packaging

Every `lean4-*` directory is a complete Skill package and must remain valid when copied or installed without the rest of this collection. In particular:

- the directory name matches the `name` in `SKILL.md`;
- runtime references stay inside the package;
- required provenance and third-party notices stay inside the package;
- no Skill depends on `../references`, sibling Skills, or the collection root at runtime.

The root `references/` directory is the canonical source for reusable material shared by multiple packages. `scripts/sync-packages.py` vendors the required subset into each Skill; run `scripts/sync-packages.py --check` to detect drift and validate package names. Skill-specific references remain owned by that Skill.

## Shared source material

- `references/mathlib-guide.md` — search and integration with local declarations and mathlib;
- `references/verification.md` — live, file-local, dependency-aware, and project-level verification gates;
- `references/performance-optimization.md` — measured Lean elaboration/build performance work;
- `references/simp-reference.md` — `simp`, simp-lemma, and simproc design;
- `references/branches/mathlib-upstream.md` — additional policy and review bar for work intended for upstream mathlib.

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.

Collection-level upstream provenance and licensing are recorded in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); each independently installable Skill vendors the same required notices.
