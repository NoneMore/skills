# GitHub Issues backend

Representation and operations for the tracker. The issue model owns semantics.

## Capability requirement

Use this backend only when GitHub Issues are enabled and the available tooling/API can read and write issues, labels, assignees, native sub-issues, and native issue dependencies.

If native sub-issues or dependencies cannot be read and written, use Local Markdown. Do not encode those relations in issue text.

## Representation

- **Type:** exactly one of `type:investigation` or `type:change` for managed work; neither for intake.
- **Status:** exactly one of `status:needs-triage`, `status:needs-info`, `status:ready`, `status:waiting`, `status:done`, or `status:cancelled`, subject to the semantic contract.
- **Sources:** one reserved body line, for example `Sources: #101, #117`; use `Sources: None` when empty.
- **Hierarchy:** native sub-issues.
- **Dependencies:** native issue dependencies.
- **Claim:** GitHub assignee.

Terminal statuses use GitHub closed state. Other statuses use open state.

Repository labels such as `bug`, `enhancement`, or `documentation` remain independent.

## Setup

Create missing tracker type and status labels. Preserve unrelated labels.

## Operations

When creating managed work, set exactly one managed-work type and a status allowed by the semantic contract. Intake has no managed-work type.

When changing status, replace the existing `status:*` label and keep GitHub open/closed state consistent with terminal status.

When changing Sources, preserve the rest of the issue body.

Use native operations for hierarchy and dependencies, and assignee operations for claim.

After a mutation, re-read the fields that were changed and verify the intended values persisted.
