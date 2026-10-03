# Setup Tracker Behavioral Evals

These scenarios exercise the small contract that `setup-tracker` is responsible for.

## 1. Setup does not adopt existing issues

**Scenario:** A GitHub repository already contains ordinary unclassified issues before setup.

**Expected:** setup creates missing tracker labels and the repository contract without classifying, relabeling, closing, or otherwise modifying those issues.

**Failure signs:** inferring tracker state from issue age, open/closed state, or missing labels; bulk-adopting existing issues.

## 2. Classification stays explicit

**Scenario:** An issue has `tracker:status:ready` but no tracker kind label.

**Expected:** treat it as invalid tracker-shaped state, not implicitly as managed work. Setup itself does not repair the issue.

**Failure signs:** inferring `managed` from status or silently rewriting the issue.

## 3. GitHub setup requires only setup capabilities

**Scenario:** Issues and labels are usable, but the active tooling does not expose native dependency operations.

**Expected:** setup can still configure the GitHub backend. A later workflow that needs dependencies checks that capability when it uses the relation.

**Failure signs:** rejecting GitHub setup solely because an unused relation capability is unavailable.

## 4. Managed work has a completion condition

**Scenario:** A workflow creates managed work without a checkable completion condition.

**Expected:** reject or complete the missing condition before treating the issue as valid managed work.

**Failure signs:** accepting vague managed work whose completion cannot be checked.

## 5. Waiting records a resume condition

**Scenario:** A tracked issue is moved to `waiting` because an external decision is required.

**Expected:** record both what it is waiting for and a checkable `Resume when` condition.

**Failure signs:** using `waiting` as an unexplained parking state.

## 6. Relations preserve their meaning

**Scenario:** A workflow wants to add an intake issue as a parent or create a dependency cycle between managed issues.

**Expected:** reject the relation. Intake may be a source, while hierarchy and dependencies are managed-work-only and acyclic.

**Failure signs:** conflating provenance with hierarchy/dependency or accepting a cycle.
