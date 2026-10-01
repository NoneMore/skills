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

## Work-item identity and provenance

The shared work-item protocol uses one semantic role per participating item:

- `request`
- `decision-map`
- `decision-ticket`
- `spec`
- `implementation-ticket`

**Role representation:** use exactly one `work-item:<role>` project label. Read role from those labels; if more than one canonical role label is present, treat the item as inconsistent rather than guessing. Apply the role with `glab issue update <n> -R <group/project> --label "work-item:<role>"` (or the `glab mr update` equivalent when an MR is configured as a request surface), removing any conflicting canonical role label first. If a required role label does not exist, create it through the project labels API: `glab api --method POST "projects/<url-encoded-project-path>/labels" -f name="work-item:<role>" -f color="#6E7781" -f description="Work item role: <role>"`.

**Provenance representation:** store zero or more immediate sources on the derived artifact as one reserved description line near the top:

```text
Derived-From: #<n>, #<n>
```

A missing line or `Derived-From: None` means an empty source set. Read only the immediate references on that line. Do not copy transitive ancestors. When writing provenance to an existing item, read its full description, replace or insert only the reserved line, preserve the remaining description verbatim, then write the complete description back.

Role identifies what the artifact is. `Derived-From` explains which immediate earlier artifacts materially informed it. Neither is hierarchy, blocking, triage state, Wayfinder type/state, or tracker open/closed state; never infer one from another.

After changing role or provenance, re-read the item and verify the persisted role and immediate source set.

## Relationships

- **Hierarchy**: use native parent/child relationships where the configured GitLab tier/API exposes them. Otherwise persist `Parent: #<n>` in the child description and read hierarchy from that reserved line.
- **Blocking**: use GitLab's native blocking link where available. Add it with the `/blocked_by #<n>` quick action posted as a note. On tiers where native blocking links are unavailable, fall back to `Blocked by: #<n>, #<n>` in the child description; a ticket is unblocked when every blocker is closed.

Hierarchy says what work a ticket belongs to; blocking says what must finish first; provenance says why a derived artifact exists. Do not infer any one from another.

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

- **Map**: a single issue with work-item role `decision-map` plus label `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body and any `Derived-From` sources. `glab issue create -R <group/project> --label wayfinder:map`, then persist the work-item role through the operation above.
- **Child ticket**: an issue with work-item role `decision-ticket`, linked to the map through the hierarchy representation above and labelled `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). The Wayfinder type is not the work-item role. Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: GitLab's **native blocking link**, the canonical, UI-visible representation. Add it with the `/blocked_by #<n>` quick action, posted as a note (`glab issue note <child> -R <group/project> --message "/blocked_by #<blocker>"`). Native blocking links are a Premium/Ultimate feature; on the free tier (or where unavailable) fall back to a `Blocked by: #<n>, #<n>` line at the top of the description. A ticket is unblocked when every blocker is closed.
- **Frontier query**: `glab issue list -R <group/project> -F json` scoped to the map's children, then drop any child with an assignee or an open blocker. Inspect native issue links with `glab api --paginate "projects/<url-encoded-project-path>/issues/<iid>/links"`; a `link_type` of `is_blocked_by` whose linked issue has `state: opened` is a live blocker. With the text fallback, resolve every issue named in the `Blocked by` line and treat any open one as a live blocker. First in map order wins.
- **Claim**: `glab issue update <n> -R <group/project> --assignee @me`, the session's first write.
- **Resolve**: `glab issue note <n> -R <group/project> --message "<answer>"`, then `glab issue close <n> -R <group/project>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
