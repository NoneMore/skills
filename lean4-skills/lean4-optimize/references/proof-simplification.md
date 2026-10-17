# Proof Strategy Simplification

Use when an already-correct proof is structurally more complicated than the mathematical or library argument needs to be.

## Highest-leverage questions

1. Does mathlib already provide the result or a more general theorem?
2. Is the proof manually unfolding a definition that has an API theorem?
3. Is a large case split really expressing equality/congruence with a simpler function or structure?
4. Is repeated bookkeeping hiding a reusable mathematical helper?
5. Is a manual equality of morphisms/functions better expressed by an extensionality theorem?
6. Is the chosen representation fighting the library's canonical abstraction?

Search before extracting helpers: replacing a long local argument with an existing theorem is usually better than formalizing the long argument into another local API.

## Helper extraction

Extract a helper when it creates a meaningful reusable or verification boundary. Prefer the weakest assumptions justified by actual use, keep proof-specific helpers private, and avoid generalizing solely for abstraction's sake.

A helper is not valuable just because a block is long. Keep arguments inline when the block is a one-off expression of the core mathematical reasoning and extraction would merely add parameters and navigation.

## Congruence and extensionality

Before manual pointwise or case reasoning, search for `congr`, `EqOn`, `EventuallyEq`, or `ext`-style theorems appropriate to the structure. They often preserve the intended abstraction and reduce definitional bookkeeping.

Use the parent `lean4-optimize` skill for baseline, verification, and stopping behavior. For measured elaboration/build cost, follow [performance guidance](performance.md).
