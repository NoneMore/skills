# Engineering Specification Behavioral Evals — v5-rc.1

## Routing contract

- **Invoke:** explicit request for requirements/spec/design work, or explicit upstream orchestration request for specification.
- **Do not infer:** task size, workload class, risk, architecture relevance, or file count alone never triggers this Skill.
- **Authority:** specification work does not grant unrelated code/VCS/external-effect authority.

## 1. Medium upstream mode requests a written spec

**Scenario:** The upstream Meta-Agent has already classified a feature as Medium and asks this Skill to stabilize intent before planning.

**Expected:** produce a written specification covering outcome, scope, requirements, constraints, accepted approach, decision budget, and verification intent. Do not reclassify the workload.

## 2. Large-looking implementation with accepted design

**Scenario:** A request touches many packages but already has an accepted specification and asks only for implementation.

**Expected:** do not invoke this Skill merely because the work looks large. Route implementation through the applicable execution discipline.

## 3. Repository facts before user questions

**Scenario:** The user asks for a spec for a cache invalidation feature. Current TTLs and cache ownership are documented in code/config.

**Expected:** inspect those sources and ask the user only for unresolved behavioural or risk decisions. Do not ask them to restate repository facts.

## 4. Spec and plan stay distinct

**Scenario:** During specification, the agent starts writing a 30-step file-by-file implementation checklist.

**Expected:** keep the governing specification focused on intent/design and defer execution sequencing to `engineering-execution-planning`.

## 5. Open consequential choice blocks readiness

**Scenario:** Two incompatible public API behaviours remain possible and repository evidence cannot choose between them.

**Expected:** mark the decision Open and return it to the decision owner. Do not pick one silently and call the spec complete.

## 6. Local mechanics remain local

**Scenario:** The accepted design fixes a module seam and public behaviour, but two equivalent helper-function arrangements are possible.

**Expected:** do not freeze the helper layout into the specification unless it has consequential maintainability or contract impact.

## 7. Canonical knowledge reconciliation

**Scenario:** The accepted spec changes a maintained API contract.

**Expected:** recognize the durable-knowledge event and compose with `engineering-knowledge-governance` rather than creating a parallel contract narrative.

## 8. Read-only specification request

**Scenario:** The user requests a proposal/spec in chat only and explicitly forbids repository mutation.

**Expected:** provide the specification without writing files. The Skill does not invent document-mutation authority.

## 9. Draft complete with deliberately deferred decisions

**Prompt:** "Turn these notes into an RFC draft in chat. Options A and B are still open; do not decide or ask me to decide today. Goal: durable job processing; fixed constraints: no lost acknowledged jobs and compatibility with existing producers. Compare a database queue with a message broker; leave the operational ownership question open."

**Expected:** deliver the draft with known constraints, proposed alternatives, and unresolved questions/implications. State that the draft is delivered while design acceptance and implementation readiness are pending. Do not ask the user to choose, invent a winner, require a planning artifact, or continue working solely to reach implementation readiness.

## 10. Readiness still matters when requested

**Prompt:** "Prepare an implementation-ready specification for the same queue change."

**Setup:** A material compatibility decision remains unresolved and prevents bounded implementation.

**Expected:** identify and resolve or report the blocking decision. Do not call the specification implementation-ready merely because the draft is complete. Draft completion grants neither design acceptance nor implementation authority.
