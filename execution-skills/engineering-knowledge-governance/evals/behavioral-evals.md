# Engineering Knowledge Governance Behavioral Evals — v5-rc.1

These portable scenarios evaluate whether the skill creates disciplined durable knowledge without turning every engineering task into a documentation task. They are evaluation specifications, not a runtime-specific harness.

Evaluate repository state and decisions, not wording.

## Routing sanity checks

Route on a **concrete persistence or reconciliation decision**, not on the mere possibility that engineering work could later produce one. Re-evaluate routing when the task state changes.

### Entry routing

| Request / situation | Expected routing |
| --- | --- |
| Review a PR and report findings only | Do not route initially |
| Investigate a repository failure with no request to persist conclusions | Do not route initially |
| Run a temporary performance experiment with no persistence request | Do not route initially |
| Explain a function with no persistence decision | Do not route |
| Record the accepted design for future implementation | Use `engineering-knowledge-governance` |
| Investigate an incident and record durable conclusions future maintainers need | Use `engineering-knowledge-governance` |
| Reconcile a known stale canonical contract | Use `engineering-knowledge-governance` |
| Implement a change that is already known to invalidate a maintained external contract | Compose with the implementation skill and use governance for reconciliation |

### Mid-task routing

| Discovered situation | Expected routing |
| --- | --- |
| Review discovers that a canonical API contract is materially stale | Route now for the persistence/reconciliation decision |
| Investigation establishes a non-obvious durable invariant absent from maintained knowledge | Route now |
| Experiment establishes a consequential external constraint future work depends on | Route now |
| Implementation unexpectedly invalidates maintained design or operational knowledge | Route now for reconciliation |
| Review finds only ordinary code defects | Do not route |
| Investigation produces only disposable hypotheses or conclusions already represented by code/tests/history | Do not route |
| Experiment only resolves the current local implementation choice | Do not route |

## 1. Read-only code review does not create documentation by default

**Setup:** A PR review finds three ordinary implementation bugs. The repository has no stale documentation related to them.

**Prompt:** "Review this PR and report actionable findings."

**Pass conditions:**

- Keep ordinary findings in the review output.
- Do not create `review-notes.md`, `findings.md`, or another repository document merely to archive the review.
- If no durable repository knowledge is missing or stale, persist nothing.

**Failure signs:** Treating review findings as automatically durable repository documentation.

## 2. Review reveals a stale canonical contract

**Setup:** During a read-only review, the agent discovers that the maintained API contract document contradicts both current production behavior and accepted decisions. The review request does not authorize repository mutation.

**Prompt:** "Review this PR only; do not change files."

**Pass conditions:**

- Identify that the canonical contract appears stale and that reconciliation is needed.
- Do not modify the repository because the underlying task is read-only.
- Report the durable-knowledge issue rather than creating an alternative document.

**Failure signs:** Editing documentation despite read-only authority, or creating a parallel contract note.

## 3. Investigation conclusion earns persistence

**Setup:** A difficult incident investigation establishes a non-obvious invariant: a queue consumer must never acknowledge before a database commit because recovery depends on the ordering. The invariant is absent from maintained docs and likely to matter in future changes.

**Prompt:** "Investigate the duplicate-processing failures and record anything future maintainers genuinely need."

**Pass conditions:**

- Persist the consequential invariant because losing it would materially degrade future work.
- Put it in the repository's existing canonical design/operational home rather than a new generic notes file.
- Preserve relevant provenance or evidence linking the conclusion to observed behavior.

**Failure signs:** Leaving a high-value invariant only in the chat, or creating an unnecessary parallel document.

## 4. Investigation noise stays transient

**Setup:** The investigation tries five hypotheses; four are disproven and have no future value. The fifth explains the bug and is already represented clearly by a new regression test and canonical bug fix.

**Prompt:** "Investigate and fix the parser regression."

**Pass conditions:**

- Do not persist a diary of discarded hypotheses merely because investigation occurred.
- Persist additional knowledge only if the persistence test is met.
- Let code, tests, and version history carry information that is already adequately represented there.

**Failure signs:** Creating an investigation log with no durable decision value.

## 5. Temporary experiment remains temporary

**Setup:** A branch-local benchmark script and generated output compare two implementation options. The experiment only resolves the current choice; future work does not depend on the raw script or raw output.

**Prompt:** "Run a quick experiment to choose between these two local implementations."

**Pass conditions:**

- Use the experiment as transient feedback.
- Do not preserve disposable benchmark scaffolding or raw output as durable documentation by default.
- Persist nothing if the conclusion has no durable consequence beyond the chosen code.

**Failure signs:** Committing experiment artifacts merely because they were useful during the task.

## 6. Experiment establishes a durable constraint

**Setup:** Repeated measurements establish that an external vendor enforces a hard undocumented 64 KiB payload limit, and future integrations will fail if this is forgotten.

**Prompt:** "Determine the real payload limit and record the result if it matters for future integrations."

**Pass conditions:**

- Persist the limit because reconstructing it later is expensive and risky.
- Record provenance/freshness sufficient to judge the claim, including that it was observed rather than vendor-documented when relevant.
- Put it in the canonical integration contract/runbook area instead of a generic experiment note.

**Failure signs:** Recording an unqualified eternal fact with no provenance, or keeping only raw experimental output.

## 7. Implementation reconciles an existing canonical document

**Setup:** A user-authorized API behavior change makes an accepted API specification stale.

**Prompt:** "Change endpoint X from 404 to 204 and keep maintained documentation consistent."

**Pass conditions:**

- Update the existing canonical specification rather than creating `api-change-v2.md`.
- Keep status/current-state wording accurate.
- Update relevant references if the artifact moves or changes identity.

**Failure signs:** Parallel sources of truth or stale canonical documentation after completion.

## 8. Accepted design is not current behavior

**Setup:** A design proposal has been accepted but implementation is scheduled for later.

**Prompt:** "Record the accepted design so another team can implement it next month."

**Pass conditions:**

- Make accepted target state distinguishable from current runtime behavior.
- Preserve rationale/constraints that materially shape implementation.
- Do not describe the target design as already implemented.

**Failure signs:** Future readers could reasonably mistake the accepted design for current behavior.

## 9. Plan and design do not collapse into one lifecycle

**Setup:** A migration has a durable architecture decision and a temporary execution sequence.

**Prompt:** "Document the migration decision and enough execution state for the next agent."

**Pass conditions:**

- Keep durable design rationale distinguishable from transient coordination state.
- Reuse repository conventions rather than mechanically creating `design.md` plus `plan.md` when a better canonical arrangement already exists.
- Make it possible to retire the plan without losing the design decision.

**Failure signs:** Treating a completed plan as the permanent design record or duplicating the same authoritative claim across both.

## 10. Cross-agent handoff remains minimal

**Setup:** Work pauses mid-task with one unresolved assumption and a partially verified implementation. The repository already has a maintained project plan.

**Prompt:** "Leave enough state for another agent to continue tomorrow."

**Pass conditions:**

- Update the existing coordination artifact if appropriate.
- Persist only outcome/scope, current state, unresolved uncertainty, evidence gaps, and consequential constraints needed for continuation.
- Do not create a new handoff file merely because the session ends.

**Failure signs:** Session diary, duplicated plan, or missing consequential unresolved state.

## 11. Rename or move preserves discoverability

**Setup:** A canonical architecture document must move to the repository's established ADR area.

**Prompt:** "Move this decision record into the canonical ADR structure."

**Pass conditions:**

- Follow repository naming conventions.
- Update inbound references.
- Avoid duplicate aliases unless compatibility truly requires them.
- Preserve canonical identity and status clearly enough for future readers.

**Failure signs:** Broken references, duplicate authoritative copies, or a new naming taxonomy inconsistent with the repository.

## 12. Stale transient artifact is retired

**Setup:** A migration completed months ago. Its old active plan conflicts with current behavior and has no continuing operational value; version control retains history.

**Prompt:** "Clean up the maintained docs so they describe the current migration state."

**Pass conditions:**

- Retire or delete the obsolete transient plan when repository policy permits.
- Preserve only historically relevant material whose continuing role is explicit.
- Leave one coherent current truth.

**Failure signs:** Keeping contradictory active-looking documents merely for archival comfort.

## 13. Engineering activity alone does not force governance routing

**Setup:** A small implementation changes a private helper, all behavior and maintained contracts remain unchanged, and the prompt does not ask to record or reconcile knowledge.

**Prompt:** "Simplify this private helper without changing behavior."

**Pass conditions:**

- Do not route to `engineering-knowledge-governance` merely because implementation work occurred.
- If inspection reveals no stale maintained knowledge and no concrete persistence decision, perform no governance work and create no documentation.
- If the task later invalidates maintained knowledge, routing may become appropriate at that point for reconciliation.

**Failure signs:** Treating every implementation, review, investigation, experiment, design, or handoff as sufficient by itself to load or apply governance.

## Suggested evaluation dimensions

- **Persistence judgment:** Did the agent avoid both knowledge loss and documentation overproduction?
- **Canonicality:** Is there one trustworthy home for each durable claim?
- **Lifecycle clarity:** Are current state, target state, decisions, and transient coordination distinguishable?
- **Trust:** Are provenance, freshness, and uncertainty represented when materially necessary?
- **Reconciliation:** Did consequential work remove materially stale or contradictory maintained claims?
- **Authority:** Did documentation mutation stay within the underlying task's permissions?
- **Composition:** Did governance remain independent of the task-specific coding/review/research/experiment workflow?


## Universal consideration is not universal invocation

**Scenario:** A bounded implementation is complete. The code and existing canonical sources remain accurate; no durable design/fact/constraint emerged.

**Expected behaviour:** the engineering workflow performs a lightweight knowledge-impact check but does not invoke governance or create documentation.

**Failure signs:** treating "documentation is first-class" as a requirement to write a task note for every change.
