---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when the requested outcome is to translate an informal mathematical claim into a Lean declaration, choose its canonical types or hypotheses, decide its intended generality, or explicitly revise an existing statement. Do not use when a concrete Lean declaration is already fixed and only its proof needs completion, or when the main task is open-ended reconnaissance before the intended formal object is known."
license: MIT
---

# Lean 4 Formalize

## Purpose

Turn mathematical intent into a faithful Lean declaration whose statement design is explicit rather than accidental.

## Invariants

- Preserve existing declarations unless statement revision is explicitly authorized.
- Prefer the weakest faithful statement: make hypotheses explicit and do not hide assumptions behind new axioms.
- Follow local project conventions. For upstream mathlib work, load [upstream mathlib guidance](references/branches/mathlib-upstream.md).

## Workflow

1. Resolve the mathematical claim and intended level of generality. If a source contains several claims, make the selected claim or selection rule explicit.
2. Search mathlib and local code for canonical types, definitions, theorem shapes, and existing results before choosing an encoding; use [mathlib search and integration](references/mathlib-guide.md) when useful.
3. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis changes.
4. Check that the declaration itself elaborates. A draft may contain an explicitly reported proof hole when the requested outcome is only statement design.
5. If proving exposes a statement mismatch, revise only declarations created for the task or existing declarations the user explicitly authorized for statement work.

## Composition

If the main uncertainty precedes statement design—what object, abstraction, library API, assumption boundary, or generalization should be pursued—use `lean4-explore` to reduce that uncertainty first. Once the intended encoding is selected, this skill owns the durable declaration.

When the user also requires a checked proof, hand the settled declaration to `lean4-prove`. If evidence instead supports falsity, use `lean4-refute` to certify that result rather than mutating the statement to make it provable.

Use [verification guidance](references/verification.md) when the declaration spans files, imports, or project integration boundaries.

## Completion

- **Draft:** the intended claim is represented faithfully in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the generated declaration is subsequently completed under the `lean4-prove` checked-proof contract.

Any unresolved statement ambiguity or proof hole makes the result partial; report it explicitly.
