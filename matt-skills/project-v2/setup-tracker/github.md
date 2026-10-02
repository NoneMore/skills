# GitHub Issues backend

GitHub Issues is the reference backend for tracker v2 when all required native capabilities are available.

Tracker semantics are defined only in [ISSUE-MODEL.md](ISSUE-MODEL.md). This file defines GitHub representation and operations.

Setup replaces `<owner>/<repo>` with the canonical repository and stores that repository identity in `docs/agents/issues.md`. All commands target it explicitly with `-R <owner>/<repo>`.

## Required capabilities

The GitHub backend requires read/write access to:

- Issues;
- labels;
- assignees;
- native sub-issues;
- native issue dependencies.

If the installed tooling cannot perform an operation directly, the corresponding GitHub API operation is acceptable. If either the tooling or API cannot read and write native sub-issues or dependencies, this backend is not usable; setup must choose Local Markdown instead of inventing a textual fallback.

## Representation

### Type

Managed-work type is represented by exactly one label:

- `type:investigation`
- `type:change`

Untyped issues represent external intake.

Repository taxonomy such as `bug`, `enhancement`, or `documentation` remains independent.

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

Terminal statuses use GitHub closed state. Non-terminal statuses use open state. GitHub open/closed state is storage state, not another lifecycle dimension.

### Sources

Store direct provenance in one reserved body line near the top:

```text
Sources: #101, #117, #129
```

Use `Sources: None` when there are no direct sources. References are same-repository issue numbers in this prototype.

Preserve the rest of the issue body when updating the line.

### Hierarchy

Use GitHub native sub-issues.

### Dependencies

Use GitHub native issue dependencies.

### Claim

Use GitHub assignee.

## Setup

Create the managed type and status labels if they do not already exist.

Suggested label descriptions:

- `type:investigation` — Managed work that resolves uncertainty
- `type:change` — Managed work that changes observable state
- `status:needs-triage` — External intake awaiting maintainer evaluation
- `status:needs-info` — External intake missing information needed for evaluation
- `status:ready` — Managed work ready to be claimed
- `status:in-progress` — Managed work is actively being worked
- `status:blocked` — Managed work held by an explicit prerequisite
- `status:waiting` — No active work until an external event or decision
- `status:done` — Completion condition satisfied or intake addressed
- `status:cancelled` — Will not be completed or acted on as defined

Do not remove or rename unrelated repository labels.

## Core operations

Commands are semantic examples. Keep arguments equivalent across shells and pass generated/multiline Markdown through UTF-8 files or stdin rather than interpolating it into the command line.

### Read

```text
gh issue view <n> -R <owner>/<repo> --comments \
  --json number,title,body,state,labels,assignees,parent,subIssues,blockedBy
```

If a field is unavailable in the installed `gh` version, use the corresponding GitHub API operation. If the native relation cannot be read and written through either surface, the GitHub backend does not satisfy tracker-v2 requirements.

### Create

Create external intake without a managed type label.

Create managed work with exactly one type label and one status permitted for managed work by `ISSUE-MODEL.md`. When created from other issues, write the exact direct `Sources:` set at creation time.

### Change type

Follow the type invariants in `ISSUE-MODEL.md`. Correct an accidentally assigned type only as metadata repair.

### Change status

Remove the old `status:*` label and add exactly one new status label whose meaning and applicability match `ISSUE-MODEL.md`.

Close the GitHub issue when moving to `done` or `cancelled`; reopen it before moving from a terminal status to a non-terminal status.

After every mutation, re-read the issue and verify exactly the intended type, status, and relations persisted.

### Sources

Update only the reserved `Sources:` line and preserve the rest of the body.

### Parent/child

Use native sub-issue operations.

### Blocking

Use native issue dependency operations.

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

## Frontier

The basic executable frontier is the set of issues that are:

- open;
- managed work with exactly one `type:*` label;
- `status:ready`;
- unassigned;
- not blocked by an open dependency.

This is a derived query, not persisted state.
