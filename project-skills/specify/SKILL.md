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

When the project already has a durable contract for the relevant semantics, identify the artifact that owns those semantics from repository instructions, architecture guides, established documentation structure, or other authoritative project evidence before drafting a replacement.

Do not invent a global precedence between documentation, tests, code, ADRs, tracker items, examples, or research artifacts. Determine their roles from the project's established conventions. If ownership is materially ambiguous or conflicting, make that ambiguity explicit rather than silently choosing a source of truth.

When revising an existing contract, distinguish the current contract from the proposed change, preserve settled semantics outside the requested change, and express the change as a delta when that makes review clearer. When persistence is requested, fold the accepted result into the established authoritative contract rather than creating a parallel current-state store.

Keep normative behavior and durable decisions distinct from current implementation details, migration progress, historical explanation, and supporting evidence when mixing those roles would make future changes ambiguous.

Artifacts may provide requirements, evidence, rationale, implementation, or proposed changes depending on project convention. Do not promote an artifact into contract authority merely because it exists.

## Persistence

A specification is valuable because it preserves a contract. When the user requests persistence, use the requested destination or an established project source of truth when one clearly applies. If the user has not requested a persistent project mutation, return the complete specification in conversation. Do not invent a new persistence convention merely to make the spec durable.

## Specialized guidance

- Use [spec-shape.md](references/spec-shape.md) as a starting structure when useful, not as a mandatory template.
- Use [contract-maintenance.md](references/contract-maintenance.md) when revising, reconciling, or normalizing an existing durable project contract.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.

When persistence of an existing contract change is part of the requested outcome, the established source of truth should describe the resulting current contract without leaving an accidental parallel current-state specification behind.
