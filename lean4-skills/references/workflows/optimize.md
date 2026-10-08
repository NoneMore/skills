# Proof Optimization Workflow

Use after correctness is established when the user wants a clearer, more maintainable, shorter, or faster proof. Preserve statements, signatures, and existing docstrings.

## Choose the optimization level

- **Strategy refactor:** find a more direct mathematical/library approach, replace manual arguments with existing lemmas, or extract genuinely reusable helpers. Load `../proof-simplification.md` and `../proof-refactoring.md`.
- **Golf:** simplify already-correct proof terms/tactics without redesigning the surrounding API. Load `../proof-golfing.md` and, only when needed, `../proof-golfing-patterns.md`.
- **Performance:** diagnose elaboration/build cost before changing code. Load `../performance-optimization.md` and `../profiling-workflows.md`.

Do not combine all three by default.

## Contract

1. Establish a clean baseline for the target.
2. Identify a concrete improvement opportunity; do not optimize merely because a transform is imaginable.
3. Apply one coherent change at a time.
4. Re-verify after each change and reject transformations that regress diagnostics or materially reduce readability without compensating benefit.
5. Stop when remaining opportunities are marginal or speculative.

Correctness and maintainability outrank token count. A shorter proof that is more inference-heavy, brittle, or opaque is not automatically better.