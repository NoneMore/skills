---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the requested outcome is evidence-backed findings about correctness, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only. Do not use when the trust basis itself is the requested outcome; use lean4-trust for a trust audit or cleanup. Do not use when upstream mathlib contribution readiness is the requested outcome; use lean4-mathlib-contribute. Plain explanation without an evaluation request does not need this skill; use lean4-explore only when choosing among formal directions is itself the open task."
license: MIT
---

# Lean 4 Review

## Purpose

Independently evaluate existing Lean proof code and return prioritized, evidence-backed findings without inventing work.

## Scope

Prefer the smallest scope that answers the request: one declaration, one file, changed files, or an explicitly requested project review. Do not silently widen a local review to the whole project.

Review-only requests are read-only with respect to project source. Verification may use the project's normal Lean/Lake gates and their generated build artifacts when needed to establish a material claim. If fixes are also explicitly requested, substantiate each material finding before making the corresponding bounded change.

## Review order

1. **Correctness signals:** diagnostics, unresolved `sorry`/`admit`, and material trust/axiom concerns. When a correctness finding depends on actual elaboration or integration, run the check appropriate to that scope and report what ran. If an imported source changed, a passing `lake env lean` check against possibly stale built artifacts is not dependency-aware; use a dependency-aware or project gate before treating the result as conclusive.
2. **Proof robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, accidental definitional dependence.
3. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports. Search local declarations and active imports before widening outward and validate candidate APIs in the actual project context.
4. **Maintainability:** proof structure, naming, comments/docstrings, and local style.
5. **Optimization opportunities:** only when they materially improve directness, determinism, performance, or clarity.

Treat project-specific simplification policy as authoritative when global simp behavior is material.

Search, abstraction comparison, diagnostic checks, and other reconnaissance needed to substantiate a review finding remain part of review; they do not create separate routing outcomes. Trust concerns may be reported as ordinary correctness findings, but if inspecting or changing the declaration's trust basis is itself the requested outcome, use `lean4-trust`. Likewise, an explicit upstream mathlib acceptance/readiness review belongs to `lean4-mathlib-contribute` rather than generic review.

## Output and completion

Return prioritized findings with location, evidence, impact, and a concrete recommendation. Distinguish blockers from advisory suggestions. If there are no material findings, say so rather than inventing nits.

A review is complete when the requested scope has been examined against the material review dimensions and every reported finding is supported by observable evidence. If a material correctness claim could not be verified at the required dependency or integration scope, state that limitation rather than treating a weaker local check as conclusive.
