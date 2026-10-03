# GitHub Issues backend

## Requirements

Setup requires GitHub Issues and label read/write access. Native sub-issue or dependency capability is required only when a workflow uses that relation.

## Representation

| Model field | GitHub representation |
| --- | --- |
| Kind | repository-defined taxonomy, such as an existing label or native issue type; optional and not setup-managed |
| Type | `tracker:type:investigation`, `tracker:type:change`, or no type label while unclassified |
| Status | one allowed `tracker:status:*` label |
| Sources | reserved `Sources:` body line (`Sources: None` when empty) |
| Parent | native sub-issue relation |
| BlockedBy | native issue dependency |

Required tracker labels:

- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:needs-triage`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`

GitHub open/closed state may mirror status for usability but is not canonical tracker state.

A native GitHub Issue does not need tracker labels merely because it is external input. It may remain untracked, be triaged in place, or be referenced as a source by tracked work. Setup does not create or prescribe repository Kind labels.

## Body

Every tracked issue contains:

```markdown
Sources: <#101, owner/repo#117, https://example.com/source|None>
```

A source reference may identify another tracked issue or durable external/native provenance. Referencing a GitHub Issue or URL does not make that source a tracked issue.

Whenever `Type` is set, the issue also contains:

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
