---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the requested outcome is evidence-backed findings about correctness, trust, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only. Plain explanation without an evaluation request does not need this skill; use lean4-explore only when choosing among formal directions is itself the open task."
license: MIT
---

# Lean 4 Review

## Purpose

Independently evaluate existing Lean proof code and return prioritized, evidence-backed findings without inventing work.

## Scope

Prefer the smallest scope that answers the request: one declaration, one file, changed files, or an explicitly requested project review. Do not silently widen a local review to the whole project.

Review-only requests are read-only with respect to project source. Verification may use the project's normal Lean/Lake gates and their generated build artifacts when needed to establish a material claim. If fixes are also requested, substantiate the finding first, then compose with the capability that owns the change (`lean4-prove`, `lean4-diagnose`, `lean4-trust`, or `lean4-optimize`) rather than turning review into an unbounded implementation workflow.

Follow applicable repository Lean guidance when present; project policy and established documentation take precedence over generic review defaults.

## Review order

1. **Correctness signals:** diagnostics, unresolved `sorry`/`admit`, and material trust/axiom concerns. When a correctness finding depends on actual elaboration, changed imports, or project integration, load [verification guidance](../references/verification.md) and report what actually ran; a file-local pass is not dependency-aware when changed imported artifacts may be stale.
2. **Proof robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, accidental definitional dependence.
3. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports. Search local declarations and active imports before widening outward and validate candidate APIs in the actual project context.
4. **Maintainability:** proof structure, naming, comments/docstrings, and local style.
5. **Optimization opportunities:** only when they materially improve directness, determinism, performance, or clarity.

For upstream mathlib work, consult current authoritative contribution policy and nearby current mathlib code. Treat project-specific simplification policy as authoritative when global simp behavior is material.

A standalone request to explain how existing code works, with no evaluation request and no open design decision, does not require a specialized Lean 4 Skill. If the question instead asks which abstraction, API, or formal direction should be pursued, use `lean4-explore` for that decision.

## Output and completion

Return prioritized findings with location, evidence, impact, and a concrete recommendation. Distinguish blockers from advisory suggestions. If there are no material findings, say so rather than inventing nits.

A review is complete when the requested scope has been examined against the material review dimensions and every reported finding is supported by observable evidence. If a material correctness claim could not be verified at the required dependency or integration scope, state that limitation rather than treating a weaker local check as conclusive.
