---
name: design
description: Resolve material software, system, domain, or interface design choices into a coherent direction. Use when the user explicitly wants design or architecture decisions, tradeoff resolution, domain modeling, interface design, or architectural improvement.
disable-model-invocation: true
---

# Design

## Purpose

Resolve material design choices into a coherent, evolvable direction for the user's requested outcome.

## Accepts

A design question, an architecture or domain problem, an interface or seam decision, or an existing codebase area whose structure needs improvement.

## Owns

- explicit material design decisions rather than silent delegation to later implementation;
- coherence between the chosen direction and the constraints that motivated it;
- a clear distinction between settled decisions and genuinely open design questions;
- decision-changing factual uncertainty is investigated when proportionate or kept explicit rather than silently assumed;
- intentionally deferred material choices name what blocks them and, when knowable, what would make them decidable.

Design primarily addresses choices whose consequences extend beyond a single implementation task. Keep the result at the level needed to explain material structure, constraints, and tradeoffs; do not turn it into a task-specific implementation checklist or acceptance contract. Revisit decisions when constraints or evidence change, and keep shared design knowledge coherent with the revised direction.

The default result is the decisions and remaining material uncertainty in conversation. Persist a design artifact only when the user requests one or durability is part of the requested outcome through an established project convention. When persisting, retain only knowledge whose future value justifies the artifact, such as shared domain language or a current architectural decision that later work should know. Update its authoritative home when the decision evolves rather than maintaining competing current versions.

## Specialized guidance

Load guidance for each concern that could materially change the design. The references group related lenses to make them easier to discover; loading a lens does not make its mechanisms mandatory. When a concern is plausibly material, prefer consulting the short relevant reference over silently assuming it away.

- [module-design.md](references/module-design.md) for module depth, interface and seam design, restructuring shallow modules, and comparison of alternatives;
- [system-semantics.md](references/system-semantics.md) for failure behavior, cross-boundary state correctness, operational interfaces, and trust or authority boundaries;
- [compatibility-and-migration.md](references/compatibility-and-migration.md) when existing callers, data, or deployments constrain the target design.

Research, code reading, experiments, spikes, prototypes, and interactive pressure-testing are techniques available to design; none is a required stage.

## Done when

The material choices needed for the requested design outcome are explicit and mutually coherent, and any remaining uncertainty is clearly bounded enough that it is not being silently passed downstream as an accidental design decision.
