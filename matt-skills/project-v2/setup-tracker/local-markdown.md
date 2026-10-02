# Local Markdown backend

Local Markdown is the degraded fallback when no GitHub repository satisfies the complete tracker-v2 capability set.

Tracker semantics are defined only in [ISSUE-MODEL.md](ISSUE-MODEL.md). This file defines Local Markdown representation and operations.

## Storage

Store all issues under:

```text
.tracker/issues/
```

Use one file per issue:

```text
.tracker/issues/<NNNN>-<slug>.md
```

Assign the next monotonically increasing four-digit number by scanning existing conforming files. The number is the local issue identity.

### Existing files

Before configuring Local Markdown, inspect every existing `.tracker/issues/*.md` file.

Each file must already match the tracker-v2 header contract below. If any file does not match, stop without modifying the tracker. Do not reinterpret or migrate legacy files; migration is outside this prototype.

## Representation

Each file begins with:

```markdown
# <title>

Type: <investigation|change|None>
Status: <canonical status>
Sources: <NNNN, NNNN|None>
Parent: <NNNN|None>
Blocked-By: <NNNN, NNNN|None>
Assignee: <actor|None>
```

Then follows the issue body and append-only discussion/evidence sections as needed.

### Type

Use:

- `Type: None` for external intake;
- `Type: investigation` or `Type: change` for managed work.

### Status

Use exactly one canonical status from `ISSUE-MODEL.md`, respecting whether that status applies to intake or managed work.

There is no separate local tracker-state field. `done` and `cancelled` are terminal; every other status is non-terminal.

### Sources

Store direct local issue numbers only:

```text
Sources: 0001, 0007
```

Use `Sources: None` when empty.

### Hierarchy

Store the direct parent only:

```text
Parent: 0004
```

Use `Parent: None` when there is no parent.

### Dependencies

Store direct blockers:

```text
Blocked-By: 0002, 0009
```

Use `Blocked-By: None` when there are no blockers.

### Claim

Store the active assignee in `Assignee`. Use `Assignee: None` when unclaimed.

## Operations

### Create

Create the next numbered file with the complete header. Choose type and status according to `ISSUE-MODEL.md`.

### Read

Read the whole file, including discussion/evidence.

### List/search

Scan `.tracker/issues/*.md` and parse the required header fields. Treat a malformed header as tracker corruption; do not silently guess missing values.

### Mutate

Rewrite only the relevant header field or body section. Preserve unrelated content.

After mutation, re-read the file and verify the intended value persisted.

### Close

Set `Status: done` or `Status: cancelled`. Reopening means changing to an appropriate non-terminal status.

### Frontier

Executable frontier is derived by scanning for:

- `Type: investigation|change`;
- `Status: ready`;
- `Assignee: None`;
- every `Blocked-By` issue terminal.

No frontier flag is stored.
