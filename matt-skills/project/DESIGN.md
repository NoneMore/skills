# Matt Project Skills: Capability-Oriented Design

> Status: draft design direction. This document defines the intended shape and review criteria for the project skill suite. It deliberately does **not** preserve the current workflow protocol or every current skill.

## Why this refactor

The project skills have accumulated a preferred idea-to-ship sequence, tracker lifecycle states, handoff rules, canonical result records, and cross-skill transition requirements. Those mechanisms make one path explicit, but they also turn a collection of skills into a workflow protocol.

That is the wrong center of gravity.

The suite should optimize for:

1. **Flexibility** — enter at the capability needed from the state that actually exists.
2. **Composability** — combine capabilities in many orders without hidden predecessor/successor contracts.
3. **Clear local boundaries** — every skill owns a recognizable local outcome and knows when it is done.
4. **Coverage before exclusivity** — overlap is acceptable; uncovered gaps are worse.
5. **Minimal protocol** — use code, Git, issues, PRs, CI, docs, and explicit artifacts as sources of truth instead of maintaining a second agent-specific lifecycle.
6. **Capabilities, not methods** — a skill should represent a useful job to accomplish, not merely one technique for accomplishing it.

The goal is not less discipline. The goal is to keep discipline local to the capability that needs it instead of encoding it as a global sequence.

---

## 1. Capabilities, not stages

A skill describes **what useful job it can complete**, not where it sits in a project lifecycle.

Bad framing:

```text
idea -> grill -> spec -> tickets -> implement -> test -> review -> reconcile
```

This turns skill names into workflow stages. Any deviation then requires recovery rules, state transitions, or special cases.

Preferred framing:

```text
conversation / issue / code / diff / failure / decision / artifact
                         |
             choose a useful capability
                         |
               produce a local outcome
```

Examples:

- `to-spec` can synthesize a spec from any sufficiently complete source material.
- `to-tickets` can decompose any sufficiently concrete body of work.
- `implement` can implement from an issue, spec, ticket, conversation, or another explicit contract when enough intent is present.
- `code-review` can review a diff whether or not `implement` produced it.
- `diagnosing-bugs` can investigate a failure without assuming a later implementation flow.
- `prototype` can answer a runnable design question wherever that question appears.

Common combinations may exist. They are examples, not lifecycle law.

---

## 2. Capabilities, not development techniques

A development technique is not automatically a skill.

A skill deserves to exist when it owns a distinct useful outcome. A technique only describes **how** another capability may choose to work.

### TDD is a technique, not a capability boundary

Test-driven development is one valid implementation method, but it is not the only one. Requiring a dedicated `tdd` skill makes one development method part of the suite's topology and encourages artificial sequencing:

```text
implement -> tdd -> review
```

That is exactly the kind of coupling this refactor is removing.

The intended direction is therefore to remove `tdd` as a project skill.

Testing remains important, but responsibility belongs to the capability doing the work:

- `implement` owns appropriate verification of the behavior it changes;
- `diagnosing-bugs` may add a regression test when that is the strongest way to preserve the diagnosis/fix;
- `prototype` may use tests when they help answer the target question, but should not be forced to production-level verification;
- `code-review` may evaluate whether the available verification is sufficient for the claimed change.

The owning capability may use test-first development, test-after development, characterization tests, property tests, manual verification, static checks, or another suitable method. The suite should not prescribe one universal order.

A useful rule:

> **Methods may be guidance inside capabilities; they should become standalone skills only when they own an independently useful outcome.**

The same test should be applied to other candidates: if a skill is mainly a methodology, style, ritual, or preferred ordering rather than a locally complete job, it should probably become reference guidance or disappear.

---

## 3. Manual invocation is control, not sequencing

User-invoked skills remain valuable because the human chooses which capability to apply.

Manual invocation must not imply a canonical sequence.

Prefer:

> The requested change is implemented and verified. An independent `code-review` may be useful if you want one.

Avoid:

> Implementation is complete. Transition to review state, invoke `code-review`, persist the result, then reconcile.

The first preserves user control. The second creates a workflow engine in prose.

---

## 4. Boundary model for every skill

Every project skill should be reviewable with the same local boundary model.

### Purpose

One sentence describing the local problem this capability solves.

### Accepts

The natural forms of input it can work from. Inputs should be semantic rather than tied to predecessor skills.

Examples: a conversation, issue, spec, diff, failing command, design question, code area, or artifact.

### Owns

The useful outcome this skill is responsible for producing.

A skill should not need another skill to finish the responsibility it claims to own.

### May also

Adjacent work the skill may perform when useful to complete its owned outcome.

Overlap is expected here. Explicit overlap is healthier than artificial gaps.

### Done when

A local completion condition that does not depend on the skill's position in a larger flow.

Good examples:

- a diagnosis is supported by evidence;
- a spec is sufficiently decision-complete for its intended use;
- a decomposition is independently actionable;
- requested behavior is implemented and appropriately verified;
- review findings are reported;
- a prototype answered the target question.

Bad examples:

- the next lifecycle state was persisted;
- another skill was invoked;
- a parent artifact was reconciled;
- an item reached a suite-specific terminal state.

### Does not require

Predecessors, successors, tracker roles, lifecycle markers, or suite-specific persisted state that are intentionally not prerequisites.

This section exists to expose accidental temporal coupling.

---

## 5. Coverage over disjointness

The capability map should aim for practical coverage, not mutually exclusive partitions.

Overlap is usually tolerable:

- `diagnosing-bugs` may run experiments that resemble `research` or `prototype`;
- `prototype` may discover architectural constraints that overlap with `codebase-design`;
- `implement` may diagnose a small failure encountered while implementing;
- `code-review` may identify design problems even though architecture capabilities exist.

The dangerous case is a gap:

```text
Skill A owns the first half.
Skill B owns the second half.
Neither owns a useful complete outcome from the user's current state.
```

When forced to choose, prefer **overlap with clear centers of gravity** over **clean-looking separation with uncovered space**.

A merge/delete signal is stronger when two skills have the same natural inputs, same owned outcome, and same completion condition.

---

## 6. No hidden predecessor contracts

A skill should not require another skill to have run merely to manufacture suite-specific state.

Legitimate prerequisites are intrinsic to the work:

- review needs something to review;
- implementation needs enough intent to implement;
- diagnosis needs an observable symptom or failure;
- decomposition needs a sufficiently concrete body of work.

Suspicious prerequisites exist only because of the suite:

- a work-item role must have been persisted first;
- another skill must have written a canonical result block;
- a lifecycle field must be at the right stage;
- a reconciliation pass must run before an otherwise valid capability may start.

Skills should consume reality, not proof that another skill previously ran.

---

## 7. Prefer real sources of truth

Do not create a second database about the work unless the extra state represents genuinely new information with no natural home elsewhere.

Prefer:

- code and tests for behavior;
- commits and branches for code history;
- issues for requested work and discussion;
- PRs/MRs for proposed delivery and review;
- CI for automated verification;
- ADRs/domain docs for durable design knowledge;
- explicit specs, research notes, or prototypes when the artifact itself is the useful output.

Be suspicious of:

- canonical implementation-result records duplicating commit/PR/test state;
- reconciliation records duplicating whether requirements are satisfied;
- claim/suspend/awaiting-delivery state layered over tracker state;
- roles whose main purpose is deciding which skill may run next.

If state is needed only to make the workflow protocol work, remove the protocol before formalizing the state.

---

## 8. Composition rules

1. **Direct entry:** any skill should be directly usable when its natural inputs exist.
2. **Local completion:** a skill owns its result; another skill is not required merely to finish its job.
3. **Advisory neighbors:** a skill may suggest another capability but does not own the next step.
4. **Optional context stays optional:** richer context may improve results without becoming a setup gate unless intrinsically necessary.
5. **Integrations are adapters:** GitHub, GitLab, local Markdown, Jira, Linear, etc. should expose only the operations a local capability actually needs.
6. **Techniques stay internal:** testing styles, refactoring techniques, interviewing styles, and similar methods should normally be guidance used by capabilities rather than workflow nodes.
7. **Real human gates only:** ask for human decisions where a real product, architecture, publication, destructive, or authorization choice exists—not because the suite crossed a phase boundary.

---

## 9. Protocol smells to remove

Treat these as warnings during the refactor:

- a named "main flow" that most work is expected to follow;
- "after this, invoke X" as a correctness requirement;
- correctness depending on a previous skill's private output format;
- suite-wide lifecycle enums;
- claim/release/suspend machinery used mainly for agent coordination;
- canonical result blocks duplicating Git/tracker/CI evidence;
- a reconciliation phase required to decide whether completed work counts;
- setup configuring operations unrelated to the capability being used;
- work-item roles used mainly for routing between skills;
- a standalone skill whose real distinction is only a preferred method or ordering;
- recovery logic whose main job is resuming the suite's own state machine.

Not every occurrence is automatically wrong, but each must justify why it belongs to a local capability.

---

## 10. Design tests

### Direct-entry test

Can the skill start from natural real-world inputs without running a preparatory suite skill?

### Reorder test

Does it still make sense if neighboring capabilities happen in a different order?

### Deletion test

If an adjacent skill disappeared, would this skill still complete the outcome it claims to own?

### Completion test

Can we say in one or two sentences when the local job is done?

### Method-vs-capability test

Does the skill own an independently useful result, or does it mainly prescribe how another capability should work?

If the latter, prefer reference guidance or inline instructions over a standalone skill.

### Source-of-truth test

Is the skill reading/writing the natural durable source, or maintaining a second representation solely for workflow coordination?

### Coverage test

Across representative tasks, is there at least one skill that can own a useful outcome from the user's actual starting state?

### Overlap test

Where skills overlap, can we explain the difference in their primary outcomes without forbidding useful adjacent work?

### Small-task test

Can a small task use one capability directly without paying setup/protocol costs designed for large projects?

---

## 11. Scenario matrix

Validate the suite against real tasks rather than a canonical flow. At minimum:

- "This flaky test fails sometimes. Find out why."
- "I know exactly what to change; implement this small request."
- "I have a rough feature idea and need to sharpen it."
- "Turn this conversation into a durable spec."
- "Break this body of work into independently useful slices."
- "I need to see whether this UI/state model works before deciding."
- "Review this PR against intended behavior."
- "Improve this awkward module without changing behavior."
- "Research these two libraries and leave me evidence."
- "I am halfway through a task and need to hand it to another agent."
- "I have an existing external issue; help me act on it."
- "I do not know which capability fits this situation."

For each scenario, record:

1. which skills can accept it directly;
2. which skill(s) own a useful local outcome;
3. whether any transition exists only because of suite protocol;
4. whether overlap is confusing;
5. whether a common task falls into an uncovered gap.

Fix gaps before optimizing overlap away.

---

## 12. Tentative capability map (not a sequence)

This table is only for checking coverage. Rows imply no order and do not commit us to preserving every current skill.

| Capability area | Existing skills that may cover it |
| --- | --- |
| Clarify / challenge intent | `grill-with-docs`, `grilling` |
| Navigate available capabilities | `ask-matt` |
| Research external facts | `research` |
| Explore with runnable evidence | `prototype`, `diagnosing-bugs` |
| Model domain language | `domain-modeling` |
| Design code boundaries | `codebase-design` |
| Produce a durable specification | `to-spec` |
| Decompose work | `to-tickets` |
| Implement behavior and verify the change | `implement` |
| Diagnose failures | `diagnosing-bugs` |
| Improve existing structure | `improve-codebase-architecture` |
| Review changes | `code-review` |
| Transfer context | `handoff` |
| Configure optional integrations | `setup-matt-pocock-skills` |
| Large ambiguous decision spaces | `wayfinder` |

`tdd` is intentionally absent: test-driven development is treated as an optional implementation technique, not a project capability.

---

## 13. Settled design decisions

These are part of the direction unless later evidence changes them.

### Manual choice stays

Users should remain free to explicitly choose capabilities. Simplifying workflow protocol does not mean introducing an automatic orchestrator.

### Coverage is more important than non-overlap

Prefer a modest amount of understandable overlap over common tasks falling between skill boundaries.

### TDD should not remain a standalone project skill

Testing is part of implementation/diagnosis/review as appropriate. Test-first is one possible method, not the suite's required development sequence.

### Do not replace the current protocol with a centralized protocol

The target is deletion of unnecessary lifecycle machinery, not moving it into a schema or shared workflow engine.

---

## 14. Open questions for implementation discussion

### What should `ask-matt` become?

The current router teaches a main flow. A capability-oriented version could instead present plausible capabilities for the user's current state and explain their different outcomes without defining a normal lifecycle.

### How broad should `implement` be?

It clearly owns implementation plus appropriate verification, but details remain open: how much local diagnosis, refactoring, documentation, or review should it perform before those become better handled as separately chosen capabilities?

The answer should maximize local completeness without turning `implement` into an all-purpose agent.

### Does `reconcile` survive at all?

Much of its current purpose appears coupled to lifecycle machinery. Remove that machinery first, then see whether any independently useful capability remains. Do not preserve it by default.

### How small should `setup-matt-pocock-skills` become?

Setup should configure only genuinely shared optional integrations or documentation conventions. Determine those needs from rewritten local capabilities rather than designing a suite-wide tracker contract up front.

### What persistence should be default versus optional?

Some capabilities naturally produce durable artifacts (`to-spec`, research notes, ADRs). Others may not need persistence. Decide capability by capability whether persistence is the product, useful evidence, or historical workflow machinery.

### Which human confirmation gates are intrinsic?

Keep gates for real decisions or authority boundaries. Remove gates that only mark transitions between artificial stages.

### How much overlap is too much?

Overlap is healthy until two skills have effectively the same inputs, outcome, and completion condition. That is a stronger merge/delete signal than superficial similarity.

### Is `wayfinder` one capability or a workflow bundle?

Determine whether "map and resolve a large ambiguous decision space" is a coherent local outcome or whether the current skill bundles multiple capabilities.

### Where should optional concurrent-agent coordination live?

Claiming/blocking can be useful for genuine concurrent execution, but it should not be mandatory `implement` semantics. Decide whether this belongs in a separate optional capability/integration.

---

## 15. Migration constraint

Optimize for simplification, not preservation of current behavior.

Do not ask:

> How do we reproduce every current lifecycle behavior in the new design?

Ask:

1. What useful local capability exists here?
2. What natural inputs does it need?
3. What outcome does it own?
4. What real source of truth already represents surrounding state?
5. Is this a capability or merely a method?
6. Which rules disappear once no canonical sequence is assumed?

Deleting skills, protocol, setup, persisted metadata, and cross-skill instructions is an expected outcome of this refactor.

---

## Target end state

```text
small, locally complete capabilities
+ broad natural inputs
+ clear completion conditions
+ intentional overlap
+ strong practical coverage
+ manual user choice
+ techniques selected locally
+ minimal shared state
+ no required canonical order
```

The suite should feel like a toolbox, not a workflow runtime.
