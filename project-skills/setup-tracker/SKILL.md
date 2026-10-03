---
name: setup-tracker
description: "Configure the project tracker with the intended GitHub Issues or Local Markdown backend."
disable-model-invocation: true
---

# Setup Tracker

Configure issue tracking only. Do not install or emulate downstream workflows. Do not migrate, adopt, repair, or reinterpret pre-existing work.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md) before writing configuration. It is the only authority for tracker semantics. Read the selected backend document for representation and operations.

The files in this skill are setup inputs. After successful setup, `docs/agents/issues.md` is the repository-local tracker contract and must not depend on the skill installation path.

The contract version written by this Skill is `1`. Contract version is a repository protocol/schema version, not a product or Skill release version. The normative semantic and backend contract text for a published contract version is immutable: any normative change requires a new `Contract-Version`. A missing or different version, or the same version with different normative contract text, requires migration and must not be silently rewritten by setup.

## Process

### 1. Choose the intended backend

Inspect repository remotes, repository metadata, and any explicit user choice.

If the user explicitly selected Local Markdown, use Local Markdown.

Otherwise, when exactly one GitHub repository matches the workspace, GitHub is the intended backend. If several GitHub repositories are plausible, ask which is canonical. If no GitHub repository is intended for this workspace, use Local Markdown.

For an intended GitHub backend, verify that Issues are enabled and that the available GitHub tooling/API, taken together, can read and write:

- issues, labels, and assignees;
- native sub-issues;
- native issue dependencies.

Use any available GitHub API or tool surface that can satisfy these operations; do not treat the absence of one convenience command as backend failure. If any required GitHub capability still cannot be performed, stop and report the exact missing capability. Do not fall back to Local Markdown and do not create textual GitHub fallbacks for hierarchy or dependencies.

### 2. Inspect existing state and enforce the setup boundary

For GitHub, record the exact `owner/repo`, inspect existing labels and `.github/ISSUE_TEMPLATE/` when present, inspect `docs/agents/issues.md`, and inspect issues carrying any canonical `tracker:kind:*`, `tracker:type:*`, or `tracker:status:*` label. Then run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation.

Ordinary existing GitHub issues with no canonical tracker labels are outside this tracker. Preserve them and do not classify, validate, close, relabel, or otherwise adopt them.

For Local Markdown, inspect `docs/agents/issues.md` and `.tracker/issues/*.md` if present, then run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation.

Any failed setup-only check stops setup before tracker mutation. Migration, takeover, adoption, and repair are out of scope.

### 3. Configure the backend

Do not write `docs/agents/issues.md` yet. That file is the final publication/commit marker for successful setup.

For GitHub:

- perform the mutations in the backend document's `Setup-only checks and mutations` section after all preflight checks pass;
- keep existing useful intake templates;
- when a common intake surface is missing, copy the corresponding default form from `templates/github/ISSUE_TEMPLATE/` into `.github/ISSUE_TEMPLATE/` without replacing a different existing form;
- ensure the issue-template chooser keeps blank issues enabled; when `config.yml` already exists, change only `blank_issues_enabled` and preserve its other configuration.

The shipped forms are intake UX only. They explicitly classify created issues as intake and apply `tracker:status:needs-triage`. Do not expose `investigation` or `change` as public issue-template choices; managed work is created by internal workflows against the tracker contract.

A blank GitHub issue remains unclassified and outside the tracker until a downstream triage or intake workflow explicitly classifies it. Setup never adopts it.

For Local Markdown, perform the mutation in the backend document's `Setup-only checks and mutations` section after all preflight checks pass.

### 4. Verify backend state before publishing the contract

For GitHub, verify:

- every required GitHub capability remains usable;
- canonical tracker kind, type, and status labels are available;
- unrelated labels were not removed or renamed;
- when a compatible current contract already existed, every tracked issue still satisfies the backend invariants;
- ordinary unclassified existing issues remain untouched;
- common external intake has a usable form or blank-issue path;
- shipped forms apply both `tracker:kind:intake` and `tracker:status:needs-triage`;
- blank issues are enabled and remain unclassified until explicitly adopted by a downstream workflow;
- no public issue template asks reporters to choose managed-work type or internal tracker state.

For Local Markdown, verify the issue root exists. When a compatible current contract already existed, verify every tracked issue file still satisfies the required header, body, relation, waiting, and claim invariants.

If backend verification fails, stop without publishing a repository contract.

### 5. Publish the repository-local contract

Write `docs/agents/issues.md` only after backend configuration and verification succeed.

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

Do not copy the marker lines themselves. Do not paraphrase, summarize, reorder, deduplicate, or otherwise rewrite contract text. Apart from the backend-identity values above and insignificant surrounding blank lines, two runs against the same contract version and backend must produce the same normative contract text.

Do not copy backend-selection, capability-detection, setup-only checks/mutations, or any other text outside the marked contract regions. The generated `docs/agents/issues.md` must not contain references to `ISSUE-MODEL.md`, `github.md`, `local-markdown.md`, this skill directory, or any installation-specific path.

The generated `docs/agents/issues.md` is the project authority after setup. A fresh checkout must be able to interpret the tracker from repository contents alone.

If a compatible `docs/agents/issues.md` already exists, re-running setup must not silently rewrite normative text. If its `Contract-Version: 1` normative text differs from the current version-1 source, stop and require migration or repair.

After the contract is written, if the active harness exposes a project instruction artifact, add or update one short issue-tracker pointer to `docs/agents/issues.md`. Do not copy the contract into project instructions.

### 6. Verify the published contract

Re-read `docs/agents/issues.md` and verify:

- `Model: tracker` and `Contract-Version: 1` are exact;
- the selected backend identity is exact;
- the semantic contract region exactly matches the marked semantic source text;
- the runtime contract region exactly matches the marked selected-backend source text;
- setup-only text and contract markers are absent;
- tracked issues require explicit kind and explicit lifecycle status;
- unclassified repository issues are explicitly outside the tracker and setup does not adopt them;
- executable frontier is defined once, in the semantic portion;
- managed work requires a checkable completion condition;
- waiting managed work requires `Waiting for` and `Resume when` content;
- hierarchy and dependency endpoint/cycle rules are present;
- managed-work assignee is defined as a single execution claim rather than long-lived ownership;
- same-issue top-level execution is non-concurrent and subagents do not independently claim it;
- Skill-owned extension sections remain permitted;
- no reference depends on a skill file or installation path.

If project instructions were changed, verify the issue-tracker pointer resolves and is not duplicated.

Setup is complete only when every applicable check passes.

### 7. Stop

Report the configured backend. Do not continue into downstream workflows.
