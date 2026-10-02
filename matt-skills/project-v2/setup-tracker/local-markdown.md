# Local Markdown backend

Local Markdown is the degraded fallback for repositories that do not have a usable GitHub Issues surface.

It mirrors the GitHub semantic model rather than defining a second model.

## Storage

Store all issues under:

```text
.tracker/issues/
```

Use one file per issue:

```text
.tracker/issues/<NNNN>-<slug>.md
```

Assign the next monotonically increasing four-digit number by scanning existing files. The number is the local issue identity.

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

`Type: None` means the issue is intake/unmanaged.

Managed work has exactly one of:

- `investigation`
- `change`

Do not mutate an external/intake issue into managed work. Create a separate managed issue and reference the intake issue in `Sources`.

### Status

Use the canonical statuses from `ISSUE-MODEL.md`.

There is no separate local tracker-state field. `done` and `cancelled` are terminal; every other status is non-terminal.

### Sources

`Sources` contains direct local issue numbers only. Record direct provenance, never its transitive closure.

### Hierarchy and dependencies

`Parent` is decomposition.

`Blocked-By` is scheduling dependency.

They are independent from each other and from Sources.

### Claim

`Assignee` mirrors GitHub assignee. Setting it claims the issue; clearing it releases the claim.

Do not add an execution-state field.

## Operations

### Create

Create the next numbered file with complete metadata. Managed work must have a type; intake uses `Type: None`.

### Read

Read the whole file, including discussion/evidence.

### List/search

Scan `.tracker/issues/*.md` and parse the header fields.

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
