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
- a clear distinction between settled decisions and genuinely open design questions.

The default result is the decisions and remaining material uncertainty in conversation. Persist only knowledge whose durability is part of the value, such as an existing domain glossary or a current architectural decision that future work should know.

## Specialized guidance

Load only what materially helps the current design problem:

- [domain-modeling.md](references/domain-modeling.md) for domain language, `CONTEXT.md`, and ADR discipline;
- [deep-modules.md](references/deep-modules.md) for module/interface/seam vocabulary and deep-module design;
- [deepening.md](references/deepening.md) when restructuring shallow module clusters;
- [design-it-twice.md](references/design-it-twice.md) when materially different interface alternatives are worth comparing;
- [decision-maps.md](references/decision-maps.md) when a large decision space benefits from a compact durable index;
- [context-format.md](references/context-format.md) and [adr-format.md](references/adr-format.md) only when those project artifacts are actually being written.

Research, code reading, experiments, spikes, prototypes, and interactive pressure-testing are techniques available to design; none is a required stage.

## Done when

The material choices needed for the requested design outcome are explicit and mutually coherent, and any remaining uncertainty is clearly bounded enough that it is not being silently passed downstream as an accidental design decision.

## Does not require

A tracker item, a prototype, a grilling session, an ADR, a domain glossary, or any prescribed next capability.
