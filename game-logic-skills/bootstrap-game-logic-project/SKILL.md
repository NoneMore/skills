---
name: bootstrap-game-logic-project
description: Initialize or explicitly upgrade a project-local store for durable game-logic findings, evidence, applications, validation, and rollback. Invoke only when the user asks to set up or upgrade this infrastructure.
disable-model-invocation: true
---

# Bootstrap Game Logic Project

Initialize or explicitly upgrade a project-local, shared knowledge and artifact store. This is a **user-invoked capability**; Analyze and Apply must never invoke it as a bookkeeping dependency.

## Accepts

An explicitly identified project and a request to initialize, inspect, or upgrade its durable game-logic infrastructure. Advice and previews are read-only; only a setup or upgrade request authorizes writing. The project root must be separate from installed game files.

## Owns

- Installing the canonical project-store helper and its human-readable contract into the project.
- Initializing new stores, or migrating legacy stores only when an upgrade was explicitly requested.
- Preserving existing files and rejecting unrequested overwrites.
- Verifying the resulting project environment without analyzing or applying game mechanics.

## Approach

1. Identify the project root and a filesystem-safe project ID. Inspect `artifacts/manifest.json`, `.game-logic/`, and existing local policy before writing. Do not infer permission to replace a distinct established project.
2. For a requested initial setup, run `python scripts/bootstrap.py --root <project-root> --project <project-id>` from this Skill directory. This installs `.game-logic/bin/project_store.py`, `.game-logic/STORE.md`, and `.game-logic/bootstrap.json`, then initializes a schema-4 store if absent. Repeated runs with matching installed files are idempotent.
3. For an **explicit upgrade request only**, use the same command with `--upgrade`. The installer validates existing content and links, migrates verified schema-3 manifests to schema 4, and updates the pinned tool/rules. Never silently replace a locally edited or unmanaged installed tool or policy.
4. Use `python scripts/project_store.py --self-test` and `python scripts/bootstrap.py --self-test` when validating the package itself. Verify the installed project with `python <project-root>/.game-logic/bin/project_store.py verify --root <project-root>` and `check-links`.
5. Report installed paths, schema/version state, and any blocked migration. Do not invoke `$analyze-game-logic` or `$apply-game-logic` to complete setup.

The bundled `scripts/project_store.py` and `assets/STORE.md` are the single distribution sources. Project-local copies are pinned installations, not independently maintained implementations. Do not duplicate the schema or CLI in this Skill; refer to the installed tool's `--help` and `STORE.md`.

## Completion

A requested setup is complete when the project's pinned helper, rules, and version metadata exist; the manifest and reference checks pass; and subsequent Analyze or Apply work can find and use them without loading this Skill. A read-only request is complete when the current state and required changes are explained without modifying files.
