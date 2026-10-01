---
name: setup-matt-pocock-skills
description: "Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills."
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker**: where issues live, the exact tracker project/repo identity, and the operations downstream skills rely on (GitHub by default; local markdown is also supported out of the box)
- **Triage labels**: the strings used for the five canonical triage roles
- **Domain docs**: where `CONTEXT.md` and ADRs live, and the consumer rules for reading them

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config`: which remote is the canonical issue-tracker project? Record the exact GitHub `owner/repo` or GitLab `group/project`; don't make downstream skills rediscover it from cwd.
- The active agent harness/runtime when known, its project-instruction loader semantics, and existing candidates such as `AGENTS.override.md`, `AGENTS.md`, `CLAUDE.md`, or configured fallback names. Determine which artifact is actually effective before proposing an edit; filenames are not interchangeable across harnesses.
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/`: does this skill's prior output already exist?
- `.scratch/`: a sign that a local-markdown issue tracker convention is already in use
- Is the `triage` skill installed? Record this only to explain which workflows will consume the vocabulary; Section B still runs because `to-spec` and `to-tickets` also depend on the `ready-for-agent` role.
- Monorepo / multi-context signals: workspace manifests and tooling (`pnpm-workspace.yaml`, package-manager `workspaces`, Cargo workspaces, `go.work`, Nx/Turborepo/Bazel configuration), multiple independently owned packages/apps, or existing bounded-context docs. Treat these as evidence, not a JS-specific gate: absence of any one signal does not prove the repo is single-context.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order. One section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip a section only when exploration already settled it (for example, Section C when there's no monorepo).

**Section A: Issue tracker.**

> Explainer: The "issue tracker" is where issues live for this repo. Skills like `to-tickets`, `triage`, and `to-spec` read from and write to it. They need to know whether to call `gh issue create`, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub**: issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.): collect enough detail to satisfy the tracker contract below instead of recording only a loose paragraph.

Record the choice in `docs/agents/issue-tracker.md`. For GitHub/GitLab, also record the canonical project identity discovered above and have commands target it explicitly rather than relying on the current working directory's remote. The GitHub and GitLab templates carry a "PRs/MRs as a request surface" flag, defaulted **off**. Leave it off and don't raise it: a user who wants external PRs/MRs in the triage queue can flip the flag in the file later.

For **Other** trackers, `docs/agents/issue-tracker.md` is a capability contract, not freeform notes. It must say how to perform, or explicitly mark unsupported and give a fallback for:

- identify the exact project/workspace;
- create, read, list/search, and comment on a ticket;
- apply/remove the configured triage state and terminally close/reject an item;
- create parent/child relationships or the fallback representation;
- add/read blocking relationships or the fallback representation;
- claim work and query the Wayfinder frontier (open + unblocked + unclaimed children);
- re-read an item after mutation so consumers can verify persisted state.

If the tracker cannot support one of these operations, write the limitation and durable fallback into the document so consumers never have to invent tracker behavior.

**Section B: Triage label vocabulary.** Always configure this vocabulary. `triage` consumes it when installed, and `to-spec` / `to-tickets` consume the `ready-for-agent` role even when `triage` itself is absent. Ask exactly one question:

> Do you want to keep the default triage labels? (recommended: **yes**)

The defaults are the five canonical roles, each label string equal to its name: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. On **yes**, write them as-is. Only if the user says no, usually because their tracker already uses other names (e.g. `bug:triage` for `needs-triage`), collect the overrides so `triage` applies existing labels instead of creating duplicates.

**Section C: Domain docs.** Default to **single-context** (one `CONTEXT.md` + `docs/adr/` at the repo root) when exploration found no meaningful multi-context evidence. Write it without asking in that case.

Offer **multi-context** (a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files) when exploration found credible multi-context evidence, whether or not the repo uses a JavaScript workspace tool. Then confirm which layout they want.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, and `docs/agents/triage-labels.md`

Let them edit before writing.

### 4. Write

**Pick the instruction artifact to edit:**

- Honor an explicitly requested artifact first.
- Otherwise use the active harness's effective project-instruction loader semantics discovered in step 1. Edit an existing artifact only if that harness will actually load it at the intended scope.
- Do **not** hard-code `CLAUDE.md` over `AGENTS.md`, or vice versa. For example, Codex normally selects `AGENTS.override.md` then `AGENTS.md` then configured fallback names; Pi normally selects `AGENTS.override.md`, `AGENTS.md`, `AGENTS.MD`, `CLAUDE.md`, then `CLAUDE.MD` within a directory.
- If exact loader behavior is unavailable and multiple plausible artifacts exist, ask which runtime/artifact should receive the block. If none exists, propose the active harness's normal project artifact; fall back to `AGENTS.md` only when no better loader evidence exists.
- If an installed harness-authoring/reference skill (such as `agents-md-wizard`) is available, use its maintained loader profile instead of duplicating stale assumptions here.

Never create or edit a file merely because its name looks familiar; the goal is for the `## Agent skills` block to be loaded by the runtime that will consume it.

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
