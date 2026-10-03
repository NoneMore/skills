# Local Markdown backend

Representation and operations for the tracker. The issue model owns semantics.

## Storage

Store issues as:

```text
.tracker/issues/<NNNN>-<slug>.md
```

Use the next monotonically increasing four-digit number.

Before setup, every existing `.tracker/issues/*.md` file must already match the header below. Otherwise stop without modifying the tracker; migration is out of scope.

## Header

```markdown
# <title>

Type: <investigation|change|None>
Status: <canonical status>
Sources: <NNNN, NNNN|None>
Parent: <NNNN|None>
Blocked-By: <NNNN, NNNN|None>
Assignee: <actor|None>
Reporter: <actor|Unknown|None>
Origin: <source-ref|Unknown|None>
```

`Type: None` represents intake. Other field meanings and allowed statuses come from the semantic contract.

For intake, `Reporter` preserves the original reporter identity and `Origin` preserves the source reference when one exists. Use `Unknown` when intake provenance is unavailable. `None` means the field is not applicable and is valid only for managed work.

## Intake body

Preserve intake content after the header as:

```markdown
## Intake

<original wording and evidence>

## Discussion

<speaker-attributed discussion>
```

Do not paraphrase or replace the original intake wording or evidence. Preserve existing discussion entries and append new discussion with speaker attribution.

Managed work does not require these body sections.

## Operations

Create new issues with the complete header.

When creating intake, record `Reporter` and `Origin`, preserve the original wording and evidence under `## Intake`, and preserve discussion under `## Discussion`.

Read the whole file. For list/search, parse the required header fields; do not guess missing values.

When mutating, change only the relevant header field or body section and preserve unrelated content. Re-read the changed fields afterward.

Set `Status: done` or `Status: cancelled` for terminal issues.
