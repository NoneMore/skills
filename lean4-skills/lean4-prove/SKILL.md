---
name: lean4-prove
description: "Use for formal mathematics in Lean 4/mathlib when a concrete Lean declaration, theorem statement, or proof goal already exists and the task is to complete or repair its proof with the target held fixed unless explicitly authorized otherwise."
license: MIT
---

# Lean 4 Prove

## Workflow

1. Inspect the exact goal, nearby source, and current diagnostics.
2. Identify the goal's mathematical shape; search local and imported APIs before broader mathlib for direct results. Validate candidates in context before building helpers; re-search when failures reveal a materially different formulation or abstraction.
3. Try a bounded set of materially different proof strategies; use cheap live feedback to discriminate a few plausible candidates, or compile them one at a time.
4. Treat attempts with the same structural blocker or growing helper chain as one strategy; if that pattern repeats or a helper spawns unresolved helpers, stop extending it and reframe. For dependent-type failures, compare expected and actual indexed types; distinguish definitional equality, transport, and statement mismatch; test a minimal conversion or bridge in context before retrying tactics.
5. Apply the smallest coherent passing change. Keep the statement and public API fixed unless revision is explicitly authorized.
6. Verify the affected scope and report what ran. If an imported source changed, a file-local check against possibly stale artifacts is not dependency-aware verification.

Do not add axioms, `sorry`, or `admit` to manufacture completion. Stop when no materially new bounded avenue remains; report the blocker, useful evidence, and smallest next action.

## Completion

Complete means the agreed target elaborates, the requested proof scope has no unresolved `sorry`/`admit`, and the verification gate actually claimed passed for the affected scope.
