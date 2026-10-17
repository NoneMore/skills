---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when translating mathematical intent into a Lean declaration, choosing canonical types or hypotheses, deciding intended generality, or explicitly revising a statement."
license: MIT
---

# Lean 4 Formalize

## Purpose

Turn mathematical intent into a faithful Lean declaration whose statement design is explicit rather than accidental.

## Invariants

- Preserve existing declarations unless statement revision is explicitly authorized.
- Prefer the weakest faithful statement: make hypotheses explicit and do not hide assumptions behind new axioms.
- Follow local project conventions.

## Workflow

1. Resolve the mathematical claim and intended level of generality. If a source contains several claims, make the selected claim or selection rule explicit.
2. Search local code and active imports before widening to mathlib for canonical types, definitions, theorem shapes, and existing results. Search by meaning/type rather than guessed names and validate candidates in the actual project context.
3. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis changes.
4. Check that the declaration itself elaborates. Diagnose local type, instance, namespace, import, or API errors as part of making this declaration valid. A draft may contain an explicitly reported proof hole when the requested outcome is only statement design.
5. If proving exposes a statement mismatch, revise only declarations created for the task or existing declarations the user explicitly authorized for statement work.

Statement-design work may include ordinary API search, encoding comparison, hypothesis testing, generality decisions, and local elaboration repair. If the same request also requires a checked proof, settle the declaration first, then complete and verify that proof without silently changing the statement. If evidence shows the requested claim may be false, report that rather than weakening the statement to make it provable.

A statement-design-only result needs the declaration skeleton to elaborate in its intended context. When the requested deliverable also includes a checked proof across changed files or project boundaries, run the repository-configured gate appropriate to that affected scope and report what ran; do not label a file-local elaboration check as project verification.

## Completion

- **Draft:** the intended claim is represented faithfully in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the declaration and requested proof elaborate under the required verification gate.

Any unresolved statement ambiguity or proof hole makes the result partial; report it explicitly.
