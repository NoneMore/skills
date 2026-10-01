# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Repository

**Repository: `<owner>/<repo>`.** Setup replaces this placeholder with the canonical GitHub repository. Treat it as configuration: pass `-R <owner>/<repo>` on tracker commands instead of inferring a repository from the current working directory.

## Conventions

- **Create an issue**: `gh issue create -R <owner>/<repo> --title "..." --body "..."`. For multi-line bodies, prefer `--body-file -` with stdin/heredoc.
- **Read an issue**: `gh issue view <number> -R <owner>/<repo> --comments --json number,title,body,state,labels,comments`.
- **List issues**: `gh issue list -R <owner>/<repo> --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> -R <owner>/<repo> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> -R <owner>/<repo> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> -R <owner>/<repo> --comment "..."`

Do not rediscover the repository from `git remote -v` after setup; the configured repository above is the source of truth.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> --comments` and `gh pr diff <number>` for the diff.
- **List external PRs for triage**: do **not** request `authorAssociation` from `gh pr list --json`; that field is not exposed there. Query the REST PR list instead, for example `gh api --paginate "repos/<owner>/<repo>/pulls?state=open&per_page=100" --jq '.[] | select(.author_association == "CONTRIBUTOR" or .author_association == "FIRST_TIME_CONTRIBUTOR" or .author_association == "NONE") | {number, title, body, labels: [.labels[].name], author: .user.login, authorAssociation: .author_association}'`. Fetch comments/details for selected PRs with `gh pr view <number> -R <owner>/<repo> --comments`. Drop `OWNER`/`MEMBER`/`COLLABORATOR`.
- **Comment / label / close**: `gh pr comment`, `gh pr edit --add-label`/`--remove-label`, `gh pr close`.

GitHub shares one number space across issues and PRs, so a bare `#42` may be either: resolve with `gh pr view 42` and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> -R <owner>/<repo> --comments`.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body. `gh issue create -R <owner>/<repo> --label wayfinder:map ...`.
- **Child ticket**: create it as a native sub-issue with `gh issue create -R <owner>/<repo> --parent <map> ...` (or attach an existing issue with `gh issue edit <map> -R <owner>/<repo> --add-sub-issue <child>`). Where the installed GitHub/GHES version lacks native sub-issues, add the child to a task list in the map body and put `Part of #<map>` at the top of the child body. Labels: `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: prefer GitHub's native issue dependencies. Add an edge with `gh issue edit <child> -R <owner>/<repo> --add-blocked-by <blocker>`; inspect it with `gh issue view <child> -R <owner>/<repo> --json blockedBy`. Where dependencies aren't available, fall back to a `Blocked by: #<n>, #<n>` line at the top of the child body. A ticket is unblocked when every blocker is closed.
- **Frontier query**: get child identities from `gh issue view <map> -R <owner>/<repo> --json subIssues`; for open children, inspect `state,assignees,blockedBy` with `gh issue view`. Drop any child with an open blocker or an assignee; first in map order wins. If using the task-list fallback, derive children from that list and resolve `Blocked by` references explicitly.
- **Claim**: `gh issue edit <n> -R <owner>/<repo> --add-assignee @me`, the session's first write.
- **Resolve**: `gh issue comment <n> -R <owner>/<repo> --body "<answer>"`, then `gh issue close <n> -R <owner>/<repo>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
