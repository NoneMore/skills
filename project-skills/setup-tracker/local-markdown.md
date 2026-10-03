# Local Markdown backend

Local Markdown representation for the issue model.

## Storage

Store tracked issues as `.tracker/issues/<ID>.md` using positive integer IDs. New issues normally use one greater than the greatest existing ID. Never overwrite an existing issue file; on collision choose another unused ID.

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
Origin: <source-ref|Unknown|None>
```

`intake` requires `Type: None`; `managed` requires one managed-work type. Every tracked issue stores one allowed status.

## Body

Preserve intake wording/evidence and discussion, for example under `## Intake` and `## Discussion`.

Managed work contains:

```markdown
## Completion condition
<checkable condition>
```

Any tracked issue with status `waiting` also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```

Preserve unrelated header fields and body sections when updating an issue.

Before changing `Parent` or `Blocked-By`, enforce the issue model's endpoint and cycle rules. `Sources` may reference existing intake or managed work but must not self-reference.

Assignment, claiming, and execution ownership are not part of this format.
