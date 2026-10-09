---
name: specify
description: Turn sufficiently settled intent into a durable specification that can guide implementation or verification. Use when the user explicitly wants a spec, requirements contract, or persistent implementation-facing statement of intent.
disable-model-invocation: true
---

# Specify

## Purpose

Produce a durable contract for sufficiently settled intent.

## Accepts

Conversation decisions, an issue or request, an existing design, project context, or any combination that is concrete enough to specify without inventing material product or design choices.

## Owns

- the problem or outcome being addressed;
- intended observable behavior and scope;
- material settled decisions that constrain implementation;
- non-goals or boundaries whose omission would create material scope ambiguity;
- acceptance conditions that can distinguish a satisfying result from a non-satisfying one;
- explicit material unresolved questions when the source material is not yet decision-complete.

If a material product or design choice remains unresolved, do not silently resolve it as part of specification. Preserve it as an unresolved decision unless the user explicitly delegates resolution of the choice; if delegated, explicitly resolve and record it before presenting the result as implementation-ready.

## Existing contracts

When relevant semantics already have an established durable owner, identify that source from authoritative project evidence and revise it rather than creating parallel contract truth. Do not infer authority from artifact type or mere existence.

When no owner is established and choosing a durable location is part of the delegated outcome, use the project's existing conventions and the smallest durable granularity that remains usable for downstream implementation and verification. Do not introduce a specification hierarchy or standalone artifact merely for uniformity.

For revisions, distinguish the current contract from the proposed change, preserve settled semantics outside the requested change, and fold a persisted result into current truth. Keep material ownership conflicts explicit rather than silently choosing among conflicting artifacts.

## Persistence

A specification is valuable because it preserves a contract. When the user requests persistence, use the requested destination or an established project source of truth when one clearly applies. If persistence requires establishing a new source and choosing that source is delegated, use the placement guidance below. Otherwise do not invent a new persistence convention merely to make the spec durable.

If the user has not requested a persistent project mutation, return the complete specification in conversation.

## Specialized guidance

- Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.
- Use [contract-placement.md](references/contract-placement.md) when a durable contract location or granularity is not already established.
- Use [contract-maintenance.md](references/contract-maintenance.md) when revising, reconciling, or normalizing an existing durable project contract.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.

When persisted, the selected authoritative source should directly describe the resulting current contract without leaving an accidental parallel current-state specification behind.
