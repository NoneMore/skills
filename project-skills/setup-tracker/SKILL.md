---
name: setup-tracker
description: "Configure the project tracker with the intended GitHub Issues or Local Markdown backend."
disable-model-invocation: true
---

# Setup Tracker

Configure issue tracking only. Do not run downstream workflows and do not migrate, classify, repair, close, or relabel existing issues.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md), then read only the selected backend document. After setup, `docs/agents/issues.md` is the repository-local tracker contract so downstream workflows do not depend on this Skill's installation path.

## Process

### 1. Choose the backend

Inspect repository remotes and any explicit user choice.

- If the user explicitly selected Local Markdown, use it.
- Otherwise, if exactly one GitHub repository clearly matches the workspace, use GitHub.
- If several GitHub repositories are plausible, ask which is canonical.
- If no GitHub repository is intended for the workspace, use Local Markdown.

### 2. Inspect existing configuration

Read `docs/agents/issues.md` when it exists.

If it clearly configures a different tracker or backend and the user did not ask to replace it, stop and report the conflict.

For GitHub, inspect the repository identity, whether Issues are enabled, and existing canonical tracker labels. For Local Markdown, inspect whether `.tracker/issues/` exists.

Do not inspect or mutate ordinary existing issues as part of setup. Unclassified issues remain outside the tracker.

### 3. Configure the backend

For GitHub, require issue and label read/write capability. Ensure these labels exist, creating only missing labels and preserving unrelated labels:

- `tracker:kind:intake`
- `tracker:kind:managed`
- `tracker:type:investigation`
- `tracker:type:change`
- `tracker:status:needs-triage`
- `tracker:status:ready`
- `tracker:status:waiting`
- `tracker:status:done`

Do not modify issue templates. Native sub-issue and dependency capabilities are not setup prerequisites; a downstream workflow that needs one of those relations checks the required capability when it uses it.

For Local Markdown, ensure `.tracker/issues/` exists. Do not rewrite existing issue files.

### 4. Publish the repository contract

Write `docs/agents/issues.md` as a self-contained contract.

Start with backend identity:

For GitHub:

```markdown
# Issue tracker
Backend: github
Repository: <owner>/<repo>
```

For Local Markdown:

```markdown
# Issue tracker
Backend: local-markdown
Issue root: .tracker/issues/
```

Then append the complete contents of `ISSUE-MODEL.md` and the complete selected backend document. The generated file must contain those rules directly; it must not depend on resolving Skill-relative links at runtime.

If the same backend is already configured by this Skill, refresh this generated contract without changing existing tracked issues.

If the active harness exposes a project instruction artifact, add or update one short pointer to `docs/agents/issues.md`; do not copy the contract into project instructions.

### 5. Verify

Re-read only the configuration changed by setup.

For GitHub, verify the canonical labels exist and `docs/agents/issues.md` names the intended repository. For Local Markdown, verify the issue root exists and the contract names it.

Verify the generated contract is self-contained and includes:

- explicit `intake` / `managed` classification;
- `investigation` / `change` managed-work types;
- allowed lifecycle statuses;
- a checkable completion condition for managed work;
- waiting, source, hierarchy, and dependency rules;
- the selected backend representation;
- no execution-claim or orchestration protocol.

### 6. Stop

Report the configured backend. Do not continue into downstream work.
