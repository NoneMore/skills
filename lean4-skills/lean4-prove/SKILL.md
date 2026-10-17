---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the task is to complete or repair its proof with the target held fixed unless explicitly authorized otherwise."
license: MIT
---

# Lean 4 Prove

Produce a checked proof for an existing target without silently changing what is being proved or weakening the accepted trust basis.

## Workflow

1. Inspect the exact goal, nearby source, and current diagnostics.
2. Search local declarations and active imports before widening to mathlib; search by meaning and type shape, then validate candidates in the project context.
3. Try a small set of materially different proof strategies, using live feedback when available or compiling candidates one at a time.
4. Apply the smallest coherent passing change. Keep the statement and public API fixed unless revision is explicitly authorized.
5. Run the lightest verification gate that exercises the affected scope and report what ran. If an imported source changed, do not treat a file-local check against possibly stale artifacts as dependency-aware verification.

Do not add axioms, `sorry`, or `admit` to manufacture completion. Do not widen proof repair into unrelated cleanup.

## Stop and completion

Stop when no materially new bounded avenue remains; return the blocker, useful evidence, and smallest next action.

Complete means the agreed target elaborates, the requested proof scope has no unresolved `sorry`/`admit`, and the affected scope passed the verification gate actually claimed.
