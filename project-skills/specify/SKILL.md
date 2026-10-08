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

A specification is valuable because it persists a contract. Persist it to the user's requested destination or an established project source of truth when one clearly applies. If neither applies, return the complete specification without inventing a new persistence convention.

Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.
