---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the task needs evidence-backed findings about correctness, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only."
license: MIT
---

# Lean 4 Review

Independently evaluate existing Lean proof code and return prioritized, evidence-backed findings without inventing work.

Review only the requested scope. Review-only requests are read-only with respect to project source; if fixes are explicitly requested, substantiate each material finding before making the corresponding bounded change.

## Review order

1. **Correctness:** diagnostics, unresolved `sorry`/`admit`, and material trust concerns. Use a verification gate that actually exercises any dependency or integration boundary behind the claim.
2. **Robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, accidental definitional dependence.
3. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports. Validate candidate APIs in the project context.
4. **Maintainability:** proof structure, naming, comments/docstrings, and local style.
5. **Optimization:** only when it materially improves directness, determinism, performance, or clarity.

Project-specific conventions are authoritative where material. Supporting search, diagnostics, and small experiments do not change the read-only contract.

## Completion

Return prioritized findings with location, evidence, impact, and recommendation. Distinguish blockers from advisory suggestions. If there are no material findings, say so rather than inventing nits. State any verification limitation that prevents a material correctness claim from being conclusive.
