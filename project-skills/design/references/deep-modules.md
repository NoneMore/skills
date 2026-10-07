# Deep modules and seams

Use this vocabulary when interface shape, test seams, or architectural locality are central to the design.

- **Module**: anything with an interface and an implementation, from a function to a package or tier-spanning slice.
- **Interface**: everything callers must know to use the module correctly, including invariants, errors, ordering, configuration, and material performance characteristics.
- **Implementation**: behavior hidden behind the interface.
- **Seam**: a place where behavior can vary without editing the caller at that point.
- **Adapter**: a concrete implementation filling a role at a seam.
- **Depth**: leverage provided by the interface: substantial useful behavior behind comparatively little caller-facing knowledge.
- **Leverage**: capability callers gain per unit of interface they must learn.
- **Locality**: how well related change, knowledge, bugs, and verification stay concentrated instead of spreading across callers.

## Heuristics

Prefer modules whose interfaces hide meaningful complexity rather than merely forwarding it. Use the deletion test: if deleting the module would scatter its complexity across callers, it is probably earning its place; if the complexity simply disappears, the module may be shallow indirection.

Treat the public interface as the preferred behavioral test surface. Internal seams can exist for implementation needs, but do not expose them merely to make tests convenient.

Do not introduce an abstraction solely because variation is imaginable. A seam earns its cost when real variation, isolation, or boundary control materially benefits the system.

When the design space is genuinely open, compare materially different interfaces rather than polishing the first plausible shape.
