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
- **Local simplification:** remove ceremony or redundant steps when the result becomes clearer and at least as stable. Shorter source is not automatically better.
- **Performance:** localize and measure elaboration/build cost before changing code. Load [performance guidance](../references/performance-optimization.md).

Do not combine all three by default. For simplifier-specific work, load [`simp` guidance](../references/simp-reference.md).

## Contract

1. Record the verified baseline and the concrete property to improve.
2. Search local code/mathlib when an existing direct theorem may remove complexity; use [mathlib search guidance](../references/mathlib-guide.md) when useful.
3. Apply one coherent change at a time.
4. Re-run the same semantic verification gate after each change; for performance work, rerun the same measurement as well. Use [verification guidance](../references/verification.md) when scope matters.
5. Reject changes that regress correctness, diagnostics, trust, or maintainability without a compensating requested benefit.
6. Stop when remaining opportunities are marginal, speculative, or outside the requested surface.

If choosing the improvement requires substantial open-ended reconnaissance across abstractions, APIs, generalizations, or alternatives, `lean4-explore` may support that investigation; this skill still owns the durable change to an already-correct proof.

Correctness and maintainability outrank token or line count.
