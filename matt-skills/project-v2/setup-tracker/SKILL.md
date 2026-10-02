---
name: setup-tracker
description: "Prototype setup for the v2 project tracker: GitHub Issues first, local Markdown fallback, with managed work reduced to investigation and change issues."
disable-model-invocation: true
---

# Setup Tracker

Configure a repository to use the tracker v2 issue model.

This skill configures only issue tracking. It does not install or emulate downstream project workflows.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration. Treat it as the only authority for tracker semantics; backend documents define storage and operations.

## Process

### 1. Detect the backend

Inspect repository remotes, repository metadata, and the available GitHub tooling/API.

A GitHub repository is usable for tracker v2 only when:

- GitHub Issues are enabled;
- labels and assignees can be read and written;
- native sub-issues can be read and written;
- native issue dependencies can be read and written.

If exactly one usable GitHub repository is associated with the workspace, choose GitHub.

If multiple usable GitHub repositories are plausible tracker targets, show them and ask the user which repository is canonical.

If no candidate satisfies the complete GitHub capability set, choose Local Markdown. Do not invent textual GitHub fallbacks for hierarchy or dependencies.

Do not ask the user to choose among tracker vendors.

### 2. Inspect existing tracker state

For GitHub:

- record the exact `owner/repo`;
- inspect existing labels before creating anything;
- preserve unrelated labels and community taxonomy.

For Local Markdown:

- inspect `.tracker/issues/` if present;
- if it contains any `*.md` file that does not match the tracker-v2 header contract in [local-markdown.md](local-markdown.md), stop without modifying the tracker; migration is out of scope;
- preserve every conforming existing file;
- determine the next available local issue number.

### 3. Present the proposed configuration

Show:

- selected backend;
- GitHub repository identity or local issue root;
- the two managed-work type representations;
- the canonical status representations;
- how Sources, Parent, Blocked-By, and Assignee will be represented.

State that external intake and internally created managed work follow [ISSUE-MODEL.md](ISSUE-MODEL.md). Do not add downstream workflow behavior to this setup.

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

Semantics: <path to this skill's ISSUE-MODEL.md>
Backend operations: <path to this skill's local-markdown.md>
```

For GitHub, create missing tracker-v2 labels described in [github.md](github.md). Do not delete or rename unrelated labels.

If the active harness has a project instruction artifact, add or update one short `## Issue tracker` pointer to `docs/agents/issues.md`. Do not copy the semantic contract into project instructions.

### 5. Verify

Re-read `docs/agents/issues.md` and verify:

- the selected backend and repository/root are exact;
- the `Semantics` pointer resolves to this skill's `ISSUE-MODEL.md`;
- the `Backend operations` pointer resolves to the selected backend document.

If a project instruction artifact was changed, re-read it and verify it contains exactly one issue-tracker pointer to `docs/agents/issues.md`, and that the pointer resolves.

For GitHub, also verify:

- both managed type labels exist;
- every canonical status label exists;
- native sub-issues and native issue dependencies remain readable and writable through the selected tooling/API;
- no setup mutation changed unrelated labels.

For Local Markdown, also verify:

- the issue root can be created and written;
- every pre-existing issue file was preserved unchanged;
- every `*.md` issue file matches the tracker-v2 header contract.

Setup is complete only when every applicable verification above passes.

### 6. Stop

Report the configured backend and model.

Do not continue into triage, investigation, specification, decomposition, implementation, reconciliation, or any other downstream workflow. Those workflows are intentionally absent from this prototype.
