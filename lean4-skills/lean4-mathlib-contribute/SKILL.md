---
name: lean4-mathlib-contribute
description: "User-invoked mode to assess or adapt an existing Lean 4 artifact for upstream mathlib contribution readiness using current policy and nearby current code."
disable-model-invocation: true
license: MIT
---

# Lean 4 Mathlib Contribute

## Workflow

1. Start from a concrete artifact and establish whether the user wants findings or adaptation.
2. Consult current authoritative contribution guidance; if it cannot be retrieved, state that policy compliance remains unverified.
3. Inspect nearby current mathlib code where API shape, generality, placement, naming/docs, imports, attributes, proof robustness, duplication, or maintenance cost could affect readiness.
4. If adaptation is requested, make the smallest evidence-backed changes that address substantiated gaps without weakening the accepted trust basis. Review-only requests remain read-only.
5. Run the repository-configured gate for the affected scope and re-check criteria materially changed by the edits.

## Completion

Claim upstream readiness only when applicable current policy was consulted, relevant nearby code was inspected, required verification passed, and no known material blocker remains. Otherwise return the strongest verified result and remaining readiness uncertainty.
