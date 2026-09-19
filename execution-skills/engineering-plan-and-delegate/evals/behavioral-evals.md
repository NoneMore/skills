# Engineering Plan and Delegate Behavioral Evals — v5-rc.1

## Routing contract

- **Invoke:** explicit user or upstream Meta-Agent selection of plan/delegation mode.
- **Do not infer:** Small/Medium/Large, file count, complexity, risk, or possible subagent use never grants invocation permission.

## 1. Explicit delegation

**Scenario:** `/engineering-plan-and-delegate — split this accepted specification between two coding agents.`

**Expected:** use `engineering-execution-planning`, then `engineering-handoff` for each actual receiving boundary.

## 2. Large workload alone

**Scenario:** Upstream says a migration is Large but does not select plan/delegation mode; Large shaping is handled elsewhere.

**Expected:** this Skill does not auto-invoke from the workload label.

## 3. Medium planning profile

**Scenario:** An upstream Meta-Agent directly requests `engineering-execution-planning` as part of its Medium profile but does not choose delegation mode.

**Expected:** planning can occur without invoking this orchestration wrapper.

## 4. Unresolved consequential design

**Scenario:** Accepted outcome exists, but the plan requires choosing an incompatible public API policy.

**Expected:** return that choice to specification/design rather than hiding it in a delegated task.

## 5. No decomposition needed

**Scenario:** User explicitly invokes plan/delegation, but one bounded executor can complete the work with clear proof obligations.

**Expected:** say direct execution is sufficient; do not manufacture work packages or artificial parallelism.

## 6. Hypothetical handoff

**Scenario:** A plan notes that a future subagent could own a later step, but no handoff is being made now.

**Expected:** do not invoke `engineering-handoff` yet.

## 7. Real handoff

**Scenario:** The primary agent now sends one planned unit to another model.

**Expected:** compose `engineering-handoff` with Outcome, Scope, Governing Sources, Fixed/Local/Open, Verification, and Escalation.

## 8. Capability is not capacity class

**Scenario:** A user-classified Small task has one high-consequence cryptographic choice.

**Expected:** do not reclassify it Medium/Large. Use appropriately strong reasoning for the decision if this mode is explicitly active.
