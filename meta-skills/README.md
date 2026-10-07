# Meta Skills

Agent Skills for shaping the agent environment and for deriving new Skill candidates from real interaction evidence.

Before materially changing a Skill, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Skills

### `agents-md-wizard`

Create, refresh, or audit `AGENTS.md` or an equivalent workspace instruction artifact. It resolves effective loading, preserves existing human policy, and keeps scoped instructions minimal.

### `skill-prototype-forge`

Derive the smallest defensible Agent Skill prototype from current conversations, relevant accessible prior conversations, or user-supplied interaction evidence. It is evidence-driven and is not intended for greenfield Skill authoring without interaction evidence.

## Installation

Install the skill folders you want under your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R agents-md-wizard "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skill-prototype-forge "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; supporting references, examples, evals, and runtime metadata stay local to the skill that needs them.
