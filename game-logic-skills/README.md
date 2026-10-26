# Game Logic Skills

Agent Skills for recovering and applying authorized offline/single-player game logic with explicit evidence and version scope.

## Skills

### `analyze-game-logic`

Recover and verify game mechanics when the relevant behavior, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale.

### `apply-game-logic`

Apply already-recovered, version-scoped gameplay knowledge to calculators, simulators, instrumentation, mods, tests, or scoped local gameplay changes.

## Composition

`analyze-game-logic` owns recovery and verification. `apply-game-logic` consumes established findings and should return to analysis only when material mechanic knowledge is missing or stale.

Collection-level composition evaluations live under `evals/`.

## RPG Maker MV/MZ

The analysis engine registry now includes a specialized RPG Maker MV/MZ adapter so confirmed MV/MZ projects do not fall into generic Web/JS recovery merely because they use JavaScript, NW.js or Pixi. Analysis starts with event/database JSON, active plugin order and engine method overrides; a generic JS adapter remains available for a separately material bundle/obfuscation boundary.

A read-only classifier and indexer is bundled:

```sh
python analyze-game-logic/scripts/rpgmaker_triage.py /path/to/project --events --hooks
python -m unittest discover -s tests -v
```

Use `--out /path/outside/game-tree/report.json` if you want to save a report. This helper inventories candidate evidence; it does not execute a game, prove effective hook ownership, or modify files.


## Installation

Install either or both skill folders under your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R apply-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; references, scripts, evals, and runtime metadata are loaded only where needed.
