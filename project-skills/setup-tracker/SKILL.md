---
name: setup-tracker
description: "Configure the project tracker with GitHub Issues when supported, otherwise Local Markdown."
disable-model-invocation: true
---

# Setup Tracker

Configure issue tracking only. Do not install or emulate downstream workflows.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration. It is the only authority for tracker semantics. Read the selected backend document for representation and operations.

The files in this skill are setup inputs. After setup, `docs/agents/issues.md` is the repository-local tracker contract and must not depend on the skill installation path.

## Process

### 1. Choose the backend

Inspect repository remotes, repository metadata, and available GitHub tooling/API.

GitHub is usable only when the selected repository has Issues enabled and the available tooling/API can read and write:

- issues, labels, and assignees;
- native sub-issues;
- native issue dependencies.

If exactly one usable GitHub repository matches the workspace, use it. If several are plausible, ask which is canonical. If none is usable, use Local Markdown.

Do not create textual GitHub fallbacks for hierarchy or dependencies.

### 2. Inspect existing state

For GitHub, record the exact `owner/repo` and inspect existing labels.

For Local Markdown, inspect `.tracker/issues/*.md` if present. If any existing issue does not match the header in [local-markdown.md](local-markdown.md), stop without modifying the tracker. Migration is out of scope.

### 3. Configure

Write `docs/agents/issues.md` as a self-contained repository-local contract.

Start with backend identity:

For GitHub:

```markdown
# Issue tracker
Model: tracker
Backend: github
Repository: <owner>/<repo>
```

For Local Markdown:

```markdown
# Issue tracker
Model: tracker
Backend: local-markdown
Issue root: .tracker/issues/
```

Then materialize into the same file:

1. the complete semantic contract from [ISSUE-MODEL.md](ISSUE-MODEL.md);
2. the complete representation and operations contract from the selected backend document.

Adapt document headings as needed so the result is one coherent file. Preserve the meaning of the source contracts. Do not leave references to `ISSUE-MODEL.md`, `github.md`, `local-markdown.md`, this skill directory, or any installation-specific path in `docs/agents/issues.md`.

The generated `docs/agents/issues.md` is the project authority after setup. A fresh checkout must be able to interpret the tracker from repository contents alone.

For GitHub, create missing tracker labels described in [github.md](github.md). Preserve unrelated labels.

For Local Markdown, ensure `.tracker/issues/` exists.

If the active harness exposes a project instruction artifact, add or update one short issue-tracker pointer to `docs/agents/issues.md`. Do not copy the contract into project instructions.

### 4. Verify

Re-read `docs/agents/issues.md` and verify:

- the backend identity is exact;
- the full semantic contract and selected backend representation/operations are present;
- executable frontier is defined once, in the semantic portion;
- no reference depends on a skill file or installation path.

If project instructions were changed, verify the issue-tracker pointer resolves and is not duplicated.

For GitHub, verify:

- required capabilities and tracker labels are available;
- unrelated labels were not removed or renamed.

For Local Markdown, verify the issue root exists, existing files were preserved, and every issue file matches the header.

Setup is complete only when every applicable check passes.

### 5. Stop

Report the configured backend. Do not continue into downstream workflows.
