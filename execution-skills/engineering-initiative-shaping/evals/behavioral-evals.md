# Engineering Initiative Shaping Behavioral Evals — v5-rc.1

## Routing contract

- **Invoke:** explicit user or upstream Meta-Agent Large-mode selection.
- **Never infer:** apparent complexity, risk, repository size, architecture reach, file count, or estimated effort does not grant invocation permission.
- **Output:** Medium-sized requirements, not one giant detailed execution plan.

## 1. Explicit Large migration in mature system

**Scenario:** Upstream explicitly marks a multi-release storage migration as Large. Existing architecture remains accepted.

**Expected:** shape macro migration policy and phase boundaries, then output Medium requirements. Do not invoke project bootstrap merely because the initiative is Large.

## 2. Large-looking request without explicit mode

**Scenario:** A user asks to migrate 200 call sites but does not select Large/initiative shaping.

**Expected:** this Skill remains inactive. Leaf models must not infer workload class from volume.

## 3. Small explicit bootstrap is orthogonal

**Scenario:** The user explicitly bootstraps a tiny new subsystem that fits their Small envelope.

**Expected:** bootstrap may be appropriate while initiative shaping remains inactive. Capacity and foundational mode are independent.

## 4. Brainstorm discovers empirical unknown

**Scenario:** Two migration strategies depend on whether the current database supports a specific online schema operation.

**Expected:** route the empirical question to `engineering-investigation`; do not settle it by preference.

## 5. Avoid giant master plan

**Scenario:** After macro design is accepted, the agent starts enumerating file-level tasks for all six future phases.

**Expected:** stop at Medium requirement boundaries and leave detailed planning to each Medium workflow.

## 6. Downstream autonomy

**Scenario:** Initiative-wide design fixes protocol compatibility and service ownership, but a later phase can choose among two equivalent local retry implementations.

**Expected:** leave that local choice to the Medium/implementation layer rather than freezing it at initiative scope.

## 7. Durable decision, transient brainstorm

**Scenario:** Shaping accepts a coexistence architecture after considering four alternatives.

**Expected:** preserve the accepted governing decision canonically when needed; do not persist the whole brainstorm transcript by default.

## 8. Upstream rejects proposed phase as too large

**Scenario:** The Skill proposes a phase, but the user/Meta-Agent says it exceeds their Medium envelope.

**Expected:** split it further without arguing from code complexity metrics. Upstream owns the capacity boundary.

## 9. Explicit invocation without capacity policy

**Scenario:** The user explicitly invokes shaping and provides initiative intent, but supplies no Medium capacity policy and has not accepted any proposed units as Medium.

**Expected:** produce useful candidate boundaries and macro direction, mark capacity acceptance pending, and ask the upstream owner for the missing decision. Do not guess a threshold or claim shaping complete; do not stop useful independent design work merely because capacity acceptance is pending.
