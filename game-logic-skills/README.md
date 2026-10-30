# Game Logic Skills

Agent Skills for recovering and applying authorized offline/single-player game logic with explicit evidence and version scope.

## Skills

### `analyze-game-logic`

Recover and verify game mechanics when a behavior, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale. Retain useful notes or evidence when warranted; preservation need not imply ongoing maintenance.

### `apply-game-logic`

Apply already-recovered, version-scoped gameplay knowledge to calculators, simulators, instrumentation, mods, tests, or scoped local gameplay changes.

## Composition and continuity

`analyze-game-logic` owns mechanic recovery, verification, and any reusable architecture understanding. `apply-game-logic` consumes sufficiently verified knowledge and returns to analysis only for material missing or stale facts. Neither requires a project-level artifact store, normalized handoff, or companion Skill for bookkeeping.

One-off analysis needs no persistent project structure. When continuity is useful, keep readable architecture notes and/or build-scoped evidence snapshots: system boundaries, state/data flows, recognisable function and variable roles, and ways to locate and revalidate behavior in a later build. Maintain an overview only when useful; historical notes and evidence snapshots may simply remain available for reading. Version-specific addresses remain useful evidence for that build, not cross-version authority. Retained applications keep implementation, validation, and rollback materials together.

Existing schema-3/4 stores are **not** automatically migrated, modified, or deleted. Their files may be consulted as historical evidence, with version-sensitive claims revalidated before reuse; the new workflow does not require their manifests or tools.

Collection-level composition evaluations live under `evals/`.

## Installation

Install either or both skills under your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R apply-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; specialized references and scripts are loaded only as needed.
