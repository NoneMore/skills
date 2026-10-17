---
name: lean4-optimize
description: "Use after a Lean 4/mathlib proof is already correct when the task is a durable local improvement in clarity, maintainability, robustness, brevity where that helps clarity, or measured performance."
license: MIT
---

# Lean 4 Optimize

Establish a verified baseline before claiming an optimization. Keep the public theorem statement and accepted trust basis unchanged.

## Choose one surface

- **Strategy simplification:** prefer a more direct mathematical/library argument or useful helper. Load [proof strategy simplification](references/proof-simplification.md).
- **Local simplification:** remove ceremony when the result becomes clearer and at least as stable. Load [simp and simp-lemma design](references/simplification.md) when global simp behavior is material.
- **Performance:** localize and measure cost before changing code. Load [performance guidance](references/performance.md).

Do not combine all three by default.

## Workflow

1. Record the baseline and concrete property to improve; if correctness is not established, repair or report that blocker first.
2. Search local and imported APIs when an existing result may remove complexity.
3. Apply one coherent change at a time.
4. Re-run the baseline verification scope; for performance work, rerun the same measurement.
5. Reject regressions in correctness, trust, diagnostics, or maintainability unless the user requested the tradeoff.

Stop when remaining opportunities are marginal, speculative, or out of scope. Correctness and maintainability outrank token or line count.
