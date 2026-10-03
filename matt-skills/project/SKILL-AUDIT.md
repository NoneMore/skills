# Matt Project Skills: Consolidation Audit

> Status: draft design audit. This document applies the capability-oriented rules in `DESIGN.md` to the current `matt-skills/project` skill set. It is intentionally about shape and ownership, not migration mechanics.

## Goal

The current project suite has too many independently invokable units because several different things have been modeled as skills:

- real user-facing capabilities;
- development methods;
- vocabulary/reference material;
- wrappers around other skills;
- routers over the suite;
- global setup/protocol machinery;
- long-running workflow coordinators.

Those categories should not all have equal standing.

The default should be: **fewer, broader locally-complete capabilities, with methods and references absorbed underneath them.**

This is not a push toward one giant skill. A skill still needs a clear local outcome. The point is to stop promoting every reusable idea or workflow step into a separate node in the suite.

---

## The skill-existence test

Something deserves to remain a standalone skill only when most of the following are true:

1. **Independent outcome** — a user can reasonably ask for this result directly, and the result is useful on its own.
2. **Direct entry** — it can start from natural project state, not from suite-specific lifecycle state manufactured by another skill.
3. **Local completion** — it can say when its own job is done without handing correctness to another skill.
4. **Meaningful specialization** — it changes agent behavior enough that a dedicated instruction surface materially improves the result.
5. **Reusable shape** — the capability recurs across projects and tasks rather than encoding one preferred workflow.
6. **Absorption would lose something** — folding it into an adjacent capability would materially reduce clarity, quality, discoverability, or coverage.

A thing should usually **not** be a standalone skill when its main identity is one of these:

- a method: TDD, red-green-refactor, a specific interviewing style, a particular refactoring heuristic;
- a reference: vocabulary, glossary, smell list, format rules;
- a wrapper: “call skills A and B, then stop”;
- a router: “choose which other skill should run”;
- protocol glue: lifecycle transitions, canonical result records, reconciliation state;
- setup required only because the suite invented a shared protocol;
- a workflow bundle whose internal steps are themselves independently useful capabilities.

Methods and references can still be valuable. They should live **inside or beside** capabilities, not automatically become capabilities themselves.

---

## Size discipline

Large skills deserve suspicion because size often comes from one of three causes:

1. the skill owns several different outcomes;
2. the skill embeds a global workflow or lifecycle;
3. the skill contains reference material that should be loaded only when relevant.

Size alone is not a failure. Some hard capabilities need substantial guidance. But a large skill should be able to explain why the complexity is intrinsic to its local outcome.

Prefer this shape:

```text
small SKILL.md
  -> clear purpose / inputs / ownership / completion
  -> optional references for techniques or deep guidance
```

over this shape:

```text
large SKILL.md
  -> global state machine
  -> tracker protocol
  -> phase ordering
  -> method doctrine
  -> output persistence rules
  -> downstream routing
```

A reference file does not need to be separately invokable to be reusable.

---

## Current inventory

There are currently 18 project-level skills:

- `ask-matt`
- `code-review`
- `codebase-design`
- `diagnosing-bugs`
- `domain-modeling`
- `grill-with-docs`
- `handoff`
- `implement`
- `improve-codebase-architecture`
- `prototype`
- `reconcile`
- `research`
- `setup-matt-pocock-skills`
- `tdd`
- `to-spec`
- `to-tickets`
- `triage`
- `wayfinder`

The audit below is deliberately biased toward deletion and absorption. The burden of proof is on keeping a separate skill.

---

## Initial disposition

| Current skill | Initial disposition | Reason |
| --- | --- | --- |
| `implement` | **Keep, rewrite heavily** | Clear independent outcome: make a requested code change work and verify it. Remove lifecycle, mandatory TDD, mandatory review, canonical result records, and tracker orchestration. |
| `diagnosing-bugs` | **Keep, shrink** | Evidence-backed diagnosis is a real independent capability. Keep the feedback-loop discipline, but remove ritual that is not necessary for every investigation. Allow overlap with implementation when a repair is obvious/useful. |
| `code-review` | **Keep, shrink** | Independent read-only evaluation of a diff/PR is a clear capability. Spec conformance can absorb the useful part of `reconcile`. Tracker setup should not be a prerequisite. |
| `prototype` | **Keep, broaden and shrink** | “Build a cheap concrete artifact to answer a question” is independently useful. Current logic/UI branching and capture protocol are too prescriptive for the core skill. |
| `research` | **Keep or merge into investigation** | Evidence-backed external/source research is useful, but background-agent execution and mandatory Markdown persistence are implementation choices. Re-evaluate whether it is distinct enough from a broader `investigate` capability. |
| `to-spec` | **Keep, rewrite heavily** | Producing a durable specification from sufficiently settled material is a clear transformation. Remove tracker lifecycle, mandatory roles, testing doctrine, and prescribed next step. |
| `to-tickets` | **Keep, rewrite heavily** | Decomposing concrete work into actionable slices is independently useful. Publishing is optional integration; work-item roles and execution-frontier semantics should disappear. |
| `triage` | **Keep only if reduced to intake assessment** | Raw incoming issues/PRs do need assessment. The capability should classify, clarify, close/defer, or make actionable using the tracker’s native concepts—not maintain a suite-wide state machine. |
| `handoff` | **Keep for now; consider moving to global** | Producing a portable continuation artifact is independently useful, but it is not specifically a project-lifecycle capability. Remove suite-routing instructions from the handoff. |
| `domain-modeling` | **Absorb or reshape into `design`** | Much of it is design guidance plus durable glossary/ADR maintenance. Useful behavior, but likely not a separate node from the broader act of designing a system. |
| `codebase-design` | **Absorb as reference/design guidance** | The current skill is primarily vocabulary and principles for deep modules. That is valuable reference material, but vocabulary is not by itself an independent project capability. |
| `improve-codebase-architecture` | **Merge into a broader design/architecture capability** | Scanning for architectural friction is useful, but the current skill is a workflow bundle: scan, generate HTML, rank, grill, update domain docs. Keep the architectural-review outcome, not the bundle. |
| `grill-with-docs` | **Remove** | Pure wrapper over `grilling` + `domain-modeling`, plus phase-transition instructions. It owns no distinct local outcome that those behaviors cannot cover directly. |
| `tdd` | **Remove** | TDD is a development method, not a unique capability. Testing strategy belongs to the capability doing the work. |
| `reconcile` | **Remove** | Mostly exists to reconcile lifecycle state the suite itself created. Requirement satisfaction belongs in review/verification or in the owning task’s normal completion. |
| `setup-matt-pocock-skills` | **Remove or reduce to optional integration setup** | Most of its size configures lifecycle machinery that should disappear. Capabilities should discover/use Git/tracker/docs directly where possible and ask only for missing integration details they actually need. |
| `ask-matt` | **Remove as a skill; replace with a catalog if useful** | Routing is product/documentation UX, not a project capability. A README/catalog can explain available capabilities without becoming part of the execution graph. |
| `wayfinder` | **Dissolve and preserve only the useful primitives** | It is currently a multi-session workflow engine over decision maps, ticket types, claims, frontiers, research/prototype/grilling, and tracker state. The underlying need is real; the current skill bundles too many independently useful capabilities. |

This is an audit direction, not yet a migration checklist. Names may change and some rows may converge further.

---

## Likely consolidation clusters

### 1. Implementation

`implement` should become the owner of ordinary code changes.

It should be allowed to:

- inspect the codebase;
- clarify small ambiguities that do not require a separate design exercise;
- choose an appropriate testing strategy;
- write tests before, during, or after implementation;
- run type checks, linters, targeted tests, full tests, manual checks, or other verification as appropriate;
- perform small diagnostic experiments when implementation uncovers uncertainty;
- optionally use review techniques before reporting completion.

It should not require:

- `tdd`;
- `code-review`;
- `reconcile`;
- a tracker role;
- a claim state;
- an implementation-result schema;
- a delivery lifecycle.

The capability is complete when the requested change is implemented and there is proportionate evidence that it works.

### 2. Investigation

There is a plausible consolidation between `diagnosing-bugs` and `research`.

Both fundamentally answer:

> We do not know something important yet. Gather evidence until we do.

Possible broad capability: `investigate`.

It could accept:

- a failing behavior;
- a performance regression;
- an unknown API/library fact;
- a repository-history question;
- a technical uncertainty that needs experiments or source reading.

Its owned outcome would be an **evidence-backed answer**.

Specialized techniques could then live as references:

- tight repro loops;
- bisection;
- instrumentation;
- primary-source research;
- benchmarks;
- differential testing.

Open question: debugging may be common and specialized enough to deserve a direct `diagnosing-bugs` entry even if it overlaps a broader investigation capability. Coverage matters more than eliminating that overlap.

### 3. Design / architecture

`domain-modeling`, `codebase-design`, `improve-codebase-architecture`, and much of `grill-with-docs` currently occupy one broad space: help make design decisions and improve system shape.

A likely end state is one user-facing capability such as `design` or `architecture`, backed by references for:

- domain language and glossary maintenance;
- ADR guidance;
- deep-module vocabulary;
- seam/interface design;
- design-it-twice;
- architecture review/deepening heuristics;
- interviewing/grilling technique.

The capability can accept either:

- a new design question; or
- an existing codebase area that needs architectural improvement.

Its outcome is not “run the design process.” Its outcome is a **clear design decision or architecture direction**, with durable docs updated only when those docs are themselves useful.

This avoids splitting “design a module,” “model the domain,” “scan architecture,” and “interview about design” into separate workflow nodes.

### 4. Specification and decomposition

`to-spec` and `to-tickets` appear worth keeping separate because they produce different independently useful artifacts:

- a spec captures settled intent and decisions;
- tickets decompose work into independently actionable pieces.

They should still overlap freely. A small task may skip both. A user may create tickets directly from a conversation. A spec may be useful without tickets.

Neither should encode what happens next.

### 5. Review / verification

`code-review` should absorb the useful part of `reconcile`:

- compare implementation against intended behavior when intent is available;
- identify missing, incorrect, or extra behavior;
- evaluate maintainability/standards when useful.

There is no need for a separate lifecycle reconciliation capability merely to decide whether code satisfies a request.

If the user asks “does the current system satisfy this spec?” without presenting a fresh diff, review should be broad enough to inspect the relevant current code/behavior rather than require a synthetic implementation lifecycle.

### 6. Intake / tracker interaction

`triage` can remain if it is about a real user problem:

> I have raw incoming issues/PRs; help me decide what each one needs.

It should use the tracker’s native state and conventions rather than impose five canonical suite states.

`setup-matt-pocock-skills` should not remain a mandatory precondition. If a tracker action needs information that cannot be discovered, ask for that information at the point of use or provide a small optional integration configuration surface.

### 7. Multi-session work

`wayfinder` should not survive merely because large efforts span many sessions.

Large work can already compose:

- design/interview;
- research/investigation;
- prototype;
- spec;
- decomposition;
- handoff;
- tracker-native issues and dependencies.

If an explicit **decision map** proves useful as an independent artifact, preserve that artifact pattern. Do not automatically preserve the current Wayfinder workflow, ticket taxonomy, claim protocol, or “one ticket per session” rule around it.

The test is whether users independently ask for “map this decision space” as a result—not whether the old workflow needs a coordinator.

---

## A possible target shape

This is intentionally illustrative rather than a final naming decision.

An aggressive but plausible project suite could be roughly:

```text
design          # decide system/domain/architecture shape
investigate     # answer uncertain technical questions with evidence
prototype       # build a cheap artifact to learn from
implement       # make requested code changes and verify them
review          # evaluate code/behavior against intent and quality
specify         # turn settled intent into a durable specification
decompose       # split concrete work into actionable pieces
triage          # assess raw incoming tracker work
handoff         # package continuation context (possibly global, not project)
```

That is about half the current count without intentionally creating a coverage gap.

It is not important that the final number is nine. It is important that every remaining skill has a strong reason to exist independently.

---

## What disappears into references or ordinary reasoning

A smaller suite does **not** mean losing the ideas currently encoded in deleted skills.

The following can remain as reusable guidance without being invokable nodes:

- TDD / red-green-refactor;
- mocking guidance;
- test seam guidance;
- deep-module vocabulary;
- design-it-twice;
- code smell baselines;
- debugging feedback-loop techniques;
- domain glossary format;
- ADR format;
- tracer-bullet decomposition guidance;
- research source-quality rules;
- decision-map patterns;
- handoff formatting conventions.

The distinction is important:

> **Instruction reuse does not require skill proliferation.**

References are for knowledge. Skills are for capabilities.

---

## Open boundary questions

The next design discussion should focus on these, in order:

1. **Do `research` and `diagnosing-bugs` converge into one `investigate` capability, or is debugging specialized enough to keep a dedicated entry?**
2. **Should `domain-modeling`, `codebase-design`, and architecture improvement become one broad `design` capability, or are there two genuinely different user-facing outcomes hidden there?**
3. **How broad should `review` be?** Diff/PR review only, or also current-state verification against a spec/request?
4. **Does `triage` remain project-level, or is ordinary tracker handling enough once the suite state machine disappears?**
5. **Is `handoff` project-specific at all, or should it move to global/meta utilities?**
6. **Does the useful core of Wayfinder reduce to an optional decision-map artifact pattern, or is there still a standalone capability after removing its orchestration machinery?**
7. **What, if anything, still requires shared setup after all lifecycle coupling is removed?**

These questions should be answered by real scenario coverage, not by preserving the existing directory structure.

---

## Migration rule

When removing a skill, do not ask “where do all of its lines go?”

Instead classify each piece:

- **capability behavior** -> move into the capability that owns the outcome;
- **useful technique/reference** -> move to an optional reference;
- **integration detail** -> keep only near the capability that needs it;
- **workflow sequencing** -> delete;
- **suite-specific lifecycle/protocol** -> delete;
- **duplicated real-world state** -> delete and read the real source instead.

A successful consolidation should delete substantial instruction text, not merely relocate it.