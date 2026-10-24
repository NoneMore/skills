# Module and interface design

Use for module/interface boundaries, shallow module clusters, or material interface alternatives. Apply the relevant heuristics without treating every subsection as mandatory.

## Concepts and evaluation

- **Module**: anything with an interface and an implementation, from a function to a package or tier-spanning slice.
- **Interface**: everything callers must know to use the module correctly, including invariants, errors, ordering, configuration, and material performance characteristics.
- **Implementation**: behavior hidden behind the interface.
- **Seam**: a place where behavior can vary without editing the caller at that point.
- **Adapter**: a concrete implementation filling a role at a seam.
- **Depth**: leverage provided by the interface: substantial useful behavior behind comparatively little caller-facing knowledge.
- **Leverage**: capability callers gain per unit of interface they must learn.
- **Locality**: how well related change, knowledge, bugs, and verification stay concentrated instead of spreading across callers.

### Module depth and locality

Prefer modules that hide meaningful complexity. If removing a module would scatter complexity across callers, it likely earns its place; if the complexity disappears, it may be shallow indirection.

Treat the public interface as the preferred behavioral test surface. Internal seams can exist for implementation needs, but do not expose them merely to make tests convenient.

Do not introduce an abstraction solely because variation is imaginable. A seam earns its cost when real variation, isolation, or boundary control materially benefits the system.

## Deepening shallow module clusters

### Classify dependencies before choosing a seam

Different dependencies justify different designs:

- **In-process computation or memory** can often remain fully inside the deepened module with no adapter.
- **Local substitutable infrastructure** such as a test database or in-memory filesystem may stay behind an internal seam when a realistic local stand-in already exists.
- **Owned remote services** can justify a port when transport genuinely varies or isolation at that boundary materially improves the design.
- **True external services** often need a narrow injected boundary so production and test behavior can be controlled without leaking vendor details through the module's public interface.

Do not introduce a port merely because a dependency exists. The seam should pay for itself through real variation, isolation, or locality.

### Design a meaningful verification boundary

When a deepened interface becomes the meaningful behavioral boundary, make clear which behaviors can be verified through it and where lower-level verification still protects distinct guarantees. Do not prescribe test deletion merely because the module boundary changed.

A successful deepening should reduce caller knowledge and concentrate related change, not merely add another abstraction layer around the same scattered complexity.

## Comparing alternatives

Compare alternatives when the first plausible interface risks premature commitment. Skip exploration when the choice is constrained or cheap to reverse.

### Frame the design problem

Make the shared constraints explicit before comparing alternatives: caller needs, invariants, dependency boundaries, operational constraints, compatibility requirements, and important domain language. The alternatives should solve the same problem rather than quietly changing the requirements.

### Generate genuinely different alternatives

Vary a meaningful design dimension rather than cosmetically renaming one proposal:

- smallest possible caller-facing interface;
- strongest optimization for the common path;
- flexibility for known real variation;
- a different seam placement or ownership boundary.

For each alternative, capture the interface callers must understand, a representative usage example, what complexity it hides, dependency handling, and the main tradeoffs.

### Compare on consequences

Compare alternatives using the constraints that matter to this design: depth/leverage, locality of future change, seam placement, error and invariant handling, migration cost, operational consequences, and testability through meaningful behavior.

Prefer a recommendation over an unranked menu when the evidence supports one. A hybrid is useful only when it preserves the strengths that made the source alternatives distinct rather than accumulating both interfaces.
