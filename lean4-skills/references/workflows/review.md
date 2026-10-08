# Review Workflow

Use for code review of Lean proofs. **Review is read-only:** do not edit, stage, commit, or restore files as part of the review.

## Scope

Prefer the smallest scope that answers the request: one goal/declaration, one file, changed files, or an explicitly requested project review. Do not silently widen a local review to the whole project.

## Review order

1. Correctness signals: diagnostics, unresolved sorries, trust/axiom concerns.
2. Proof robustness: unnecessary automation, brittle rewrites, typeclass/coercion issues.
3. Library integration: existing mathlib lemmas, duplicated helpers, avoidable imports.
4. Maintainability: proof structure, naming, comments/docstrings, local style.
5. Optimization opportunities only when they materially improve directness, determinism, performance, or clarity.

When the target is upstream mathlib, load `../branches/mathlib-upstream.md` and use `../mathlib-review-taxonomy.md` as the additional review bar.

## Output

Return prioritized findings with file/location, evidence, impact, and a concrete recommendation. Distinguish blockers from advisory style suggestions. If there are no material findings, say so rather than inventing nits.

Completion is the report itself; files must remain unchanged.