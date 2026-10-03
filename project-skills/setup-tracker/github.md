# GitHub Issues backend

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a workflow uses that relation.

## Representation

A GitHub issue is tracked when it has exactly one supported `tracker:type:*` label and exactly one supported `tracker:status:*` label.

| Model field | GitHub representation |
| --- | --- |
| Type | `tracker:type:investigation` or `tracker:type:change` |
| Status | `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`, or `tracker:status:cancelled` |
| Sources | reserved `Sources:` body line (`Sources: None` when empty) |
| Parent | native sub-issue relation |
| BlockedBy | native issue dependency |

Required tracker labels:

- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`, `tracker:status:cancelled`

GitHub open/closed state may mirror terminal status for usability but is not canonical tracker state.

## Body

A tracked issue contains:

```markdown
Sources: <#101, owner/repo#117, https://example.com/source|None>

## Completion condition
<checkable condition>
```

A `waiting` issue also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```
