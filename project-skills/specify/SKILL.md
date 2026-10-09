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

## Persistence

A specification is valuable because it preserves a contract. Do not infer a project's authoritative contract source from artifact type, proximity, or repository evidence alone.

When the user requests persistence, use one of these explicitly chosen paths:

- update an existing durable source designated by the user; or
- when the user chooses to establish or normalize specification persistence, use the unified specification shape described in [spec-shape.md](references/spec-shape.md) at a destination designated by the user.

Do not create a new contract source, choose among competing existing sources, or introduce a persistence convention unless the user has chosen that path. If the user has not designated an existing source or chosen a destination for the unified specification shape, return the complete specification in conversation and make the missing persistence decision explicit.

For revisions, distinguish the current contract from the proposed change, preserve settled semantics outside the requested change, and when persistence is authorized fold the resulting semantics into the designated current contract rather than leaving an accidental parallel current-state specification.

## Specialized guidance

- Use [spec-shape.md](references/spec-shape.md) as the unified specification shape when that persistence path is chosen, and as a starting structure when useful otherwise; it is not a mandatory template.
- Use [contract-placement.md](references/contract-placement.md) when persistence requires the user's explicit source-or-destination choice.
- Use [contract-maintenance.md](references/contract-maintenance.md) when revising an existing user-designated durable contract source.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.

When persisted, the designated source should directly describe the resulting current contract without leaving an accidental parallel current-state specification behind.
