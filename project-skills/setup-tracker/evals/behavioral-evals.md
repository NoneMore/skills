# Setup Tracker Behavioral Evals

| # | Scenario | Expected |
| --- | --- | --- |
| 1 | GitHub contains ordinary native issues without the supported tracker type/status pair. | Configure the tracker without adopting or modifying those issues. |
| 2 | Work must produce an observable code or behavior change but requires analysis or discovery during implementation. | Classify it as `change`; analysis performed to make the change does not make it an `investigation`. |
| 3 | A tracked parent has one or more tracked children and remains `ready`. | Treat the parent as not being an execution leaf; represent any remaining directly executable work as a child. |
| 4 | A workflow is unsure what to do next, but no named external event or decision prevents project-local work. | Do not move the issue to `waiting`; uncertainty or further analysis is not a waiting condition. |
| 5 | A workflow moves an issue to `waiting`. | Require a named external event or decision in `Waiting for` and a `Resume when` condition that can be checked directly as true or false. |
| 6 | GitHub Issues and labels work, but native dependency operations are unavailable. | Setup succeeds; a later workflow that uses the relation checks that capability. |
| 7 | A tracked issue is `ready` but has an unresolved `BlockedBy` dependency. | Keep `Status` as `ready` while treating it as blocked and not actionable; do not add a duplicate blocked status. |
| 8 | Work is intentionally terminated before its completion condition is satisfied. | Use `cancelled`, not `done`; a cancelled blocker does not satisfy dependents. |
| 9 | A `done` or `cancelled` issue later motivates additional project work. | Keep the terminal issue unchanged and create new tracked work, recording the terminal issue in `Sources` when it is direct provenance. |
| 10 | The same backend identity is configured with `Contract-Version: 2` and source contract files are unchanged. | Make only missing backend changes and regenerate the same self-contained `docs/agents/issues.md`; do not modify project instructions unless requested. |
| 11 | The same backend identity is configured but `Contract-Version` is missing or is not `2`. | Stop before changing backend resources or rewriting `docs/agents/issues.md`; require an explicit user-directed upgrade or migration. |
| 12 | `docs/agents/issues.md` configures GitHub `owner/a`, but the project resolves to `owner/b` and replacement was not requested. | Stop before changing resources in `owner/b` or rewriting the generated contract. |
| 13 | Setup publishes `docs/agents/issues.md` for either backend. | Include `Contract-Version: 2`, the backend identity, and the complete current issue model plus selected backend representation without Skill-relative dependencies. |
| 14 | The user asks to wire the tracker into project instructions. | Add or update one pointer in an instruction artifact the active environment uses; do not guess a filename. |
