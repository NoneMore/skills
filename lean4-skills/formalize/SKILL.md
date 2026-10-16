---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when translating an informal mathematical claim into Lean, choosing canonical types or hypotheses, deciding the intended level of generality, or explicitly revising a Lean statement. Do not use when the theorem statement is already fixed and only its proof needs completion."
license: MIT
---

# Lean 4 Formalize

## Purpose

Turn mathematical intent into a faithful Lean declaration whose statement design is explicit rather than accidental.

## Invariants

- Preserve existing declarations unless statement revision is explicitly authorized.
- Prefer the weakest faithful statement: make hypotheses explicit and do not hide assumptions behind new axioms.
- Follow local project conventions. For upstream mathlib work, load [upstream mathlib guidance](../references/branches/mathlib-upstream.md).

## Workflow

1. Resolve the mathematical claim and intended level of generality. If a source contains several claims, make the selected claim or selection rule explicit.
2. Search mathlib and local code for canonical types, definitions, theorem shapes, and existing results before choosing an encoding; use [mathlib search and integration](../references/mathlib-guide.md) when useful.
3. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis changes.
4. Check that the declaration itself elaborates. A draft may contain an explicitly reported proof hole when the requested outcome is only statement design.
5. If proving exposes a statement mismatch, revise only declarations created for the task or existing declarations the user explicitly authorized for statement work.

## Composition

When the user also requires a checked proof, hand the settled declaration to `lean4-prove`. If evidence instead supports falsity, use `lean4-refute` to certify that result rather than mutating the statement to make it provable.

Use [verification guidance](../references/verification.md) when the declaration spans files, imports, or project integration boundaries.

## Completion

- **Draft:** the intended claim is represented faithfully in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the generated declaration is subsequently completed under the `lean4-prove` checked-proof contract.

Any unresolved statement ambiguity or proof hole makes the result partial; report it explicitly.
