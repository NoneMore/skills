---
name: lean4-skills
description: "Use for formal mathematics in Lean 4 and mathlib: proving or repairing theorems, filling proof holes, formalizing or refuting mathematical statements, debugging Lean/Lake diagnostics, searching mathlib, reviewing or simplifying proofs, and explaining formalized mathematics. Do not use for general Lean application development or other theorem provers."
license: MIT
---

# Lean 4

This is the portable entry point for formal mathematics in Lean 4 and mathlib. Load only the guidance relevant to the current task.

## Shared invariants

- Preserve existing theorem statements, declaration signatures, and public API unless statement design is explicitly in scope. If the statement itself is the blocker, surface that rather than silently weakening it.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the trust basis to make a proof or repair succeed. Surface existing assumptions explicitly. If the user accepts a partial result or trust-basis change, report it as partial or changed rather than as ordinary verified completion.
- Follow local project conventions. For work intended for upstream mathlib, also load [references/branches/mathlib-upstream.md](references/branches/mathlib-upstream.md).

## Task guide

Load only what the task needs:

| Task | Guidance |
|---|---|
| Fill a proof hole or repair a proof failure | [prove](references/prove.md) |
| Design or explicitly revise a Lean statement | [formalize](references/formalize.md) |
| Search for and certify a counterexample or negation | [disprove](references/disprove.md) |
| Diagnose a non-proof Lean/Lake failure | [compilation errors](references/compilation-errors.md) |
| Inspect or remove unwanted trust assumptions | [axiom elimination](references/axiom-elimination.md) |
| Review Lean proof code | [review](references/review.md) |
| Improve an already-correct proof | [optimize](references/optimize.md) |

For explanation or exploration, use only the narrower references needed by the question; there is no separate learning mode.

## Capability and verification policy

Prefer the strongest available feedback loop without assuming a particular host or plugin installation:

- Use live goal, diagnostic, search, hover, or candidate-testing capabilities when the runtime provides them.
- Otherwise use Lean/Lake and project search directly.
- Missing rich tooling is a capability reduction, not permission to skip semantic verification.
- Use the lightest verification gate that establishes the property the task requires. Load [references/verification.md](references/verification.md) when file, dependency, or integration scope matters.
- State what actually ran. If a required gate cannot run, distinguish a locally checked result from an integration-verified result.

Portable behavior depends on available capabilities, not a particular host or plugin implementation.

## Scope and stopping

Make the smallest coherent change that satisfies the task. Cross-file edits are allowed when necessary; do not modify generated caches or dependency checkouts such as `.lake/packages` unless the task specifically concerns them. Do not widen a local proof or repair into unrelated refactoring or repository cleanup.

Do not repeat the same failed avenue without new evidence. When no materially new bounded avenue remains, stop with the blocker, evidence already gathered, and the smallest useful next action.

## Specialized references

Load only when material to the task:

- [mathlib search and integration](references/mathlib-guide.md)
- [verification gates](references/verification.md)
- [upstream mathlib policy](references/branches/mathlib-upstream.md)
- [proof strategy simplification](references/proof-simplification.md)
- [performance optimization](references/performance-optimization.md)
- [`simp` and simp-lemma design](references/simp-reference.md)
- [mathlib review taxonomy](references/mathlib-review-taxonomy.md)
