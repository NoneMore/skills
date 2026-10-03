# Skill Design Principles

A compact framework for designing, implementing, and maintaining agent skills.

## Core Mental Model

A skill does not change the model's parameters, base knowledge, or fundamental reasoning capacity. But it can extend the **effective capability of the agent system** by packaging instructions, domain knowledge, executable procedures, resources, and access paths.

A skill is therefore a **task-scoped cognitive and operational scaffold**: it makes useful behavior more reliable, efficient, reusable, and verifiable.

Its main sources of value are:

1. **Lower reasoning cost** — avoid re-deriving how a recurring task should be approached.
2. **Lower context cost** — keep specialized rules, conventions, and references out of always-loaded instructions.
3. **Lower behavioral variance** — make similar tasks converge on similar depth, structure, and completion standards.
4. **Lower verification cost** — make important work end in explicit, checkable conditions.
5. **Operational leverage** — move deterministic work to scripts, tools, and structured resources when probabilistic execution is unnecessary.

> **Model capability is not the same as system capability.**
>
> Skills do not make the underlying model smarter; they improve and can extend the system around it.

---

## L0 — Purpose

Ask first: **why should this exist as a skill?**

A skill should encode reusable task knowledge or execution patterns that materially improve cost, consistency, reliability, or capability. Avoid turning every preference, one-off instruction, or prompt pattern into a skill.

The goal is not to maximize instructions. It is to minimize unnecessary reasoning, context, and uncertainty while preserving good judgment.

---

## L1 — Scope and Placement

Put information at the lowest level where it is reliably available when needed.

| Content | Best home |
|---|---|
| Rules that apply to nearly every task | `AGENTS.md` or equivalent workspace instructions |
| A reusable workflow for a recognizable task class | Skill |
| Branch-specific domain knowledge | `references/` |
| Deterministic computation or transformation | `scripts/` |
| Live or external state | Tool / API / MCP |
| Access enforcement and authorization | Runtime / tool boundary |
| Task-specific authority policy | Skill |
| Reusable output skeletons or artifacts | `assets/` |
| One-off requirements | User prompt |

Do not duplicate cheap facts that the environment can reveal directly. Documentation should add conventions, rationale, constraints, or non-obvious knowledge rather than cache easily discoverable state without reason.

---

## L2 — Behavioral Contract

Treat a skill as a behavioral contract:

> **Task context → controlled workflow → verifiable outcome**

A well-designed skill makes the following clear when relevant:

- **Trigger / anti-trigger** — when the skill should and should not be used.
- **Inputs / preconditions** — what information and state are required to proceed.
- **Authority** — what the agent may read, change, execute, or delegate.
- **Invariants** — what must remain true throughout execution.
- **Decision points** — meaningful branches and how to resolve them.
- **Output and completion** — what must be produced and what observable conditions mean “done.”
- **Failure behavior** — what to do when information, tools, or permissions are insufficient.
- **Stop boundary** — where the skill must stop rather than expanding scope opportunistically.

Prefer explicit, checkable completion criteria over vague instructions such as “be thorough.”

---

## L3 — Information Architecture

Design for limited attention and context.

### Progressive disclosure

Keep the common path in the main skill file and load specialized material only when the relevant branch is reached.

```text
metadata → SKILL.md → references / scripts / assets on demand
```

### Authoritative sources, deliberate repetition

Each rule, definition, or invariant should have one authoritative source. Avoid accidental duplication, but allow deliberate local restatement of critical constraints when it materially improves execution reliability.

### Context pointers

A useful pointer states both **what** the referenced material contains and **when** it should be loaded.

### Locality

Keep definitions, rules, caveats, and completion conditions close to the workflow that uses them. Split files only when the reduction in context or complexity justifies the added indirection.

### Prune aggressively

Remove instructions that are irrelevant, stale, behaviorally inert, or cheaper to discover at runtime. Shorter instructions make important constraints easier to notice and maintain.

---

## L4 — Routing and Composition

A skill that cannot be discovered reliably is functionally absent.

Treat discovery metadata as an index, not as marketing copy. A useful description should explain both **what the skill does** and **when it should be selected**.

When multiple skills coexist, design for:

- distinct and discriminating triggers,
- minimal unnecessary overlap,
- clear model-invoked vs. user-invoked behavior,
- explicit dependencies where composition is intentional,
- router skills only when they reduce real discovery cost,
- granularity justified by independent discoverability or materially different context.

Skill quality is bottlenecked by its weakest critical layer: good execution cannot compensate for failed routing, and good routing cannot compensate for an unreliable workflow.

---

## L5 — Engineering and Runtime Specification

Conceptual quality and format validity are separate concerns.

Use the open [Agent Skills specification](https://agentskills.io/specification) as the baseline packaging contract, then apply runtime-specific extensions only where required.

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

`SKILL.md` should remain the canonical entry point. Runtime-specific metadata should extend the skill rather than redefine its core behavior.

Engineering concerns include:

- valid frontmatter and naming,
- stable relative references,
- minimal runtime assumptions,
- bounded tool permissions,
- explicit dependencies,
- portable packaging where useful,
- deterministic mechanisms for deterministic work.

Format compliance is the floor, not the definition of a good skill.

---

## L6 — Evaluation and Governance

Skill execution is partially probabilistic, so structural validity alone is not enough. Evaluate routing, behavior, and outcomes empirically.

At minimum, test four dimensions:

| Evaluation | Question |
|---|---|
| Positive routing | Does the skill activate when it should? |
| Negative routing | Does it stay inactive when it should? |
| Behavioral | Does it follow its contract after activation? |
| Outcome | Does the result satisfy the completion criteria? |

Also monitor lifecycle concerns:

- routing regressions,
- unnecessary token or context growth,
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
2. **Contract** — Are the required behavior, authority, and stopping condition explicit?
3. **Context** — Is information loaded only where it is needed?
4. **Routing** — Can the right task discover the skill without excessive overlap?
5. **Execution** — Are deterministic operations delegated to deterministic mechanisms where appropriate?
6. **Compatibility** — Does the package conform to the target skill/runtime specification?
7. **Evaluation** — Can routing, behavioral, and outcome regressions be detected?

> **A good skill does not try to make the underlying model smarter. It makes the surrounding system more capable, clearer, cheaper, more constrained, more reusable, and easier to verify.**
