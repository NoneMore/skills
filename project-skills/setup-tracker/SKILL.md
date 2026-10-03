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

- issues and labels;
- assignees, including checking whether a concrete GitHub login is assignable;
- native sub-issues;
- native issue dependencies;
- complete tracker-wide and relation result sets, including pagination to exhaustion when the underlying API is paginated.

Use any available GitHub API or tool surface that can satisfy those operations; do not treat the absence of one convenience command as backend failure. If any required GitHub capability still cannot be performed, stop and report the exact missing capability. A tool that exposes only a truncated first page without a way to continue is insufficient for checks that require the complete set. Do not fall back to Local Markdown and do not create textual GitHub fallbacks for hierarchy or dependencies.

### 2. Inspect existing state and enforce the setup boundary

For GitHub, record the exact `owner/repo`, inspect existing labels and `.github/ISSUE_TEMPLATE/` when present, inspect `docs/agents/issues.md`, and inspect issues carrying any canonical `tracker:kind:*`, `tracker:type:*`, or `tracker:status:*` label. Exhaust every result page needed to establish whether tracker-shaped issues already exist and to validate relation graphs. Then run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation.

A canonical tracker label that already exists but is archived or otherwise unusable is a setup conflict, not a missing label. Stop before mutation rather than unarchiving, renaming, replacing, or repairing it.

Ordinary existing GitHub issues with no canonical tracker labels are outside this tracker. Preserve them and do not classify, validate, close, relabel, or otherwise adopt them.

For Local Markdown, inspect `docs/agents/issues.md` and `.tracker/issues/*.md` if present, then run every check in the backend document's `Setup-only checks and mutations` section before making any tracker mutation.

Any failed setup-only check stops setup before tracker mutation. Migration, takeover, adoption, and repair are out of scope.

### 3. Configure the backend

Do not write `docs/agents/issues.md` yet. That file is the final publication/commit marker for successful tracker configuration.

For GitHub:

- perform the mutations in the backend document's `Setup-only checks and mutations` section after all preflight checks pass;
- keep existing useful intake templates;
- when a common intake surface is missing, copy the corresponding default form from `templates/github/ISSUE_TEMPLATE/` into `.github/ISSUE_TEMPLATE/` without replacing a different existing form;
- ensure the issue-template chooser keeps blank issues enabled; when `config.yml` already exists, change only `blank_issues_enabled` and preserve its other configuration.

The shipped forms are intake UX only. They explicitly classify created issues as intake and apply `tracker:status:needs-triage`. Do not expose `investigation` or `change` as public issue-template choices; managed work is created by internal workflows against the tracker contract.

A blank GitHub issue remains unclassified and outside the tracker until a downstream triage or intake workflow classifies it under the persisted intake-cutover rule. Setup never adopts historical unclassified issues.

For Local Markdown, perform the mutation in the backend document's `Setup-only checks and mutations` section after all preflight checks pass.

### 4. Verify backend state before publishing the contract

For GitHub, verify:

- every required GitHub capability remains usable, including complete enumeration for global checks and assignability checks for claims;
- canonical tracker kind, type, and status labels are available, usable, and not archived;
- unrelated labels were not removed or renamed;
- when a compatible current contract already existed, every tracked issue still satisfies the backend invariants, using complete pagination for issue and relation enumeration;
- ordinary unclassified existing issues remain untouched;
- common external intake has a usable form or blank-issue path;
- shipped forms apply both `tracker:kind:intake` and `tracker:status:needs-triage`;
- blank issues are enabled and remain unclassified until explicitly adopted by a downstream workflow under the contract cutover;
- no public issue template asks reporters to choose managed-work type or internal tracker state.

For Local Markdown, verify the issue root exists. When a compatible current contract already existed, verify every tracked issue file still satisfies the required filename, header, body, relation, waiting, terminal-status, and claim invariants.

If backend verification fails, stop without publishing a repository contract.

### 5. Publish the repository-local contract

Only publish `docs/agents/issues.md` after backend configuration and verification succeed. If no compatible contract exists, create it now. If an exact compatible contract already exists, preserve it unchanged rather than rewriting it on every setup run.

For a new GitHub contract, immediately before writing `docs/agents/issues.md`, determine the greatest existing repository issue or pull-request number from a reliable complete query; use `0` when neither exists. Record that immutable value as the intake cutover. Do not recompute or advance it on later compatible setup runs.

For GitHub:

```markdown
# Issue tracker
Model: tracker
Contract-Version: 1
Backend: github
Repository: <owner>/<repo>
Intake-Cutover-Number: <highest existing issue-or-PR number|0>
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

Do not copy the marker lines themselves. Do not paraphrase, summarize, reorder, deduplicate, or otherwise rewrite contract text. Apart from the backend-identity values above and insignificant surrounding blank lines, two repositories using the same contract version and backend must have the same normative contract text.

Do not copy backend-selection, capability-detection, setup-only checks/mutations, or any other text outside the marked contract regions. The generated `docs/agents/issues.md` must not contain references to `ISSUE-MODEL.md`, `github.md`, `local-markdown.md`, this skill directory, or any installation-specific path.

The generated `docs/agents/issues.md` is the project authority after setup. A fresh checkout must be able to interpret the tracker, including the GitHub intake boundary, from repository contents alone.

If a compatible `docs/agents/issues.md` already exists, re-running setup must preserve its backend identity values, including `Intake-Cutover-Number` for GitHub, and must not silently rewrite normative text. If its `Contract-Version: 1` normative text differs from the current version-1 source, stop and require migration or repair.

After the contract exists, if the active harness exposes a project instruction artifact, add or update one short issue-tracker pointer to `docs/agents/issues.md`. Do not copy the contract into project instructions.

### 6. Verify the published contract

Re-read `docs/agents/issues.md` and verify:

- `Model: tracker` and `Contract-Version: 1` are exact;
- the selected backend identity is exact;
- for GitHub, `Intake-Cutover-Number` is a non-negative integer, is unchanged on compatible reruns, and the runtime contract defines the eligibility rule for unclassified issues above versus at/below that boundary;
- the semantic contract region exactly matches the marked semantic source text;
- the runtime contract region exactly matches the marked selected-backend source text;
- setup-only text and contract markers are absent;
- tracked issues require explicit kind and explicit lifecycle status;
- terminal lifecycle states cannot return to a different status through ordinary operations;
- unclassified repository issues are explicitly outside the tracker and setup does not adopt historical ones;
- executable frontier is defined once, in the semantic portion;
- managed work requires a checkable completion condition;
- waiting managed work requires `Waiting for` and `Resume when` content;
- hierarchy and dependency endpoint/cycle rules are present;
- GitHub global invariant checks require complete enumeration rather than a first-page result;
- managed-work assignee is defined as a single execution claim rather than long-lived ownership;
- for GitHub, claim acquisition requires a concrete assignable GitHub login;
- same-issue top-level execution is non-concurrent and subagents do not independently claim it;
- Skill-owned extension sections remain permitted;
- no reference depends on a skill file or installation path.

If project instructions were changed, verify the issue-tracker pointer resolves and is not duplicated.

Setup is complete only when every applicable check passes.

### 7. Stop

Report the configured backend. Do not continue into downstream workflows.
