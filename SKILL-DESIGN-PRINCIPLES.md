# Skill Design Principles

A compact framework for designing, implementing, and maintaining agent skills.

## Core Mental Model

A skill is not a magic capability upgrade. It does not change the model's parameters, base knowledge, or fundamental reasoning capacity.

A skill is a **task-scoped cognitive and operational scaffold**: it helps an agent turn existing capabilities into more reliable, efficient, and repeatable outcomes.

Its main sources of value are:

1. **Lower reasoning cost** — avoid re-deriving how a recurring task should be approached.
2. **Lower context cost** — keep specialized rules, conventions, and references out of always-loaded instructions.
3. **Lower behavioral variance** — make similar tasks converge on similar depth, structure, and completion standards.
4. **Lower verification cost** — make important work end in explicit, checkable conditions.
5. **Operational leverage** — move deterministic work to scripts, tools, and structured resources when the model should not do it probabilistically.

A useful distinction is:

> **Model capability is not the same as system capability.**
>
> Skills improve the system around the model, not the model itself.

---

## L0 — Metacognition

Ask first: **why should this exist as a skill?**

A skill should encode reusable task knowledge that materially improves cost, consistency, reliability, or execution. Avoid turning every preference or prompt pattern into a skill.

The goal is not to maximize instructions. The goal is to minimize unnecessary reasoning, context, and uncertainty while preserving good judgment.

---

## L1 — Scope and Placement

Put information at the lowest level where it is reliably available when needed.

| Content | Best home |
|---|---|
| Rules that apply to nearly every task | `AGENTS.md` or equivalent workspace instructions |
| A reusable workflow for a recognizable task class | Skill |
| Branch-specific domain knowledge | `references/` |
| Deterministic computation or transformation | `scripts/` |
| Live, permissioned, or external state | Tool / API / MCP |
| Reusable output skeletons or artifacts | `assets/` |
| One-off requirements | User prompt |

Do not duplicate cheap facts that the environment can reveal directly. Documentation should add conventions, rationale, constraints, or non-obvious knowledge rather than cache easily discoverable state without reason.

---

## L2 — Behavioral Contract

Treat a skill as a behavioral contract:

> **Task context → controlled workflow → verifiable outcome**

A well-designed skill makes the following clear when relevant:

- **Trigger** — when the skill should be used.
- **Anti-trigger** — similar cases where it should not be used.
- **Inputs** — information required to proceed.
- **Preconditions** — conditions that must already hold.
- **Authority** — what the agent may read, change, execute, or delegate.
- **Invariants** — rules that must remain true throughout execution.
- **Decision points** — meaningful branches and how to resolve them.
- **Output contract** — what the skill must produce.
- **Completion criteria** — observable conditions that distinguish done from not done.
- **Failure behavior** — what to do when information, tools, or permissions are insufficient.
- **Stop boundary** — where the skill must stop rather than expanding scope opportunistically.

Prefer explicit, checkable completion criteria over vague instructions such as “be thorough.”

---

## L3 — Information Architecture

Design for limited attention and context.

### Progressive disclosure

Keep the common path in the main skill file and load specialized material only when the relevant branch is reached.

A typical hierarchy is:

```text
metadata → SKILL.md → references / scripts / assets on demand
```

### Single source of truth

Each rule, definition, or invariant should have one authoritative location. Repetition increases maintenance cost and creates stale copies.

### Context pointers

A good pointer states both:

1. what the referenced material contains; and
2. when it should be loaded.

### Locality

Keep definitions, rules, caveats, and completion conditions close to the workflow that uses them. Split files only when the reduction in context or complexity justifies the added indirection.

### Prune aggressively

Remove instructions that are:

- irrelevant to the task,
- stale relative to the environment, or
- behaviorally inert.

Shorter instructions make important constraints easier to notice and maintain.

---

## L4 — Routing and Composition

A skill that cannot be discovered reliably is functionally absent.

Treat discovery metadata as an index, not as marketing copy. A useful description should explain both **what the skill does** and **when it should be selected**.

When multiple skills coexist, design for:

- distinct and discriminating triggers,
- minimal overlap,
- clear model-invoked vs. user-invoked behavior,
- explicit dependencies where composition is intentional,
- router skills only when they reduce real discovery cost,
- skill granularity justified by independent discoverability or materially different context.

A useful approximation is:

> **Skill quality ≈ routing quality × execution quality**

If either side approaches zero, the skill is ineffective.

---

## L5 — Engineering and Runtime Specification

Conceptual quality and format validity are separate concerns.

Use the open [Agent Skills specification](https://agentskills.io/specification) as the baseline packaging contract, then apply runtime-specific extensions only where required.

A common structure is:

```text
skill-name/
├── SKILL.md
├── references/   # optional
├── scripts/      # optional
├── assets/       # optional
├── evals/        # recommended for non-trivial behavior
└── agents/       # runtime-specific metadata when needed
```

`SKILL.md` should remain the canonical entry point. Runtime-specific metadata, such as OpenAI integration metadata, should extend the skill rather than redefine its core behavior.

Engineering concerns include:

- valid frontmatter and naming,
- stable relative references,
- minimal runtime assumptions,
- bounded tool permissions,
- portable packaging,
- explicit dependencies,
- deterministic scripts for deterministic work.

Format compliance is the floor, not the definition of a good skill.

---

## L6 — Evaluation and Governance

Skills are probabilistic programs and should be evaluated as such.

At minimum, test four dimensions:

| Evaluation | Question |
|---|---|
| Positive routing | Does the skill activate when it should? |
| Negative routing | Does it stay inactive when it should? |
| Behavioral | Does it follow its contract after activation? |
| Outcome | Does the result satisfy the completion criteria? |

Also monitor lifecycle concerns:

- routing regressions,
- unnecessary token/context growth,
- stale references,
- broken scripts or runtime assumptions,
- permission or safety expansion,
- redundant or overlapping skills,
- behavior that has become a no-op,
- opportunities to merge, simplify, or delete skills.

Deleting a skill can be a valid improvement.

---

## Design Test

Before adding or changing a skill, ask:

1. **Task fit** — Is this reusable behavior actually worth skillizing?
2. **Contract** — Is the required behavior and stopping condition explicit?
3. **Context** — Is information loaded only where it is needed?
4. **Routing** — Can the right task discover the skill without excessive overlap?
5. **Execution** — Are deterministic operations delegated to deterministic mechanisms where appropriate?
6. **Compatibility** — Does the package conform to the target skill/runtime specification?
7. **Evaluation** — Can we detect routing, behavioral, and outcome regressions?

A compact model is:

```text
Skill Effectiveness
≈ Task Fit
× Routing
× Behavioral Contract
× Context Design
× Execution Reliability
× Evaluation Quality
```

A weakness near zero in any major factor can dominate the whole system.

---

## Principle

> **A good skill does not try to make the model smarter. It makes the surrounding system clearer, cheaper, more constrained, more reusable, and easier to verify.**
