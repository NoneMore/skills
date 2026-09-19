# AGENTS.md Wizard

**Version: v0.6**

A workspace-agnostic Meta Skill for creating, refreshing, or auditing agent instruction artifacts. `AGENTS.md` is the generic fallback, but the authoring method is not tied to one runtime.

The core contract is:

**Inspect facts. Present choices. Ask decisions. Confirm the draft. Encode behavior.**

## What changed in v0.6

v0.6 changes the default from autonomous authoring to a user-controlled guided workflow:

- a bare invocation authorizes focused inspection and interviewing, not a file write;
- workspace observations are separated from human policy decisions;
- authority, mutability, lifecycle, synchronization, ownership, and scope hypotheses require user confirmation;
- the wizard presents facts, recommendations, open choices, target, and scope before drafting;
- every create or refresh receives a reviewable draft/patch and explicit pre-write approval;
- target substitution and nested artifact creation are recommendations, never silent autonomous choices;
- best-effort, no-interview, and write-without-review remain explicit user-controlled exceptions;
- verification stays proportional to the instruction artifact and avoids testing unchanged project code.

The v0.5 runtime consolidation remains: ordinary runs use the self-contained core, with references loaded only for a live loader, composition, or drafting issue.

## Core behavior

The wizard separates two concerns that are easy to conflate:

- **target intent** — what artifact and scope the user asked for;
- **loader semantics** — what the active harness actually loads and how applicable instructions compose.

A user-requested filename does not redefine a harness loader. Conversely, a harness default does not erase an explicitly requested deliverable. For generic/result-oriented setup, the wizard recommends the effective harness target and asks the user to confirm it; an explicitly named inert file is diagnosed rather than silently replaced.

The wizard inspects the workspace before interviewing. It uses maintained docs, configuration, code, notebooks, data/status structure, and existing instructions as evidence, but does not treat workspace shape as proof of human policy. It reports observed facts separately from recommended interpretations and asks the user to decide choices that affect authority, mutability, lifecycle, synchronization, ownership, approval, or scope. Typical rounds contain 1–3 questions.

A bare `$agents-md-wizard` invocation stops at a guided checkpoint. Before writing, the wizard shows the proposed target, scope, behavioral contract, material policy changes, and assumptions, then asks for approval. Zero policy questions is reserved for cases where the user already supplied the material contract or requested an evidence-based audit; pre-write approval still applies unless the user explicitly waived review.

Existing instruction artifacts are prior human intent, not disposable boilerplate. Refreshes preserve valid guardrails, remove verified drift or duplication, and surface only unresolved material conflicts.

For scoped work, the wizard writes a local delta only when the active instruction topology actually composes broader and narrower instructions. Local candidates are classified as **inherit / extend / narrow / override**; unchanged broader policy is omitted locally. Path nesting alone never proves inheritance.

## Runtime architecture

```text
SKILL.md
├── resolve target + effective loading
├── focused workspace inspection
├── observation/policy separation
├── guided decision interview
├── smallest effective instruction surface
├── reviewable draft / migration preview
└── user-approved write + proportional verification / audit

references/
├── scoped-composition.md      # only for difficult composed scopes
├── authoring-patterns.md      # only for difficult drafting/migration
└── harnesses/
    ├── codex.md               # concrete loader boundary
    └── pi.md                  # concrete loader boundary
```

Ordinary create/refresh work should not preload the reference directory. When exact loader behavior matters, load only the matching concrete harness profile. The two common references are exception lookup, not required reading.

For an unknown harness, the core uses a conservative fallback: honor an explicit artifact, avoid inventing discovery/precedence/inheritance semantics, and ask only if the unknown loader behavior changes what must be written.

## Authoring standard

The output should be the smallest instruction surface that reliably changes downstream behavior. Good content includes non-obvious source-of-truth relationships, mutation/lifecycle rules, durable invariants, branch-specific pointers, surprising dependencies, and observable completion criteria.

Avoid generic quality slogans, exhaustive trees, copied manifests, transient inventories, or duplicated maintained docs. When another document owns detailed truth, use a precise task-triggered pointer.

Before writing, the wizard checks that the draft is:

- **Grounded** — consequential rules come from evidence, governing context, or settled human decisions.
- **Effective** — the chosen artifact is actually meaningful to the harness, unless the user deliberately requested otherwise.
- **Scoped** — local rules are genuine deltas when composition exists.
- **Lean** — no low-value duplication or cheap environmental facts.
- **Observable** — important completion rules can be checked.
- **Preserving** — valid existing human intent is not silently lost.

## Modes

- **Create / setup** — inspect, interview, preview, obtain approval, then establish the effective project instruction artifact.
- **Refresh / update** — inspect drift, preview the minimal policy migration, obtain approval, then patch.
- **Audit / review** — report ranked findings without editing.
- **Best effort / skip interview / write without review** — explicit exceptions that permit more autonomy within the user-supplied scope.
- **Scoped / local** — create or refresh a narrower instruction surface using actual harness composition semantics.

## Package layout

```text
agents-md-wizard/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── authoring-patterns.md
│   ├── scoped-composition.md
│   └── harnesses/
│       ├── codex.md
│       └── pi.md
├── examples/
├── evals/
│   └── scenarios.md
├── CHANGELOG.md
└── README.md
```

Examples and evals remain in the source ZIP for development and regression testing. A registry can package only runtime-required files if it prefers a smaller distribution.

## Suggested prompts

```text
Use $agents-md-wizard to inspect this workspace, ask me the policy decisions, and show me the proposed AGENTS.md before writing it.
```

```text
Use $agents-md-wizard to refresh the existing agent instructions. Show the proposed policy changes and wait for my approval before writing.
```

```text
Create local agent instructions for `analysis/`. Reuse broader rules only if this harness actually composes them.
```

```text
Audit our AGENTS.md, but don't edit anything.
```

```text
Use $agents-md-wizard in best-effort mode, write without review, and list material assumptions.
```

## Installation and publishing

Install/copy the `agents-md-wizard` directory wherever your harness loads Skills. `agents/openai.yaml` keeps invocation explicit by default; other harnesses should use their own invocation mechanism.

Exact Skill installation paths vary by harness and version. No license is included in this ZIP; add the license appropriate for your project before publishing to a shared registry.
