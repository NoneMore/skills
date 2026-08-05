# Versioned Analysis Records

Use an analysis record to preserve target knowledge across agents and sessions without carrying stale conclusions across game builds.

## Decide when a record is required

Perform bounded analysis before target-dependent implementation, but do not equate that rule with mandatory full reverse engineering. Source and an exact-fingerprint existing record may already meet the evidence threshold.

Create or update a record when any of these occurs:

- discover a target-specific signature, locator, call relationship, timing fact, implementation seam, or compatibility bound;
- invoke `ilspycmd`, Il2CppInspectorRedux, Cpp2IL, Ghidra, a debugger, or another reverse-engineering tool for the task;
- generate or materially reuse an interop/shim DLL, C# stub, disassembly, metadata export, address map, or Ghidra project;
- reject or supersede a plausible hypothesis or implementation approach.

Do not require a new record for a load-only/configuration scaffold, documentation-only wording change, or mechanical edit that produces no target knowledge. When source or a compatible record fully answers the question, cite that evidence and record only genuinely new findings.

## Reuse before rediscovery

1. Search the repository for an analysis record naming the game, target type, method, token, or build marker.
2. Compare its fingerprint and tool versions with the current inputs.
3. Reuse **Observed** evidence only when the relevant fingerprint fields still match. Re-evaluate **Inferred** claims when any premise changed.
4. Create a new build directory instead of silently updating a record for another fingerprint.

Use Markdown and copy [analysis-record-template.md](../assets/analysis-record-template.md). Follow the repository's documentation convention. Otherwise place records at:

```text
docs/unity-analysis/<game-slug>/<build-id>/<target-slug>.md
```

Build `build-id` from an explicit game version when reliable. Otherwise use stable abbreviated hashes from the IL2CPP native/metadata pair or the Mono target assembly. Never use timestamps alone as a build identity.

Keep the compact Markdown record in the repository only when repository policy permits it. Keep proprietary or bulky analysis artifacts in a persistent, user-scoped analysis root outside the mod repository, organized by game, build fingerprint, and tool version. Record that root and the exact artifact paths in the Markdown record. Do not use an OS temporary directory for the only copy of a decompilation, Ghidra project, generated wrapper set, address map, or other costly result.

The Markdown record is the required reusable index and evidence ledger, not a container for bulk decompiler output. An artifact folder or tool database alone is not a saved analysis record. Preserve the template's YAML frontmatter and headings. A project may add fields or sections, but do not remove the fingerprint, tool ledger, evidence classification, compatibility, artifact-location, or pending-work data required by the template.

## Version the record

Copy [analysis-record-template.md](../assets/analysis-record-template.md) and preserve:

- schema identifier `unity-modding-analysis/v1`;
- monotonically increasing `analysis_revision` for the same fingerprint;
- game/build, backend, OS, architecture, loader, interop/generator, native module, metadata, and inspected assembly versions or hashes as applicable;
- exact tool name and version for every generated observation.
- highest intervention level used (`shallow`, `intermediate`, or `deep`) and the reason for every escalation.

When the record schema changes incompatibly, create a new schema version and state the migration or compatibility rule. A tool upgrade does not automatically invalidate evidence, but the new version must be recorded and changed output must be reviewed.

The analysis-level fields added to the v1 template are additive. Existing v1 records remain reusable when their fingerprint and evidence are sufficient; fill the new fields when such a record is next revised rather than rewriting it only for format compliance.

## Classify evidence

- **Observed** — directly supported by source, metadata, an exact artifact, a deterministic tool output, or a runtime marker. Cite the file/hash, token/RVA, command/output path, or log locator.
- **Inferred** — an explanation derived from observations. Record its premises, confidence, and what would disprove it.
- **Pending** — unresolved or untested. Record the missing asset, runtime action, tool, or user decision needed next.

Do not promote a claim because it is plausible. One absent call in one run is not proof that a method is unused. Preserve disproved or superseded hypotheses in the rejected-hypotheses section so another agent does not repeat them.

## Keep the record reusable

Record:

- the analysis question and explicit stop boundary;
- the shallow/intermediate/deep progression actually used, what each level answered, and the evidence gap that justified each escalation;
- target assembly/module, declaring type, complete signature, parameter names when relevant to a patch framework, token/RVA or other locator, and call timing;
- tool ledger with versions, relevant invocations/configuration, input fingerprints, output locations, and known limitations;
- for Agent-driven Ghidra work, the persistent project/program identity, Ghidra and integration versions, transport scope, allowed mutations, and mutation log location;
- candidate implementation seams and why each is supported or rejected;
- validation matrix covering representative positive and negative paths;
- compatibility bounds and the exact facts that must be rechecked after an update;
- concise next actions for every Pending item.

Store summaries, signatures, hashes, commands, and evidence locators. Keep proprietary binaries, bulk decompiler output, generated wrappers, Ghidra projects/databases, and copied game source outside the mod repository unless the user explicitly requires and authorizes a suitable private location. Preserve them in the recorded persistent analysis root; reserve temporary directories for reproducible scratch work and promote useful results before cleanup or handoff.
