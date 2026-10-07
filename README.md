# Skills: Curated Agent Capabilities Collection

A modular collection of reusable Agent Skills for modern coding agents and agentic workflows.

This repository treats skills as **task-scoped cognitive and operational scaffolds**: they do not make the underlying model intrinsically smarter, but they can make recurring work more reliable, efficient, constrained, and easier to verify.

The repository favors reusable workflows, progressive disclosure, bounded authority, explicit completion criteria, and evaluation over large always-loaded instruction sets.

---

## Design & Authoring

Before creating or materially changing a skill, read [Skill Design Principles](SKILL-DESIGN-PRINCIPLES.md).

The guide organizes skill design into seven layers:

- **L0 — Metacognition:** understand what skills can and cannot improve.
- **L1 — Scope and Placement:** decide whether knowledge belongs in a skill, workspace instructions, references, scripts, tools, or the user prompt.
- **L2 — Behavioral Contract:** define triggers, authority, invariants, outputs, completion criteria, and stop boundaries.
- **L3 — Information Architecture:** use progressive disclosure, locality, context pointers, and a single source of truth.
- **L4 — Routing and Composition:** make skills discoverable without unnecessary overlap and compose them deliberately.
- **L5 — Engineering and Runtime Specification:** follow the [Agent Skills specification](https://agentskills.io/specification) and add runtime-specific metadata only where needed.
- **L6 — Evaluation and Governance:** test routing, behavior, outcomes, regressions, maintenance cost, and eventual deprecation.

The central idea is simple:

> **Model capability is not the same as system capability. Skills improve the system around the model, not the model itself.**

---

## Core Design Principles

1. **Use skills only for reusable task behavior.** Do not turn every preference, project fact, or one-off prompt into a skill.
2. **Load information only when it becomes relevant.** Keep common-path instructions close; move branch-specific material behind explicit pointers.
3. **Maintain one source of truth.** Avoid duplicating rules across `AGENTS.md`, `SKILL.md`, references, and runtime metadata.
4. **Bound authority and scope.** Make clear what the agent may read, change, execute, or delegate, and where the workflow must stop.
5. **Prefer verifiable completion over vague emphasis.** Replace instructions like “be thorough” with observable coverage and completion criteria.
6. **Delegate deterministic work to deterministic mechanisms.** Use scripts and tools when a reliable procedure should not depend on probabilistic generation.
7. **Evaluate skills as behavior, not prose.** Test whether they trigger correctly, stay inactive when irrelevant, follow their contract, and produce acceptable outcomes.

For the full framework and design test, see [SKILL-DESIGN-PRINCIPLES.md](SKILL-DESIGN-PRINCIPLES.md).

---

## Contributing & License

Contributions, new skills, and issue reports are welcome.

Every skill should have a clear `SKILL.md` entry point and a narrowly defined purpose. Add `references/`, `scripts/`, `assets/`, `evals/`, and runtime-specific metadata only when they serve a concrete need.

New or substantially revised skills should:

- follow the baseline [Agent Skills specification](https://agentskills.io/specification),
- follow the principles in [SKILL-DESIGN-PRINCIPLES.md](SKILL-DESIGN-PRINCIPLES.md),
- keep permissions and authority explicit and bounded,
- avoid unnecessary duplication and always-loaded context, and
- include routing or behavioral evaluations when the behavior is non-trivial or regression-prone.

This repository is distributed under the [MIT License](LICENSE).
