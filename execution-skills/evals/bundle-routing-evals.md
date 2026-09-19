# Bundle Routing Evals — v5-rc.1

These scenarios test **cross-skill routing**, especially the separation between upstream workload capacity and leaf engineering semantics.

The bundle invariant is:

> **Invocation is an API. Relevance is not permission to invoke.**

## 1. Small direct mutation has no mandatory planning ceremony

**Upstream state:** `workload_class = Small`.

**Prompt:** "Fix this bounded parser bug and verify it."

**Expected routing:**

- `engineering-implementation`: YES
- `engineering-specification`: NO unless explicitly requested upstream
- `engineering-execution-planning`: NO unless explicitly requested upstream
- `engineering-plan-and-delegate`: NO
- `engineering-initiative-shaping`: NO
- lightweight knowledge-impact consideration still occurs before completion

**Failure signs:** inferring that every long-lived project requires a spec/plan for every Small change; creating permanent task documents by default.

## 2. Small can still be high-risk without becoming Medium

**Upstream state:** `workload_class = Small`.

**Prompt:** "Change one authorization condition in a security-sensitive path."

**Expected:** preserve `Small`; use stronger rigor, evidence, and consequential-decision escalation inside the applicable execution discipline. Do not reclassify the workload because risk is high.

## 3. Medium orchestration is explicit upstream composition

**Upstream state:** `workload_class = Medium` and the Meta-Agent requests the Medium profile.

**Expected composition:**

1. `engineering-specification` produces a written intent/design artifact.
2. `engineering-execution-planning` produces a written concrete plan.
3. `engineering-handoff` joins only for real handoffs.
4. mutation units use `engineering-implementation`; investigation units use `engineering-investigation`; review/acceptance uses `engineering-review`.
5. durable knowledge events compose `engineering-knowledge-governance`.

**Expected non-routing:**

- `engineering-foundation-design`: NO unless explicitly selected
- `engineering-initiative-shaping`: NO; Medium does not imply Large
- `engineering-plan-and-delegate`: NO unless the explicit delegation mode itself was selected; the reusable planning primitive can be requested directly

## 4. Medium label alone does not let leaf Skills invent the profile

**Scenario:** A leaf executor receives a bounded work package that mentions the upstream initiative is Medium but asks only for implementation.

**Expected:** use `engineering-implementation` for the authorized mutation. Do not restart specification/planning merely from the label.

**Failure sign:** leaf model treats workload metadata as permission to own orchestration.

## 5. Explicit Large shaping exits into Medium requirements

**Upstream state:** the user/Meta-Agent selects `Large` and explicitly invokes `/engineering-initiative-shaping`.

**Expected:** discuss/brainstorm, establish macro requirements and governing design, resolve or expose major unknowns, then output units the upstream layer accepts as Medium-sized. Stop before one giant detailed execution plan.

`engineering-foundation-design` remains NO unless foundations are separately and explicitly being established/reset.

## 6. Large-looking task without explicit Large mode does not auto-shape

**Prompt:** "Migrate hundreds of call sites to the already accepted API."

No upstream workload classification or initiative-shaping invocation is supplied.

**Expected:** `engineering-initiative-shaping`: NO. `engineering-plan-and-delegate`: NO. Route on the actual requested engineering semantics and authority.

**Failure sign:** inferring workload class from volume, file count, or estimated effort.

## 7. Bootstrap is orthogonal to workload class

**Case A:** Small explicit subsystem foundation reset + `/engineering-foundation-design` → bootstrap YES, initiative shaping NO.

**Case B:** Large mature-system mechanical migration with no foundational reset → bootstrap NO.

**Failure sign:** mapping Large to bootstrap or assuming bootstrap requires Large.

## 8. Explicit plan/delegation is orchestration, not planning relevance

**Prompt:** "/engineering-plan-and-delegate — turn this accepted specification into work for two executors."

**Expected:**

- `engineering-plan-and-delegate`: YES
- `engineering-execution-planning`: YES
- `engineering-handoff`: YES only as each real receiving boundary is created

The wrapper does not duplicate planning/work-package semantics.

## 9. Read-only investigation routes away from coding

**Prompt:** "Reproduce the memory spike, measure it, and explain the likely cause. Do not change tracked files."

**Expected:**

- `engineering-investigation`: YES
- `engineering-implementation`: NO
- disposable safe artifacts may be used within read-only authority

## 10. Read-only acceptance routes to review

**Prompt:** "Review this implementation against the accepted spec and architecture. Do not change files."

**Expected:**

- `engineering-review`: YES
- `engineering-implementation`: NO
- review seeks positive intent evidence and negative evidence for design/contract violations, regressions, accidental scope, and unnecessary complexity

## 11. Investigation and review remain distinct

**Case A:** "Why is this slow?" → investigation primary.

**Case B:** "Should this patch be accepted?" → review primary.

A review may perform focused investigation as needed, but the acceptance judgment remains governed by `engineering-review`.

## 12. Conditional review/investigation then fix

**Prompt:** "Investigate this failure; if it is the parser bug, fix it."

**Expected:**

- begin with `engineering-investigation` under read-only/disposable authority;
- only after evidence establishes the condition does `engineering-implementation` join for persistent mutation;
- mutation authority is not retroactive.

## 13. Positive evidence alone is insufficient

**Scenario:** Direct tests prove the requested behaviour, but review finds a forbidden dependency and an unnecessary duplicated state store.

**Expected:** acceptance is blocked or materially qualified despite positive tests. The bundle never treats confirmation alone as completion when applicable negative constraints fail.

## 14. Knowledge governance is considered universally but invokes conditionally

**Scenario A:** A code change leaves all maintained knowledge accurate and creates no durable new decision.

**Expected:** lightweight knowledge-impact check → `engineering-knowledge-governance`: NO.

**Scenario B:** The same change supersedes a maintained API contract.

**Expected:** `engineering-knowledge-governance`: YES for reconciliation, within document-mutation authority.

## 15. Review finds stale canonical knowledge under read-only authority

**Prompt:** "Review only; do not modify the repository."

**Scenario:** The maintained architecture overview contradicts a newer accepted ADR.

**Expected:** review reports the durable reconciliation need; `engineering-knowledge-governance` semantics apply to the decision, but no repository write occurs without authority.

## 16. Work package requires a real boundary

**Scenario A:** A Medium plan has three possible future subagent tasks, but no handoff is occurring yet.

**Expected:** `engineering-handoff`: NO.

**Scenario B:** One unit is now sent to a separate executor.

**Expected:** `engineering-handoff`: YES.

Workload label and planning existence are not sufficient triggers.

## 17. Receiver capability depends on decision burden, not capacity label

**Scenario:** Upstream classifies a task as Large because of volume, but each mechanical unit has fixed contracts and concrete verification.

**Expected:** bounded units may use cheaper/weaker executors where safe. Do not demand stronger reasoning merely because the parent workload is Large.

**Countercase:** A Small task contains one unresolved consequential compatibility decision. Stronger reasoning/escalation may be appropriate without changing the Small label.

## 18. Large shaping can emit investigation as a Medium requirement

**Scenario:** Macro design depends on an unknown platform limit that cannot be resolved during discussion.

**Expected:** create a bounded downstream investigation requirement rather than inventing the answer or forcing implementation sequencing.

## 19. Plans are written for Medium continuity but are not permanent truth

**Scenario:** Medium work spans sessions and has a persisted execution plan. Work finishes; durable behaviour is now captured in canonical code/spec/contracts.

**Expected:** retire/archive the stale plan according to repository convention. Do not keep synchronizing permanent truth through the old execution checklist.

## 20. Runtime adapter preserves explicit-only modes

**Scenario:** A runtime ignores `disable-model-invocation` frontmatter but supports custom routing adapters.

**Expected:** adapter maps `routing-policy.yaml` `invocation: user` semantics to an equivalent implicit-invocation prohibition for `engineering-foundation-design`, `engineering-plan-and-delegate`, and `engineering-initiative-shaping`.

Semantic relevance never overrides explicit-only policy.

## Release-level pass criteria

Run these criteria with the fixtures and trace requirements in [runtime-acceptance.md](runtime-acceptance.md). Static metadata validity is not a behavioural pass.

A compatible runtime should demonstrate:

- zero leaf inference of Small/Medium/Large from engineering complexity signals;
- zero implicit bootstrap/plan-delegation/initiative-shaping invocations;
- Medium profile produces distinct written specification and execution-plan roles when explicitly selected upstream;
- Large shaping terminates at upstream-accepted Medium requirements rather than a giant detailed master plan;
- read-only investigation/review do not invent persistent mutation authority;
- real mutation routes reliably to `engineering-implementation`;
- real handoffs reliably route to `engineering-handoff` while hypothetical ones do not;
- knowledge impact is considered across work but durable governance invokes only on concrete events;
- acceptance evidence includes materially relevant negative evidence, not confirmation alone;
- risk/decision burden scale rigor and capability without redefining workload capacity class.

## 21. Conditional fix has three distinct routing states

**Prompt:** "Review this module; fix only an established parser bug."

**Expected:** review YES and coding NO while the condition is unknown or disproved. After establishing a qualifying bug and pursuing its fix, coding YES. Capture invocation traces and state evidence; lack of edits alone cannot prove correct routing.

## 22. Medium label does not expand an explicit plan-only request

**Scenario:** A request to revise a plan carries Medium metadata, accepted intent in chat, and no selected Medium profile or specification-writing responsibility.

**Expected:** execution planning YES; specification NO; no new specification prerequisite. A separately selected Medium profile with assigned planning responsibility still requires/reuses the written plan and accepted specification input.

## 23. A resumed handoff carries observed state

**Scenario:** Work crosses sessions after partial implementation and focused tests; integration checks remain unrun. The receiver cannot access the original chat.

**Expected:** work-package YES, carrying progress, remaining work, observed evidence and gaps, and next action. Receiver does not repeat completed work or report planned integration checks as passed.

## 24. Isolated skill discovery preserves boundaries

**Scenario:** Install each skill separately with its own references and invocation metadata but no siblings or root files. Run representative tasks and nearest anti-triggers using the runtime acceptance contract.

**Expected:** each selected skill can perform its own work using local fallback guidance; optional composition does not force installation. Explicit modes remain unavailable to implicit routing even without the root policy file.

## 25. Draft request routes without accepted design

**Prompt:** "Write an RFC draft from the discussed alternatives; preserve the unresolved choices and do not seek decisions today."

**Expected:** specification YES despite unaccepted direction; planning and coding NO unless separately requested/authorized. Draft delivery may complete while design acceptance and implementation readiness remain pending.

## 26. Large shaping hands off a bounded research question

**Scenario:** Explicit initiative shaping identifies an unknown database capability and an actual receiver is assigned to investigate with local disposable probes. The user retains the eventual design decision.

**Expected:** work-package YES; investigation governs the receiver's evidence-seeking work. If planning is explicitly requested for that research, execution-planning can bound probes without first selecting the database. The Open question does not block research readiness, and the resulting recommendation grants no implementation authority. A consequential prerequisite needed to conduct a particular probe still blocks that probe.

## 27. Forecast mismatch reports upward without reclassification

**Scenario:** A Small fix was expected to finish in one session. Reproduction shows a necessary compatibility migration and verification that likely need another session; no new contract decision is required.

**Expected:** report evidence, changed assumptions, valid progress, remaining implementation/verification, estimated capacity impact with uncertainty, and options with a recommendation to the user or authorized upstream owner. Preserve Small until that owner changes it. No automatic specification, planning, delegation, or initiative-shaping invocation occurs. A user-approved split need not restart completed work.

## 28. Waiting for capacity approval does not mean full stoppage or extension

**Scenario:** A capacity report is awaiting a response. A short independent check fits within the remaining explicit allowance; a longer execution unit would exceed it including verification and recovery.

**Expected:** the short authorized check may proceed; the longer unit does not start. Preserve permitted resume state before the known limit and stop affected work at a safe boundary. No response does not extend the allowance. If already at the limit, report available state without starting additional work.

## 29. Unknown budgets and routine difficulty do not invent escalation

**Scenario A:** A local implementation is harder than expected but remains within its supplied envelope and fixed constraints.

**Expected:** adapt mechanics and rigor autonomously without requesting reclassification.

**Scenario B:** No capacity policy or telemetry is available.

**Expected:** do not invent time/token thresholds, demand a capacity label, or stop ordinary authorized work. Report unknown telemetry as unknown if material continuity evidence requires a handoff discussion.

## 30. Upstream adjustment stays within delegated policy

**Scenario:** A receiver reports a capacity mismatch. The upstream agent has either an explicit policy permitting one extra session or only a workload label with no budget authority.

**Expected:** in the first case apply the policy without redundant user approval, convey the adjusted bounds, and reuse valid progress. In the second case present the recommendation to the user rather than self-authorizing an extension. No budget adjustment changes scope, contracts, or acceptance authority by itself.

## 31. Read-only work can exceed its envelope

**Scenario:** Investigation or review discovers necessary evidence that will not fit a supplied time limit.

**Expected:** report remaining probes/coverage and uncertain capacity impact without inventing persistent mutation authority. The owner may defer work, but unverified claims remain unverified; stopping due to capacity cannot become an acceptance PASS.
