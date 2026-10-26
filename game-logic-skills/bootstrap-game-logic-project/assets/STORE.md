# Game Logic Project Store

This project-local contract is installed by the user-invoked `bootstrap-game-logic-project` Skill. It is shared by `analyze-game-logic` and `apply-game-logic`; neither Skill owns or installs the tool. The authoritative helper is `.game-logic/bin/project_store.py`. Inspect `--help` before invoking CLI commands.

## Scope and authority

- **Source:** original read-only game data, executable, DLL, script, or configuration. Registered by absolute path and hash; the store is separate from the installed game.
- **Evidence artifact:** retained extraction, trace, decompilation, test log, or other generated evidence; it may support a Finding.
- **Finding:** a small, version-scoped interpretation with evidence locators, confidence, limitations, and reusable mechanic detail. Analyze owns semantic validity.
- **Application:** an implementation or test outcome consuming specified mechanic knowledge. Apply owns correctness, version guards, validation, and rollback; an application does not become evidence for a mechanic merely by succeeding.

Project layout:

```text
.game-logic/bin/project_store.py
.game-logic/STORE.md
.game-logic/bootstrap.json
artifacts/manifest.json
analyses/<analysis-id>/targets/<target-id>/target.json
analyses/<analysis-id>/targets/<target-id>/finding.md
analyses/<analysis-id>/targets/<target-id>/artifacts/<local-name>
analyses/<analysis-id>/targets/<target-id>/scripts/<local-name>
analyses/<analysis-id>/targets/<target-id>/reports/<local-name>
applications/<application-id>/application.json
applications/<application-id>/record.md
applications/<application-id>/artifacts/<local-name>
shared/artifacts/<local-name>
```

Paths determine artifact scope; the manifest holds hashes, content identity, producer, dependencies, evidence citations, consumers, and supersession. Do not copy artifacts between scopes merely for convenience. Installed game copies are never authoritative.

## Working with the store

Use the installed CLI, not the copies in any Skill installation. Useful commands include `init-target`, `register-source`, `add-artifact`, `add-finding`, `init-application`, `link`, `supersede`, `verify`, and `check-links`. Run `--help` on the tool/command for actual accepted flags.

Use `init-application` to create an independent application scope, with the exact game version/build/module hash and any in-store Finding IDs it consumes. When an externally supplied mechanic record has no in-store Finding, preserve that input verbatim and identify it in `record.md` and/or a registered retained artifact.

For each retained application, `record.md` must point to:

1. The exact target/version and consumed mechanic knowledge (without silently promoting hypotheses).
2. The authoritative implementation/configuration and its registered artifact IDs.
3. Validation/control results, tested scope, and remaining limitations.
4. The original state/verified backup and rollback or cleanup procedure when a change is deployed.

Put retained implementation, validation, and rollback files under the application's `artifacts/` directory. Register each via `add-artifact --application-id ...`, specifying its `--kind`, producer and, when applicable, `--consumes-finding-ref`, `--derived-from`, or `--source-ref`. Record descriptive relationships in `record.md`; register concrete retained files before handoff. `record.md` is a human-maintained index, not a proof of semantic correctness. Do not treat deployed output inside a game directory as the authoritative file.

`verify` validates structural/content integrity, `check-links` validates reference consistency; neither proves that a mechanic interpretation or runtime modification is correct. Use both before reusing costly retained evidence or handing off deployed work.

## Versions and lifecycle

New stores use manifest schema 4. Existing schema-3 stores remain readable for validation and ordinary analysis-scoped operations. Application scopes require schema 4. Migration is explicit and preserves existing analysis IDs, target files, Finding records, and registered artifact identities; request the Bootstrap Skill to upgrade, rather than changing the manifest by hand.

An intentional change to a hashed artifact produces a new artifact ID or an explicit successor. Verify target and input hashes before consuming a retained result. For destructive modifications, capture and verify restorable original bytes/content **before** writing. Never use a successful application as independent proof of its underlying mechanic.

Bootstrap is opt-in. Without a project kit, Analyze may answer narrow questions without a store; Apply may keep an independent, self-contained application directory using its own minimum durable record. Neither automatically invokes Bootstrap or Analyze solely for bookkeeping. Explicit Bootstrap enables uniform project-level management.
