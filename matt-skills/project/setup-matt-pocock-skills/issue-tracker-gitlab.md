# Issue tracker: GitLab

Issues and specs for this repo live as GitLab issues. Use the [`glab`](https://gitlab.com/gitlab-org/cli) CLI for all operations.

## Project

**Project: `<group/project>`.** Setup replaces this placeholder with the canonical GitLab project (including subgroup namespace when applicable). Treat it as configuration: pass `-R <group/project>` on tracker commands instead of inferring a project from the current working directory. For API endpoints that require a project path, also render `<url-encoded-project-path>` from the same identity (for example `group/subgroup/project` → `group%2Fsubgroup%2Fproject`) instead of relying on cwd-derived `:id` / `:fullpath` placeholders.

## Conventions

- **Create an issue**: `glab issue create -R <group/project> --title "..." --description "..."`. For multi-line descriptions from stdin/heredoc, use `--description-file -`; `--description -` opens an editor and is not the stdin form.
- **Read an issue**: `glab issue view <number> -R <group/project> --comments`. Use `-F json` for machine-readable output.
- **List issues**: `glab issue list -R <group/project> -F json`
- **Comment on an issue**: `glab issue note <number> -R <group/project> --message "..."`. GitLab calls comments "notes".
- **Apply / remove labels**: `glab issue update <number> -R <group/project> --label "..."` / `--unlabel "..."`. Multiple labels can be comma-separated or by repeating the flag.
- **Close**: `glab issue close <number> -R <group/project>`. `glab issue close` does not accept a closing comment, so post the explanation first with `glab issue note <number> -R <group/project> --message "..."`, then close.
- **Merge requests**: GitLab calls PRs "merge requests". Use `glab mr create`, `glab mr view`, `glab mr note`, etc., with the same configured `-R <group/project>`.

Do not rediscover the project from `git remote -v` after setup; the configured project above is the source of truth.

## Work-item metadata

- **Role:** read `work-item:<role>` project labels. To write a role, remove any other `work-item:*` role labels, add the target with `glab issue update <n> -R <group/project> --label "work-item:<role>"` (or `glab mr update` for a configured MR request surface), and create the target first when missing with `glab api --method POST "projects/<url-encoded-project-path>/labels" -f name="work-item:<role>" -f color="#6E7781" -f description="Work item role: <role>"`.
- **Derived from:** read source references from one reserved description line near the top: `Derived-From: #<n>, #<n>`. Missing or `Derived-From: None` means no sources. Preserve the rest of the description when updating this line.

## Hierarchy

Store `Part of #<parent>` near the top of a child description. Role and provenance are independent from hierarchy, blocking, triage state, Wayfinder metadata, and tracker open/closed state.

## Implementation execution and delivery

Used by `implement`. Triage readiness, execution coordination, delivery state, and GitLab open/closed state remain independent even when labels or assignment represent some of them.

- **Delivery policy:** `Mode: <direct-commit|merge-request>`. `Target branch: <branch>`. Setup replaces both placeholders. For merge-request mode, publish from the implementation branch with `glab mr create -R <group/project> --target-branch <branch> --fill --yes` when no delivery MR already exists.
- **Execution frontier:** start from open issues carrying work-item role `request`, `spec`, or `implementation-ticket` plus the configured `ready-for-agent` triage label. Exclude any issue with an assignee, an open blocker, `execution:blocked`, or `execution:awaiting-delivery`. Also exclude a `spec` once it has any child whose role is `implementation-ticket`; those children own execution. Use `glab issue list -R <group/project> --output json` for candidates, then inspect hierarchy/blocking using the configured representations. An explicitly named item may still be read outside the frontier for resume/finalization.
- **Claim:** `glab issue update <n> -R <group/project> --assignee @me`, and make this the implementation session's first tracker mutation. Re-read the item and confirm the assignee plus frontier exclusion before code/test mutation. When resuming a suspended item, assign first and remove its execution label only afterward.
- **Blocked / awaiting delivery:** use labels `execution:blocked` and `execution:awaiting-delivery`, creating them with the project labels API when missing. Add the appropriate label before releasing the active claim with `glab issue update <n> -R <group/project> --unassign`, so the item never re-enters the normal frontier between writes. A real blocker should also use the configured blocking relationship.
- **Implementation Result:** store exactly one canonical issue note containing `<!-- skills:implementation-result -->` followed by the semantic result body required by `implement`. Read notes with `glab api --paginate projects/<url-encoded-project-path>/issues/<iid>/notes`; create the note when the marker is absent, otherwise update that note with `glab api --method PUT projects/<url-encoded-project-path>/issues/<iid>/notes/<note-id> -f body="..."`. Re-entry updates this record instead of appending another.
- **Delivery evidence:** for direct-commit mode, verify the implementation SHA is reachable from the configured target branch using the repository's current Git refs (refresh the target ref before checking). For merge-request mode, inspect the recorded MR with `glab api projects/<url-encoded-project-path>/merge_requests/<iid>`; delivery is complete only when `state` is `merged` and `target_branch` equals the configured target branch.
- **Finalize delivered:** first upsert the Implementation Result to `Outcome: delivered`; then remove any execution coordination label, close the issue, and release the active assignee. Re-read the issue and canonical result; a closed issue with the same delivered result is an idempotent no-op on later entry.
- **Abandon:** upsert `Outcome: abandoned`, close the issue, remove execution labels/active assignee, and re-read both the terminal issue and canonical result.

## Merge requests as a triage surface

**MRs as a request surface: no.** _(Set to `yes` if this repo treats external merge requests as feature requests; `triage` reads this flag.)_

When set to `yes`, MRs run through the same labels and states as issues, using the `glab mr` equivalents:

- **Read an MR**: `glab mr view <number> -R <group/project> --comments` and `glab mr diff <number> -R <group/project>` for the diff.
- **List external MRs for triage**: `glab mr list -R <group/project> -F json`, then keep only submissions whose author username is absent from the configured project's effective member set. Query that set explicitly with `glab api --paginate "projects/<url-encoded-project-path>/members/all" | jq -r '.[].username'`. The `/members/all` endpoint includes inherited members visible to the authenticated user. If membership cannot be established, do not silently classify that MR as external.
- **Comment / label / close**: use `glab mr note <number> -R <group/project>`, `glab mr update <number> -R <group/project> --label`/`--unlabel`, and `glab mr close <number> -R <group/project>`.

Unlike GitHub, GitLab numbers issues and MRs separately, so `#42` is unambiguous once you know which surface the maintainer means.

## When a skill says "publish to the issue tracker"

Create a GitLab issue.

## When a skill says "fetch the relevant ticket"

Run `glab issue view <number> -R <group/project> --comments`.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body. `glab issue create -R <group/project> --label wayfinder:map`.
- **Child ticket**: an issue carrying `Part of #<map>` at the top of its description and labels `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: GitLab's **native blocking link**, the canonical, UI-visible representation. Add it with the `/blocked_by #<n>` quick action, posted as a note (`glab issue note <child> -R <group/project> --message "/blocked_by #<blocker>"`). Native blocking links are a Premium/Ultimate feature; on the free tier (or where unavailable) fall back to a `Blocked by: #<n>, #<n>` line at the top of the description. A ticket is unblocked when every blocker is closed.
- **Frontier query**: `glab issue list -R <group/project> -F json`, keep issues whose description contains `Part of #<map>`, then drop any child with an assignee or an open blocker. Inspect native issue links with `glab api --paginate "projects/<url-encoded-project-path>/issues/<iid>/links"`; a `link_type` of `is_blocked_by` whose linked issue has `state: opened` is a live blocker. With the text fallback, resolve every issue named in the `Blocked by` line and treat any open one as a live blocker. First in map order wins.
- **Claim**: `glab issue update <n> -R <group/project> --assignee @me`, the session's first write.
- **Resolve**: `glab issue note <n> -R <group/project> --message "<answer>"`, then `glab issue close <n> -R <group/project>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
