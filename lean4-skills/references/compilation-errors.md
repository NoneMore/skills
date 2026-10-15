# Lean 4 Diagnostic Triage

Use this reference after obtaining the exact current diagnostic and nearby source context. Diagnose the class of failure before changing code; avoid treating every elaboration failure as a proof-search problem.

## Type mismatch

Compare the expected and actual types before adding coercions or `convert` steps. Common causes include:

- a wrong implicit argument or universe;
- a missing/incorrect coercion;
- equality or eventual-equality in the wrong direction;
- a declaration found by name whose signature is not the one assumed;
- elaboration against a different local typeclass instance.

Prefer making the intended type explicit at the smallest point that explains the mismatch.

## Failed to synthesize instance

First determine whether the required instance truly does not exist or whether its parameters still contain unresolved metavariables. If the target class is not fully determined, add type/implicit annotations before manufacturing a local instance.

If an instance really is missing, provide actual evidence or import the module that defines it. Writing `inferInstance` only repeats synthesis; it does not create evidence that was absent.

When several instances of the same class are in scope, inspect which instance each relevant term was elaborated against and make the intended one explicit at the smallest boundary. Do not broaden into general instance redesign unless the task actually requires it.

## Recursion depth and heartbeat/timeouts

These are different failures.

- recursion-depth errors usually indicate elaboration/reduction depth;
- heartbeat or tactic/typeclass timeouts indicate too much work or search.

Do not reflexively increase limits. First narrow broad `simp`, automation, typeclass search, or deeply nested terms; make polymorphic parameters explicit; or split a large elaboration problem into smaller checked lemmas. Load [references/performance-optimization.md](references/performance-optimization.md) when the failure is performance-driven.

## Unknown identifier / invalid field

Check spelling, namespace, imports, and the actual declaration signature. Dot notation is not interchangeable with every namespace function. Search the active imports or mathlib rather than guessing API names.

A local name may also disappear after substitution/case tactics rewrite the context; inspect the current goal instead of assuming the pre-tactic context still exists.

## Unsolved goals / tactic failed

Inspect the remaining goal. A tactic may have made useful progress even when it did not close everything. Prefer a direct lemma or goal-appropriate solver over repeatedly adding broader automation.

For proof-search failures, use `references/prove.md` for iteration and stopping guidance.

## "No goals to be solved"

An earlier tactic already closed the goal. Remove the redundant later tactic rather than trying to force Lean to keep a goal open.

## Imports and module-system diagnostics

Import placement and visibility are semantic in Lean. In module-system code, public/private visibility and `public import` affect what downstream modules can use. For work intended for upstream mathlib, load `references/branches/mathlib-upstream.md` and consult the current authoritative contribution guidance.

After changing an imported source file, distinguish a file-local check from dependency-aware verification; see [references/verification.md](references/verification.md).

## Debugging rule

Use the smallest source change that tests the current hypothesis, then re-read the diagnostic. If the same error persists with no new evidence, stop repeating that repair avenue. Use `references/prove.md` when the remaining problem is proof search; otherwise continue from the diagnostic evidence here.
