---
name: design
description: Resolve material software, system, domain, or interface design choices into a coherent direction. Use when the user explicitly wants design or architecture decisions, tradeoff resolution, domain modeling, interface design, or architectural improvement.
disable-model-invocation: true
---

# Design

## Purpose

Resolve material design choices into a coherent direction sufficiently clear for the user's requested outcome.

## Accepts

A design question, an architecture or domain problem, an interface or seam decision, or an existing codebase area whose structure needs improvement.

## Owns

- explicit material design decisions rather than silent delegation to later implementation;
- coherence between the chosen direction and the constraints that motivated it;
- a clear distinction between settled decisions and genuinely open design questions;
- decision-changing factual uncertainty is investigated when proportionate or kept explicit rather than silently assumed;
- intentionally deferred material choices name what blocks them and, when knowable, what would make them decidable.

## Approach

Frame the material design question and constraints. Identify choices about structure, concepts, interfaces, boundaries, or behavior. Compare consequential alternatives against relevant tradeoffs, and pressure-test the direction with scenarios, edge cases, or evidence when useful.

Adapt the depth and techniques to the problem rather than following mandatory stages.

## Result

Present the design in conversation. Make the chosen direction concrete through whichever responsibilities, concepts, interfaces, interactions, and invariants matter to the problem. Explain the rationale for non-obvious choices and distinguish settled decisions from material open questions.

Keep detail decision-centered: elaborate interfaces, behaviors, invariants, and scenarios only as far as needed to resolve or communicate material design choices. Stop when the direction is coherent; specification completeness is not a design completion criterion.

Use diagrams, examples, or interface sketches when they clarify the design. Do not substitute an implementation plan or task-level acceptance contract for the design.

## Specialized guidance

Consult the short reference for each plausibly material concern rather than silently assuming it away. Related lenses are grouped to reduce missed considerations; loading a reference does not require adopting every mechanism it describes.

- [module-design.md](references/module-design.md) for module depth, interface and seam design, restructuring shallow modules, and comparison of alternatives;
- [system-semantics.md](references/system-semantics.md) for failure behavior, cross-boundary state correctness, operational interfaces, and trust or authority boundaries;
- [compatibility-and-migration.md](references/compatibility-and-migration.md) when existing callers, data, or deployments constrain the target design.

Use code reading, research, experiments, or prototypes when they help settle material choices.

## Done when

The material choices needed for the requested design outcome are explicit and mutually coherent, and any remaining uncertainty is clearly bounded enough that it is not being silently passed downstream as an accidental design decision.
