---
name: lean4-optimize
description: "Use after a Lean 4/mathlib proof is already correct when the task is a durable local improvement in clarity, maintainability, robustness, brevity where that helps clarity, or measured performance."
license: MIT
---

# Lean 4 Optimize

## Purpose

Improve an already-correct Lean proof without trading away correctness, trust, or maintainability.

## Preconditions

Establish a clean verified baseline for the target first. If the proof is not correct yet, do not optimize an unverified baseline. If the request also includes repair, establish correctness before measuring or claiming an optimization; otherwise report the missing baseline as the blocker.

Do not introduce new axioms, `sorry`, or `admit`, and do not change the public theorem statement merely to make optimization easier.

## Choose one optimization surface

- **Strategy simplification:** replace an indirect proof with a more direct mathematical/library argument or extract a genuinely useful helper. Load [proof strategy simplification](references/proof-simplification.md).
- **Local simplification:** remove ceremony or redundant steps when the result becomes clearer and at least as stable. Shorter source is not automatically better. Load [simp and simp-lemma design](references/simplification.md) when global simp policy, rewrite orientation, or simproc design is material.
- **Performance:** localize and measure elaboration/build cost before changing code. Load [performance guidance](references/performance.md).

Do not combine all three by default.

## Contract

1. Record the verified baseline and the concrete property to improve. The baseline gate must match the correctness scope the task intends to preserve.
2. Search local code and active imports before widening to mathlib when an existing direct theorem may remove complexity; validate candidate declarations in the actual project context.
3. Apply one coherent change at a time.
4. Re-run the same semantic verification gate after each change; for performance work, rerun the same measurement as well. If an optimization changes an imported source and the baseline was only file-local, strengthen the check to the dependency or repository integration scope before claiming correctness was preserved.
5. Reject changes that regress correctness, diagnostics, trust, or maintainability without a compensating requested benefit.
6. Stop when remaining opportunities are marginal, speculative, or outside the requested surface.

Library search, abstraction comparison, local diagnostics, and small experiments may all be used to choose and verify an improvement. Correctness and maintainability outrank token or line count.
