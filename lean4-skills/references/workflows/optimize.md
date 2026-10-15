# Proof Optimization Workflow

Use only after correctness is established and the user wants a clearer, more maintainable, shorter, or faster proof. Preserve statements, signatures, and existing docstrings.

Choose the smallest optimization surface that matches the request:

- **Strategy simplification:** replace an indirect proof with a more direct mathematical/library argument or extract a genuinely useful helper. Load `../proof-simplification.md`.
- **Local simplification:** shorten or clarify an already-correct proof without redesigning surrounding API. Prefer direct terms and exact discovered lemmas over ceremony or broad automation when that improves clarity and stability; shorter source is not automatically better.
- **Performance:** diagnose elaboration/build cost before changing code. Load `../performance-optimization.md`.

Do not combine all three by default.

## Contract

1. Establish a clean verified baseline for the target.
2. Identify a concrete improvement; do not optimize merely because a transformation is imaginable.
3. Apply one coherent change at a time.
4. Re-verify after each change and reject changes that regress diagnostics, trust, or maintainability without a compensating benefit.
5. Stop when remaining opportunities are marginal, speculative, or outside the requested optimization surface.

For local simplification, low-risk examples include removing redundant `by exact`, replacing unnecessary `simpa` with `exact`, eta-reducing when types make equivalence clear, or shrinking an explicit `simp only [...]` set when verification/lint evidence shows entries are unused. Do not inline named intermediate facts that carry mathematical meaning or create harder-to-read nested terms.

Correctness and maintainability outrank token or line count.
