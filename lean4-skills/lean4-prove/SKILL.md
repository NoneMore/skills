---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the task is to complete or repair its proof, including removal of an unacceptable trust dependency, with the target held fixed unless explicitly authorized otherwise."
license: MIT
---

# Lean 4 Prove

## Workflow

1. Inspect the exact goal, nearby source, and current diagnostics.
2. Search local and imported APIs before broader mathlib; validate candidates in the project context.
3. Try a bounded set of materially different proof strategies, using live feedback when available or compiling candidates one at a time.
4. Apply the smallest coherent passing change. Keep the statement and public API fixed unless revision is explicitly authorized. If removing an unacceptable axiom or assumption, trace the dependency and replace it with an accepted proof rather than another forbidden assumption.
5. Verify the affected scope and report what ran. If an imported source changed, a file-local check against possibly stale artifacts is not dependency-aware verification. When trust cleanup was requested, re-check the target declaration's trust basis against the stated policy.

Do not add axioms, `sorry`, or `admit` to manufacture completion. Stop when no materially new bounded avenue remains; report the blocker, useful evidence, and smallest next action.

## Completion

Complete means the agreed target elaborates, the requested proof scope has no unresolved `sorry`/`admit`, and the verification gate actually claimed passed for the affected scope. When trust cleanup is part of the task, the target must also satisfy the stated trust policy; otherwise report the remaining dependency or derivability blocker instead of weakening the statement or policy implicitly.
