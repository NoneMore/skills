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

## Governance

Follow established project specification governance when it exists. Explicit user direction takes precedence over the fallback rules below.

When no applicable governance exists, preserve contract integrity using these minimal rules:

- Separate authority from change. Treat an established authoritative specification as the current contract. Material modifications to that contract are proposed changes until they are explicitly accepted through an established project process or by the user.
- Specify behavior before implementation. Specifications describe observable behavior, interfaces, constraints, and acceptance conditions. Keep incidental implementation detail outside the contract unless that implementation constraint is itself a settled requirement.
- Make contract changes explicit. When changing an existing specification, identify what is added, modified, removed, or renamed when doing so materially improves reviewability. Do not make reviewers infer semantic changes from a rewritten document.
- Do not infer authority from recency. A newer file, timestamp, or proposal does not automatically supersede an existing authoritative specification. Supersession or promotion must be explicit.
- Do not silently reconcile conflicts. When authoritative material or concurrent proposed changes conflict, preserve the conflict as an unresolved material decision unless the user explicitly delegates its resolution.
- Preserve useful provenance. Keep references to authoritative issues, designs, decisions, or prior specifications when they are needed to understand why the contract exists or changed.

These are semantic fallback rules, not a repository workflow. Do not invent directory layouts, numbering schemes, approval stages, archival structures, or mandatory artifact types unless the project already defines them or the user explicitly asks to establish them.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.
