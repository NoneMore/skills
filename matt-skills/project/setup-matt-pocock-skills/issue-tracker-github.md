# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

Shared tracker semantics are defined in [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md). This file defines only the GitHub representation, operations, fallbacks, and verification used to realize that contract.

## Repository

**Repository: `<owner>/<repo>`.** Setup replaces this placeholder with the canonical GitHub repository. Treat it as configuration: pass `-R <owner>/<repo>` on tracker commands instead of inferring a repository from the current working directory.

Commands in this adapter are argument contracts: adapt shell syntax without changing the arguments. Quote account selectors such as `"@me"`. Pass generated or multiline Markdown through UTF-8 files or stdin instead of interpolating it into the command line: use `--body-file <file>` / `--body-file -` where available, and `gh api --field "body=@<file>"` / `--field "body=@-"` for API fields. Do not require POSIX heredocs.

## Conventions

- **Create an issue**: `gh issue create -R <owner>/<repo> --title "..." --body "..."`; use `--body-file` for generated or multiline bodies.
- **Read an issue**: `gh issue view <number> -R <owner>/<repo> --comments --json number,title,body,state,labels,comments`.
- **List issues**: `gh issue list -R <owner>/<repo> --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`
- **Comment on an issue**: `gh issue comment <number> -R <owner>/<repo> --body-file <file>` for generated text; `--body "..."` is fine for a short literal.
- **Apply / remove labels**: `gh issue edit <number> -R <owner>/<repo> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> -R <owner>/<repo>`; if a closing note is needed, comment first using the operation above.

Do not rediscover the repository from `git remote -v` after setup; the configured repository above is the source of truth.

## Work-item metadata

- **Role:** read `work-item:<role>` labels. To write a role, remove any other `work-item:*` role labels, add the target label with `gh issue edit <n> -R <owner>/<repo> --add-label "work-item:<role>"` (or `gh pr edit` for a configured PR request surface), and create the target first when missing with `gh label create "work-item:<role>" -R <owner>/<repo> --description "Work item role: <role>"`.
- **Derived from:** read source references from one reserved body line near the top: `Derived-From: #<n>, #<n>`. Missing or `Derived-From: None` means no sources. Preserve the rest of the body when updating this line.

## Relationships

- **Hierarchy**: native sub-issues are canonical. Create a child with `gh issue create -R <owner>/<repo> --parent <parent> ...`, attach an existing issue with `gh issue edit <parent> -R <owner>/<repo> --add-sub-issue <child>`, and read with `gh issue view <parent> -R <owner>/<repo> --json subIssues,subIssuesSummary` or `--json parent` on the child. If unsupported, fall back to `Parent: #<n>` in the child body.
- **Blocking**: native issue dependencies are canonical. Add with `gh issue edit <child> -R <owner>/<repo> --add-blocked-by <blocker>` and inspect with `gh issue view <child> -R <owner>/<repo> --json blockedBy`. If unsupported, fall back to `Blocked by: #<n>, #<n>` in the child body; a ticket is unblocked when every blocker is closed.

Hierarchy says what work a ticket belongs to; blocking says what must finish first. Do not infer one from the other.

## Implementation execution and delivery

Used by `implement`. Eligibility, frontier, coordination, result, and terminal semantics come from [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md); this section defines their GitHub realization.

- **Delivery policy:** `Mode: <direct-commit|pull-request>`. `Target branch: <branch>`. Setup replaces both placeholders. For pull-request mode, publish with `gh pr create -R <owner>/<repo> --base <branch> --fill` when no delivery PR already exists.
- **Execution frontier realization:** enumerate candidate issues with `gh issue list ... --json number,title,body,labels,assignees`; inspect role, tracker state, configured triage label, `blockedBy`, assignees, `execution:suspended`, and child roles with `gh issue view` as needed. Preserve the provider's configured ordering and apply the eligibility/frontier predicates from [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md).
- **Claim / release / suspend:** claim with `gh issue edit <n> -R <owner>/<repo> --add-assignee "@me"`; release with `--remove-assignee "@me"`. Suspension uses one `execution:suspended` label; create it with `gh label create "execution:suspended" -R <owner>/<repo> --description "Implementation execution is suspended"` if missing. Realize contract ordering by adding suspension before removing the assignee, and by assigning the current actor before removing suspension on resume.
- **Implementation Result:** store exactly one issue comment containing `<!-- skills:implementation-result -->` followed by the semantic result required by `implement`. Read comments with `gh api --paginate repos/<owner>/<repo>/issues/<n>/comments`; create the marked comment with `gh issue comment <n> -R <owner>/<repo> --body-file <file>` when absent, otherwise update it with `gh api --method PATCH repos/<owner>/<repo>/issues/comments/<comment-id> --field "body=@<file>"`.
- **Delivery evidence:** for direct-commit mode, run `gh api "repos/<owner>/<repo>/compare/<commit>...<target-branch>" --jq .status`; `ahead` or `identical` means the target contains the commit. For pull-request mode, inspect the recorded PR with `gh pr view <pr> -R <owner>/<repo> --json state,mergedAt,baseRefName,url,mergeCommit`; require merged state and the configured target branch.
- **Terminal operation:** close the issue and clear `execution:suspended` plus any active assignee. The operation is safe to repeat.

## Upstream reconciliation

Used by `reconcile`. The workflow decides requirement satisfaction; this adapter only persists and verifies its inputs/results.

- **Reconciliation Result:** store exactly one issue comment containing `<!-- skills:reconciliation-result -->` followed by the semantic result defined by `reconcile`. Read comments with `gh api --paginate repos/<owner>/<repo>/issues/<n>/comments`; create the marked comment with `gh issue comment <n> -R <owner>/<repo> --body-file <file>` when absent, otherwise update it with `gh api --method PATCH repos/<owner>/<repo>/issues/comments/<comment-id> --field "body=@<file>"`.
- **Source-keyed upstream note:** on each direct provenance source, store one comment keyed by the satisfied spec: `<!-- skills:reconciliation-from:#<spec> -->`. Create it when absent and update that same comment on rerun. The workflow supplies the role-appropriate delivery summary, remaining scope, or realization backlink.

## Post-mutation verification

After a tracker mutation, re-read the affected issue with `gh issue view <n> -R <owner>/<repo> --json number,state,body,labels,assignees,parent,subIssues,blockedBy` plus the configured comment/API read when verifying canonical result or reconciliation-note storage. Verify the semantic fact required by [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md); a successful `gh` exit alone is not sufficient for claim ownership or other race-sensitive writes.

## External-request discovery

- **Operation:** query the REST issue list oldest first, exclude pull requests, and exclude `OWNER`, `MEMBER`, and `COLLABORATOR` author associations:

  `gh api --paginate "repos/<owner>/<repo>/issues?state=open&sort=created&direction=asc&per_page=100" --jq '.[] | select(has("pull_request") | not) | select(.author_association != "OWNER" and .author_association != "MEMBER" and .author_association != "COLLABORATOR") | {number, title, body, createdAt: .created_at, labels: [.labels[].name], author: .user.login, authorAssociation: .author_association}'`

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> -R <owner>/<repo> --comments` and `gh pr diff <number> -R <owner>/<repo>` for the diff.
- **List external PRs for triage**: do **not** request `authorAssociation` from `gh pr list --json`; that field is not exposed there. Query the REST PR list instead, oldest first, and exclude internal associations: `gh api --paginate "repos/<owner>/<repo>/pulls?state=open&sort=created&direction=asc&per_page=100" --jq '.[] | select(.author_association != "OWNER" and .author_association != "MEMBER" and .author_association != "COLLABORATOR") | {number, title, body, createdAt: .created_at, labels: [.labels[].name], author: .user.login, authorAssociation: .author_association}'`.
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
- **Frontier query**: get child identities and map order from `gh issue view <map> -R <owner>/<repo> --json subIssues`; inspect the child facts required by the shared Wayfinder frontier rule with `gh issue view`. If using the task-list fallback, derive the same ordered child set from that list and resolve `Blocked by` references explicitly before applying [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md).
- **Claim**: `gh issue edit <n> -R <owner>/<repo> --add-assignee "@me"`, the session's first write.
- **Resolve**: write `<answer>` to a UTF-8 file, run `gh issue comment <n> -R <owner>/<repo> --body-file <file>`, then `gh issue close <n> -R <owner>/<repo>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
