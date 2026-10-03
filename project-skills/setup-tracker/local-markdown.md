# Local Markdown backend

Representation and operations for the tracker. The issue model owns semantics.

<!-- repository-contract:start -->

## Storage

Store tracked issues as:

```text
.tracker/issues/<NNNN>.md
```

Use the next monotonically increasing four-digit numeric ID. The numeric ID is the canonical local issue reference and the complete filename stem; do not add a title-derived suffix to the canonical issue path.

Create the candidate path with a create-only operation that must fail rather than overwrite when that numeric ID already exists. Because every creator of the same candidate ID targets the same path, a create-only collision atomically detects that the ID was claimed. On collision, rescan and retry with the next available number. If the active runtime cannot provide create-only semantics, concurrent issue creation must be serialized by the caller.

## Header

```markdown
# <title>

Kind: <intake|managed>
Type: <investigation|change|None>
Status: <canonical status>
Sources: <NNNN, NNNN|None>
Parent: <NNNN|None>
Blocked-By: <NNNN, NNNN|None>
Assignee: <actor|None>
Reporter: <actor|Unknown|None>
Origin: <source-ref|Unknown|None>
```

`Kind` explicitly classifies the tracked issue. `Kind: intake` requires `Type: None`; `Kind: managed` requires exactly one managed-work type. Missing, contradictory, or malformed classification is invalid and must not be reinterpreted as another kind.

Every tracked issue stores exactly one explicit status allowed for its kind.

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

Create new tracked issues with the complete header using the create-only numeric-ID collision protocol in the Storage section.

When creating intake, set `Kind: intake`, `Type: None`, an explicit intake status, `Reporter`, and `Origin`; preserve the original wording and evidence under `## Intake` and discussion under `## Discussion`.

When creating managed work, set `Kind: managed`, exactly one managed-work type, an explicit managed-work status, `Reporter: None`, and `Origin: None`; write the required completion condition and preserve any Skill-owned extension sections supplied by the creating workflow.

Read the whole file. For list/search, parse the required header fields; do not guess missing values.

Before adding or changing `Parent` or `Blocked-By`, verify that every referenced issue exists, every endpoint is managed work, and the resulting hierarchy or dependency graph would remain acyclic. `Sources` may reference tracked intake or managed work but must reference existing tracked issues and must not self-reference.

To acquire a managed-work claim, first verify that the issue is on the executable frontier and `Assignee: None`. The runtime must already guarantee that the same managed issue is not being executed concurrently by another top-level executor; subagents are part of the claiming execution and do not claim the issue independently. Then set `Assignee` to the current actor and re-read the complete header. Execution may proceed only while the current actor remains the sole assignee and the issue remains `ready` with no live blocker.

Release the claim by restoring `Assignee: None` when execution stops, when handing work off, or before moving the issue out of `ready`.

When mutating, change only the relevant header field or owned body section and preserve unrelated content. Entering `waiting` requires the active `## Waiting` section; leaving `waiting` requires removing that active section. Re-read the changed fields or sections afterward.

Set `Status: done` or `Status: cancelled` before treating an issue as terminal.

<!-- repository-contract:end -->

## Setup-only checks and mutations

Inspect `docs/agents/issues.md` and `.tracker/issues/` before setup.

If no compatible current tracker contract exists and `.tracker/issues/` already contains issue files, stop without modifying them. Adopting, repairing, or migrating existing local issue files belongs to a separate migration/takeover workflow.

When a compatible current contract already exists, every `.tracker/issues/*.md` file must use the canonical `<NNNN>.md` numeric-ID filename and match the required header and body invariants above. Also verify that source references are valid, managed-work-only relation endpoint rules hold, hierarchy and dependency graphs are acyclic, waiting sections match status, and managed-work claims contain at most one actor. A non-canonical issue filename or any state that would make a numeric reference ambiguous is invalid and stops setup without repair.

If `docs/agents/issues.md` already declares a different tracker model, backend, or contract version, stop. If it declares the same contract version but its normative contract text differs from the current version-1 contract, also stop. Replacing, upgrading, repairing, or taking over a tracker contract is migration and is out of scope.

Ensure `.tracker/issues/` exists.
