# Local Markdown backend

Representation and operations for tracker v2. Semantics live in [ISSUE-MODEL.md](ISSUE-MODEL.md).

## Storage

Store issues as:

```text
.tracker/issues/<NNNN>-<slug>.md
```

Use the next monotonically increasing four-digit number.

Before setup, every existing `.tracker/issues/*.md` file must already match the v2 header below. Otherwise stop without modifying the tracker; migration is out of scope.

## Header

```markdown
# <title>

Type: <investigation|change|None>
Status: <canonical status>
Sources: <NNNN, NNNN|None>
Parent: <NNNN|None>
Blocked-By: <NNNN, NNNN|None>
Assignee: <actor|None>
```

`Type: None` represents intake. Other field meanings and allowed statuses come from `ISSUE-MODEL.md`.

## Operations

Create new issues with the complete header.

Read the whole file. For list/search, parse the required header fields; do not guess missing values.

When mutating, change only the relevant header field or body section and preserve unrelated content. Re-read the changed fields afterward.

Set `Status: done` or `Status: cancelled` for terminal issues.

## Frontier

Executable frontier work is:

- `Type: investigation|change`;
- `Status: ready`;
- `Assignee: None`;
- with every `Blocked-By` issue terminal.

Frontier is derived, not stored.
