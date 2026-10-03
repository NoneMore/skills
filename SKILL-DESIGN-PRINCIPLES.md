# Skill Design Principles

A compact framework for designing, implementing, and maintaining agent skills.

## Core Mental Model

A skill does not change the model's parameters, base knowledge, or fundamental reasoning capacity. It extends the **effective capability of the agent system** by packaging task-specific instructions, knowledge, procedures, resources, and access paths.

A skill is therefore a **task-scoped cognitive and operational scaffold**: it makes useful behavior more reliable, efficient, reusable, and verifiable.

Its main sources of value are:

1. **Lower reasoning cost** — avoid re-deriving recurring procedures.
2. **Lower context cost** — keep specialized rules and references out of always-loaded instructions.
3. **Lower behavioral variance** — make similar tasks converge on similar execution and completion standards.
4. **Lower verification cost** — end important work in explicit, checkable conditions.
5. **Operational leverage** — move deterministic work to scripts, tools, and structured resources when probabilistic execution is unnecessary.

> **Model capability is not system capability.** Skills improve the system around the model; they do not make the underlying model smarter.

---

## L0 — Purpose

Ask first: **why should this exist as a skill?**

A skill should encode reusable task knowledge or execution patterns that materially improve cost, consistency, reliability, or capability. Do not turn every preference, one-off instruction, or prompt pattern into a skill.

The goal is to reduce unnecessary reasoning, context, and uncertainty while preserving judgment.

---

## L1 — Scope and Placement

Put information at the lowest level where it is reliably available when needed.

| Content | Best home |
|---|---|
| Rules that apply to nearly every task | `AGENTS.md` or equivalent workspace instructions |
| Reusable workflow for a recognizable task class | Skill |
| Branch-specific domain knowledge | `references/` |
| Deterministic computation or transformation | `scripts/` |
| Live or external state | Tool / API / MCP |
| Behavioral scope and permission expectations | Skill |
| Actual authorization and access enforcement | Runtime / tool boundary |
| Reusable output skeletons or artifacts | `assets/` |
| One-off requirements | User prompt |

Do not cache cheap facts the environment can reveal directly. Documentation should add conventions, rationale, constraints, or non-obvious knowledge.

---

## L2 — Behavioral Contract

Treat a skill as a behavioral contract:

> **Task context → controlled workflow → verifiable outcome**

A well-designed skill makes the following clear when relevant:

- **Inputs / preconditions** — what information and state are required.
- **Behavioral scope** — what the agent should read, change, execute, or delegate within the task.
- **Invariants** — what must remain true throughout execution.
- **Decision points** — meaningful branches and how to resolve them.
- **Output and completion** — what must be produced and what observable conditions mean “done.”
- **Failure behavior** — what to do when information, tools, or permissions are insufficient.
- **Stop boundary** — where the skill must stop rather than expanding scope opportunistically.

Routing intent should be explicit in discovery metadata before activation; the skill body may refine it once loaded.

Prefer explicit, checkable completion criteria over vague instructions such as “be thorough.”

---

## L3 — Information Architecture

Design for limited attention and context.

Keep the common path in the main skill file and load specialized material only when the relevant branch is reached:

```text
metadata → SKILL.md → references / scripts / assets on demand
```

Use these rules:

- **One authoritative source** — each rule, definition, or invariant should have a canonical home. Repeat critical constraints locally only when it materially improves execution reliability.
- **Useful pointers** — say both what referenced material contains and when it should be loaded.
- **Locality** — keep rules, caveats, and completion conditions near the workflow that uses them.
- **Justified indirection** — split files only when reduced context or complexity outweighs navigation cost.
- **Aggressive pruning** — remove stale, irrelevant, behaviorally inert, or cheaply discoverable instructions.

Shorter instructions make important constraints easier to notice and maintain.

---

## L4 — Routing and Composition

A skill that cannot be discovered reliably is functionally absent.

Treat discovery metadata as an index, not marketing copy. It should explain both **what the skill does** and **when it should be selected**. Routing-critical information belongs here because it must be available before the skill body is loaded.

When multiple skills coexist, design for:

- distinct and discriminating triggers,
- minimal unnecessary overlap,
- clear model-invoked vs. user-invoked behavior,
- explicit dependencies where composition is intentional,
- router skills only when they reduce real discovery cost,
- granularity justified by independent discoverability or materially different context.

Good execution cannot compensate for failed routing, and good routing cannot compensate for an unreliable workflow.

---

## L5 — Engineering, Trust, and Runtime

Conceptual quality, package validity, and runtime enforcement are separate concerns.

Where portability or compatible runtimes matter, use the open [Agent Skills specification](https://agentskills.io/specification) as a baseline packaging contract, then add runtime-specific extensions only where required.

A practical extended structure is:

```text
skill-name/
├── SKILL.md
├── references/   # optional
├── scripts/      # optional
├── assets/       # optional
├── evals/        # recommended for non-trivial behavior
└── agents/       # runtime-specific metadata when needed
```

`SKILL.md` should remain the canonical behavioral entry point. Runtime-specific metadata should extend the skill rather than redefine it.

Engineering concerns include:

- valid frontmatter and naming,
- stable relative references,
- minimal runtime assumptions,
- explicit dependencies,
- bounded tool permissions,
- deterministic mechanisms for deterministic work,
- portable packaging where useful.

### Trust boundaries

A skill can declare behavioral scope, but **prompt text is not an authorization boundary**. Sensitive permissions, access control, and irreversible actions must be enforced by the runtime or tool layer.

Treat bundled instructions, scripts, retrieved content, and tool outputs according to their trust level. External content should not gain authority merely because it appears inside the execution context.

Format compliance is the floor, not the definition of a good skill.

---

## L6 — Evaluation and Governance

Skill execution is partially probabilistic, so structural validity alone is not enough. Evaluate routing, behavior, and outcomes empirically.

At minimum, test:

| Evaluation | Question |
|---|---|
| Positive routing | Does the skill activate when it should? |
| Negative routing | Does it stay inactive when it should? |
| Behavioral | Does it follow its contract after activation? |
| Outcome | Does the result satisfy the completion criteria? |

Also watch for routing regressions, context growth, stale references, broken scripts or runtime assumptions, permission expansion, redundant skills, and behavior that has become a no-op.

Merge, simplify, or delete skills when they no longer earn their complexity.

---

## Design Test

Before adding or changing a skill, ask:

1. **Task fit** — Is this reusable behavior worth skillizing?
2. **Contract** — Are behavior, scope, completion, failure, and stopping conditions explicit?
3. **Context** — Is information loaded only where it is needed?
4. **Routing** — Can the right task discover the skill without excessive overlap?
5. **Execution** — Are deterministic operations delegated to deterministic mechanisms where appropriate?
6. **Trust and compatibility** — Are authorization boundaries enforced outside prompt text, and does the package fit the target runtime?
7. **Evaluation** — Can routing, behavioral, and outcome regressions be detected?

> **A good skill makes the surrounding system clearer, cheaper, more reliable, more constrained, more reusable, and easier to verify.**
