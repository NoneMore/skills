# Game Logic Skills

Agent Skills for recovering and applying authorized offline/single-player game logic with explicit evidence and version scope.

## Skills

### `bootstrap-game-logic-project`

Explicitly initialize or upgrade a project-local, versioned store for game-logic findings and retained application artifacts. **User-invoked only:** Analyze and Apply never route to it automatically.

### `analyze-game-logic`

Recover and verify game mechanics when the relevant behavior, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale.

### `apply-game-logic`

Apply already-recovered, version-scoped gameplay knowledge to calculators, simulators, instrumentation, mods, tests, or scoped local gameplay changes.

## Composition

`analyze-game-logic` owns recovery and verification. `apply-game-logic` consumes established findings and should return to analysis only when material mechanic knowledge is missing or stale. Both use an already initialized project store when available; neither initializes or upgrades it automatically. For tasks without a store, lightweight analysis and self-contained application records remain valid.

Collection-level composition evaluations live under `evals/`.

## Installation

Install whichever skills you want under your Codex skills directory. Install Bootstrap only if you want explicit project initialization/upgrades:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R apply-game-logic "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R bootstrap-game-logic-project "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Each skill keeps its canonical behavioral entry point in `SKILL.md`; references, scripts, evals, and runtime metadata are loaded only where needed.

Invoke `$bootstrap-game-logic-project` explicitly for initialization/upgrades. The installed project-local tool and rules live under `.game-logic/`. The helper supports a schema-3-to-4 migration only on an explicitly requested upgrade, and schema 4 adds independent `applications/` scopes.
