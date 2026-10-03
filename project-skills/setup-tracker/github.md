# GitHub Issues backend

GitHub representation for the tracker. `ISSUE-MODEL.md` owns semantics.

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a downstream workflow actually uses the corresponding relation.

## Representation

- **Kind:** exactly one of `tracker:kind:intake` or `tracker:kind:managed`.
- **Type:** managed work has exactly one of `tracker:type:investigation` or `tracker:type:change`; intake has neither.
- **Status:** exactly one allowed `tracker:status:*` label for the issue kind.
- **Sources:** one reserved `Sources:` line in the issue body; use `Sources: None` when empty.
- **Hierarchy:** native sub-issues.
- **Dependencies:** native issue dependencies.

Canonical status labels are:

- `tracker:status:needs-triage`
- `tracker:status:ready`
- `tracker:status:waiting`
- `tracker:status:done`

An issue without a tracker kind label is outside the tracker. Repository labels such as `bug`, `enhancement`, or `documentation` remain independent.

GitHub open/closed state is not the canonical tracker status. Workflows may keep it aligned for usability, for example closing `done` issues.

## Managed issue body

Managed issues contain:

```markdown
Sources: <#101, #117|None>

## Completion condition

<issue-specific, checkable completion condition>
```

When status is `waiting`, also record:

```markdown
## Waiting

Waiting for: <external event or decision>

Resume when: <checkable condition>
```

Additional workflow-owned sections are allowed. Preserve unrelated body content when updating tracker fields or workflow-owned sections.

## Intake

Intake keeps the reporter's original issue content and discussion. A workflow that accepts intake may create separate managed work and record the intake issue in `Sources`.

Setup never classifies existing unclassified issues. A downstream workflow may classify a specific unclassified issue only when that workflow explicitly chooses to triage or adopt it.

## Relations

Before adding a parent or dependency relation, verify the semantic endpoint and cycle rules from `ISSUE-MODEL.md`.

If the active GitHub tooling cannot perform a relation operation, the workflow that needs that relation must stop or ask the user for another representation. Missing relation tooling does not make initial tracker setup fail.

GitHub assignees are ordinary repository metadata under this contract; they are not tracker lifecycle or claim state.
