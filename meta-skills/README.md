# Meta Skills

Agent Skills for shaping the agent environment, clarifying decisions, and transferring work between sessions.

Before materially changing a Skill, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Skills

### `agents-md-wizard`

Create, refresh, or audit `AGENTS.md` or an equivalent workspace instruction artifact. It resolves effective loading, preserves existing human policy, and keeps scoped instructions minimal.

### `skill-prototype-forge`

Derive the smallest defensible Agent Skill prototype from current conversations, relevant accessible prior conversations, or user-supplied interaction evidence.

### `grilling`

Interactively pressure-test a plan, decision, or idea with the minimum sufficient high-leverage questions needed to reach a responsible decision state.

### `handoff`

Package the current work into a compact continuation brief for another agent or session without duplicating durable project artifacts.

## Installation

Install only the skill folders you want under your runtime's skill directory. Each skill keeps its canonical behavioral entry point in `SKILL.md`; supporting references, examples, evals, and runtime metadata stay local to the skill that needs them.
