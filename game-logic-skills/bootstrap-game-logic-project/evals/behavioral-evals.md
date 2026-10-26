# Explicit Bootstrap Evals

## 1. User explicitly initializes

- A user requests a persistent game-logic project and names a separate project root.
- Bootstrap installs one pinned project helper and one human-readable store contract, creates schema-4 storage, and validates it.
- Repeating initialization without changes is idempotent; no gameplay analysis or application is triggered.

## 2. Ordinary Analyze / Apply never bootstrap

- A triage request without an initialized project finishes without creating a manifest.
- A retained Apply request without an initialized project retains a self-contained record, not an implicit Bootstrap call.
- Missing or stale mechanic facts may trigger a narrow Analyze call, but storage alone cannot.

## 3. Explicit upgrade preserves earlier research

- A verified schema-3 store is not migrated during ordinary initialization.
- An explicit upgrade migrates to schema 4 while preserving Source, Artifact, Finding IDs, and hashes.
- Existing local modifications and failed integrity checks prevent silent overwrites.

## 4. Application artifact is first class

- In schema 4, an Application consumes one or more Finding IDs and stores version-guarded implementation, validation, and rollback files in its own scope.
- Project Store verifies file hashes and finding references; it does not mistake an application artifact for evidence that a Finding is true.
- Supersession and a later session can be audited without relying on conversation history.
