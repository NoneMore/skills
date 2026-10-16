---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the requested outcome is evidence-backed findings about correctness, trust, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only; explanation or reconnaissance without an evaluation request belongs to lean4-explore."
license: MIT
---

# Lean 4 Review

## Purpose

Independently evaluate existing Lean proof code and return prioritized, evidence-backed findings without inventing work.

## Scope

Prefer the smallest scope that answers the request: one declaration, one file, changed files, or an explicitly requested project review. Do not silently widen a local review to the whole project.

Review-only requests are read-only. If fixes are also requested, substantiate the finding first, then compose with the capability that owns the change (`lean4-prove`, `lean4-diagnose`, `lean4-trust`, or `lean4-optimize`) rather than turning review into an unbounded implementation workflow.

## Review order

1. **Correctness signals:** diagnostics, unresolved `sorry`/`admit`, and material trust/axiom concerns.
2. **Proof robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, accidental definitional dependence.
3. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports; use [mathlib search guidance](references/mathlib-guide.md) when useful.
4. **Maintainability:** proof structure, naming, comments/docstrings, and local style.
5. **Optimization opportunities:** only when they materially improve directness, determinism, performance, or clarity.

For upstream mathlib work, load [upstream guidance](references/branches/mathlib-upstream.md) as an additional review bar. Use [`simp` guidance](references/simp-reference.md) when global simplification policy is material.

If the user is asking why existing code works, what abstraction it represents, or which nearby API is canonical without asking for an evaluation, use `lean4-explore` instead.

## Output and completion

Return prioritized findings with location, evidence, impact, and a concrete recommendation. Distinguish blockers from advisory suggestions. If there are no material findings, say so rather than inventing nits.

A review is complete when the requested scope has been examined against the material review dimensions and every reported finding is supported by observable evidence.
