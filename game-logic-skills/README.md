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

Use the [specialized adapter](analyze-game-logic/references/engine-rpgmaker-mv-mz.md) for evidenced MV/MZ gameplay rather than generic JavaScript bundle recovery. Inspect relevant project files, event JSON, and enabled plugins directly with available search and JSON tools; use focused deterministic commands when the task needs them.

## Installation

Install either or both skill folders under your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R apply-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; references, scripts, evals, and runtime metadata are loaded only where needed.
