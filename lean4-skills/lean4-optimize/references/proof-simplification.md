# Proof Strategy Simplification

Use when an already-correct proof is structurally more complicated than the mathematical or library argument needs to be.

## Highest-leverage questions

1. Does mathlib already provide the result or a more general theorem?
2. Is the proof manually unfolding a definition that has an API theorem?
3. Is a large case split really expressing equality/congruence with a simpler function or structure?
4. Is repeated bookkeeping hiding a reusable mathematical helper?
5. Is a manual equality of morphisms/functions better expressed by an extensionality theorem?
6. Is the chosen representation fighting the library's canonical abstraction?

Search existing APIs by the goal's mathematical shape before constructing local helpers or representation conversions. Prefer a direct library result when it removes substantial proof machinery.

## Helper extraction

Extract a helper for meaningful reuse or a verification boundary, not merely because a block is long. Recurring representation mismatches may justify a small bridge lemma when it removes repeated conversion work; keep one-off core reasoning inline when extraction only adds parameters and navigation. Prefer the weakest assumptions justified by actual use, keep proof-specific helpers private, and expose public helpers only for stable caller-facing contracts.

## Congruence and extensionality

Before manual pointwise or case reasoning, search for `congr`, `EqOn`, `EventuallyEq`, or `ext`-style theorems appropriate to the structure. They often preserve the intended abstraction and reduce definitional bookkeeping.

Use the parent `lean4-optimize` skill for baseline, verification, and stopping behavior. For measured elaboration/build cost, follow [performance guidance](performance.md).
