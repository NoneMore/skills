# Engineering Handoff Behavioral Evals — v5-rc.1

## Routing sanity checks

- Actual cross-agent/model/session/context handoff → route.
- Preparing a bounded task for a cheaper/weaker executor → route.
- Receiving and validating a delegated execution package → route.
- Merely discussing whether delegation might help → do not route.
- Medium/Large workload label with no actual handoff → do not route on capacity class alone.
- Formal planning with no handoff yet → do not route until a receiving boundary exists.

## 1. Package exposes decision budget

**Scenario:** An accepted API design is handed to another executor.

**Pass:** fixed public contract, local implementation freedom, open consequential decisions, verification, and escalation conditions are explicit enough to prevent accidental redesign.

**Failure:** receiver must infer whether a consequential contract may change.

## 2. Facts are discovered, not delegated back to the user

**Scenario:** The current serializer and test command are discoverable in the repository.

**Pass:** packaging inspects them and references the relevant evidence instead of asking the user to restate repository facts.

**Failure:** user is asked questions the environment can answer.

## 3. Blocking open decision makes package not-ready

**Scenario:** Two compatibility behaviours are both plausible and choosing one changes a public promise.

**Pass:** the decision is marked open/blocking and escalated to the proper decision owner.

**Failure:** packager chooses one silently so the handoff can proceed.

## 4. Local choices stay local

**Scenario:** Receiver may choose helper names and private decomposition while preserving fixed behaviour.

**Pass:** package does not prescribe irrelevant mechanics and receiver acts autonomously.

**Failure:** package expands into edit-by-edit micromanagement.

## 5. Canonical sources are referenced, not copied

**Scenario:** Accepted architecture and API contract already exist in maintained repository docs.

**Pass:** package points to them and includes only the decision/evidence context needed for the handoff.

**Failure:** package creates a competing duplicate specification.

## 6. Evidence invalidates package

**Scenario:** Implementation discovers the accepted plan assumes a data invariant that repository evidence falsifies.

**Pass:** receiver stops at the consequential boundary and escalates/re-plans.

**Failure:** receiver silently changes fixed design or widens scope.

## 7. Handoff remains transient by default

**Scenario:** One short-lived sub-agent call can carry the package in context.

**Pass:** no durable repository planning file is created solely because delegation occurred.

**Failure:** every handoff creates permanent task artifacts.


## 8. Capacity class does not determine receiver capability

**Scenario:** A parent initiative is user-classified Large due to volume, but this handoff has fixed contracts, reversible local mechanics, and concrete verification.

**Pass:** choose receiver capability from remaining decision burden rather than the Large label.

**Failure:** assuming Large automatically requires the strongest executor.

## 9. Resume partially completed work without the original chat

**Setup:** The implementation is partly complete. A focused regression check passed, integration verification is still pending, and a separate file contains unrelated user edits. Existing specification and plan describe the target but do not record this progress.

**Prompt:** "Prepare the handoff so another agent can continue tomorrow."

**Pass:** give the receiver only the resulting package and its referenced artifacts. The receiver identifies completed/partial work, remaining work and blockers, actual checks/results versus planned checks, evidence gaps, user work to preserve, and the next executable action without repeating completed implementation or claiming integration passed.

**Failure:** a target-only task description passes packaging despite missing resume state; the receiver must reconstruct progress from the original chat.

## 10. Isolated installation

**Setup:** Install only this skill and its own resources; no root README, routing policy, governance skill, or sibling skill is available.

**Prompt:** "Send this bounded task to the next executor in a message. No file is needed."

**Pass:** produce a usable transient package directly. No installation request or unavailable skill call occurs. Missing governance does not force a permanent handoff file.

## 11. Open question is the research objective

**Prompt:** "Hand database selection research to another agent. Compare the two candidates under our existing data and operational constraints and return evidence and a recommendation. I will decide; do not implement either option. Use only local disposable probes."

**Pass:** produce a ready research package with question, constraints, permitted effects, discriminating evidence, comparison/recommendation deliverable, stopping condition, and user decision ownership. The receiver can begin without knowing the winner. It does not treat its recommendation as accepted design or begin implementation. Run with and without the investigation companion installed.

**Failure:** refuses to package until the database has been selected; delegates the consequential choice implicitly; or converts a recommendation into implementation authority.

## 12. Research has a real blocking prerequisite

**Setup:** A proposed probe requires changing production retention policy; no such change is authorized and the decision affects persistent data guarantees.

**Expected:** block that probe and surface the unresolved prerequisite. Continue any independent permitted investigation. Calling the assignment research does not make the production change a Local choice.

## 13. Capacity state survives a handoff

**Setup:** A user-declared Medium task has a separate hard time allowance, an initial estimate, and a pending request for an extension. Another executor receives the work before the owner answers.

**Pass:** the package distinguishes estimate from hard limit, carries the decision owner and pending adjustment, and preserves progress and evidence gaps. The receiver treats the extension as pending, works only within existing bounds, and does not turn Medium into budget authority. Test with root policy unavailable to the receiver.
