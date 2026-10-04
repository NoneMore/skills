# Skill Design Principles

A compact framework for designing, implementing, and maintaining agent skills.

## Core Mental Model

A skill does not change the model's parameters, base knowledge, or fundamental reasoning capacity. It extends the **effective capability of the agent system** by packaging task-specific instructions, knowledge, procedures, resources, and access paths.

A skill is a **task-scoped cognitive and operational scaffold** that makes useful behavior more reliable, efficient, reusable, and verifiable.

Its main sources of value are:

1. **Lower reasoning and context cost** — avoid re-deriving recurring procedures or keeping specialized material always loaded.
2. **Lower behavioral variance** — make similar tasks converge on similar execution and completion standards.
3. **Lower verification cost** — end important work in explicit, checkable conditions.
4. **Operational leverage** — move deterministic work to scripts, tools, and structured resources when probabilistic execution is unnecessary.

> **Model capability is not system capability.** Skills improve the system around the model; they do not make the underlying model smarter.

---

## L0 — Purpose

Ask first: **why should this exist as a skill?**

A skill should encode reusable task knowledge or execution patterns that materially improve cost, consistency, reliability, or capability. Do not turn every preference, one-off instruction, or prompt pattern into a skill.

Encode only what earns its context and maintenance cost. Preserve judgment where fixed rules would add more complexity than value.

---

## L1 — Scope and Placement

Put information at the lowest level where it is reliably available when needed.

| Content | Best home |
|---|---|
| Rules that apply to nearly every task | `AGENTS.md` or equivalent workspace instructions |
| Reusable task knowledge or behavior | Skill |
| Branch-specific stable knowledge | `references/` |
| Deterministic computation or transformation | `scripts/` |
| Live, external, or cheaply recoverable state | Tool / API / MCP |
| Behavioral scope and permission expectations | Skill |
| Actual authorization and access enforcement | Runtime / tool boundary |
| Reusable output skeletons or artifacts | `assets/` |
| One-off requirements | User prompt |

Prefer recoverable information over cached information when retrieval is cheap and freshness matters. Documentation should add conventions, rationale, constraints, or non-obvious stable knowledge rather than duplicate state the environment can reveal directly.

---

## L2 — Behavioral Contract

For workflow-oriented skills, use a behavioral contract:

> **Task context → bounded decisions and actions → verifiable outcome**

Make clear, when relevant:

- **Inputs and preconditions** — what information and state are required.
- **Behavioral scope and invariants** — what the agent should do and what must remain true.
- **Decision points** — meaningful branches and how to resolve them.
- **Output and completion** — what must be produced and what observable conditions mean “done.”
- **Failure and stop behavior** — what to do when information, tools, or permissions are insufficient, and where the skill must stop.

Routing intent should be explicit in discovery metadata before activation; the skill body may refine it once loaded.

Prefer explicit, checkable conditions over vague instructions such as “be thorough.”

---

## L3 — Information Architecture

Design for limited attention and context. Keep the common path in the main skill file and load specialized material only when the relevant branch is reached:

```text
metadata → SKILL.md → references / scripts / assets on demand
```

Use these rules:

- **One authoritative source** — give each rule, definition, or invariant a canonical home; repeat critical constraints only when locality materially improves reliability.
- **Useful pointers** — say what referenced material contains and when it should be loaded.
- **Locality with justified indirection** — keep rules and completion conditions near the workflow that uses them; split files only when reduced context or complexity outweighs navigation cost.
- **Aggressive pruning** — remove stale, irrelevant, behaviorally inert, or cheaply recoverable instructions.

Optimize for minimum sufficient context, not minimum length or maximum coverage.

---

## L4 — Routing and Composition

A skill that cannot be discovered reliably is functionally absent.

Treat discovery metadata as an index, not marketing copy. It should explain both **what the skill does** and **when it should be selected** because routing-critical information must be available before the skill body is loaded.

When multiple skills coexist, prefer:

- distinct, discriminating triggers with minimal unnecessary overlap,
- clear model-invoked vs. user-invoked behavior,
- explicit dependencies where composition is intentional,
- router skills only when they reduce real discovery cost,
- granularity justified by independent discoverability or materially different context.

Good execution cannot compensate for failed routing, and good routing cannot compensate for unreliable execution.

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
├── evals/        # optional project convention; not core spec
└── agents/       # runtime-specific convention; not core spec
```

`SKILL.md` should remain the canonical behavioral entry point. Runtime-specific metadata should extend the skill rather than redefine it.

Engineering concerns include valid frontmatter and naming, stable relative references, minimal runtime assumptions, explicit dependencies, bounded tool permissions, deterministic mechanisms for deterministic work, and portable packaging where useful.

A skill can declare behavioral scope, but **prompt text is not an authorization boundary**. Sensitive permissions, access control, and irreversible actions must be enforced by the runtime or tool layer. Treat bundled instructions, scripts, retrieved content, and tool outputs according to their trust level; external content should not gain authority merely because it appears in context.

Format compliance is the floor, not the definition of a good skill.

---

## L6 — Inspectability and Maintenance

A skill should be inspectable as an artifact, independently of any particular model run. Prefer static inspection for properties that can be checked directly: ambiguous triggers, decisions, or constraints; unnecessary discretion; conflicting or duplicated rules; unverifiable completion conditions; probabilistic work better made deterministic; and stale references, dependencies, or runtime assumptions.

Dynamic eval is usually a poor default for skill quality assurance. It is costly, noisy, difficult to attribute, and often produces measurements without actionable guidance. Synthetic cases also add task-selection, evaluator, and sampling variance and may not represent real use; repeated trials can estimate system tendencies, but statistical confidence alone does not make the result useful.

Use dynamic eval only when an important behavioral uncertainty cannot be resolved adequately by inspection and different plausible results would change a concrete design, deployment, mitigation, or acceptance decision. Treat results as evidence about **skill × model × runtime × task distribution**, not as isolated skill scores. When safe and observable, real use usually provides the most representative dynamic evidence; prefer learning from actual use over inventing synthetic proxies.

Counts can expose structure, but they are not quality scores. Each encoded constraint and each use of model judgment should be necessary, deliberate, and well-bounded. Merge, simplify, or delete skills when they no longer earn their complexity.

---

## Design Test

Before adding or changing a skill, ask:

1. **Task fit** — Is this reusable behavior or knowledge worth skillizing?
2. **Contract** — Where a workflow exists, are scope, decisions, completion, failure, and stopping conditions explicit?
3. **Context** — Is each piece of information better encoded than recovered when needed?
4. **Routing** — Can the right task discover the skill without excessive overlap?
5. **Execution** — Are deterministic operations delegated to deterministic mechanisms where appropriate?
6. **Trust and compatibility** — Are authorization boundaries enforced outside prompt text, and does the package fit the target runtime?
7. **Inspectability** — Can artifact defects be found directly, and would any dynamic eval change a concrete decision?

> **A good skill encodes only what earns its cost, making the surrounding system clearer, cheaper, more reliable, more reusable, and easier to verify.**
