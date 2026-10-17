---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the task needs evidence-backed findings about correctness, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only."
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

Treat project-specific simplification policy as authoritative when global simp behavior is material. Bounded search, abstraction comparison, local diagnostic checks, and small experiments may all be used to substantiate findings; review-only work remains read-only regardless of what supporting guidance was also loaded.

## Output and completion

Return prioritized findings with location, evidence, impact, and a concrete recommendation. Distinguish blockers from advisory suggestions. If there are no material findings, say so rather than inventing nits.

A review is complete when the requested scope has been examined against the material review dimensions and every reported finding is supported by observable evidence. If a material correctness claim could not be verified at the required dependency or integration scope, state that limitation rather than treating a weaker local check as conclusive.
