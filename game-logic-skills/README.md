# Game Logic Skills

Agent Skills for recovering and applying authorized offline/single-player game logic with explicit evidence and version scope.

## Skills

### `analyze-game-logic`

Recover and verify game mechanics when a behavior, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale. Retain useful notes or evidence when warranted; preservation need not imply ongoing maintenance.

### `apply-game-logic`

Apply already-recovered, version-scoped gameplay knowledge to calculators, simulators, instrumentation, mods, tests, or scoped local gameplay changes.

## Composition and continuity

`analyze-game-logic` recovers and verifies mechanics; `apply-game-logic` consumes sufficiently verified, version-scoped knowledge and returns to analysis only for missing or stale material facts. Neither requires a project store or normalized handoff.

Unrequested one-off analysis needs no persistence. When continuity is useful, retain concise architecture notes or build-scoped evidence to help rediscover and revalidate behavior in later builds. Historical snapshots need no ongoing maintenance; retained applications keep implementation, validation, and rollback together. Existing schema-3/4 stores are not automatically migrated, modified, or deleted, but may be consulted as historical evidence.

Collection-level composition evaluations live under `evals/`.

## RPG Maker MV/MZ

Use the [specialized adapter](analyze-game-logic/references/engine-rpgmaker-mv-mz.md) for confirmed MV/MZ gameplay, not generic JS bundle recovery. Its read-only helper locates candidate roots, event commands and enabled-plugin hints without executing project JavaScript:

```sh
python analyze-game-logic/scripts/rpgmaker_triage.py /path/to/project --events --hooks
python -m unittest discover -s tests -v
```

`--out /path/outside/game-tree/report.json` saves a report outside the project. Hook matches do not prove runtime ownership.

## Installation

Install either or both skills under your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R apply-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; specialized references and scripts are loaded only as needed.
