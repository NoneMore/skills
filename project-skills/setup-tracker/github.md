# GitHub Issues backend

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

Required tracker labels:

- `tracker:kind:intake`, `tracker:kind:managed`
- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:needs-triage`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`

GitHub open/closed state may mirror status for usability but is not canonical tracker state.

## Body

Every tracked issue contains:

```markdown
Sources: <#101, #117|None>
```

Managed work also contains:

```markdown
## Completion condition
<checkable condition>
```

A `waiting` issue also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```
