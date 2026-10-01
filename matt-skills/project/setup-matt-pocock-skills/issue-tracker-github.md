# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Repository

**Repository: `<owner>/<repo>`.** Setup replaces this placeholder with the canonical GitHub repository. Treat it as configuration: pass `-R <owner>/<repo>` on tracker commands instead of inferring a repository from the current working directory.

## Conventions

- **Create an issue**: `gh issue create -R <owner>/<repo> --title "..." --body "..."`. For multi-line bodies, use `--body-file -` with stdin/heredoc.
- **Read an issue**: `gh issue view <number> -R <owner>/<repo> --comments --json number,title,body,state,labels,comments`.
- **List issues**: `gh issue list -R <owner>/<repo> --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`
- **Comment on an issue**: `gh issue comment <number> -R <owner>/<repo> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> -R <owner>/<repo> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> -R <owner>/<repo> --comment "..."`

Do not rediscover the repository from `git remote -v` after setup; the configured repository above is the source of truth.

## Relationships

- **Hierarchy**: native sub-issues are canonical. Create a child with `gh issue create -R <owner>/<repo> --parent <parent> ...`, attach an existing issue with `gh issue edit <parent> -R <owner>/<repo> --add-sub-issue <child>`, and read with `gh issue view <parent> -R <owner>/<repo> --json subIssues,subIssuesSummary` or `--json parent` on the child. If unsupported, fall back to `Parent: #<n>` in the child body.
- **Blocking**: native issue dependencies are canonical. Add with `gh issue edit <child> -R <owner>/<repo> --add-blocked-by <blocker>` and inspect with `gh issue view <child> -R <owner>/<repo> --json blockedBy`. If unsupported, fall back to `Blocked by: #<n>, #<n>` in the child body; a ticket is unblocked when every blocker is closed.

Hierarchy says what work a ticket belongs to; blocking says what must finish first. Do not infer one from the other.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> -R <owner>/<repo> --comments` and `gh pr diff <number> -R <owner>/<repo>` for the diff.
- **List external PRs for triage**: do **not** request `authorAssociation` from `gh pr list --json`; that field is not exposed there. Query the REST PR list instead, oldest first, and exclude internal associations: `gh api --paginate "repos/<owner>/<repo>/pulls?state=open&sort=created&direction=asc&per_page=100" --jq '.[] | select(.author_association != "OWNER" and .author_association != "MEMBER" and .author_association != "COLLABORATOR") | {number, title, body, createdAt: .created_at, labels: [.labels[].name], author: .user.login, authorAssociation: .author_association}'`. Fetch comments/details for selected PRs with `gh pr view <number> -R <owner>/<repo> --comments`.
- **Comment / label / close**: use `gh pr comment <number> -R <owner>/<repo>`, `gh pr edit <number> -R <owner>/<repo> --add-label`/`--remove-label`, and `gh pr close <number> -R <owner>/<repo>`.

GitHub shares one number space across issues and PRs, so a bare `#42` may be either: resolve with `gh pr view 42 -R <owner>/<repo>` and fall back to `gh issue view 42 -R <owner>/<repo>`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue. When decomposing an existing issue/spec, use the configured hierarchy above; when there is no source issue, do not invent a synthetic parent.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> -R <owner>/<repo> --comments`.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body. `gh issue create -R <owner>/<repo> --label wayfinder:map ...`.
- **Child ticket**: link it to the map using the hierarchy above; with the hierarchy fallback, maintain the map task list so the frontier can enumerate children. Labels: `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Once claimed, assign it to the driving dev.
- **Blocking**: use the blocking representation above.
- **Frontier query**: get child identities from `gh issue view <map> -R <owner>/<repo> --json subIssues`; for open children, inspect `state,assignees,blockedBy` with `gh issue view`. Drop any child with an open blocker or an assignee; first in map order wins. If using the task-list fallback, derive children from that list and resolve `Blocked by` references explicitly.
- **Claim**: `gh issue edit <n> -R <owner>/<repo> --add-assignee @me`, the session's first write.
- **Resolve**: `gh issue comment <n> -R <owner>/<repo> --body "<answer>"`, then `gh issue close <n> -R <owner>/<repo>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
