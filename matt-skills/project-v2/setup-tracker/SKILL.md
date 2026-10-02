---
name: setup-tracker
description: "Configure the tracker v2 prototype with GitHub Issues when supported, otherwise Local Markdown."
disable-model-invocation: true
---

# Setup Tracker

Configure issue tracking only. Do not install or emulate downstream workflows.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration. It is the only authority for tracker semantics.

## Process

### 1. Choose the backend

Inspect repository remotes, repository metadata, and available GitHub tooling/API.

GitHub is usable only when the selected repository has Issues enabled and the available tooling/API can read and write:

- labels and assignees;
- native sub-issues;
- native issue dependencies.

If exactly one usable GitHub repository matches the workspace, use it. If several are plausible, ask which is canonical. If none is usable, use Local Markdown.

Do not create textual GitHub fallbacks for hierarchy or dependencies.

### 2. Inspect existing state

For GitHub, record the exact `owner/repo` and inspect existing labels.

For Local Markdown, inspect `.tracker/issues/*.md` if present. If any existing issue does not match the v2 header in [local-markdown.md](local-markdown.md), stop without modifying the tracker. Migration is out of scope.

### 3. Configure

Write `docs/agents/issues.md`.

For GitHub:

```markdown
# Issue tracker
Model: tracker-v2
Backend: github
Repository: <owner>/<repo>
Semantics: <path to ISSUE-MODEL.md>
Operations: <path to github.md>
```

For Local Markdown:

```markdown
# Issue tracker
Model: tracker-v2
Backend: local-markdown
Issue root: .tracker/issues/
Semantics: <path to ISSUE-MODEL.md>
Operations: <path to local-markdown.md>
```

For GitHub, create missing tracker-v2 labels described in [github.md](github.md). Preserve unrelated labels.

If the active harness exposes a project instruction artifact, add or update one short issue-tracker pointer to `docs/agents/issues.md`. Do not copy the contract into project instructions.

### 4. Verify

Re-read `docs/agents/issues.md` and verify its backend identity and both referenced files resolve.

If project instructions were changed, verify the issue-tracker pointer resolves and is not duplicated.

For GitHub, verify the required labels and native relation capabilities are available after setup.

For Local Markdown, verify existing files were preserved and every issue file matches the v2 header.

Setup is complete only when every applicable check passes.

### 5. Stop

Report the configured backend. Do not continue into downstream workflows.
