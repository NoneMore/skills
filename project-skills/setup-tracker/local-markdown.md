# Local Markdown backend

## Storage

Store tracked issues as `.tracker/issues/<ID>.md` using positive integer IDs. New issues normally use one greater than the greatest existing ID; on collision choose another unused ID.

`.tracker/issues/` contains tracked work, not mirrored copies of external intake. External reports, messages, documents, or other durable inputs should normally remain at their source and be referenced through `Sources` when they motivate tracked work.

## Header

```markdown
# <title>

Kind: <repository-defined category|None>
Type: <investigation|change|None>
Status: <needs-triage|ready|waiting|done>
Sources: <ID, URL, reference|None>
Parent: <ID|None>
Blocked-By: <ID, ID|None>
```

`Kind` is optional repository/project taxonomy. `Type: None` is allowed while work is not yet classified; `ready` requires a typed issue. Source references may identify another local tracked issue or durable external provenance, and do not create a tracked copy of that source.

## Body

Whenever `Type` is set, the issue contains:

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
