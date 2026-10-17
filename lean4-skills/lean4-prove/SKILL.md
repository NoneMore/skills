---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the requested outcome is to complete or repair its proof with the target held fixed unless explicitly authorized otherwise. Local elaboration, typeclass, API, and tactic diagnostics encountered while repairing that target remain part of proving, as do comparisons among proof strategies. Use `lean4-diagnose` when root-cause investigation across module, dependency, toolchain, build, or integration boundaries is itself the requested outcome."
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

1. Inspect the exact goal, declaration, nearby source, and current diagnostics before editing. Treat local type mismatches, instance failures, unknown identifiers, and tactic errors as part of repairing this proof unless evidence shows a broader boundary failure.
2. Search local declarations and active imports before widening to mathlib. Search by mathematical meaning and type shape rather than guessed declaration names, and validate candidates in the actual project context.
3. Try a small set of materially different proof candidates. Induction schemes, rewrite plans, direct structural arguments, automation choices, and theorem-selection alternatives remain ordinary proving work while the formal target stays fixed. Prefer live goal/candidate feedback when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change. Cross-file support edits are allowed when genuinely required, but do not widen the task into unrelated cleanup.
5. Verify the changed target and affected dependency boundary with the lightest sufficient gate. `lake env lean path/to/File.lean` is a fast file-local check and does not rebuild changed imports. After changing an imported source, use a dependency-aware check such as `lake lean path/to/File.lean`, or the repository's configured build/test gate when integration scope matters. Repository-configured gates take precedence, and state what actually ran.

## Boundaries

- If the statement itself needs design or revision, proof completion for the fixed target is no longer the governing outcome; do not silently change it.
- Search, theorem lookup, API comparison, local diagnostics, small Lean experiments, and materially different proof strategies remain part of proving while the formal target stays fixed. Their presence does not by itself select `lean4-recon`.
- Use `lean4-recon` only when the requested work changes from completing the fixed target to deliberately widening semantic context to challenge the surrounding problem framing or API boundary before committing to an implementation.
- If several artifacts fail because of a shared module, dependency, toolchain, build, or integration change and the requested result is the common root cause or migration path, use `lean4-diagnose` for that boundary-owned investigation.
- Do not widen a proof-completion task into another independently requested outcome unless the user actually asks for it.

## Stop and completion

Do not repeat the same failed avenue without new evidence. When no materially new bounded avenue remains, stop with the blocker, evidence already gathered, and the smallest useful next action.

A proof is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, and the affected scope satisfies the chosen verification gate. State what actually ran; do not collapse weaker local checks into stronger integration claims.
