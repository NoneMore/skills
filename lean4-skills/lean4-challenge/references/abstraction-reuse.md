# Mathematical abstraction and reuse

Use when work within one proof or across declarations might express the same mathematics, not merely similar tactic syntax.

- Compare hypotheses, constructions, conclusions, and the underlying invariant at representative sites; include repetition inside one proof.
- Search existing local/mathlib theorems, including plausible earlier modules under different notation.
- Compare reusing an existing theorem, a local/private helper, a public theorem, and **no extraction**.
- In scratch Lean, test the proposed helper at its intended use; for cross-declaration reuse, test a meaningfully different consumer when it could change the choice.
- Weigh unnatural parameters, strengthened hypotheses, coercions, inference cost, dependency direction, and new API surface against reduced mathematical duplication.
