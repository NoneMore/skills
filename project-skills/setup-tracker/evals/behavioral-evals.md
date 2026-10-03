# Setup Tracker Behavioral Evals

| # | Scenario | Expected |
| --- | --- | --- |
| 1 | GitHub contains ordinary native issues with no `tracker:status:*` label. | Configure the tracker without adopting or modifying those issues. |
| 2 | A GitHub issue has `tracker:status:ready` but no tracker type label. | Treat it as tracked but invalid; setup does not repair or rewrite the issue. |
| 3 | A GitHub issue has both `tracker:status:ready` and legacy `tracker:status:needs-triage`. | Treat it as tracked but invalid because it has more than one `tracker:status:*` label and one is unsupported; setup does not repair or rewrite it. |
| 4 | GitHub Issues and labels work, but native dependency operations are unavailable. | Setup succeeds; a later workflow that needs the relation checks that capability. |
| 5 | A valid issue is `ready` but has an unresolved `BlockedBy` dependency. | The published contract keeps its `Status` as `ready` while defining it as blocked and not actionable until the dependency is satisfied; do not add a duplicate blocked status. |
| 6 | Work is intentionally terminated before its completion condition is satisfied. | The published contract uses `cancelled`, not `done`; `done` means the completion condition is satisfied, and a cancelled blocker does not by itself satisfy dependents. |
| 7 | A `done` or `cancelled` issue later motivates additional project work. | Keep the terminal issue unchanged and represent the later work as a new tracked issue, recording the terminal issue in `Sources` when it is direct provenance. |
| 8 | The same backend identity is configured with `Contract-Version: 2` and source contract files are unchanged. | Make only missing backend changes and regenerate the same self-contained `docs/agents/issues.md`; do not append stale content or modify project instructions unless requested. |
| 9 | The same backend identity is configured but `Contract-Version` is missing or is not `2`. | Stop before changing backend resources or rewriting `docs/agents/issues.md`; report that explicit user-directed upgrade or migration is required. |
| 10 | `docs/agents/issues.md` configures GitHub `owner/a`, but the project resolves to `owner/b` and replacement was not requested. | Stop before changing resources in `owner/b` or rewriting the generated contract. |
| 11 | Setup publishes `docs/agents/issues.md` for either backend. | Include `Contract-Version: 2`, identify the configured backend identity, and include the complete current issue model plus selected backend representation without Skill-relative dependencies. |
| 12 | The user asks to wire the tracker into project instructions. | Add or update one pointer in an instruction artifact the active environment uses; say what `docs/agents/issues.md` contains and when to read it, and do not guess a filename. |
| 13 | Legacy `tracker:kind:*` or `tracker:status:needs-triage` labels already exist. | Create only missing current required labels and preserve legacy labels; setup does not migrate existing issues. |
