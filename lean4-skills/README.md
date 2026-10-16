# Lean 4 Skills

Locally complete capabilities for formal mathematics in Lean 4 and mathlib. These are outcome-oriented skills, not stages in a required workflow.

Before materially changing this family, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `lean4-prove` — complete or repair a proof for an already-settled Lean proposition.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is in scope.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — diagnose Lean/Lake failures in formal-mathematics work when the problem is not yet ordinary proof search.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

Each capability is directly discoverable from its own metadata. There is intentionally no model-invoked family router: selection belongs to discovery, and cross-skill handoffs are explicit where one outcome turns into another.

## Compatibility

The root `SKILL.md` is a temporary **user-invoked compatibility shim** for explicit `$lean4-skills` callers. It sets `disable-model-invocation: true`, contains no independent Lean workflow, and delegates to exactly the child capability that owns the requested outcome. New metadata and documentation must not depend on the legacy entry point. Remove the shim once known callers using the old name have migrated.

## Shared references

The family keeps reusable knowledge that does not own a user-facing outcome under `references/`:

- `mathlib-guide.md` — search and integration with local declarations and mathlib;
- `verification.md` — live, file-local, dependency-aware, and project-level verification gates;
- `performance-optimization.md` — measured Lean elaboration/build performance work;
- `simp-reference.md` — `simp`, simp-lemma, and simproc design;
- `branches/mathlib-upstream.md` — additional policy and review bar for work intended for upstream mathlib.

Critical safety and completion constraints are repeated in the skills that need them when locality materially improves reliability; specialized reusable knowledge remains shared.

## Scope

This family is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.

Upstream provenance and licensing are recorded in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
