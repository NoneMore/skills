---
name: decompose
description: Break engineering work into actionable units with truthful dependencies and verifiable completion boundaries. Use when the user explicitly wants work items, implementation slices, or dependency-aware breakdowns.
disable-model-invocation: true
---

# Decompose

## Purpose

Break down engineering work into actionable units whose boundaries and dependencies make execution easier.

## Accepts

A user-supplied request, issue, specification, design, existing plan, or other engineering work.

## Owns

- coverage of the work being broken down;
- coherent, actionable units with meaningful deliverables;
- real dependencies and opportunities for independent execution;
- necessary integration and sequencing work;
- completion signals grounded in established outcomes and constraints.

## Approach

Break down the requested work at a useful granularity. Prefer independently verifiable end-to-end slices where feasible; preserve real ordering and cross-cutting work when independent slicing is unsafe, as in migrations or mechanical changes.

Use only real prerequisites as dependency edges. Respect settled product and design decisions; do not invent material scope, behavior, design choices, or acceptance requirements. Where unresolved decisions block reliable decomposition, identify the affected work and decompose only what does not predetermine them.

## Result

Present work items or ordered steps in a form appropriate to the request, without imposing a mandatory task schema.

Use [tracer-bullets.md](references/tracer-bullets.md) when work-item boundaries or dependency edges need specialized guidance.

Publish to a tracker only when requested and authorized, following the project's existing conventions.

## Done when

The requested work is accounted for as far as it can be reliably decomposed, actionable units have clear deliverables and completion signals, dependencies represent real constraints, and blocked work is not presented as ready.
