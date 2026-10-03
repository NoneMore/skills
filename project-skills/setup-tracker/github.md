# GitHub Issues backend

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a workflow uses that relation.

## Membership and representation

Any issue with a `tracker:status:*` label participates in the tracker. A valid tracked issue has exactly one `tracker:status:*` label and it is supported, and exactly one `tracker:type:*` label and it is supported.

| Model field | GitHub representation |
| --- | --- |
| Type | `tracker:type:investigation` or `tracker:type:change` |
| Status | one of the supported `tracker:status:*` labels |
| Sources | reserved `Sources:` body line (`Sources: None` when empty) |
| Parent | native sub-issue relation |
| BlockedBy | native issue dependency |

Required tracker labels:

- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`, `tracker:status:cancelled`

Legacy or otherwise unsupported `tracker:status:*` or `tracker:type:*` labels make a participating issue invalid rather than adding another state or type.

GitHub open/closed state may mirror terminal status for usability but is not canonical tracker state.

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
