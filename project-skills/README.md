# Project Skills

Locally complete project capabilities plus a small optional tracker configuration skill. These are capabilities, not stages in a required software lifecycle.

Before materially changing a skill, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `design` — resolve material software, domain, architecture, and interface choices into a coherent direction.
- `implement` — turn a requested production change into working, verified production behavior.
- `review` — independently evaluate an existing result and report evidence-backed findings.
- `specify` — turn sufficiently settled intent into a durable implementation-facing contract.
- `decompose` — split concrete work into independently actionable pieces with truthful dependencies.

These skills accept natural project inputs and do not require each other to have run first. Research, debugging, prototyping, testing, and similar techniques are used inside the capability that owns the requested outcome rather than forming a mandatory cross-skill pipeline.

## Tracker setup

`setup-tracker` remains an optional backend-independent configuration capability for projects that want the repository's tracker contract. The project capabilities above do not require that tracker merely to operate.
