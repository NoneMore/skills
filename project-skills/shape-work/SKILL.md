---
name: shape-work
description: "Shape an engineering request against existing project evidence, then decide whether it is ready for direct implementation, needs a bounded investigation, or needs explicit execution planning."
disable-model-invocation: true
---

# Shape Work

Turn a user-stated engineering outcome into a trustworthy next execution contract without depending on a harness-specific Plan Mode.

Shaping answers: **what kind of work is this in the current project, and what must happen next?** It does not own detailed execution planning or evidence-producing investigation.

## Authority and tracker contract

Shaping is read-only by default. Do not modify production code, tracked project work, repository history, deployment state, dependencies, or external systems merely to understand the request.

If `docs/agents/issues.md` exists, read it before describing or persisting tracked work. If the user explicitly asks to persist shaped work, the configured tracker contract is authoritative. If persistence is requested but no tracker contract exists, stop before tracker mutation and tell the user to run `setup-tracker`.

Do not require a tracker merely to shape work transiently.

## 1. Establish the desired outcome

Start from the user's requested observable result, not from an assumed implementation.

Use conversation context and existing project evidence to clarify:

- the outcome the user wants to become true;
- material non-goals or constraints already stated;
- the current system behavior relevant to that outcome;
- existing seams, invariants, and conventions that constrain implementation.

Inspect repository evidence before asking the user for facts the project can answer. Ask only about consequential product intent, trade-offs, inaccessible facts, or decisions that evidence cannot settle.

Do not turn implementation mechanics into requirements merely because they appear likely.

## 2. Reconnaissance uses existing evidence only

Shaping may inspect evidence that already exists, including:

- source code and tests;
- schemas, configs, manifests, and build metadata;
- maintained project documentation and ADRs;
- existing tracker items and durable project records;
- existing logs or artifacts already supplied to the session;
- relevant repository history when it explains current state.

Use this evidence to understand the current implementation and expose uncertainty.

Shaping must not resolve a consequential unknown by manufacturing new evidence. In particular, do not perform or initiate:

- reproductions whose result is needed to decide the route;
- benchmark, load, performance, or capacity measurement;
- experimental instrumentation;
- disposable prototypes or comparative implementations;
- exploratory test execution intended to establish an uncertain behavior;
- external technical research needed to establish a new fact;
- temporary migrations or other empirical probes.

Ordinary read-only repository navigation is reconnaissance. A probe whose observation would answer a disputed or unknown engineering question is investigation.

## 3. Separate known facts, local mechanics, and consequential unknowns

Classify unresolved matters by their effect on the next step.

- **Known** — existing evidence already establishes the fact strongly enough to proceed.
- **Local** — reversible implementation mechanics that a normal executor can decide without changing the requested outcome, accepted contracts, or material risk.
- **Consequential unknown** — an unanswered question whose answer could materially change scope, architecture, compatibility, data behavior, operational shape, security posture, or whether the requested change is viable.
- **Decision needed** — a consequential choice that evidence cannot decide because it depends on user/product/risk intent rather than an empirical fact.

Do not escalate ordinary implementation uncertainty into investigation. Analysis or discovery needed while implementing a well-defined observable change still belongs to the change unless a consequential unknown must be resolved first.

## 4. Stop at the investigation boundary

When a consequential unknown cannot be resolved from existing evidence and answering it requires a new observation, experiment, measurement, reproduction, prototype, or external research, shaping must stop resolving that question.

Produce the smallest useful investigation contract:

```markdown
Question: <decision-relevant question>
Why it matters: <what route or decision depends on the answer>
Known evidence: <relevant existing evidence and its limits>
Completion condition: <what evidence-backed answer would resolve the uncertainty>
```

When `engineering-investigation` is available, hand this contract to it. Otherwise report the investigation contract for the user or harness to execute separately. Do not emulate the investigation inside `shape-work`.

An investigation may later reveal implementation work. Do not pre-commit to that implementation before the evidence exists.

## 5. Choose the lightest valid next shape

After reconnaissance, end in exactly one of these states.

### Direct change

Use when the desired observable outcome is stable, no consequential unknown blocks starting, and detailed coordination is unnecessary before implementation.

Return a compact execution contract:

```markdown
Outcome: <observable state change>
Constraints: <only governing constraints that matter>
Completion condition: <checkable evidence that the outcome exists>
Sources: <direct provenance, if any>
```

Do not expand this into a layer-by-layer task list. Implementation details remain local unless they are already governing constraints.

### Investigation required

Use when a consequential empirical unknown must be resolved first. Return the investigation contract from Section 4. Do not simultaneously invent the implementation that depends on its answer.

### Execution planning required

Use when intent and governing constraints are stable and there is no blocking consequential unknown, but safe execution needs explicit decomposition, sequencing, dependency analysis, migration stages, or coordination across independently meaningful units.

When `engineering-execution-planning` is available, hand off the accepted intent and governing evidence to it. Harness-native Plan Mode may be used as an interface when available, but `shape-work` must not depend on it or assume its semantics.

Do not manufacture multiple work items merely because many files or layers are involved.

### User decision required

Use when the route depends on a consequential product, compatibility, risk, policy, or architecture choice that evidence cannot settle. Present the decision and the smallest set of materially distinct options; do not disguise a preference as an empirical investigation.

## 6. Persist only durable work, and only when requested

Tracker persistence is an output option, not a prerequisite for shaping.

When the user explicitly asks to persist the shaped result, follow `docs/agents/issues.md` exactly:

- persist a direct observable state change as one `change` when it is genuinely one execution leaf;
- persist an empirical uncertainty as one `investigation` whose completion condition is the answer/evidence, not the later implementation;
- persist multiple changes only after their independently meaningful boundaries and real dependency edges are established; do not translate every implementation step into a tracked issue;
- preserve direct provenance in `Sources`;
- use `Parent` only for real decomposition and `BlockedBy` only for true scheduling dependencies;
- keep completion conditions outcome-level and checkable rather than using implementation checklists as the definition of done.

Do not persist transient implementation mechanics, speculative task lists, or a plan merely because it was written down.

## 7. Report the shaping result

Keep the report compact. State:

- the desired outcome as understood;
- the most relevant existing evidence;
- the selected next shape (`direct change`, `investigation required`, `execution planning required`, or `user decision required`);
- the contract or handoff needed for that next step;
- whether anything was persisted.

Do not include a transcript of repository exploration.

## Exit condition

Shaping is complete when the next kind of work is unambiguous without pretending unknown evidence already exists: either a bounded change can start, a bounded investigation is defined, explicit execution planning is warranted from accepted intent, or a named user decision is required.
