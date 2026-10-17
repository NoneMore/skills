---
name: lean4-optimize
description: "Use after a Lean 4/mathlib proof is already correct when the task is a durable local improvement in clarity, maintainability, robustness, brevity where that helps clarity, or measured performance."
license: MIT
---

# Lean 4 Optimize

Establish a verified baseline before claiming an optimization. Keep the public theorem statement and accepted trust basis unchanged.

## Choose one primary surface

- **Strategy simplification:** prefer a more direct mathematical/library argument or useful helper. Load [proof strategy simplification](references/proof-simplification.md).
- **Local simplification:** preserve the proof strategy while removing ceremony when the result becomes clearer and at least as stable. Load [local proof cleanup](references/local-cleanup.md). Load [simp and simp-lemma design](references/simplification.md) when simplifier policy or global simp behavior is material.
- **Performance:** localize and measure cost before changing code. Load [performance guidance](references/performance.md).

Choose one primary surface. Record secondary benefits, but do not widen into other optimization surfaces by default.

## Candidate acceptance

Correctness, the accepted trust basis, and the public theorem contract are hard invariants. Accept a candidate only when it materially improves the selected property without an unacceptable regression in directness, clarity, maintainability, inference/search burden, determinism, or verification cost.

Brevity alone does not justify heavier automation or loss of meaningful proof structure. Prefer the narrowest change that achieves the improvement.

## Workflow

1. Record the baseline and concrete property to improve; if correctness is not established, repair or report that blocker first. Keep the target scope to the declarations or files implicated by the user's request. Do not widen from the referenced change to other dirty or related code merely to find more optimization opportunities; report broader opportunities separately.
2. Search local and imported APIs when an existing result may remove complexity.
3. Apply one coherent change at a time.
4. Re-run the baseline verification scope; for performance work, rerun the same measurement.
5. Reject regressions in correctness, trust, diagnostics, or maintainability unless the user requested the tradeoff. If a change affects global simp behavior, imports, or reusable API surface, verify a scope broad enough to exercise that integration boundary.

Stop when remaining opportunities are marginal, speculative, or out of scope. Correctness and maintainability outrank token or line count.

## Completion

Report the baseline, the property improved, and the verification gate that passed. For performance work, report comparable before/after measurements. Mention material tradeoffs or promising candidates that were rejected rather than presenting them as wins.
