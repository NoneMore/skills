---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when the requested outcome is to translate mathematical intent into a Lean declaration, choose its canonical types or hypotheses, decide its intended generality, or explicitly revise an existing statement. Ordinary API, encoding, hypothesis, generality, and local elaboration decisions needed to deliver that declaration remain part of this skill. Use `lean4-recon` only when deliberate context expansion to challenge the current framing is itself the requested outcome before committing to a declaration."
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

## Boundaries

Statement-design decisions required to produce the requested declaration stay here, including ordinary choices of canonical types, hypotheses, generality, API, and local elaboration repair. Search or comparison needed for those choices does not by itself make Recon a separate outcome.

Use `lean4-recon` when the request is instead to challenge the current problem framing before committing to a declaration by deliberately widening semantic context beyond what statement completion requires. If a concrete declaration is already fixed and only its proof remains, use `lean4-prove`. If the work reveals a shared module, dependency, toolchain, build, or integration failure whose root cause is now the requested result, use `lean4-diagnose`. Merely choosing mathlib APIs while creating a declaration remains ordinary formalization.

If the same request also requires a checked proof, settle the declaration first, then complete and verify that proof without silently changing the statement. If evidence instead shows the requested claim may be false, report that rather than weakening the statement to make it provable.

A statement-design-only result needs the declaration skeleton to elaborate in its intended context. When the requested deliverable also includes a checked proof across changed files or project boundaries, run the repository-configured gate appropriate to that affected scope and report what ran; do not label a file-local elaboration check as project verification.

## Completion

- **Draft:** the intended claim is represented faithfully in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the declaration and requested proof elaborate under the required verification gate.

Any unresolved statement ambiguity or proof hole makes the result partial; report it explicitly.
