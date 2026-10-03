# Local Markdown backend

Local Markdown representation for the tracker. The issue model owns semantics.

## Storage

Store tracked issues as:

```text
.tracker/issues/<ID>.md
```

Use positive integer IDs. New issues normally use one greater than the greatest existing ID. Never overwrite an existing issue file; if creation collides, choose another unused ID and retry.

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

`Kind: intake` requires `Type: None`. `Kind: managed` requires exactly one managed-work type. Every tracked issue stores one status allowed for its kind.

For intake, preserve the original reporter and source when known. Managed work may use `Reporter: None` and `Origin: None`.

## Intake body

Preserve the original intake content and discussion rather than rewriting it as managed work. A simple representation is:

```markdown
## Intake

<original wording and evidence>

## Discussion

<speaker-attributed discussion>
```

## Managed issue body

Managed issues contain:

```markdown
## Completion condition

<issue-specific, checkable completion condition>
```

When status is `waiting`, also record:

```markdown
## Waiting

Waiting for: <external event or decision>

Resume when: <checkable condition>
```

Additional workflow-owned sections are allowed. Preserve unrelated header fields and body sections when updating an issue.

## Relations

Before changing `Parent` or `Blocked-By`, verify the endpoint and cycle rules in the issue model. `Sources` may reference intake or managed work but must reference existing tracked issues and must not self-reference.

Assignment, claiming, and execution ownership are intentionally not part of this file format.
