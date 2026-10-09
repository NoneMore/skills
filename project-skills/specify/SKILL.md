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

When the user requests persistence, use one of these paths:

- update a contract source explicitly designated by the user as authoritative for the relevant scope, or unambiguously identified by the project's established contract-management convention; or
- when the user chooses to establish or normalize specification persistence, use the unified specification shape described in [spec-shape.md](references/spec-shape.md) at a destination designated by the user.

A path or filename alone designates a destination, not an authoritative contract role. A user designation is sufficient when it explicitly assigns the source that role for the relevant scope. Treat a project convention as established only when maintained project authority or an enforced or maintained index/manifest explicitly assigns the relevant contract role or lifecycle; filenames, proximity, content similarity, implementation, tests, or history alone are not sufficient.

Do not create a new contract source, choose among competing existing sources, or introduce a persistence convention unless the user has chosen that path. Repository evidence may establish that a source participates in an existing contract-management convention and may identify the uniquely applicable source under that convention; it does not by itself promote an arbitrary artifact into a contract source or authorize choosing among ambiguous candidates. If no contract source can be resolved or has been explicitly designated, and the user has not chosen a destination for the unified specification shape, return the complete specification in conversation and make the missing persistence decision explicit.

For revisions, distinguish the current contract from the proposed change, preserve settled semantics outside the requested change, and when persistence is authorized follow the selected contract source's established lifecycle when one exists so the resulting current contract remains unambiguous rather than leaving an accidental competing current-state specification.

## Specialized guidance

- Use [spec-shape.md](references/spec-shape.md) as the unified specification shape when that persistence path is chosen, and as a starting structure when useful otherwise; it is not a mandatory template.
- Use [contract-placement.md](references/contract-placement.md) when persistence requires resolving a contract source or choosing a new destination.
- Use [contract-maintenance.md](references/contract-maintenance.md) when revising a selected contract source.

## Done when

The durable spec is clear enough that downstream work can act and verify against it without silently inventing material choices. If that condition cannot be met, the spec may still capture settled material, but it must clearly identify the unresolved decisions that block a reliable contract.

When persisted, the selected contract role or project's contract-management convention should identify the resulting current contract without an accidental competing current-state specification.
