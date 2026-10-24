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

Identify the work and constraints in the available context, then break it down at a useful granularity. Prefer independently verifiable end-to-end slices where feasible. For migrations, mechanical changes, or other work that cannot safely be split into independent slices, represent the real ordering and cross-cutting work.

Treat dependencies as execution constraints, not ordering preferences. Respect settled product and design decisions; do not invent material scope, behavior, design choices, or acceptance requirements to complete a breakdown. Where unresolved decisions prevent reliable decomposition, identify the blocked work and decompose only work that does not predetermine those decisions, rather than constructing a speculative investigation plan.

## Result

Present the breakdown as work items or ordered steps, with meaningful deliverables, real dependencies, and verifiable completion signals where they matter. Do not require tickets, phases, owners, estimates, or a fixed template.

Use [tracer-bullets.md](references/tracer-bullets.md) when work-item boundaries or dependency edges need specialized guidance.

Publish to a tracker only when requested and authorized, following the project's existing conventions.

## Done when

The requested work is accounted for as far as it can be reliably decomposed, actionable units have clear deliverables and completion signals, dependencies represent real constraints, and blocked work is not presented as ready.
