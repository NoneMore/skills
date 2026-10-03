# Local Markdown backend

## Storage

Store tracked issues as `.tracker/issues/<ID>.md` using positive integer IDs. New issues normally use one greater than the greatest existing ID; on collision choose another unused ID.

## Representation

A tracked issue has this header:

```markdown
# <title>

Type: <investigation|change>
Status: <ready|waiting|done|cancelled>
Sources: <ID, URL, reference|None>
Parent: <ID|None>
Blocked-By: <ID, ID|None>
```

A tracked issue contains:

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
