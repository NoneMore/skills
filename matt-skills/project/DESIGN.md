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
6. **Capability scarcity**: reusable ideas, methods, references, routers, and wrappers should not automatically become separately invokable skills.

The goal is not to remove discipline. The goal is to move discipline back into the local capability that needs it instead of encoding discipline as a global sequence.

See [SKILL-AUDIT.md](./SKILL-AUDIT.md) for the current consolidation audit and tentative disposition of every project skill.

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

## A skill must earn its existence

A reusable idea should not become a standalone skill merely because it is useful.

A project skill should normally have:

- an independently useful user-facing outcome;
- natural inputs that exist outside this suite;
- a local completion condition;
- enough specialized behavior to justify dedicated instructions;
- a reason that absorbing it into a neighboring capability would materially reduce quality, clarity, discoverability, or coverage.

The following are normally **not** sufficient reasons for a standalone skill:

- it is a preferred development method;
- it provides shared vocabulary;
- several other skills want to consult the same guidance;
- it wraps two other skills;
- it routes users to another skill;
- it configures protocol invented by the suite itself;
- it coordinates a fixed ordering between otherwise useful capabilities.

This is why `tdd` should not remain a standalone project skill. TDD is one implementation technique. The capability doing the work owns testing and verification and may choose TDD, test-after, characterization tests, property tests, type checking, manual verification, or another appropriate strategy.

**Instruction reuse does not require skill proliferation.** Shared methods and vocabulary can live in reference material that capabilities load when useful.

---

## Size is a design signal

There is no fixed line-count limit for a skill, but size creates a burden of proof.

A large `SKILL.md` often indicates one of three problems:

1. several distinct outcomes have been bundled into one workflow;
2. global sequencing/lifecycle machinery has accumulated around a local capability;
3. reusable reference material is being loaded as core instructions every time.

Prefer:

```text
small capability contract
+ optional technique/reference material
+ natural project artifacts
```

over:

```text
global state machine
+ tracker adapter protocol
+ phase ordering
+ method doctrine
+ persistence schema
+ next-step routing
```

If a capability is intrinsically hard, it may still need substantial instructions. The question is whether the complexity belongs to the local outcome or to an invented workflow surrounding it.

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

- investigation may run experiments that resemble research or prototyping;
- prototyping may discover architectural constraints that overlap with design;
- implementation may run tests or perform small diagnostic experiments;
- review may identify design problems.

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

A skill may use another model-invoked capability or shared reference when it is genuinely part of completing its own local outcome. This should not silently expand into ownership of a project-wide lifecycle.

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

### Existence test

Does this thing produce an independently valuable result, or is it primarily a method, reference, wrapper, router, or protocol mechanism?

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

### Absorption test

If this skill were folded into its nearest neighboring capability as optional guidance, what meaningful user-facing capability would be lost?

If the answer is “none,” it probably should not remain independently invokable.

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

The current consolidation audit suggests a much smaller shape than the existing directory structure. One plausible target is:

| Capability area | Possible surviving capability |
| --- | --- |
| Make design/architecture decisions | `design` (potentially absorbing domain modeling, codebase design, architecture improvement, and design grilling) |
| Resolve technical uncertainty with evidence | `investigate` or a smaller `diagnosing-bugs` + `research` pair |
| Learn through a cheap concrete artifact | `prototype` |
| Make code changes | `implement` |
| Evaluate code/behavior | `review` |
| Produce a durable specification | `specify` / `to-spec` |
| Decompose concrete work | `decompose` / `to-tickets` |
| Assess raw incoming tracker work | `triage` |
| Transfer continuation context | `handoff` (possibly global rather than project-level) |

This is a coverage map, not a commitment to names or an ordering. It is intentionally about half the current project-skill count.

The audit currently favors removing or absorbing `tdd`, `reconcile`, `grill-with-docs`, `ask-matt`, most of `setup-matt-pocock-skills`, `codebase-design` as an invokable node, and the current workflow form of `wayfinder`.

---

## Open questions for the implementation discussion

The design direction above is intentional; these details are not settled yet.

### 1. Do `research` and `diagnosing-bugs` converge into `investigate`?

Both produce evidence-backed answers under uncertainty. Debugging may still be common and specialized enough to deserve a dedicated entry. Decide based on scenario coverage and discoverability, not on preserving names.

### 2. Does design become one capability?

`domain-modeling`, `codebase-design`, `improve-codebase-architecture`, and `grill-with-docs` heavily overlap around making better design decisions. A likely direction is one user-facing design/architecture capability backed by reusable references for domain language, ADRs, deep modules, seams, design-it-twice, and grilling technique.

The unresolved question is whether there are actually two distinct user-facing outcomes in this cluster that deserve separate capabilities.

### 3. How broad should `review` be?

The current `code-review` is diff-oriented. If `reconcile` disappears, review may also need to answer “does the current implementation satisfy this request/spec?” even without a fresh diff.

### 4. Does `triage` remain project-level?

Raw incoming work needs assessment, but the current suite-wide state machine should disappear. Decide whether a lightweight tracker-intake capability still adds enough value beyond normal issue handling.

### 5. Is `handoff` project-specific?

The output is a portable continuation artifact, which may belong under global/meta utilities rather than project engineering.

### 6. Does any standalone capability survive from `wayfinder`?

The current skill coordinates a decision-map workflow, multiple ticket types, claims, frontiers, research/prototype/grilling, and tracker state. Preserve an explicit “map this decision space” capability only if that artifact is independently valuable after orchestration is removed.

### 7. What shared setup survives?

Do not design a replacement setup contract up front. Rewrite capabilities first; then identify any configuration that is genuinely shared and cannot be discovered lazily.

### 8. Which persistence is intrinsic?

A spec is durable because the artifact is the point. A research note may or may not need persistence. A prototype may be disposable. Decide persistence per capability rather than globally.

---

## Migration constraint

The implementation refactor should optimize for simplification, not preservation of the current protocol or directory structure.

Do not ask, "How do we reproduce every current lifecycle behavior in the new design?"

Ask instead:

1. What local capability is actually useful here?
2. What natural inputs does it need?
3. What outcome does it own?
4. What real source of truth already represents the surrounding state?
5. Which current rules disappear once no canonical sequence is assumed?
6. Does this behavior need an independently invokable skill at all?

When removing a skill, classify its contents rather than moving the whole file:

- capability behavior -> absorb into the capability that owns the outcome;
- useful technique/reference -> retain as optional reference material;
- integration detail -> keep only near the capability that needs it;
- workflow sequencing -> delete;
- suite lifecycle/protocol -> delete;
- duplicated real-world state -> delete and read the real source instead.

It is acceptable—and expected—for substantial instruction text, state, setup, and cross-skill instructions to be deleted rather than relocated.

---

## Target end state

The suite should feel like this:

```text
few, locally complete capabilities
+ broad natural inputs
+ clear completion conditions
+ intentional overlap
+ strong practical coverage
+ optional methods/references underneath
+ manual user choice
+ minimal shared state
+ no required canonical order
```

Not this:

```text
many workflow stages
+ wrappers and routers
+ technique-as-skill
+ transition rules
+ lifecycle metadata
+ mandatory setup
+ recovery protocol
```
