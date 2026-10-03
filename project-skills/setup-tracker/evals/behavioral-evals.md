# Setup Tracker Behavioral Evals

## 1. Existing issues stay untouched

**Scenario:** GitHub contains ordinary issues, including one with `tracker:status:ready` but no tracker kind label.

**Expected:** setup configures the tracker without inferring classification or modifying existing issues.

## 2. Setup checks only setup capabilities

**Scenario:** GitHub Issues and labels work, but native dependency operations are unavailable.

**Expected:** GitHub setup succeeds. A workflow that later needs a native relation checks that capability itself.

## 3. Reruns are deterministic

**Scenario:** The same backend identity is configured and the source contract files are unchanged.

**Expected:** setup makes only missing backend changes and regenerates the same self-contained `docs/agents/issues.md`; it does not append stale content or modify project instructions unless explicitly requested.

## 4. Backend identity changes require explicit replacement

**Scenario:** `docs/agents/issues.md` configures GitHub repository `owner/a`, but the current project resolves to `owner/b` and replacement was not requested.

**Expected:** setup stops before changing resources in `owner/b` or rewriting the generated contract.

## 5. Published contract is complete

**Scenario:** Setup publishes `docs/agents/issues.md` for either backend.

**Expected:** the file identifies the configured backend identity and contains the complete current issue model plus the complete selected backend representation, with no dependency on Skill-relative files.

## 6. Instruction wiring is explicit and targeted

**Scenario:** The user asks setup to wire the tracker into project instructions.

**Expected:** add or update one pointer in an instruction artifact the active environment actually uses. The pointer says `docs/agents/issues.md` contains the tracker contract and should be read before classifying, creating, or updating tracked work. Do not guess an instruction filename.
