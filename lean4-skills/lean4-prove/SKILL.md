---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or current proof goal already exists and the requested outcome is to complete or repair its proof with the statement held fixed unless explicitly authorized otherwise. Do not use when the main uncertainty is statement design, open-ended abstraction/API exploration, certified refutation, review-only work, or post-correctness optimization."
license: MIT
---

# Lean 4 Prove

## Purpose

Produce a checked proof for an existing concrete formal target without silently changing what is being proved.

## Invariants

- Preserve existing theorem statements, declaration signatures, and public API unless the user explicitly expands the task to statement design.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to claim proof completion.
- Follow local project conventions. For work intended for upstream mathlib, load [upstream mathlib guidance](references/branches/mathlib-upstream.md).

## Workflow

1. Inspect the exact goal, declaration, nearby source, and current diagnostics before editing.
2. Search local declarations and mathlib when an existing result may solve or materially simplify the goal; use [mathlib search and integration](references/mathlib-guide.md) when useful.
3. Try a small set of materially different candidates. Prefer live goal/candidate feedback when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change. Cross-file support edits are allowed when genuinely required, but do not widen the task into unrelated cleanup.
5. Verify the changed target and affected dependency boundary with the lightest sufficient gate; use [verification gates](references/verification.md) whenever file, dependency, or integration scope matters.

Load [`simp` guidance](references/simp-reference.md) or [performance guidance](references/performance-optimization.md) only when that mechanism is material to the proof.

## Boundaries

- If an informal mathematical claim still needs a Lean declaration or the statement itself must be designed or revised, use `lean4-formalize`.
- If the main uncertainty is what abstraction, existing API, assumption boundary, generalization, or approach should be pursued, use `lean4-explore`. Ordinary theorem lookup needed to finish this known goal remains part of this skill.
- If there is credible evidence that the proposition is false and the requested outcome is a certified counterexample or negation, use `lean4-refute`.
- If the target is already correct and the requested outcome is simplification or speed, use `lean4-optimize`.
- If the blocker is a concrete non-proof Lean/Lake diagnostic whose class is not yet understood, use `lean4-diagnose`.
- If the task is specifically about unacceptable assumptions or trust dependencies, use `lean4-trust`.

## Stop and completion

Do not repeat the same failed avenue without new evidence. When no materially new bounded avenue remains, stop with the blocker, evidence already gathered, and the smallest useful next action.

A proof is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, and the affected scope satisfies the chosen verification gate. State what actually ran; do not collapse weaker local checks into stronger integration claims.
