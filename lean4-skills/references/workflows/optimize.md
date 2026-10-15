# Proof Optimization Workflow

Use only after correctness is established and the user wants a clearer, more maintainable, shorter, or faster proof. Preserve statements, signatures, and existing docstrings.

Choose the smallest optimization surface that matches the request:

- **Strategy simplification:** replace an indirect proof with a more direct mathematical/library argument or extract a genuinely useful helper. Load `../proof-simplification.md`.
- **Golf:** simplify an already-correct proof locally without redesigning surrounding API. Load `../proof-golfing.md`.
- **Performance:** diagnose elaboration/build cost before changing code. Load `../performance-optimization.md` and, when measurement is needed, `../profiling-workflows.md`.

Do not combine all three by default.

## Contract

1. Establish a clean verified baseline for the target.
2. Identify a concrete improvement; do not optimize merely because a transformation is imaginable.
3. Apply one coherent change at a time.
4. Re-verify after each change and reject changes that regress diagnostics, trust, or maintainability without a compensating benefit.
5. Stop when remaining opportunities are marginal, speculative, or outside the requested optimization surface.

Correctness and maintainability outrank token or line count.
