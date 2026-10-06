# AGENTS.md Wizard

A workspace-agnostic Meta Skill for creating, refreshing, or auditing `AGENTS.md` and equivalent workspace instruction artifacts.

The Skill focuses on the parts that are specific to instruction management: effective loader targeting, preservation of existing human policy, scoped composition, migration, and verification.

The core contract is:

**Inspect facts. Resolve only real decisions. Write the smallest effective instructions. Verify the result.**

## Design changes

This revision removes ceremony that does not reliably change the resulting instructions:

- explicit create/update requests now authorize writing once target, scope, and policy are grounded;
- policy questions are asked only when a non-discoverable unresolved choice would materially change the artifact;
- the mandatory interview and mandatory pre-write approval gates are removed;
- result-oriented setup uses the harness-effective target directly when loader semantics make it unambiguous;
- existing human guardrails still require a decision before an unrequested material removal or override;
- the common authoring-pattern reference is removed and the small amount of AGENTS-specific migration guidance stays in the core;
- scoped-composition and concrete harness profiles remain on-demand references because they prevent real loader/composition failures;
- evaluation coverage is consolidated around material regressions instead of protocol ceremony.

## Core behavior

The wizard keeps **target intent** separate from **loader semantics**. An explicitly requested filename remains the requested deliverable even if the active harness will not load it; the mismatch is diagnosed rather than silently substituted. A result-oriented request such as “put the project instructions wherever this harness will use them” is different: when the loader gives one clear effective target, the wizard uses it without asking a redundant filename question.

Inspection is focused and evidence-driven. The wizard reads the smallest maintained set needed to understand durable behavior, preserves existing instruction artifacts as prior human intent, avoids secret-bearing values during orientation, and does not let ordinary workspace content redirect the workflow.

Workspace evidence may establish mechanics and maintained policy, but directory shape or plausible conventions do not become policy by implication. The wizard asks only when an unresolved choice would change the target, scope, or behavioral contract. Uncertain optional material is omitted rather than turned into an interview question.

For scoped instructions, the wizard uses **inherit / extend / narrow / override** only when the active loader actually composes broader and narrower instruction files. A local file contains genuine local deltas, not a shadow copy of broader policy.

Refreshes are policy migrations rather than template rewrites: retain valid behavior, sharpen vague intent, remove verified stale/duplicated/no-op text, and stop for a human decision only when a material conflict or unrequested guardrail change remains.

## Runtime architecture

```text
SKILL.md
├── target intent vs loader semantics
├── focused workspace inspection
├── consequential decision frontier
├── smallest effective instruction surface
├── policy-preserving create/refresh/audit
└── proportional verification

references/
├── scoped-composition.md      # difficult composed scopes only
└── harnesses/
    ├── codex.md               # concrete loader boundary
    └── pi.md                  # concrete loader boundary
```

Ordinary create/refresh/audit work should use `SKILL.md` alone. Load one concrete harness profile only when exact loader behavior matters. Load `scoped-composition.md` only when a real composition, override, or drift problem exceeds the inline four-way model.

## Write behavior

A separate approval round is **not** the default. If the user asked to create or update the artifact and the behavioral contract is grounded, the wizard writes and verifies it.

The wizard stops before writing when:

- project evidence leaves a material policy conflict unresolved;
- a proposed change would remove or override a still-valid human guardrail that the user did not ask to change; or
- an unresolved target/scope choice materially changes where the instructions apply.

Explicit requests for preview/review, best-effort, or no-interview behavior are honored as written. Audit/review mode never edits files.

## Authoring standard

The output should be the smallest durable instruction surface that changes downstream behavior. Prefer non-obvious invariants, source-of-truth or lifecycle rules, precise task-triggered pointers, scoped deltas, and observable completion conditions.

Avoid generic quality slogans, copied manifests, exhaustive trees, transient inventories, and duplicated maintained documentation. A rule should earn its context and maintenance cost by preventing a plausible mistake, avoiding meaningful repeated reasoning, or lowering verification cost.

## Modes

- **Create / setup** — inspect, resolve only real decisions, write the effective requested artifact, verify.
- **Refresh / update** — preserve valid intent, remove grounded drift/duplication, stop only for unresolved material policy changes.
- **Audit / review** — report ranked behavioral findings without editing.
- **Scoped / local** — write only the local delta under loader-confirmed composition.
- **Best effort / no questions / preview first** — explicit user preferences override the default interaction style.

## Package layout

```text
agents-md-wizard/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
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

Examples and evals are development/regression material; runtime packaging may omit them.

## Suggested prompts

```text
Use $agents-md-wizard to create the effective project instructions for this workspace. Ask only if a material policy decision cannot be grounded from the repo.
```

```text
Use $agents-md-wizard to refresh the existing agent instructions, preserving valid policy and removing verified drift or duplication.
```

```text
Create local agent instructions for `analysis/`. Include only genuine local deltas under the active harness's composition rules.
```

```text
Audit our AGENTS.md, but don't edit anything.
```

## Installation and publishing

Install/copy the `agents-md-wizard` directory wherever the target harness loads Skills. `agents/openai.yaml` keeps invocation explicit by default; other harnesses should use their own invocation mechanism.
