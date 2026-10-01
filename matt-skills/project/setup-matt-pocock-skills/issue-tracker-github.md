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

## Work-item metadata

- **Role:** read `work-item:<role>` labels. To write a role, remove any other `work-item:*` role labels, add the target label with `gh issue edit <n> -R <owner>/<repo> --add-label "work-item:<role>"` (or `gh pr edit` for a configured PR request surface), and create the target first when missing with `gh label create "work-item:<role>" -R <owner>/<repo> --description "Work item role: <role>"`.
- **Derived from:** read source references from one reserved body line near the top: `Derived-From: #<n>, #<n>`. Missing or `Derived-From: None` means no sources. Preserve the rest of the body when updating this line.

Role and provenance are independent from hierarchy, blocking, triage state, Wayfinder metadata, and tracker open/closed state.

## Relationships

- **Hierarchy**: native sub-issues are canonical. Create a child with `gh issue create -R <owner>/<repo> --parent <parent> ...`, attach an existing issue with `gh issue edit <parent> -R <owner>/<repo> --add-sub-issue <child>`, and read with `gh issue view <parent> -R <owner>/<repo> --json subIssues,subIssuesSummary` or `--json parent` on the child. If unsupported, fall back to `Parent: #<n>` in the child body.
- **Blocking**: native issue dependencies are canonical. Add with `gh issue edit <child> -R <owner>/<repo> --add-blocked-by <blocker>` and inspect with `gh issue view <child> -R <owner>/<repo> --json blockedBy`. If unsupported, fall back to `Blocked by: #<n>, #<n>` in the child body; a ticket is unblocked when every blocker is closed.

Hierarchy says what work a ticket belongs to; blocking says what must finish first. Do not infer one from the other.

## Implementation execution and delivery

Used by `implement`. Triage readiness, execution coordination, delivery state, and GitHub open/closed state remain independent even when labels or assignment represent some of them.

- **Delivery policy:** `Mode: <direct-commit|pull-request>`. `Target branch: <branch>`. Setup replaces both placeholders. For pull-request mode, publish from the implementation branch with `gh pr create -R <owner>/<repo> --base <branch> --fill` when no delivery PR already exists.
- **Execution frontier:** start from open issues carrying work-item role `request`, `spec`, or `implementation-ticket` plus the configured `ready-for-agent` triage label. Exclude any issue with an assignee, an open blocker, `execution:blocked`, or `execution:awaiting-delivery`. Also exclude a `spec` once it has any child whose role is `implementation-ticket`; those children own execution. Read candidates with `gh issue list ... --json number,title,body,labels,assignees`, then inspect blockers/children with `gh issue view` as needed. An explicitly named item may still be read outside the frontier for resume/finalization.
- **Claim:** `gh issue edit <n> -R <owner>/<repo> --add-assignee @me`, and make this the implementation session's first tracker mutation. Re-read the item and confirm the assignee plus frontier exclusion before code/test mutation. When resuming a suspended item, add the assignee before removing its execution label.
- **Blocked / awaiting delivery:** use labels `execution:blocked` and `execution:awaiting-delivery`, creating either with `gh label create ... -R <owner>/<repo>` if missing. Add the appropriate label before releasing the active assignee with `gh issue edit <n> -R <owner>/<repo> --remove-assignee @me`, so the item never re-enters the normal frontier between writes. A real blocker should also use the configured blocking relationship.
- **Implementation Result:** store exactly one canonical issue comment containing `<!-- skills:implementation-result -->` followed by the semantic result body required by `implement`. Read comments with `gh api --paginate repos/<owner>/<repo>/issues/<n>/comments`; if the marker is absent, create the comment, otherwise update that comment with `gh api --method PATCH repos/<owner>/<repo>/issues/comments/<comment-id> -f body="..."`. Re-entry updates this record instead of appending another.
- **Delivery evidence:** for direct-commit mode, run `gh api "repos/<owner>/<repo>/compare/<commit>...<target-branch>" --jq .status`; delivery is complete only when the result is `ahead` or `identical`, meaning the configured target branch contains the implementation commit. For pull-request mode, inspect the recorded PR with `gh pr view <pr> -R <owner>/<repo> --json state,mergedAt,baseRefName,url,mergeCommit`; delivery is complete only when it is merged and `baseRefName` equals the configured target branch.
- **Finalize delivered:** first upsert the Implementation Result to `Outcome: delivered`; then remove any execution coordination label, close the issue, and remove the active assignee. Re-read the issue and canonical result; a closed issue with the same delivered result is an idempotent no-op on later entry.
- **Abandon:** upsert `Outcome: abandoned`, close the issue, remove execution labels/active assignee, and re-read both the terminal issue and canonical result.

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
