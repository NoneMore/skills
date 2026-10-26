# Project Knowledge

Retain evidence when a user requests it, work already spans sessions, or evidence is expensive or lossy to recover. Do not create a durable project store for throwaway lookups. **Project initialization is a separate, explicitly user-invoked capability**, not an analysis step.

## What belongs in a reusable Finding

Keep Source, evidence Artifact, and Finding distinct:

- **Source:** original read-only game binary/data/source, with version/build identity and material hashes.
- **Artifact:** generated trace, extraction, decompilation, table, validation log, or analysis workspace state with independent reuse value.
- **Finding:** the smallest reusable interpretation citing evidence locators, scoped to the observed target/version, with status (confirmed / working hypothesis / unknown), material mechanic detail, validation performed, and limitations.

Do not infer authority, state lifetime, or gameplay semantics from artifact hashes or the existence of a Finding. A downstream application may consume an existing Finding directly; no normalized handoff is required solely for protocol ceremony.

## Existing project infrastructure

When the working project already contains `.game-logic/bin/project_store.py` and `.game-logic/STORE.md`, the **installed** rules/tool are authoritative for paths, manifest schema, registration commands, lifecycle and integrity checks. Consult the installed tool's `--help` instead of copying its CLI into this reference. Retain findings and their evidence in the appropriate analysis/target scope; put genuinely cross-analysis files in shared scope.

Do not install, initialize, repair, or migrate a project store by invoking Bootstrap as part of Analyze. If the project has no installed store, a narrow question can simply be answered. For warranted persistence, preserve a coherent, version-scoped finding and expensive evidence in an authorized working location and report the limitation; the user may explicitly invoke `$bootstrap-game-logic-project` when unified project management is wanted.

## Persistence cadence

Preserve lossy evidence promptly. For cheap deterministic source searches, first close the evidence loop, then persist the coherent Finding and useful locators together. A later session should recover the target identity, authoritative evidence, validation state, and any remaining uncertainty without relying on conversation memory.
