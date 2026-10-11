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

A specification is valuable because it preserves a contract. When the user requests persistence, use the requested destination or an established project source of truth when one clearly applies. If the user has not requested a persistent project mutation, return the complete specification in conversation. Do not invent a new persistence convention merely to make the spec durable.

Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.

## Contract integrity

When persisting a specification, follow an established project source of truth and specification lifecycle when one clearly applies. Do not treat governance as absent merely because it is not already present in context; inspect the accessible project instructions and natural sources of truth needed to determine whether one applies.

If no clearly applicable governance can be established and the specification is intended to become a durable project contract, use [governance-bootstrap.md](references/governance-bootstrap.md) to surface only the minimum governance decisions that require resolution. Do not choose bootstrap answers on the user's behalf: require explicit user resolution before treating any new governance choice as authoritative. Do not bootstrap governance for a conversation-only specification, when existing project mechanisms already provide the needed properties, or by mutating project state beyond the user's authorized scope.

When changing an existing contract, keep material semantic deltas reviewable. Do not silently choose between materially conflicting sources, present materially unsettled requirements as settled, or infer authority from recency, naming, or location unless the project's governance makes that property authoritative. Preserve references when they are needed to establish authority, understand a material constraint, or explain a material change.

These are contract-integrity constraints, not a repository workflow. Do not invent directory layouts, numbering schemes, approval stages, archival structures, mandatory artifact types, or specification-specific states unless a concrete contract-integrity failure requires them and existing project mechanisms are insufficient.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.
