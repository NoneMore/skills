# Proof Golfing

Use for local simplification of an already-correct proof. Golfing does not change theorem statements, public API, or the mathematical strategy of surrounding code.

## Evaluation order

For every candidate, require correctness first, then prefer:

1. more direct proof structure;
2. less hidden inference/search burden;
3. better determinism or elaboration behavior;
4. clearer local expression;
5. fewer tokens/lines.

Shorter is not automatically better.

## Common low-risk opportunities

After verification, consider transformations such as:

- `by exact t` -> `t` when the surrounding elaboration context is genuinely equivalent;
- unnecessary `simpa` -> `exact` when no simplification is doing work;
- eta-reduction `fun x => f x` -> `f` when types make the equivalence clear;
- a simple `apply ...; exact ...` chain -> a direct term;
- replacing broad automation with the exact discovered lemma when that is clearer and more stable;
- removing unused arguments from an explicit `simp only [...]` set when Lean/lint evidence shows they are unused.

Do not mechanically inline named intermediate facts that carry mathematical meaning, are reused, or would create a deeply nested term.

## Boundary with strategy refactoring

If a better result requires a different mathematical approach, a new reusable helper, changed imports across several files, or API redesign, hand the work to strategy simplification rather than calling it golf.

## Verification

Apply one coherent transformation at a time and re-run the lightest gate that can detect regression. Reject the candidate if it introduces diagnostics, worsens trust, relies on fragile inference without a compensating benefit, or makes the proof materially harder to understand.

Stop when remaining changes are cosmetic or debatable.
