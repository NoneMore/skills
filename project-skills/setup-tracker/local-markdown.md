# Local Markdown backend

## Storage

Store tracked issues as `.tracker/issues/<ID>.md` using positive integer IDs. New issues normally use one greater than the greatest existing ID; on collision choose another unused ID.

## Header

```markdown
# <title>

Kind: <intake|managed>
Type: <investigation|change|None>
Status: <allowed status>
Sources: <ID, ID|None>
Parent: <ID|None>
Blocked-By: <ID, ID|None>
Reporter: <actor|Unknown|None>
```

`intake` uses `Type: None`; `managed` uses one managed-work type. `Reporter` is the original intake reporter when known, `Unknown` when it cannot be established, and `None` for managed work.

## Body

Preserve intake wording, evidence, and discussion, for example under `## Intake` and `## Discussion`.

Managed work contains:

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
