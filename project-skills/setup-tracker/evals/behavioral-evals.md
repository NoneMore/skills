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

**Expected:** the generated contract contains the managed-work requirement for an issue-specific, checkable completion condition and contains `Waiting for` / `Resume when` requirements for every tracked issue whose status is `waiting`, including intake.

## 5. Generated contract preserves relation semantics

**Scenario:** Setup publishes `docs/agents/issues.md` for either backend.

**Expected:** the generated contract preserves the issue model's relation constraints: intake may be a source; parent and blocking relations are managed-work-only; self-relations and cycles are forbidden where specified.

## 6. Reruns are deterministic and instruction wiring is opt-in

**Scenario:** The same backend is already configured, source contract files are unchanged, and setup is run again without a request to edit project instructions.

**Expected:** create only missing setup configuration, rebuild `docs/agents/issues.md` to the same content rather than appending duplicate contract text, leave tracked issues untouched, and do not modify project instructions.
