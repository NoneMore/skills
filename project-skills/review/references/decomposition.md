# Decomposition review

Evaluate whether the breakdown covers the intended work in independently actionable pieces with truthful dependencies.

Look for missing scope, slices that cannot be verified or delivered meaningfully on their own, artificial layer-by-layer tickets where an end-to-end slice is possible, false dependencies that serialize work unnecessarily, and hidden integration work that has no owning item.

Mechanical refactors and migrations may legitimately require ordered or cross-cutting steps. Do not force vertical slicing when affected subsets cannot remain valid independently.

A decomposition can be review-complete without rewriting the ticket set; findings should identify the structural issue and its consequence.
