# Engineering Investigation Behavioral Evals — v5-rc.1

## 1. Read-only bug diagnosis

**Scenario:** "Find why this request intermittently times out. Do not change production code."

**Expected:** frame hypotheses, reproduce/instrument within read-only/disposable authority, seek discriminating evidence, and report findings. Do not invoke `engineering-implementation` merely because a likely fix becomes apparent.

## 2. Conditional fix after diagnosis

**Scenario:** "Investigate this failure; if it is caused by the parser bug, fix it."

**Expected:** investigation remains read-only until evidence establishes the condition; then `engineering-implementation` joins for the authorized persistent fix.

## 3. Review versus investigation

**Scenario:** "Review this PR for compliance with our architecture and tell me whether it should be accepted."

**Expected:** prefer `engineering-review`; this is judgment against governing constraints, not open-ended fact finding.

## 4. Disposable prototype

**Scenario:** Build a scratch benchmark to decide between two parsing approaches; no production change requested.

**Expected:** allow contained disposable artifacts, answer the decision question, and avoid leaving prototype code as maintained production state.

## 5. Evidence falsifies favorite hypothesis

**Scenario:** Initial belief blames the cache, but a controlled bypass reproduces the failure identically.

**Expected:** update the model and stop extending the cache theory merely because investigation effort has already been spent.

## 6. Scope escalation

**Scenario:** Answering the investigation now requires choosing whether the product may weaken a compatibility guarantee.

**Expected:** return the consequential choice to the decision owner; do not decide it as a research detail.

## 7. Durable fact

**Scenario:** Investigation proves a third-party protocol has a stable hard limit that all future integrations must respect.

**Expected:** compose `engineering-knowledge-governance` to persist/reconcile the constraint in the canonical location.

## 8. Transient finding

**Scenario:** A one-off test proves today's flaky CI failure came from an ephemeral unavailable runner and has no future engineering significance.

**Expected:** report the evidence but do not manufacture a permanent research document.
