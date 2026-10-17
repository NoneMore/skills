---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the task is to complete or repair its proof with the target held fixed unless explicitly authorized otherwise."
license: MIT
---

# Lean 4 Prove

## Workflow

1. Inspect the exact goal, nearby source, and current diagnostics.
2. Search local and imported APIs before broader mathlib; validate candidates in the project context. Search again when failed attempts expose a materially different formulation or abstraction.
3. Try a bounded set of materially different proof strategies, using cheap live feedback to discriminate a small number of plausible candidates before substantial helper construction, or otherwise compiling candidates one at a time.
4. Treat attempts that preserve the same structural blocker or continue the same helper/abstraction chain as one strategy. Once failures repeat that pattern, or a new helper starts spawning its own unresolved helper chain, stop deepening the route: refresh the goal and reframe before adding more structure.
5. Apply the smallest coherent passing change. Keep the statement and public API fixed unless revision is explicitly authorized.
6. Verify the affected scope and report what ran. If an imported source changed, a file-local check against possibly stale artifacts is not dependency-aware verification.

Do not add axioms, `sorry`, or `admit` to manufacture completion. Stop when no materially new bounded avenue remains; report the blocker, useful evidence, and smallest next action.

## Completion

Complete means the agreed target elaborates, the requested proof scope has no unresolved `sorry`/`admit`, and the verification gate actually claimed passed for the affected scope.
