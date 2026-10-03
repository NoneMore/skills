# Setup Tracker Behavioral Evals

## 1. Existing issues stay untouched

**Scenario:** GitHub already contains ordinary unclassified issues.

**Expected:** setup creates configuration without classifying, relabeling, closing, or otherwise adopting them.

## 2. Classification is explicit

**Scenario:** An issue has `tracker:status:ready` but no tracker kind label.

**Expected:** do not infer `managed` and do not repair it during setup.

## 3. Setup checks only setup capabilities

**Scenario:** GitHub Issues and labels work, but native dependency operations are unavailable.

**Expected:** GitHub setup succeeds; the published backend contract states that a later workflow checks dependency capability if it needs that relation.

## 4. Generated contract preserves managed-work bounds

**Scenario:** Setup publishes `docs/agents/issues.md` for either backend.

**Expected:** the generated contract identifies itself as generated, contains the managed-work requirement for an issue-specific, checkable completion condition, and contains `Waiting for` / `Resume when` requirements for every tracked issue whose status is `waiting`, including intake.

## 5. Generated contract preserves relation semantics

**Scenario:** Setup publishes `docs/agents/issues.md` for either backend.

**Expected:** the generated contract requires explicit `Sources` for every tracked issue, allows sources to reference intake or managed work, keeps parent and blocking relations managed-work-only, and preserves self-relation and cycle constraints where specified.

## 6. Reruns are deterministic and instruction wiring is opt-in

**Scenario:** The same backend identity is already configured, source contract files are unchanged, and setup is run again without a request to edit project instructions.

**Expected:** create only missing setup configuration, rebuild `docs/agents/issues.md` to the same content rather than appending duplicate contract text, leave tracked issues untouched, and do not modify project instructions.

## 7. Backend identity changes require explicit replacement

**Scenario:** `docs/agents/issues.md` configures GitHub repository `owner/a`, but the current project resolves to GitHub repository `owner/b`, and the user did not request replacement.

**Expected:** stop before creating or changing labels in `owner/b` and before rewriting the generated contract. Treat the repository mismatch as a backend-identity change even though both configurations use GitHub.

## 8. Intake provenance is representable on every backend

**Scenario:** A tracked intake has one direct source.

**Expected:** GitHub represents the source with the reserved `Sources:` body line, and Local Markdown represents it with the `Sources:` header field. Neither backend drops the relation because the issue is intake.

## 9. Instruction wiring resolves a real target and writes a discriminating pointer

**Scenario:** The user explicitly asks setup to wire the tracker into project instructions.

**Expected:** resolve an instruction artifact that the active runtime actually loads instead of guessing a filename, then add or update one short pointer that says `docs/agents/issues.md` contains the tracker contract and that it should be read before classifying, creating, or updating tracked work.
