---
name: decompose
description: Split sufficiently concrete work into independently actionable pieces with explicit real dependencies and verification boundaries. Use when the user explicitly wants tickets, work items, implementation slices, or a dependency-aware breakdown.
disable-model-invocation: true
---

# Decompose

## Purpose

Turn concrete work into a set of actionable pieces whose boundaries and dependencies make execution easier rather than merely restating implementation layers.

## Accepts

A specification, plan, issue, conversation, design, or other sufficiently concrete body of work.

## Owns

- coverage of the intended work across the resulting items;
- slices that each deliver or verify a coherent result when the work permits it;
- explicit dependencies only where one item truly must precede another;
- acceptance information sufficient to tell when each item is complete;
- visible integration or sequencing work rather than hidden coordination assumptions.

Prefer narrow end-to-end tracer bullets when they can land and be verified independently. Do not force that shape onto mechanical refactors, migrations, or other work whose affected subsets cannot remain valid independently.

Use [tracer-bullets.md](references/tracer-bullets.md) when slice boundaries or dependency edges need deeper guidance.

Publishing the breakdown to a tracker is an optional integration step when the user asks for it and an appropriate tracker is available; the decomposition itself does not depend on a suite-specific work-item role or state machine.

## Done when

The requested scope is accounted for, each item has a clear deliverable and completion signal, dependencies represent real execution constraints, and no material work is left implicit between items.

## Does not require

A prior spec, a particular tracker backend, user approval rounds, a `ready-for-agent` state, or a prescribed implementation workflow.
