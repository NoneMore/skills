---
name: setup-tracker
description: "Prototype setup for the v2 project tracker: GitHub Issues first, local Markdown fallback, with managed work reduced to investigation and change issues."
disable-model-invocation: true
---

# Setup Tracker

Configure a repository to use the tracker v2 issue model.

This skill is deliberately narrower than the current project setup. It configures only issue tracking. It does not install or emulate downstream project workflows.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration.

## Principles

- GitHub Issues is the reference backend.
- Local Markdown is the only fallback.
- Do not offer GitLab, Jira, Linear, or an "other" tracker option.
- External issues are intake/evidence, not managed-work definitions.
- Managed work has exactly one type: `investigation` or `change`.
- Type, status, sources, hierarchy, dependencies, and assignee are independent.
- Do not create special types for requests, specs, implementation tickets, decisions, maps, tracking containers, research, prototypes, or tasks.

## Process

### 1. Detect the backend

Inspect repository remotes and repository metadata.

If exactly one usable GitHub repository is associated with the workspace and Issues are enabled, choose GitHub.

If multiple usable GitHub repositories are plausible tracker targets, show them and ask the user which repository is canonical.

If there is no usable GitHub Issues surface, choose Local Markdown.

Do not ask the user to choose among tracker vendors.

### 2. Inspect existing tracker state

For GitHub:

- record the exact `owner/repo`;
- inspect existing labels before creating anything;
- preserve unrelated labels and community taxonomy;
- inspect whether native sub-issues and issue dependencies are usable by the installed GitHub tooling/API.

For Local Markdown:

- inspect `.tracker/issues/` if present;
- preserve existing files;
- determine the next available local issue number.

### 3. Present the proposed configuration

Show:

- selected backend;
- GitHub repository identity or local issue root;
- the two managed-work types;
- canonical statuses;
- how Sources, Parent, Blocked-By, and Assignee will be represented.

Explicitly state that external issues will remain untyped intake and that project work will be created as separate managed issues.

Do not include downstream workflow behavior in this setup.

### 4. Configure

Write `docs/agents/issues.md`.

For GitHub use:

```markdown
# Issue tracker

Model: tracker-v2
Backend: github
Repository: <owner>/<repo>

Managed types:
- type:investigation
- type:change

Statuses:
- status:needs-triage
- status:needs-info
- status:ready
- status:in-progress
- status:blocked
- status:waiting
- status:done
- status:cancelled

Sources: reserved body line `Sources: ...`
Hierarchy: GitHub native sub-issues
Dependencies: GitHub native issue dependencies
Claim: GitHub assignee

Semantics: <path to this skill's ISSUE-MODEL.md>
Backend operations: <path to this skill's github.md>
```

For Local Markdown use:

```markdown
# Issue tracker

Model: tracker-v2
Backend: local-markdown
Issue root: .tracker/issues/

Managed types:
- investigation
- change

Statuses:
- needs-triage
- needs-info
- ready
- in-progress
- blocked
- waiting
- done
- cancelled

Semantics: <path to this skill's ISSUE-MODEL.md>
Backend operations: <path to this skill's local-markdown.md>
```

For GitHub, create missing tracker-v2 labels described in [github.md](github.md). Do not delete or rename unrelated labels.

If the active harness has a project instruction artifact, add or update one short `## Issue tracker` pointer to `docs/agents/issues.md`. Do not copy the full contract into project instructions.

### 5. Verify

Re-read `docs/agents/issues.md`.

For GitHub, verify:

- canonical repository identity;
- both managed type labels exist;
- every canonical status label exists;
- no setup mutation changed unrelated labels.

For Local Markdown, verify the issue root can be created/written and that existing files were preserved.

### 6. Stop

Report the configured backend and model.

Do not continue into triage, investigation, specification, decomposition, implementation, reconciliation, or any other downstream workflow. Those workflows are intentionally absent from this prototype.
