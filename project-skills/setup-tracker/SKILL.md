---
name: setup-tracker
description: "Configure the project tracker with GitHub Issues when supported, otherwise Local Markdown."
disable-model-invocation: true
---

# Setup Tracker

Configure issue tracking only. Do not install or emulate downstream workflows.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration. It is the only authority for tracker semantics. Read the selected backend document for representation and operations.

The files in this skill are setup inputs. After setup, `docs/agents/issues.md` is the repository-local tracker contract and must not depend on the skill installation path.

The contract version written by this Skill is `1`. Contract version is a repository protocol/schema version, not a product or Skill release version. A different or missing version in an existing tracker contract requires migration and must not be silently rewritten by setup.

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

For GitHub, record the exact `owner/repo`, inspect existing labels and `.github/ISSUE_TEMPLATE/` when present, then run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation. Existing issue templates are repository-owned configuration; preserve useful intake forms and unrelated templates.

For Local Markdown, inspect `.tracker/issues/*.md` if present and run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation.

Any failed setup-only check stops setup before tracker mutation. Migration is out of scope.

### 3. Configure

Write `docs/agents/issues.md` as a self-contained repository-local contract.

Start with backend identity:

For GitHub:

```markdown
# Issue tracker
Model: tracker
Contract-Version: 1
Backend: github
Repository: <owner>/<repo>
```

For Local Markdown:

```markdown
# Issue tracker
Model: tracker
Contract-Version: 1
Backend: local-markdown
Issue root: .tracker/issues/
```

Then materialize the contract mechanically:

1. copy, verbatim and in order, the content between `<!-- repository-contract:start -->` and `<!-- repository-contract:end -->` in [ISSUE-MODEL.md](ISSUE-MODEL.md);
2. append, verbatim and in order, the content between the same markers in the selected backend document.

Do not copy the marker lines themselves. Do not paraphrase, summarize, reorder, deduplicate, or otherwise rewrite contract text. Apart from the backend-identity values above and insignificant surrounding blank lines, two runs against the same Skill revision and backend must produce the same contract text.

Do not copy backend-selection, capability-detection, setup-only checks/mutations, or any other text outside the marked contract regions. The generated `docs/agents/issues.md` must not contain references to `ISSUE-MODEL.md`, `github.md`, `local-markdown.md`, this skill directory, or any installation-specific path.

The generated `docs/agents/issues.md` is the project authority after setup. A fresh checkout must be able to interpret the tracker from repository contents alone.

For GitHub:

- perform the mutations in the backend document's `Setup-only checks and mutations` section after all preflight checks pass;
- keep existing useful intake templates;
- when a common intake surface is missing, copy the corresponding default form from `templates/github/ISSUE_TEMPLATE/` into `.github/ISSUE_TEMPLATE/` without replacing a different existing form;
- ensure the issue-template chooser keeps blank issues enabled; when `config.yml` already exists, change only `blank_issues_enabled` and preserve its other configuration.

The shipped forms are intake UX only. Do not expose `investigation` or `change` as public issue-template choices; managed work is created by internal workflows against the tracker contract.

For Local Markdown, perform the mutation in the backend document's `Setup-only checks and mutations` section after all preflight checks pass.

If the active harness exposes a project instruction artifact, add or update one short issue-tracker pointer to `docs/agents/issues.md`. Do not copy the contract into project instructions.

### 4. Verify

Re-read `docs/agents/issues.md` and verify:

- `Model: tracker` and `Contract-Version: 1` are exact;
- the selected backend identity is exact;
- the semantic contract region exactly matches the marked semantic source text;
- the runtime contract region exactly matches the marked selected-backend source text;
- setup-only text and contract markers are absent;
- executable frontier is defined once, in the semantic portion;
- managed work requires a checkable completion condition;
- waiting managed work requires `Waiting for` and `Resume when` content;
- hierarchy and dependency endpoint/cycle rules are present;
- managed-work assignee is defined as a single execution claim rather than long-lived ownership;
- Skill-owned extension sections remain permitted;
- no reference depends on a skill file or installation path.

If project instructions were changed, verify the issue-tracker pointer resolves and is not duplicated.

For GitHub, verify:

- required capabilities and canonical namespaced tracker labels are available;
- unrelated labels were not removed or renamed;
- every existing issue carrying canonical tracker labels satisfies the backend preflight invariants;
- common external intake has a usable form or blank-issue path;
- shipped forms apply `tracker:status:needs-triage`;
- blank issues are enabled and an unlabeled blank issue is valid intake by the documented derived-status rule;
- no public issue template asks reporters to choose managed-work type or internal tracker state.

For Local Markdown, verify the issue root exists, existing files were preserved, and every issue file matches the required header, body, relation, waiting, and claim invariants.

Setup is complete only when every applicable check passes.

### 5. Stop

Report the configured backend. Do not continue into downstream workflows.
