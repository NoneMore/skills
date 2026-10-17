---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the task is to complete or repair its proof with the target held fixed unless explicitly authorized otherwise."
license: MIT
---

# Lean 4 Prove

## Purpose

Produce a checked proof for an existing concrete formal target without silently changing what is being proved.

## Invariants

- Preserve existing theorem statements, declaration signatures, and public API unless the user explicitly expands the task to statement design.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to claim proof completion.
- Follow local project conventions.

## Workflow

1. Inspect the exact goal, declaration, nearby source, and current diagnostics before editing.
2. Search local declarations and active imports before widening to mathlib. Search by mathematical meaning and type shape rather than guessed declaration names, and validate candidates in the actual project context.
3. Try a small set of materially different proof candidates. Induction schemes, rewrite plans, direct structural arguments, automation choices, and theorem-selection alternatives are all ordinary proving techniques. Prefer live goal/candidate feedback when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change. Cross-file support edits are allowed when genuinely required, but do not widen the task into unrelated cleanup.
5. Verify the changed target and affected dependency boundary with the lightest sufficient gate. `lake env lean path/to/File.lean` is a fast file-local check and does not rebuild changed imports. After changing an imported source, use a dependency-aware check such as `lake lean path/to/File.lean`, or the repository's configured build/test gate when integration scope matters. Repository-configured gates take precedence, and state what actually ran.

## Scope discipline

Keep the agreed target fixed unless statement revision is explicitly authorized. Search, theorem lookup, API comparison, local diagnostics, small Lean experiments, and proof-strategy comparison may all be used when they help establish the proof. Do not turn a proof-completion request into unrelated repository cleanup or silently broaden its public API.

## Stop and completion

Do not repeat the same failed avenue without new evidence. When no materially new bounded avenue remains, stop with the blocker, evidence already gathered, and the smallest useful next action.

A proof is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, and the affected scope satisfies the chosen verification gate. State what actually ran; do not collapse weaker local checks into stronger integration claims.
