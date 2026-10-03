# Setup Tracker Behavioral Evals

| # | Scenario | Expected |
| --- | --- | --- |
| 1 | GitHub contains ordinary issues, including one with `tracker:status:ready` but no tracker kind label. | Configure the tracker without inferring classification or modifying existing issues. |
| 2 | GitHub Issues and labels work, but native dependency operations are unavailable. | Setup succeeds; a later workflow that needs the relation checks that capability. |
| 3 | The same backend identity is configured and source contract files are unchanged. | Make only missing backend changes and regenerate the same self-contained `docs/agents/issues.md`; do not append stale content or modify project instructions unless requested. |
| 4 | `docs/agents/issues.md` configures GitHub `owner/a`, but the project resolves to `owner/b` and replacement was not requested. | Stop before changing resources in `owner/b` or rewriting the generated contract. |
| 5 | Setup publishes `docs/agents/issues.md` for either backend. | Identify the configured backend identity and include the complete current issue model plus selected backend representation without Skill-relative dependencies. |
| 6 | The user asks to wire the tracker into project instructions. | Add or update one pointer in an instruction artifact the active environment uses; say what `docs/agents/issues.md` contains and when to read it, and do not guess a filename. |
