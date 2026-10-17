---
name: lean4-mathlib-contribute
description: "User-invoked mode for assessing or adapting an existing Lean 4 artifact specifically for upstream mathlib contribution readiness using current contribution policy, nearby mathlib conventions, API and generality fit, naming/docs/import discipline, proof robustness, attributes, and integration evidence."
disable-model-invocation: true
license: MIT
---

# Lean 4 Mathlib Contribute

Assess or adapt an existing Lean artifact for upstream mathlib readiness using current policy, nearby current code, and verification appropriate to the affected scope.

## Contract

- Start from a concrete artifact: declaration, proof, file, diff, or PR-sized change.
- Treat contribution policy as live external state; consult current authoritative guidance at execution time.
- Inspect nearby current mathlib code when API shape, placement, naming, imports, attributes, or proof style affect the decision.
- Review-only requests are read-only. Adaptation may change API shape or generality only when explicitly requested and justified by an upstream-readiness finding.

## Workflow

1. Establish the artifact, intended upstream neighborhood when known, and whether the user wants findings or adaptation.
2. Retrieve the current contribution guidance relevant to the artifact. If it cannot be consulted, state that policy compliance remains unverified.
3. Compare the artifact with nearby current code on material concerns: canonical API, generality and hypotheses, namespace and placement, naming/docs, imports, attributes/simp behavior, proof robustness, duplication, and maintenance cost.
4. If adaptation is requested, make the smallest coherent changes that address substantiated gaps without weakening the accepted trust basis.
5. Run the repository-configured gate for the affected scope and re-check any policy or nearby-code criterion materially changed by the edits.

## Completion

Claim upstream readiness only when applicable current policy was consulted, relevant nearby code was inspected, required verification passed, and no known material blocker remains. Otherwise return the strongest verified result and the remaining readiness uncertainty.
