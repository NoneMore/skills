---
name: design
description: Resolve material software, system, domain, or interface design choices into a coherent direction. Use when the user explicitly wants design or architecture decisions, tradeoff resolution, domain modeling, interface design, or architectural improvement.
disable-model-invocation: true
---

# Design

## Purpose

Resolve material design choices into a direction that is sufficiently clear for the user's requested outcome.

## Accepts

A design question, an architecture or domain problem, an interface or seam decision, or an existing codebase area whose structure needs improvement.

## Owns

- explicit material design decisions rather than silent delegation to later implementation;
- coherence between the chosen direction and the constraints that motivated it;
- a clear distinction between settled decisions and genuinely open design questions;
- decision-changing factual uncertainty is investigated when proportionate or kept explicit rather than silently assumed;
- intentionally deferred material choices name what blocks them and, when knowable, what would make them decidable.

The default result is the decisions and remaining material uncertainty in conversation. Persist a design artifact only when the user requests one or durability is part of the requested outcome through an established project convention. When persisting, retain only knowledge whose future value justifies the artifact, such as shared domain language or a current architectural decision that later work should know.

## Specialized guidance

Load only what materially helps the current design problem:

- [domain-modeling.md](references/domain-modeling.md) for domain language and durable architectural knowledge;
- [deep-modules.md](references/deep-modules.md) for module/interface/seam vocabulary and deep-module design;
- [deepening.md](references/deepening.md) when restructuring shallow module clusters;
- [design-it-twice.md](references/design-it-twice.md) when materially different interface alternatives are worth comparing;
- [reliability.md](references/reliability.md) when failure behavior, recovery, availability, or degradation can change the design;
- [distributed-state.md](references/distributed-state.md) when state ownership, consistency, ordering, or reconciliation crosses a process or asynchronous boundary;
- [compatibility-and-migration.md](references/compatibility-and-migration.md) when existing callers, data, or deployments constrain how a target design can be reached;
- [operability.md](references/operability.md) when diagnosis, repair, or operational control materially affects the architecture;
- [security-boundaries.md](references/security-boundaries.md) when trust, authority, isolation, or data exposure materially affects the design;
- [decision-maps.md](references/decision-maps.md) when a large decision space benefits from a compact durable index.

Research, code reading, experiments, spikes, prototypes, and interactive pressure-testing are techniques available to design; none is a required stage.

## Done when

The material choices needed for the requested design outcome are explicit and mutually coherent, and any remaining uncertainty is clearly bounded enough that it is not being silently passed downstream as an accidental design decision.
