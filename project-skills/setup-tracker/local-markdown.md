# Local Markdown backend

## Storage

Any `.tracker/issues/<ID>.md` file with a positive integer ID participates in the tracker. New issues normally use one greater than the greatest existing ID; on collision choose another unused ID.

## Representation

A valid tracked issue has this header:

```markdown
# <title>

Type: <investigation|change>
Status: <ready|waiting|done|cancelled>
Sources: <ID, URL, reference|None>
Parent: <ID|None>
Blocked-By: <ID, ID|None>
```

A valid tracked issue contains:

```markdown
## Completion condition
<checkable condition>
```

A valid `waiting` issue also contains:

```markdown
## Waiting
Waiting for: <event or decision>
Resume when: <checkable condition>
```
