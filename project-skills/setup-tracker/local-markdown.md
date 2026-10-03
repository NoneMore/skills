# Local Markdown backend

Representation and operations for the tracker. The issue model owns semantics.

<!-- repository-contract:start -->

## Storage

Store issues as:

```text
.tracker/issues/<NNNN>-<slug>.md
```

Use the next monotonically increasing four-digit number. Create the path with a create-only operation that must fail rather than overwrite when the candidate path already exists. On collision, rescan and retry with the next available number. If the active runtime cannot provide create-only semantics, concurrent issue creation must be serialized by the caller.

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

For managed work, `Assignee` is the execution claim and must contain at most one actor. For intake, `Assignee` is not a tracker claim; leave it `None` unless a repository-specific workflow uses it as unrelated ownership metadata.

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

## Managed-work body

Managed issues must contain:

```markdown
## Completion condition

<issue-specific, checkable completion condition>
```

When managed work is `waiting`, it must also contain exactly one active waiting section:

```markdown
## Waiting

Waiting for: <external event or human decision>

Resume when: <checkable condition>
```

Remove the active `## Waiting` section before moving managed work out of `waiting`; preserve relevant historical information in a Skill-owned notes or result section when needed.

Add `## Context` only when context beyond the title, Sources, Parent, and Blocked-By fields is needed to define or execute the work.

Skills that create or execute managed work may append structured sections they own, for example:

```markdown
## Execution notes

...

## Implementation result

...

## Conclusion

...

## Evidence

...
```

These section names are examples, not a required global set. A skill may define the sections appropriate to its workflow. When updating an owned section, preserve the completion condition and all unrelated sections.

Do not duplicate header metadata in body sections.

## Operations

Create new issues with the complete header using the create-only collision protocol in the Storage section.

When creating intake, record `Reporter` and `Origin`, preserve the original wording and evidence under `## Intake`, and preserve discussion under `## Discussion`.

When creating managed work, set `Reporter: None` and `Origin: None`, write the required completion condition, and preserve any Skill-owned extension sections supplied by the creating workflow.

Read the whole file. For list/search, parse the required header fields; do not guess missing values.

Before adding or changing `Parent` or `Blocked-By`, verify that every referenced issue exists, every endpoint is managed work, and the resulting hierarchy or dependency graph would remain acyclic. `Sources` may reference intake or managed work but must reference existing issues and must not self-reference.

To acquire a managed-work claim, first verify that the issue is on the executable frontier and `Assignee: None`, then set `Assignee` to the current actor and re-read the complete header. Execution may proceed only while the current actor remains the sole assignee and the issue remains `ready` with no live blocker. Local Markdown does not itself provide a distributed lock; concurrent claim acquisition for the same issue must be serialized when the runtime cannot provide a conditional or exclusive mutation. Re-check the claim before consequential external effects or tracker mutations.

Release the claim by restoring `Assignee: None` when execution stops, when handing work off, or before moving the issue out of `ready`.

When mutating, change only the relevant header field or owned body section and preserve unrelated content. Entering `waiting` requires the active `## Waiting` section; leaving `waiting` requires removing that active section. Re-read the changed fields or sections afterward.

Set `Status: done` or `Status: cancelled` for terminal issues.

<!-- repository-contract:end -->

## Setup-only checks and mutations

Before setup, every existing `.tracker/issues/*.md` file must already match the required header and body invariants above. Also verify that source references are valid, managed-work-only relation endpoint rules hold, hierarchy and dependency graphs are acyclic, waiting sections match status, and managed-work claims contain at most one actor. Otherwise stop without modifying the tracker; migration is out of scope.

If `docs/agents/issues.md` already declares a different tracker model, backend, or contract version, stop. Replacing or upgrading a different tracker contract is migration and is out of scope.

Ensure `.tracker/issues/` exists.
