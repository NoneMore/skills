---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib proof code when the task needs evidence-backed findings about correctness, robustness, library integration, maintainability, or proof quality. Review-only requests are read-only."
license: MIT
---

# Lean 4 Review

Review only the requested scope. Review-only requests are read-only; if fixes are explicitly requested, substantiate each material finding before making the corresponding bounded change.

## Review order

1. **Correctness:** diagnostics, unresolved `sorry`/`admit`, material trust concerns, and a verification gate that exercises any dependency or integration boundary behind the claim.
2. **Robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, and accidental definitional dependence.
3. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports; validate candidate APIs in context.
4. **Maintainability:** proof structure, naming, comments/docstrings, and project conventions. Consider optimization only when it materially improves directness, determinism, performance, or clarity.

## Completion

Return prioritized findings with location, evidence, impact, and recommendation. Distinguish blockers from advisory suggestions; if there are no material findings, say so rather than inventing nits. State verification limits that prevent a conclusive correctness claim.
