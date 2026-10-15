---
name: lean4
description: "Use for formal mathematics in Lean 4 and mathlib: proving or repairing theorems, filling sorries, formalizing or refuting mathematical statements, debugging Lean/Lake diagnostics, searching mathlib, reviewing proofs, simplifying proofs, and explaining formalized mathematics. Do not use for general Lean application development, compiler internals, FFI, custom syntax/DSL authoring, JSON tooling, linter infrastructure, Coq/Rocq, Agda, Isabelle, HOL, Mizar, Idris, or other theorem provers."
license: MIT
---

# Lean 4

This is the portable behavioral entry point for formal mathematics in Lean 4 and mathlib. Keep shared behavior here; load a workflow only when that workflow actually owns the current task, and load specialized knowledge only when the mathematical formalization task requires it.

## Shared invariants

Unless the user explicitly authorizes otherwise:

- Preserve existing theorem statements, declaration signatures, and public API. If the statement itself is the problem, hand responsibility to the formalization or refutation workflow rather than silently weakening it.
- Preserve existing docstrings on declarations being edited. New declarations may receive new documentation.
- Do not silently introduce axioms, `sorry`, `admit`, or another change to the trust basis. Surface assumptions explicitly.
- Keep unrelated files and unrelated working-tree changes untouched.
- Do not commit, push, open a PR, or perform destructive version-control operations unless the user explicitly requests that operation.
- Follow local project conventions. For work intended for upstream mathlib, also load [references/branches/mathlib-upstream.md](references/branches/mathlib-upstream.md).

## Workflow ownership

Select a workflow when one clearly owns the current task. Do not preload unrelated workflows.

| Current responsibility | Workflow |
|---|---|
| Fill a proof hole, repair a proof failure, or make the smallest supporting edits needed for a proof | [prove](references/workflows/prove.md) |
| Design a Lean statement from an informal claim or explicitly revise statement shape | [formalize](references/workflows/formalize.md) |
| Search for and certify a counterexample or negation | [disprove](references/workflows/disprove.md) |
| Review Lean code without modifying it | [review](references/workflows/review.md) |
| Improve an already-correct proof for structure, directness, size, or performance | [optimize](references/workflows/optimize.md) |
| Explain Lean, mathlib, project code, or a formal mathematical idea | [learn](references/workflows/learn.md) |

A workflow is the **current owner**, not a permanent mode for the whole request. It may explicitly hand off when responsibility changes, for example `formalize -> prove`, `prove -> formalize`, `prove -> disprove`, or `prove -> optimize`.

## Capability and verification policy

Prefer the strongest available feedback loop without assuming a particular host or plugin installation:

- Use live goal, diagnostic, search, hover, or candidate-testing capabilities when the runtime provides them.
- Otherwise use Lean/Lake and project search directly.
- Missing rich tooling is a capability reduction, not permission to skip semantic verification.
- Use the lightest verification gate that establishes the property the task requires. Load [references/verification.md](references/verification.md) when file, dependency, or integration scope matters.
- State what actually ran. If a required gate cannot run, distinguish a locally checked result from an integration-verified result.

Do not hard-code host adapter paths, helper-runtime locations, command aliases, rate limits, or implementation-specific tool inventories into portable behavior.

## Scope and stopping

Make the smallest coherent change that satisfies the agreed formalization task. Cross-file edits are allowed when they are the smallest necessary way to complete the target; they do not require a separate "deep" mode. Do not widen a proof task into open-ended refactoring or repository cleanup without user authorization.

Do not repeat the same failed avenue without new evidence. When a bounded path is exhausted, either hand off to the workflow that now owns the problem or stop with the blocker, evidence already gathered, and the smallest useful next action.

## Knowledge on demand

Use [references/INDEX.md](references/INDEX.md) as the map for specialized Lean/mathlib knowledge. References supplement the current owner; they do not redefine workflow behavior.
