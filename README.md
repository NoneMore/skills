# Skills: Curated Agent Capabilities Collection

A modular collection of reusable Agent Skills for modern coding agents and agentic workflows.

This repository treats skills as **task-scoped cognitive and operational scaffolds**: they do not make the underlying model intrinsically smarter, but they can make recurring work more reliable, efficient, constrained, and easier to verify.

## Design and authoring

Before creating or materially changing a skill, read [Skill Design Principles](SKILL-DESIGN-PRINCIPLES.md). That document is the repository's canonical design guidance for task fit, behavioral contracts, information placement, routing and composition, runtime boundaries, and inspectability. Keep design rules there rather than maintaining a second summary here.

Use the open [Agent Skills specification](https://agentskills.io/specification) as the baseline packaging contract when portability matters. Runtime-specific metadata may extend a skill where needed, but `SKILL.md` remains its canonical behavioral entry point.

## Contributing and license

Contributions, new skills, and issue reports are welcome.

Every skill should have a clear `SKILL.md` entry point and a narrowly defined purpose. Add `references/`, `scripts/`, `assets/`, `evals/`, and runtime-specific metadata only when they serve a concrete need justified by the design principles.

For new or substantially revised skills, use the design test in [SKILL-DESIGN-PRINCIPLES.md](SKILL-DESIGN-PRINCIPLES.md) and verify the resulting package against the target runtime and, where applicable, the Agent Skills specification.

This repository is distributed under the [MIT License](LICENSE).
