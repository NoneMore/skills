---
name: lean4-optimize
description: "Use only after a Lean 4/mathlib proof is already correct and the requested outcome is to make it clearer, shorter where that improves clarity, more maintainable, more robust, or measurably faster. Do not use as the primary workflow for a currently failing proof or for open-ended exploration without a requested durable improvement."
license: MIT
---

# Lean 4 Optimize

## Purpose

Improve an already-correct Lean proof without trading away correctness, trust, or maintainability.

## Preconditions

Establish a clean verified baseline for the target first. If correctness is not established, use `lean4-prove` or `lean4-diagnose` instead.

Do not introduce new axioms, `sorry`, or `admit`, and do not change the public theorem statement merely to make optimization easier.

## Choose one optimization surface

- **Strategy simplification:** replace an indirect proof with a more direct mathematical/library argument or extract a genuinely useful helper. Load [proof strategy simplification](references/proof-simplification.md).
- **Local simplification:** remove ceremony or redundant steps when the result becomes clearer and at least as stable. Shorter source is not automatically better. Load [simp and simp-lemma design](references/simplification.md) when global simp policy, rewrite orientation, or simproc design is material.
- **Performance:** localize and measure elaboration/build cost before changing code. Load [performance guidance](references/performance.md).

Do not combine all three by default.

## Contract

1. Record the verified baseline and the concrete property to improve.
2. Search local code and active imports before widening to mathlib when an existing direct theorem may remove complexity; validate candidate declarations in the actual project context.
3. Apply one coherent change at a time.
4. Re-run the same semantic verification gate after each change; for performance work, rerun the same measurement as well. Load [verification guidance](../references/verification.md) when dependency or project integration scope matters.
5. Reject changes that regress correctness, diagnostics, trust, or maintainability without a compensating requested benefit.
6. Stop when remaining opportunities are marginal, speculative, or outside the requested surface.

Library search, abstraction comparison, and small experiments needed to choose an improvement remain part of optimization when the requested outcome is a durable improvement to an already-correct proof.

Correctness and maintainability outrank token or line count.
