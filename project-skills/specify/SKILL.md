---
name: specify
description: Turn sufficiently settled intent into a precise, task-scoped implementation and verification contract. Use when the user explicitly wants a specification, requirements contract, or task-specific acceptance criteria.
disable-model-invocation: true
---

# Specify

## Purpose

Turn sufficiently settled intent into a precise contract for the work at hand, so implementation and verification do not need to invent material choices.

## Accepts

Conversation decisions, an issue or request, an existing design, project context, or any combination that is concrete enough to specify without inventing material product or design choices.

## Owns

- the specific problem or outcome being addressed;
- intended observable behavior and scope at the level the task needs;
- material settled decisions that constrain this implementation, without duplicating the broader design;
- non-goals or boundaries whose omission would create material scope ambiguity;
- acceptance conditions that distinguish a satisfying result from a non-satisfying one;
- explicit material unresolved questions when the source material is not yet decision-complete.

Specify makes settled intent actionable for a bounded piece of work; it does not own the long-term evolution of design. Treat established design and project decisions as constraints. If a material product or design choice remains unresolved, do not silently resolve it as part of specification. Keep it explicit unless the user delegates that choice; if delegated, resolve and record it before presenting the result as implementation-ready.

## Contract stability

Treat a settled specification as a stable reference while its task is implemented and verified, not as an immutable document. When new evidence or a changed request requires a material revision, make the change and its impact on implementation or acceptance explicit. Do not silently shift the contract to match an implementation after the fact.

## Lifecycle and placement

Follow an applicable project convention for specification authority, placement, change, and retention. Inspect relevant project instructions and natural sources of truth when needed to establish whether one applies; do not infer authority merely from recency, naming, or location, and do not silently resolve materially conflicting sources.

Where no applicable project convention exists, default to a task-local working specification rather than a separately maintained, long-lived project document. Return it in conversation or, when appropriate and authorized, the existing task context. Do not create a new repository-wide specification lifecycle, storage convention, approval process, or archival machinery. After the work is implemented and verified, the specification need not remain an active source of truth; ordinary issue, pull request, and version-control history may remain.

An explicit user request to persist or retain a specification can override that default. Use the requested destination or an established project mechanism without treating that one-off choice as a new general rule. Keep material contract changes reviewable where the specification is maintained.

Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.

## Done when

The specification is precise enough for the current work to be implemented and verified without silently inventing material choices. If that is not yet possible, capture the settled scope and explicitly identify the decisions that still block a reliable contract.
