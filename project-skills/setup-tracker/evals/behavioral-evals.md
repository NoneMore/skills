# Setup Tracker Behavioral Evals

## 1. Existing issues stay untouched

**Scenario:** GitHub already contains ordinary unclassified issues.

**Expected:** setup creates configuration without classifying, relabeling, closing, or otherwise adopting them.

## 2. Classification is explicit

**Scenario:** An issue has `tracker:status:ready` but no tracker kind label.

**Expected:** do not infer `managed` and do not repair it during setup.

## 3. Setup checks only setup capabilities

**Scenario:** GitHub Issues and labels work, but native dependency operations are unavailable.

**Expected:** GitHub setup succeeds; a later workflow checks dependency capability if it needs that relation.

## 4. Managed work is bounded

**Scenario:** Managed work lacks a checkable completion condition, or `waiting` lacks `Waiting for` / `Resume when`.

**Expected:** treat the issue as incomplete until those required contents exist.

## 5. Relations keep their meaning

**Scenario:** A workflow tries to use intake as a parent or create a managed-work dependency cycle.

**Expected:** reject the relation. Intake may be a source; hierarchy and dependencies are managed-work-only and acyclic.

## 6. Reruns are idempotent and instruction wiring is opt-in

**Scenario:** The same backend is already configured and setup is run again without a request to edit project instructions.

**Expected:** create only missing setup configuration, refresh `docs/agents/issues.md`, leave tracked issues untouched, and do not modify project instructions.
