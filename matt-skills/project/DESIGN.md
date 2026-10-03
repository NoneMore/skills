# Matt Project Skills: Capability-Oriented Design

> Status: draft design direction. This document defines the intended shape and review criteria for the project skill suite. It deliberately does **not** prescribe the exact migration or final implementation of each skill yet.

## Why this refactor

The project skills have gradually accumulated a strong idea-to-ship sequence, tracker lifecycle states, handoff rules, canonical result records, and cross-skill transition requirements. Those mechanisms make one preferred path explicit, but they also turn a collection of skills into a workflow protocol.

That is the wrong center of gravity for this suite.

The core properties should be:

1. **Flexibility**: a user can enter at the capability they need from the state they actually have.
2. **Composability**: skills can be combined in many orders without hidden predecessor/successor contracts.
3. **Clear local boundaries**: each skill owns a recognizable local outcome and knows when that outcome is complete.
4. **Coverage before exclusivity**: capability overlap is acceptable; uncovered gaps are worse.
5. **Minimal protocol**: durable state should live in the codebase, Git, tracker, PR, CI, or explicit artifacts—not in a second agent-specific lifecycle layered on top.

The goal is not to remove discipline. The goal is to move discipline back into the local capability that needs it instead of encoding discipline as a global sequence.

---

## Primary design principle: capabilities, not stages

A skill describes **what capability it provides**, not where it sits in a project lifecycle.

A capability may be useful before, during, after, or independently of another capability. The same skill should remain valid when entered from different directions.

Bad framing:

```text
idea -> grill -> spec -> tickets -> implement -> review -> reconcile
```

This turns skill names into workflow stages and makes every deviation require special protocol.

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
- `implement` can implement from an issue, spec, ticket, conversation, or other explicit contract when enough intent is present.
- `code-review` can review a diff whether or not `implement` produced it.
- `diagnosing-bugs` can investigate a failure without assuming a later implementation flow.
- `prototype` can answer a design question wherever that question appears.

There may still be common combinations. They are examples, not lifecycle law.

---

## Manual invocation is control, not sequencing

User-invoked skills remain user-invoked when explicit human choice is valuable. Manual invocation is a feature: the user decides which capability to apply next.

However, manual invocation must not imply a canonical sequence.

A skill may say that another capability could be useful. It should not require the user to traverse a prescribed next stage merely because this skill completed.

Prefer:

> The diff is implemented and tested. `code-review` may be useful if you want an independent review.

Avoid:

> Implementation is complete. Transition to review state, invoke `code-review`, persist the result, then reconcile.

The first preserves user control. The second creates a workflow engine in prose.

---

## Boundary model for every skill

Each project skill should be reviewable using the same local boundary model.

### Purpose

One sentence describing the capability in terms of the local problem it solves.

### Accepts

The natural forms of input the skill can work from. Inputs should be semantic rather than tied to a predecessor skill.

Examples: a conversation, issue, spec, diff, failing command, design question, code area, or existing artifact.

### Owns

The outcome this skill is responsible for producing. This is the center of the skill.

A skill should not need another skill to finish the responsibility it claims to own.

### May also

Adjacent work the skill is allowed to perform when doing so is useful to complete its owned outcome.

Overlap is expected here. Explicit overlap is healthier than artificial gaps.

### Done when

A local completion condition that can be evaluated without asking where the skill sits in a larger workflow.

Good completion conditions describe the task result:

- a diagnosis is supported by evidence;
- a spec is decision-complete enough for the intended use;
- a decomposition is independently actionable;
- requested behavior is implemented and verified;
- review findings are reported;
- a prototype answered the target question.

Bad completion conditions describe protocol position:

- the next lifecycle state was persisted;
- a downstream skill was invoked;
- the parent artifact was reconciled;
- the item reached the suite's canonical terminal status.

### Does not require

Any predecessor, successor, tracker role, lifecycle marker, or suite-specific persisted state that is intentionally *not* a prerequisite.

This section exists to catch accidental temporal coupling.

---

## Coverage over disjointness

The capability map should aim for complete practical coverage, not mutually exclusive partitions.

If two skills can both reasonably accept a task, that is usually tolerable. The distinction should come from their center of gravity, not from artificial guardrails.

For example:

- `diagnosing-bugs` may run experiments that resemble `research` or `prototype`;
- `prototype` may discover architectural constraints that overlap with `codebase-design`;
- `implement` may run tests even though `tdd` exists;
- `code-review` may identify design problems even though architecture skills exist.

The dangerous case is the opposite:

```text
Skill A owns the first half.
Skill B owns the second half.
Neither owns the transition or complete local outcome.
```

That gap forces users or agents to reconstruct hidden workflow logic.

When forced to choose, prefer **overlap with clear ownership** over **clean-looking separation with uncovered space**.

---

## No hidden predecessor contracts

A skill should not require another skill to have run merely to manufacture suite-specific state.

A prerequisite is legitimate when it is intrinsic to the work:

- review needs something to review;
- implementation needs enough intent to implement;
- a bug investigation needs an observable failure or symptom;
- ticket decomposition needs a sufficiently concrete body of work.

A prerequisite is suspect when it exists only because of the suite:

- a specific work-item role must have been persisted first;
- a previous skill must have written a canonical result block;
- a lifecycle field must say the item is at the right stage;
- a reconciliation pass must run before another otherwise-valid capability can start.

Skills should consume reality, not proof that another skill previously ran.

---

## Prefer real sources of truth

Do not create a second database about the state of the work unless the new state represents information that has no natural home elsewhere.

Prefer existing durable evidence:

- code and tests for implemented behavior;
- commits and branches for code history;
- issues for requested work and discussion;
- PRs/MRs for proposed delivery and review;
- CI for automated verification;
- ADRs and domain docs for durable design knowledge;
- explicit research/spec/prototype artifacts when the artifact itself is the useful output.

Be suspicious of suite-specific mirrors such as:

- canonical implementation result records duplicating commit/PR/test state;
- canonical reconciliation records duplicating whether requirements are satisfied;
- claim/suspend/awaiting-delivery state layered over tracker state;
- roles whose main purpose is to authorize which skill may run next.

If state is necessary only to make the workflow protocol work, remove the protocol before formalizing the state.

---

## Composition rules

### 1. Any skill should be directly enterable when its natural inputs exist

The user should not have to reconstruct the route that would normally have led there.

### 2. Skills may suggest neighbors, but do not own the next step

Suggestions are advisory and should explain why the neighboring capability may help.

### 3. Supporting composition must remain local

A skill may use another model-invoked capability when that capability is genuinely part of completing its own local outcome. This should not silently expand into ownership of a project-wide lifecycle.

### 4. Optional context must stay optional

A spec can improve review; it should not make review impossible when no spec exists. Domain docs can improve naming; their absence should not invent a setup gate unless the capability truly cannot operate without them.

### 5. Integrations are adapters, not the domain model

GitHub, GitLab, local Markdown, Jira, Linear, or another tracker may be useful persistence surfaces. The project skills should not inherit a large common tracker protocol merely to keep the suite internally consistent.

A skill should ask only for the external operations its own capability actually needs.

---

## Protocol smells to remove

During the refactor, treat the following as warning signs:

- a named "main flow" that most work is expected to follow;
- "after this, invoke X" as a correctness requirement;
- skill correctness depending on the previous skill's private output format;
- suite-wide lifecycle enums;
- claim/release/suspend protocols used primarily for agent coordination;
- canonical result blocks whose information already exists in Git/tracker/CI;
- a reconciliation phase required to decide whether completed work counts;
- setup that configures operations unrelated to the capability currently being used;
- work-item roles whose main purpose is routing between skills;
- duplicated explanations of the same cross-skill invariant in several `SKILL.md` files;
- recovery logic whose only job is to resume the suite's own state machine.

Not every occurrence is automatically wrong, but each one must justify why it belongs to the local capability rather than to an unnecessary global workflow.

---

## Design tests for a skill

Use these tests while rewriting individual skills.

### Direct-entry test

Given a natural task and enough real-world context, can the user invoke this skill directly without first running a preparatory suite skill?

### Reorder test

If neighboring capabilities happen in a different order, does this skill still make sense?

### Deletion test

If an adjacent skill disappeared from the suite, would this skill still complete the outcome it claims to own?

If not, the boundary is probably a workflow stage rather than a capability.

### Completion test

Can we state clearly, in one or two sentences, when this skill's local job is done?

### Source-of-truth test

Is the skill reading and writing the most natural durable source, or maintaining a second representation solely for agent coordination?

### Coverage test

Across representative real tasks, is there always at least one skill that can own a useful outcome from the state the user actually has?

### Overlap test

Where two skills overlap, is the difference in their primary outcome understandable without forbidding either skill from doing useful adjacent work?

### Small-task test

Can a small task use one capability directly, without paying the setup and protocol cost designed for a large project?

---

## Suite-level review method

Before finalizing the refactor, test the skill set against a scenario matrix rather than against a canonical flow.

Representative scenarios should include at least:

- "This flaky test fails sometimes. Find out why."
- "I know exactly what to change; implement this small request."
- "I have a rough feature idea and need to sharpen it."
- "Turn this conversation into a durable spec."
- "Break this body of work into independently useful slices."
- "I need to see whether this UI/state model works before deciding."
- "Review this PR against the intended behavior."
- "Improve this awkward module without changing behavior."
- "Research these two libraries and leave me evidence."
- "I am halfway through a task and need to hand it to another agent."
- "I have an existing issue from outside this suite; help me act on it."
- "I do not know which capability fits this situation."

For each scenario, record:

1. which skills can accept it directly;
2. which skill(s) clearly own a useful local outcome;
3. whether any required transition exists only because of suite protocol;
4. whether two or more skills overlap in a confusing way;
5. whether any common task falls into an uncovered gap.

Coverage gaps should be fixed before overlap is optimized away.

---

## Tentative capability map (not a sequence)

This is only a way to inspect coverage. Rows are not phases and imply no order.

| Capability area | Existing skills that may cover it |
| --- | --- |
| Clarify / challenge intent | `grill-with-docs`, `grilling` |
| Navigate the suite | `ask-matt` |
| Research external facts | `research` |
| Explore with runnable evidence | `prototype`, `diagnosing-bugs` |
| Model domain language | `domain-modeling` |
| Design code boundaries | `codebase-design` |
| Produce a durable specification | `to-spec` |
| Decompose work | `to-tickets` |
| Implement behavior | `implement`, `tdd` |
| Diagnose failures | `diagnosing-bugs` |
| Improve existing structure | `improve-codebase-architecture` |
| Review changes | `code-review` |
| Transfer context | `handoff` |
| Configure optional integrations | `setup-matt-pocock-skills` |
| Large ambiguous decision spaces | `wayfinder` |

Part of the refactor may merge, delete, narrow, or broaden entries. The map is not a commitment to preserve every current skill.

---

## Open questions for the implementation discussion

The design direction above is intentional; these details are not settled yet.

### 1. What should `ask-matt` be?

The current router teaches a main flow. In a capability-oriented suite it could instead be a lightweight catalog/decision aid: describe a few plausible capabilities for the user's current state and explain the difference without presenting one canonical lifecycle.

We should decide how opinionated it may be without rebuilding sequencing indirectly.

### 2. Where exactly is the boundary between `implement`, `tdd`, and `diagnosing-bugs`?

All three may write code/tests. That overlap is acceptable, but each needs a distinct owned outcome:

- implementation of requested behavior;
- test-first development as a technique/capability;
- evidence-backed diagnosis and repair of a failure.

We should decide whether `implement` may internally use TDD/review by default, or whether those remain independently chosen capabilities that can be composed manually.

### 3. Does `reconcile` survive at all?

Much of its current purpose appears to exist because the suite created separate implementation and contract lifecycle states. We should first remove that protocol and then see whether a smaller, independently useful capability remains (for example, verifying delivered behavior against a spec) or whether `code-review`/another verification capability already covers it.

### 4. How small should `setup-matt-pocock-skills` become?

Setup should likely configure only optional shared integrations or documentation conventions that multiple skills truly need. It should not define a large tracker capability contract solely to support suite-wide lifecycle semantics.

The remaining common configuration, if any, needs to be identified from the rewritten local capabilities rather than designed up front.

### 5. What persistence should be default versus optional?

Some skills naturally produce durable artifacts (`to-spec`, research notes, ADRs). Others may not need persistence at all. We should decide capability by capability whether persistence is the product, useful evidence, or merely historical workflow machinery.

### 6. Which human confirmation gates are intrinsic?

Manual control should remain where the user is making a real decision: product scope, architecture choice, destructive action, publication, or other meaningful commitment.

We should remove confirmation gates that exist only because a workflow crosses an artificial stage boundary.

### 7. How much overlap is too much?

The default is to tolerate overlap rather than leave gaps. Still, if two skills have the same natural inputs, same owned outcome, and same completion condition, they are probably duplicates rather than healthy overlap.

That gives us a practical merge test without requiring disjoint boundaries.

### 8. Is `wayfinder` a capability or a workflow bundle?

Its current shape coordinates a long-running decision process. We should decide whether its independently useful capability is "map and resolve a large ambiguous decision space" or whether it should decompose into smaller reusable capabilities.

### 9. What should happen to tracker-native coordination for concurrent agents?

Claiming and blocking may be useful in genuinely concurrent execution, but they should not be mandatory semantics for ordinary skill use. We should decide whether concurrency coordination belongs in a separate optional capability/integration rather than in `implement` and the core suite.

---

## Migration constraint

The implementation refactor should optimize for simplification, not preservation of the current protocol.

Do not ask, "How do we reproduce every current lifecycle behavior in the new design?"

Ask instead:

1. What local capability is actually useful here?
2. What natural inputs does it need?
3. What outcome does it own?
4. What real source of truth already represents the surrounding state?
5. Which current rules disappear once no canonical sequence is assumed?

It is acceptable—and expected—for substantial protocol code, state, setup, and cross-skill instructions to be deleted rather than relocated.

---

## Target end state

The suite should feel like this:

```text
small, locally complete capabilities
+ broad natural inputs
+ clear completion conditions
+ intentional overlap
+ strong practical coverage
+ manual user choice
+ minimal shared state
+ no required canonical order
```

Not this:

```text
workflow stages
+ transition rules
+ lifecycle metadata
+ recovery protocol
+ mandatory setup
+ hidden predecessor contracts
```

The refactor succeeds when users can compose the skills freely because each skill is locally trustworthy—not because the suite successfully shepherds every task through one correct sequence.
