# GitHub Issues backend

GitHub Issues is the reference backend for tracker v2.

Setup replaces `<owner>/<repo>` with the canonical repository and stores that repository identity in `docs/agents/issues.md`. All commands target it explicitly with `-R <owner>/<repo>`.

## Representation

### Type

Managed-work type is represented by exactly one label:

- `type:investigation`
- `type:change`

Untyped issues are allowed and are not managed work.

Do not map GitHub/community labels such as `bug`, `enhancement`, or `documentation` to managed-work type.

### Status

Status is represented by exactly one `status:*` label:

- `status:needs-triage`
- `status:needs-info`
- `status:ready`
- `status:in-progress`
- `status:blocked`
- `status:waiting`
- `status:done`
- `status:cancelled`

Terminal statuses must use GitHub closed state. Non-terminal statuses use open state.

GitHub open/closed state is storage state, not an additional semantic lifecycle.

### Sources

Store direct provenance in one reserved body line near the top:

```text
Sources: #101, #117, #129
```

Use `Sources: None` when there are no direct sources. References are same-repository issue numbers in this prototype.

Preserve the rest of the issue body when updating the line.

### Hierarchy

Use GitHub native sub-issues as canonical parent/child representation.

Hierarchy means decomposition only.

### Dependencies

Use GitHub native issue dependencies as canonical blocked-by representation.

### Claim

Use GitHub assignee as the active claim. Do not add a separate execution-state label.

## Setup

Create the managed type and status labels if they do not already exist.

Suggested label descriptions:

- `type:investigation` — Managed work that resolves uncertainty
- `type:change` — Managed work that changes observable state
- `status:needs-triage` — Intake awaiting maintainer evaluation
- `status:needs-info` — Waiting for required information
- `status:ready` — Managed work ready to be claimed
- `status:in-progress` — Managed work is actively being worked
- `status:blocked` — Cannot proceed until an explicit blocker clears
- `status:waiting` — Waiting for an external event; no active work now
- `status:done` — Completion condition satisfied
- `status:cancelled` — Will not be completed as defined

Do not remove or rename unrelated repository labels.

## Core operations

Commands are semantic examples. Keep arguments equivalent across shells and pass generated/multiline Markdown through UTF-8 files or stdin rather than interpolating it into the command line.

### Read

```text
gh issue view <n> -R <owner>/<repo> --comments \
  --json number,title,body,state,labels,assignees,parent,subIssues,blockedBy
```

If a field is unavailable in the installed `gh` version, use the corresponding GitHub API operation instead of inventing a textual fallback.

### Create managed work

Create an issue with exactly one type label and one truthful status label. New managed work normally begins `status:ready` unless it is already known to be blocked or waiting.

When created from other issues, write the exact direct `Sources:` set at creation time.

### Change type

Managed-work type is stable for the issue's identity. Do not transform `investigation` into `change`; create a new change issue sourced from the investigation.

Correct an accidentally assigned type only as metadata repair.

### Change status

Remove the old `status:*` label and add exactly one new status label. Close the GitHub issue when moving to `done` or `cancelled`; reopen it before moving from a terminal status to a non-terminal status.

After every mutation, re-read the issue and verify exactly the intended type/status/relations persisted.

### Sources

Update only the reserved `Sources:` line and preserve the rest of the body.

### Parent/child

Prefer native sub-issue operations. Creating or attaching a child does not change either issue's type or status.

### Blocking

Prefer native issue dependency operations. Do not infer blocking from parent/child order.

### Claim/release

Claim:

```text
gh issue edit <n> -R <owner>/<repo> --add-assignee "@me"
```

Release:

```text
gh issue edit <n> -R <owner>/<repo> --remove-assignee "@me"
```

Claim ownership must be verified by re-reading assignees before work begins.

## Intake rule

External issues stay external issues. Do not assign a managed-work type to an external report merely because the project decides to work on it.

Instead:

1. find an existing managed issue that already represents the work and add the external issue as a direct source; or
2. create a new `investigation` or `change` issue with the external issue as a source.

Several external reports may source the same managed investigation.

## Frontier

The basic executable frontier is the set of issues that are:

- open;
- managed work (exactly one `type:*` label);
- `status:ready`;
- unassigned;
- not blocked by an open dependency.

This is a derived query, not persisted state.
