# Versioned Analysis Records

Use an analysis record to preserve target knowledge across agents and sessions without carrying stale conclusions across game builds.

## Reuse before rediscovery

1. Search the repository for an analysis record naming the game, target type, method, token, or build marker.
2. Compare its fingerprint and tool versions with the current inputs.
3. Reuse **Observed** evidence only when the relevant fingerprint fields still match. Re-evaluate **Inferred** claims when any premise changed.
4. Create a new build directory instead of silently updating a record for another fingerprint.

Follow the repository's documentation convention. Otherwise place records at:

```text
docs/unity-analysis/<game-slug>/<build-id>/<target-slug>.md
```

Build `build-id` from an explicit game version when reliable. Otherwise use stable abbreviated hashes from the IL2CPP native/metadata pair or the Mono target assembly. Never use timestamps alone as a build identity.

## Version the record

Copy [analysis-record-template.md](../assets/analysis-record-template.md) and preserve:

- schema identifier `unity-modding-analysis/v1`;
- monotonically increasing `analysis_revision` for the same fingerprint;
- game/build, backend, OS, architecture, loader, interop/generator, native module, metadata, and inspected assembly versions or hashes as applicable;
- exact tool name and version for every generated observation.

When the record schema changes incompatibly, create a new schema version and state the migration or compatibility rule. A tool upgrade does not automatically invalidate evidence, but the new version must be recorded and changed output must be reviewed.

## Classify evidence

- **Observed** — directly supported by source, metadata, an exact artifact, a deterministic tool output, or a runtime marker. Cite the file/hash, token/RVA, command/output path, or log locator.
- **Inferred** — an explanation derived from observations. Record its premises, confidence, and what would disprove it.
- **Pending** — unresolved or untested. Record the missing asset, runtime action, tool, or user decision needed next.

Do not promote a claim because it is plausible. One absent call in one run is not proof that a method is unused. Preserve disproved or superseded hypotheses in the rejected-hypotheses section so another agent does not repeat them.

## Keep the record reusable

Record:

- the analysis question and explicit stop boundary;
- target assembly/module, declaring type, complete signature, parameter names when relevant to a patch framework, token/RVA or other locator, and call timing;
- tool ledger with versions, relevant invocations/configuration, input fingerprints, output locations, and known limitations;
- candidate implementation seams and why each is supported or rejected;
- validation matrix covering representative positive and negative paths;
- compatibility bounds and the exact facts that must be rechecked after an update;
- concise next actions for every Pending item.

Store summaries, signatures, hashes, commands, and evidence locators. Keep proprietary binaries, bulk decompiler output, generated wrappers, and copied game source outside the mod repository unless the user explicitly requires and authorizes a suitable private location.
