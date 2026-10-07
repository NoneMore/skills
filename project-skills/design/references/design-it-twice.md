# Design it twice

Use this technique when the first plausible interface may anchor the design too early and materially different alternatives could change the result. It is optional; do not pay the exploration cost when the choice is already constrained or cheap to reverse.

Use the vocabulary in [deep-modules.md](deep-modules.md), and [deepening.md](deepening.md) when the problem is specifically about consolidating shallow modules.

## Frame the design problem

Make the shared constraints explicit before comparing alternatives: caller needs, invariants, dependency boundaries, operational constraints, compatibility requirements, and important domain language. The alternatives should solve the same problem rather than quietly changing the requirements.

## Generate genuinely different alternatives

If parallel agents are available and the comparison is worth the cost, they can explore alternatives independently. Otherwise generate them sequentially. Vary a meaningful design dimension rather than producing cosmetic renames, for example:

- smallest possible caller-facing interface;
- strongest optimization for the common path;
- flexibility for known real variation;
- a different seam placement or ownership boundary.

For each alternative, capture the interface callers must understand, a representative usage example, what complexity it hides, dependency handling, and the main tradeoffs.

## Compare on consequences

Compare alternatives using the constraints that matter to this design: depth/leverage, locality of future change, seam placement, error and invariant handling, migration cost, operational consequences, and testability through meaningful behavior.

Prefer a recommendation over an unranked menu when the evidence supports one. A hybrid is useful only when it preserves the strengths that made the source alternatives distinct rather than accumulating both interfaces.
