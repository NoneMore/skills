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

## Managed-work body

Managed issues must contain:

```markdown
## Completion condition

<issue-specific, checkable completion condition>
```

Add `## Context` only when context beyond the title, sources, and linked relations is needed to define or execute the work.

Skills that create or execute managed work may append structured sections they own, for example `## Execution notes`, `## Implementation result`, `## Conclusion`, or `## Evidence`. Preserve all unrelated sections when updating an owned section.

Do not copy type, status, sources, hierarchy, dependencies, or assignee into ordinary body sections. `Sources:` is the reserved provenance line and remains the canonical GitHub body representation for direct sources.

## Intake templates

Public GitHub issue templates are intake aids only. They must not ask reporters to choose managed-work type, completion condition, hierarchy, dependencies, claim, or internal lifecycle state.

Keep existing useful intake forms. When a common intake surface is missing, setup may install the corresponding default issue form shipped with this skill. Keep blank issues enabled so valid external intake is not rejected merely because it does not fit a form.

Issues created through any form or as a blank issue remain untyped external intake. Repository taxonomy labels applied by forms remain independent from tracker type and status.

## Setup

Create missing tracker type and status labels. Preserve unrelated labels.

Preserve repository-owned issue templates. Add a shipped intake form only when the repository lacks a suitable form for that entry point, and never overwrite a different existing template. Ensure `.github/ISSUE_TEMPLATE/config.yml` has `blank_issues_enabled: true`; preserve all other existing chooser configuration.

## Operations

When creating managed work, set exactly one managed-work type and a status allowed by the semantic contract, write the required managed-work body, and preserve any Skill-owned extension sections supplied by the creating workflow. Intake has no managed-work type.

When changing status, replace the existing `status:*` label and keep GitHub open/closed state consistent with terminal status.

When changing Sources, preserve the rest of the issue body.

Use native operations for hierarchy and dependencies, and assignee operations for claim.

When a skill updates an extension section, change only the section it owns and preserve the completion condition and all unrelated content.

After a mutation, re-read the fields and body sections that were changed and verify the intended values persisted.
