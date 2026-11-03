---
name: lean4-mathlib-contribute
description: "User-invoked mode to assess or adapt an existing Lean 4 artifact for upstream mathlib contribution readiness using current policy and nearby current code."
disable-model-invocation: true
license: MIT
---

# Lean 4 Mathlib Contribute

## Workflow

1. Start from a concrete artifact and establish whether the user wants findings or adaptation.
2. Retrieve current authoritative contribution guidance from the official source map below; if it cannot be retrieved, state that policy compliance remains unverified.
3. Inspect nearby current mathlib code where API shape, generality, placement, naming/docs, imports, attributes, proof robustness, duplication, or maintenance cost could affect readiness.
4. If adaptation is requested, make the smallest evidence-backed changes that address substantiated gaps without weakening the accepted trust basis. Review-only requests remain read-only.
5. Run the repository-configured gate for the affected scope and re-check criteria materially changed by the edits.

## Finding current upstream guidance

Start with the live **Lean 4** contribution sources, not remembered policy or Lean 3 documentation:

- [Contribution scope](https://leanprover-community.github.io/contribute/index.html)
- [Contribution and PR workflow](https://leanprover-community.github.io/contribute/how-to-contribute.html)
- [Library style guide](https://leanprover-community.github.io/contribute/style.html)
- [Naming conventions](https://leanprover-community.github.io/contribute/naming.html)
- [Documentation standards](https://leanprover-community.github.io/contribute/doc.html)
- [Current mathlib4 repository](https://github.com/leanprover-community/mathlib4)

Read the contribution guidance and PR workflow for each upstream-readiness assessment; consult style, naming, and documentation pages where relevant to the artifact. Follow links from the official contribution index or mathlib4 repository if pages have moved. Then compare the artifact with nearby mathlib4 code and repository-configured checks at the relevant revision; code examples alone do not establish current policy. Do not silently substitute cached guidance or Lean 3 pages.

In the findings, identify the official URLs actually consulted, relevant neighboring files, verification performed, and any inaccessible guidance. If policy cannot be retrieved, report that limitation rather than claiming full upstream readiness.

## Completion

Claim upstream readiness only when applicable current policy was consulted, relevant nearby code was inspected, required verification passed, and no known material blocker remains. Otherwise return the strongest verified result and remaining readiness uncertainty.
