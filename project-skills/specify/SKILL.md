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

## Existing specifications

When modifying an existing specification, update the source designated by the user or the uniquely identifiable relevant specification. If multiple plausible sources conflict or it is materially ambiguous which specification should be changed, do not guess or modify them; surface the ambiguity. Apply the requested semantic change while preserving settled semantics outside its scope.

When organizing existing specifications, improve structure, consolidate duplication where the meaning is equivalent, and make conflicts or ambiguity explicit. Do not silently resolve conflicting requirements or change settled semantics merely to make the result cleaner.

Do not introduce new repository structure, lifecycle, or specification governance unless the user explicitly asks for it.

## Persistence

When the user requests persistence for a new specification, use the requested destination or an established project destination when one clearly applies. If the user has not requested a persistent project mutation, return the complete specification in conversation. Do not invent a new persistence convention merely to make the specification durable.

## Specialized guidance

- Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.
- Use [contract-maintenance.md](references/contract-maintenance.md) when modifying or organizing existing specifications.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.

For existing specifications, completion also requires changing the intended source without silently changing unrelated settled semantics; organization must preserve meaning and expose unresolved conflicts rather than deciding them implicitly.
