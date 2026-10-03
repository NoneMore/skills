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

See [SKILL-AUDIT.md](./SKILL-AUDIT.md) for the current consolidation audit and tentative disposition of every project skill, [OUTCOMES.md](./OUTCOMES.md) for the outcome/persistence model, [REVIEW.md](./REVIEW.md) for the current review boundary, and [AUTHORING.md](./AUTHORING.md) for the current skill-body authoring model.

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
- `review` can review a diff, current implementation, design, spec, decomposition, or other existing result.
- investigation techniques can be used inside whichever capability owns the requested outcome.

There may still be common combinations. They are examples, not lifecycle law.

---

## Manual invocation is control, not sequencing

User-invoked skills remain user-invoked when explicit human choice is valuable. Manual invocation is a feature: the user decides which capability to apply next.

However, manual invocation must not imply a canonical sequence.

A skill may say that another capability could be useful. It should not require the user to traverse a prescribed next stage merely because this skill completed.

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
- it coordinates a fixed ordering between otherwise useful capabilities;
- it mainly names one investigation technique or problem-solving mode.

This is why `tdd`, ordinary research/investigation, prototyping, and diagnosis should not automatically remain standalone project skills. They can be techniques used by the capability that owns the user's actual requested outcome.

**Instruction reuse does not require skill proliferation.** Shared methods and vocabulary can live in reference material that capabilities load when useful.

---

## Skills own outcomes, not artifacts

Every skill must have a clear local outcome, but it does not follow that every skill must create a durable artifact.

**Outcome and artifact are separate design decisions.**

For capabilities whose useful result is a decision, explanation, or judgment, conversation context is a valid default output. Persist only when persistence is itself part of the value: when the artifact is the requested product, future sessions/collaborators need it, the result is durable project knowledge, an existing real source of truth naturally owns it, or the user asks for it.

Do not invent canonical result blocks or per-skill output documents merely to prove that a capability ran.

The governing rule is:

> **Skills own outcomes; artifacts are created only when persistence is part of the value.**

See [OUTCOMES.md](./OUTCOMES.md) for the detailed persistence rules.

---

## How a capability skill body should be written

The core `SKILL.md` should contain guidance that remains valuable across multiple concrete methods of completing the capability.

Prefer:

```text
SKILL.md
  = capability contract
  + capability-specific invariants
  + decision heuristics

references/
  = specialized expert methods

conversation + repository
  = actual task state
```

The core skill body should not become a methodology handbook or a router over rigid task-subtype workflows.

### Capability contract

Describe what outcome the skill owns, what natural inputs it accepts, what adjacent work it may perform, when its local job is done, and what suite-specific prerequisites it explicitly does not require.

### Capability invariants

Keep instructions that remain important regardless of the exact method used. These are the most valuable behavior-shaping parts of the core skill.

Examples include preserving relevant behavior during implementation, making material design decisions explicit, or supporting review findings with evidence proportionate to the claim.

### Decision heuristics

Use conditional cues for choosing among techniques according to uncertainty, risk, evidence needs, and task shape.

For example, an implementation skill may say to investigate when the failure mechanism is unclear, use a cheap automated check when it provides stronger evidence than manual confidence, verify risky integration boundaries directly, or use a spike when it cheaply reduces uncertainty.

These heuristics enable debugging, testing, prototyping, research, or local design without turning any of them into required stages.

### Specialized references

Move reusable expert methods into optional references when they materially improve behavior but do not define a separate user-facing capability.

Possible examples include debugging, testing strategies, refactoring, migrations, performance work, domain modeling, interface design, and object-specific review guidance.

The reference taxonomy does not need to be uniform across skills. Review guidance may naturally vary by object; implementation guidance may vary by problem shape; design guidance may vary by decision domain or modeling technique.

### Core-vs-reference test

For every instruction, ask:

> Does this remain true across multiple materially different ways of completing the capability?

If yes, it probably belongs in `SKILL.md`.

If it is specific to one technique, problem shape, artifact type, or expert discipline, it probably belongs in optional reference material.

Do not replace the old horizontal workflow with vertical workflow trees such as `implement-feature`, `implement-bug`, `implement-refactor`, and `implement-migration`, each with its own rigid phases.

See [AUTHORING.md](./AUTHORING.md) for the fuller authoring guidance.

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
+ high-value invariants
+ conditional decision heuristics
+ optional technique/reference material
+ natural project artifacts
```

If a capability is intrinsically hard, it may still need substantial instructions. The question is whether the complexity belongs to the local outcome or to an invented workflow surrounding it.

---

## Boundary model for every skill

Each project skill should be reviewable using the same local boundary model.

### Purpose

One sentence describing the capability in terms of the local problem it solves.

### Accepts

The natural forms of input the skill can work from. Inputs should be semantic rather than tied to a predecessor skill.

### Owns

The outcome this skill is responsible for producing. This is the center of the skill.

### May also

Adjacent work the skill is allowed to perform when doing so is useful to complete its owned outcome.

### Done when

A local completion condition that can be evaluated without asking where the skill sits in a larger workflow.

### Does not require

Any predecessor, successor, tracker role, lifecycle marker, suite-specific persisted state, or artifact that is intentionally *not* a prerequisite.

---

## Coverage over disjointness

The capability map should aim for complete practical coverage, not mutually exclusive partitions.

If two skills can both reasonably accept a task, that is usually tolerable. The distinction should come from their center of gravity, not from artificial guardrails.

When forced to choose, prefer **overlap with clear ownership** over **clean-looking separation with uncovered space**.

---

## Investigation is baseline behavior

Reading code, docs, history, issues, external sources, reproducing failures, instrumenting, benchmarking, bisecting, comparing alternatives, testing hypotheses, writing spikes, and prototyping are ordinary evidence-gathering behaviors.

They do not need standalone project skills merely because they are useful.

Capabilities such as `design`, `implement`, `review`, and `triage` may use these actions directly when they help complete the capability's owned outcome.

---

## No hidden predecessor contracts

A skill should not require another skill to have run merely to manufacture suite-specific state.

Skills should consume reality, not proof that another skill previously ran.

---

## Prefer real sources of truth

Do not create a second database about the state of the work unless the new state represents information that has no natural home elsewhere.

Prefer code/tests, commits/branches, issues, PRs, CI, ADRs/domain docs, and explicit artifacts when the artifact itself is the useful output.

If state is necessary only to make the workflow protocol work, remove the protocol before formalizing the state.

---

## Composition rules

1. Any skill should be directly enterable when its natural inputs exist.
2. Skills may suggest neighbors, but do not own the next step.
3. Supporting composition must remain local.
4. Optional context must stay optional.
5. Integrations are adapters, not the domain model.
6. Persistence is local to the outcome.
7. References are optional expert guidance, not hidden required stages.

---

## Protocol smells to remove

During the refactor, treat the following as warning signs:

- a named main flow that most work is expected to follow;
- "after this, invoke X" as a correctness requirement;
- skill correctness depending on the previous skill's private output format;
- suite-wide lifecycle enums;
- claim/release/suspend protocols used primarily for agent coordination;
- canonical result blocks whose information already exists elsewhere;
- reconciliation required before completed work counts;
- setup unrelated to the local capability;
- work-item roles used mainly for routing between skills;
- mandatory artifacts created only for cross-skill handoff;
- rigid task-subtype branches that recreate workflow inside one capability;
- references that are effectively mandatory phases disguised as optional files.

---

## Design tests for a skill

Use these tests while rewriting individual skills:

- **Existence test** — does it produce an independently valuable result?
- **Direct-entry test** — can it start from natural inputs?
- **Reorder test** — does it still make sense if neighboring capabilities occur in another order?
- **Deletion test** — can it still finish if an adjacent skill disappears?
- **Completion test** — is the local done condition clear?
- **Source-of-truth test** — does it use natural durable state?
- **Persistence test** — is a durable artifact intrinsic to the value?
- **Absorption test** — what meaningful user-facing capability is lost if it becomes optional guidance inside a neighbor?
- **Coverage test** — do representative real tasks always have at least one skill that can own a useful result?
- **Overlap test** — where skills overlap, is the difference in primary outcome still understandable?
- **Small-task test** — can a small task use the capability without project-wide setup?
- **Core-vs-reference test** — are core instructions truly cross-method invariants/heuristics, with specialized methods moved out?

---

## Tentative capability map (not a sequence)

The current direction favors a very small project suite:

| Capability area | Possible surviving capability |
| --- | --- |
| Make design/architecture decisions | `design` |
| Make production changes | `implement` |
| Independently evaluate an existing result | `review` |
| Produce a durable specification | `specify` / `to-spec` |
| Decompose concrete work | `decompose` / `to-tickets` |
| Assess raw incoming tracker work | `triage` only if it proves independently useful |
| Transfer continuation context | `handoff`, possibly global rather than project-level |

Current direction favors removing or absorbing `tdd`, `reconcile`, `grill-with-docs`, `ask-matt`, most of `setup-matt-pocock-skills`, `prototype`, ordinary `research` / investigation, `diagnosing-bugs` as a separate capability, `codebase-design` as an invokable node, and the current workflow form of `wayfinder`.

The target count is not a quota.

---

## Current settled boundaries

### `design`

- owns reaching clear design decisions;
- may inspect, research, experiment, spike, prototype, and update durable design knowledge when useful;
- does not own delivering production behavior;
- defaults to explicit decisions and unresolved questions in conversation;
- persistence is optional.

### `review`

- owns independent evaluation of an existing result against relevant expectations;
- accepts code, implementations, designs, specs, plans, decompositions, prototypes, and other sufficiently concrete results;
- uses object-specific evaluation criteria and evidence-gathering methods rather than one universal checklist;
- defaults to findings in conversation unless a natural review surface exists;
- absorbs the useful requirement-satisfaction behavior from `reconcile`.

See [REVIEW.md](./REVIEW.md) for the detailed review model.

---

## Open questions for continued discussion

1. What exactly should `implement` own, especially for bug fixing, refactoring, testing, verification, and delivery?
2. Which implementation invariants are valuable enough to belong in core `SKILL.md`, versus optional references?
3. Is `specify` independently valuable from ordinary artifact writing, and how broad should its accepted inputs be?
4. Is `decompose` a standalone user-facing capability or mainly a planning technique for larger work?
5. Does lightweight `triage` still justify a project skill after suite-wide tracker states disappear?
6. Is `handoff` project-specific at all?
7. Does any standalone capability survive from `wayfinder`, or only optional artifact/decision-map techniques?
8. What, if anything, still requires shared setup after lifecycle coupling is removed?

---

## Migration constraint

The implementation refactor should optimize for simplification, not preservation of the current protocol or directory structure.

When removing a skill, classify its contents rather than moving the whole file:

- capability behavior -> absorb into the capability that owns the outcome;
- capability-level invariant/heuristic -> keep in that capability's core `SKILL.md`;
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
+ small core skill bodies
+ high-value invariants and heuristics
+ optional expert references
+ manual user choice
+ minimal shared state
+ no required canonical order
```

Not this:

```text
many workflow stages
+ wrappers and routers
+ technique-as-skill
+ giant method handbooks
+ task-subtype workflow trees
+ transition rules
+ lifecycle metadata
+ mandatory setup
+ recovery protocol
```
