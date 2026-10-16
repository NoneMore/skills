---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or current proof goal already exists and the requested outcome is to complete or repair its proof with the statement held fixed unless explicitly authorized otherwise. Comparing materially different proof strategies for that fixed target remains part of this skill. Do not use when the main uncertainty is statement design, a separate formal-design decision about the object/API/hypotheses, certified refutation, review-only work, or post-correctness optimization."
license: MIT
---

# Lean 4 Prove

## Purpose

Produce a checked proof for an existing concrete formal target without silently changing what is being proved.

## Invariants

- Preserve existing theorem statements, declaration signatures, and public API unless the user explicitly expands the task to statement design.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to claim proof completion.
- Follow local project conventions and applicable repository Lean guidance. For upstream mathlib work, consult current authoritative upstream policy and nearby current mathlib code.

## Workflow

1. Inspect the exact goal, declaration, nearby source, and current diagnostics before editing.
2. Search local declarations and active imports before widening to mathlib. Search by mathematical meaning and type shape rather than guessed declaration names, and validate candidates in the actual project context.
3. Try a small set of materially different proof candidates. Induction schemes, rewrite plans, direct structural arguments, automation choices, and theorem-selection alternatives remain ordinary proving work while the formal target stays fixed. Prefer live goal/candidate feedback when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change. Cross-file support edits are allowed when genuinely required, but do not widen the task into unrelated cleanup.
5. Verify the changed target and affected dependency boundary with the lightest sufficient gate. After changing an imported source file, do not treat a passing `lake env lean` check as dependency-aware. Load [verification guidance](../references/verification.md) when the distinction between live, file-local, dependency-aware, or project-level verification matters, and state what actually ran.

If a performance or simplification concern becomes a separate post-correctness improvement outcome, use `lean4-optimize` rather than widening proof completion into optimization.

## Boundaries

- If an informal mathematical claim still needs a Lean declaration or the statement itself must be designed or revised, use `lean4-formalize`.
- Use `lean4-explore` only when the blocker is a distinct formal-design decision whose resolution could change the chosen formal object, abstraction, API family, hypothesis boundary, generality, symmetry, or dependency strategy. Multiple proof strategies for the same fixed target do not by themselves cross this boundary. Ordinary theorem lookup and candidate comparison needed to finish the known goal remain part of this skill.
- If there is credible evidence that the proposition is false and the requested outcome is a certified counterexample or negation, use `lean4-refute`.
- If the target is already correct and the requested outcome is simplification or speed, use `lean4-optimize`.
- If the blocker is a concrete non-proof Lean/Lake diagnostic whose class is not yet understood, use `lean4-diagnose`.
- If the task is specifically about unacceptable assumptions or trust dependencies, use `lean4-trust`.

## Stop and completion

Do not repeat the same failed avenue without new evidence. When no materially new bounded avenue remains, stop with the blocker, evidence already gathered, and the smallest useful next action.

A proof is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, and the affected scope satisfies the chosen verification gate. State what actually ran; do not collapse weaker local checks into stronger integration claims.
