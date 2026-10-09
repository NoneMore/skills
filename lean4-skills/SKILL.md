---
name: lean4
description: "Use for Lean 4 and mathlib tasks: editing .lean files, filling proofs or sorries, debugging Lean/Lake diagnostics, searching mathlib, formalizing or refuting mathematical statements, reviewing or simplifying Lean proofs, and explaining Lean concepts. Do not use for Coq/Rocq, Agda, Isabelle, HOL, Mizar, Idris, or other theorem provers."
license: MIT
---

# Lean 4

This skill is the portable behavioral entry point for Lean 4 work. Keep the common path small: use the contract below, then load only the workflow, branch, or knowledge reference needed for the current task.

## Behavioral Contract

Establish the target and scope before editing: the declaration or error being addressed, the files that may change, and the verification level the user expects.

Maintain these invariants unless the user explicitly asks otherwise:

- Preserve existing theorem statements, declaration signatures, and public API. If the statement itself is wrong or underspecified, stop proof editing and switch to the formalization or refutation workflow.
- Preserve existing docstrings when editing existing declarations. New declarations may receive new docstrings.
- Never introduce a global axiom silently. Prefer a proof; when an assumption is genuinely part of the intended theorem, make it explicit in the statement or report it as an assumption.
- Keep unrelated files and unrelated working-tree changes untouched.
- Do not commit, push, create a PR, or perform destructive version-control operations unless the user explicitly asks for that operation.
- Follow the local project's style. When the target is upstream mathlib work, load [branches/mathlib-upstream.md](references/branches/mathlib-upstream.md).

## Common Path

1. **Inspect before editing.** Read the relevant declaration and obtain the current goal or diagnostics. Prefer live Lean/LSP state when available.
2. **Search before proving.** Search local declarations and mathlib before constructing a proof from scratch. For nontrivial library search, load [mathlib-guide.md](references/mathlib-guide.md).
3. **Test candidates before mutation.** For a proof hole, generate a small set of plausible candidates and test them against the live goal when the runtime supports it.
4. **Make the smallest useful edit.** Avoid speculative refactors while fixing a local goal or diagnostic.
5. **Verify with the lightest sufficient gate.** Use per-file diagnostics after each edit; use a dependency-aware file check after cross-file changes; reserve a project build for integration or final gates.
6. **Stop on repeated blockers.** Do not repeat the same failed approach without new evidence. Report the blocker and the attempts that ruled out the current path.

### LSP-first behavior

When available, prefer live goal/diagnostic/search tools such as `lean_goal`, `lean_diagnostic_messages`, `lean_local_search`, semantic mathlib search, `lean_loogle`, and `lean_multi_attempt`. Use scripts or full builds when live tooling is unavailable, insufficient, or the requested completion gate requires them.

For exact fallback behavior, load [branches/runtime-fallbacks.md](references/branches/runtime-fallbacks.md).

## Workflow Selection

Load exactly one primary workflow when the task needs more than the common path:

| User intent | Load |
|---|---|
| Fill proofs/sorries, repair Lean errors, or run bounded proving loops | [workflows/prove.md](references/workflows/prove.md) |
| Draft a statement or formalize an informal mathematical claim | [workflows/formalize.md](references/workflows/formalize.md) |
| Refute a statement or search for a certified counterexample | [workflows/disprove.md](references/workflows/disprove.md) |
| Review Lean code without changing it | [workflows/review.md](references/workflows/review.md) |
| Refactor, simplify, golf, or improve proof performance | [workflows/optimize.md](references/workflows/optimize.md) |
| Teach Lean, explain code, or explore a project/mathlib interactively | [workflows/learn.md](references/workflows/learn.md) |

Do not load every workflow spec up front. The workflow owns task-specific decisions and completion conditions; this file owns the shared invariants.

## Conditional Branches

Load these only when their condition is reached:

- [branches/deep-mode.md](references/branches/deep-mode.md) — a proof remains blocked after the normal bounded path, or the user explicitly requests deeper multi-file work.
- [branches/persistence.md](references/branches/persistence.md) — the user explicitly wants reusable run history or a compatible host requests persistence.
- [branches/runtime-fallbacks.md](references/branches/runtime-fallbacks.md) — expected Lean/LSP/helper capabilities are missing.
- [branches/mathlib-upstream.md](references/branches/mathlib-upstream.md) — the repository is mathlib or the user is preparing an upstream mathlib contribution.

## Completion

Use observable completion conditions rather than a generic "be thorough" rule:

- **Proof/edit:** the target elaborates, no new diagnostics were introduced in touched files, and there are no remaining sorries in the agreed proof scope unless the user explicitly accepted a partial result.
- **Debugging:** the reported diagnostic is gone and the relevant file passes the chosen verification gate.
- **Project/integration work:** run the project's integration gate when the requested scope warrants it; for a Lean project this is commonly `lake build`.
- **Trust:** the proof's trust basis has not silently changed. If axiom verification is requested or available as a project gate, report its result.
- **Review:** return findings and evidence without modifying files.

If required tools, permissions, project state, or source material are missing, state which completion condition cannot be verified and stop rather than manufacturing certainty.

## Operating Profiles

Choose the smallest profile that can complete the task:

- **Live Lean/LSP:** preferred for goal inspection, search, candidate testing, and incremental diagnostics.
- **Lean + helper scripts:** use deterministic helpers for parsing, audits, or transformations and Lean/Lake for verification.
- **Lean/Lake only:** use direct compilation and project search; expect slower feedback.
- **Read-only:** inspect and explain without edits or commits.

Host-specific path resolution and plugin adapters are not part of this portable contract; see [branches/runtime-fallbacks.md](references/branches/runtime-fallbacks.md) only when needed.

## Knowledge References

Load knowledge by symptom or topic, not as a bundle. Common entry points are [compilation-errors.md](references/compilation-errors.md) for a specific diagnostic, [sorry-filling.md](references/sorry-filling.md) for proof-hole tactics, [mathlib-guide.md](references/mathlib-guide.md) for library search, [tactics-reference.md](references/tactics-reference.md) for tactic lookup, and [mathlib-style.md](references/mathlib-style.md) for mathlib-targeted style.

The categorized reference map is [references/INDEX.md](references/INDEX.md).