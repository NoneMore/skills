# GitHub Issues backend

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a workflow uses that relation.

## Membership and representation

Any issue with a `tracker:status:*` label participates in the tracker. A valid tracked issue has exactly one supported status label and exactly one type label.

| Model field | GitHub representation |
| --- | --- |
| Type | `tracker:type:investigation` or `tracker:type:change` |
| Status | one of the supported `tracker:status:*` labels |
| Sources | reserved `Sources:` body line (`Sources: None` when empty) |
| Parent | native sub-issue relation |
| BlockedBy | native issue dependency |

Required tracker labels:

- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`

GitHub open/closed state may mirror status for usability but is not canonical tracker state.

## Body

A valid tracked issue contains:

```markdown
Sources: <#101, owner/repo#117, https://example.com/source|None>

## Completion condition
<checkable condition>
```

A valid `waiting` issue also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```
