# GitHub Issues backend

GitHub representation for the issue model.

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a workflow uses that relation.

## Representation

| Model field | GitHub representation |
| --- | --- |
| Kind | `tracker:kind:intake` or `tracker:kind:managed` |
| Type | `tracker:type:investigation` or `tracker:type:change` on managed work only |
| Status | one allowed `tracker:status:*` label |
| Sources | reserved `Sources:` body line (`Sources: None` when empty) |
| Parent | native sub-issue relation |
| BlockedBy | native issue dependency |

Canonical tracker labels are:

- `tracker:kind:intake`, `tracker:kind:managed`
- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:needs-triage`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`

An issue without a tracker kind label is outside the tracker. Ordinary repository labels remain independent. GitHub open/closed state may mirror status for usability but is not canonical tracker state.

## Body

Managed work contains:

```markdown
Sources: <#101, #117|None>

## Completion condition
<checkable condition>
```

Any tracked issue with status `waiting` also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```

Preserve unrelated body content. Intake keeps the reporter's original issue content and discussion; accepted intake may source separate managed work.

Before adding native relations, enforce the issue model's endpoint and cycle rules. If the active tooling cannot perform a required relation operation, that workflow stops; initial tracker setup still succeeds.

Assignees are ordinary GitHub metadata, not tracker lifecycle or claim state. Setup never classifies existing unclassified issues.
