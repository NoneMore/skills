---
name: setup-matt-pocock-skills
description: "Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills."
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker**: where issues live, the exact tracker project/repo identity, execution coordination, repository delivery policy, and the operations downstream skills rely on (GitHub by default; local markdown is also supported out of the box)
- **Triage labels**: the strings used for the five canonical triage roles
- **Domain docs**: where `CONTEXT.md` and ADRs live, and the consumer rules for reading them

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config`: enumerate GitHub/GitLab tracker candidates and their exact `owner/repo` or `group/project` identities. If there is exactly one candidate, propose it in Section A; if there are multiple, let the user choose the canonical project.
- Determine the active harness/runtime's project-instruction loader semantics from the environment or a maintained harness profile, and inspect the files that loader can select.
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/`: does this skill's prior output already exist?

### 2. Present findings and ask

Summarise what's present and what's missing. Then take Sections A–C in order and ask only the questions specified below.

**Section A: Issue tracker.**

> Choose where this repo tracks work; downstream engineering skills read and write through this configuration.

If Section 1 found exactly one GitHub/GitLab tracker candidate, propose it. If it found multiple candidates, present them and ask which project is canonical. If it found none, offer:

- **GitHub**: issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.): collect the operations listed in the tracker contract below.

Record the choice in `docs/agents/issue-tracker.md`. For GitHub/GitLab, also record the canonical project identity discovered above and have commands target it explicitly rather than relying on the current working directory's remote. The GitHub and GitLab templates carry a "PRs/MRs as a request surface" flag, defaulted **off**. Leave it off and don't raise it: a user who wants external PRs/MRs in the triage queue can flip the flag in the file later.

For **Other** trackers, `docs/agents/issue-tracker.md` is a capability contract, not freeform notes. For each item below, give the concrete operation or explicitly mark it unsupported with a durable fallback:

- exact project/workspace identity;
- ticket create/read/list-search/comment, apply/remove triage state, and terminal close/reject;
- read/write work-item role for `request`, `decision-map`, `decision-ticket`, `spec`, and `implementation-ticket`;
- read/write `derived-from` as zero or more direct tracker sources stored on the derived artifact; a direct source is an artifact used as input to create the current artifact, without following that source's own provenance;
- create/read parent-child and blocking relationships;
- implementation lifecycle operations: execution frontier, claim/release/suspend, canonical Implementation Result upsert, repository delivery policy/evidence, and terminal finalize/abandon;
- claiming and the Wayfinder frontier (open + unblocked + unclaimed children);
- a post-mutation verification operation so consumers can confirm persisted state.

Work-item role, `derived-from`, hierarchy, blocking, triage state, Wayfinder lifecycle, and tracker open/closed state are independent; do not infer one from another.

Consumers should never have to invent missing tracker behavior.

Then establish the repository delivery policy. Determine the repository's default branch from remote/project metadata when available and propose it as the target. Ask one question:

> When should implementation count as delivered to `<target-branch>`: after a verified direct commit reaches that branch, or only after a PR/MR is merged into it? If the target branch is different, name it.

Record the chosen mode, target branch, delivery publication operation when applicable, and concrete completion-evidence operation in `docs/agents/issue-tracker.md`. Delivery policy is repository configuration: `implement` consumes it and must not invent GitHub/GitLab-specific delivery rules.

**Section B: Triage label vocabulary.** These are triage-state roles, not work-item roles. Always configure this vocabulary. `triage` consumes it when installed, and `to-spec` / `to-tickets` consume the `ready-for-agent` role even when `triage` itself is absent. Ask exactly one question:

> Do you want to keep the default triage labels? (recommended: **yes**)

The defaults are the five canonical roles, each label string equal to its name: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. On **yes**, write them as-is. Only if the user says no, usually because their tracker already uses other names (e.g. `bug:triage` for `needs-triage`), collect the overrides so `triage` applies existing labels instead of creating duplicates.

**Section C: Domain docs.** If an existing `docs/agents/domain.md` declares a layout, preserve it unless the user asked to change it. Otherwise ask the user to choose **single-context** (one root `CONTEXT.md` + `docs/adr/`) or **multi-context** (a root `CONTEXT-MAP.md` pointing to per-context docs).

### 3. Resolve the instruction target and confirm the draft

Resolve the instruction artifact **before** asking the user to approve the draft:

- If the user explicitly named an artifact, use it; if the active runtime will not load it, say so before confirmation rather than silently substituting another file.
- Otherwise use the loader semantics from step 1 to select the effective project artifact.
- If an installed harness-authoring/reference skill (such as `agents-md-wizard`) is available, use its maintained loader profile rather than copying harness-specific filename ordering into this skill.
- If loader semantics do not identify a target, ask which runtime/artifact should receive the block. Do not invent a filename fallback.

Then show the user the selected instruction artifact and a draft of:

- The `## Agent skills` block to write there
- The contents of `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, and `docs/agents/triage-labels.md`

Let them edit before writing. Do not proceed until the write target and draft are both settled.

### 4. Write

Write the approved `## Agent skills` block to the instruction artifact selected in step 3.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

[one-line summary of layout: "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

Always include the `### Triage labels` sub-block and write `docs/agents/triage-labels.md`; publishing skills need the vocabulary even when the `triage` skill is not installed.

Then write the docs files using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md): GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md): local-markdown issue tracker
- [triage-labels.md](./triage-labels.md): label mapping used by triage and publishing workflows
- [domain.md](./domain.md): domain doc consumer rules + layout

For "other" issue trackers, write `docs/agents/issue-tracker.md` from scratch against the capability contract in Section A, using the user's tracker workflow for the concrete operations and fallbacks.

### 5. Done

Tell the user the setup is complete and which engineering skills will now read from these files. Mention they can edit `docs/agents/*.md` directly later; re-run this skill when switching tracker/project identity, changing the effective harness instruction artifact, or intentionally rebuilding the configuration from scratch.
