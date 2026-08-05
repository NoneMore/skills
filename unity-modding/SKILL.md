---
name: unity-modding
description: Evidence-first Unity Mono and IL2CPP analysis and modding. Use when discovering or documenting game types and methods, creating projects, implementing or extending features, repairing or migrating BepInEx or MelonLoader plugins, choosing managed or interop references, applying Harmony/HarmonyX or native hooks, or diagnosing loader, metadata, stripping, and ABI failures.
---

# Unity Mono / IL2CPP Modding

Work **evidence-first** and prefer source when it exists. Treat the repository and user-supplied assets as authoritative; acquire reverse-engineered assets only under an explicit asset choice. Build backend-specific work and reusable analysis from a **versioned fingerprint**, not assumptions. Before target-dependent implementation, perform only enough analysis to prove the target and behavior, starting at the shallowest useful level and escalating only for a named unanswered question.

## 1. Bound and classify the task

- Work only on a game or build the user is authorized to modify.
- For multiplayer or anti-cheat titles, keep work inside an officially supported mod environment or a developer-provided offline test build. Keep hooks local and exclude bypass, evasion, and unfair-advantage behavior.
- Inspect the existing repository and user-provided files before choosing a loader, package version, target framework, reference set, or deployment layout.
- Classify the request as one or more of: **analyze**, **create**, **implement**, **extend**, **repair**, or **migrate**.
- Separate the mod project from the game installation. Treat the installation as read-only input and deploy only explicit build outputs.

Complete this step when the authorized target, task class, source workspace, requested behavior, and allowed runtime test surface are explicit.

## 2. Run the asset gate

At the start of every task, show a concise asset check even when nothing is currently missing:

```text
Asset check
- Available: <relevant source, project, logs, references, runtime access>
- Possibly missing: <exact assets or "none currently known">
- Impact: <what can and cannot be proved without them>

Choose an asset mode:
1. Manual fill — you provide the listed assets.
2. Agent auto-fill — I acquire or generate the minimum required assets within the authorized target.
3. Existing only — I use only assets already supplied or present in the workspace. (Default)
```

If the user has already selected a mode for the current task, restate it briefly and continue. If the user does not select, adopt option 3 and continue every asset-independent part. Repeat the asset check whenever a new missing asset appears or its impact changes.

For option 1, name the exact files, acceptable versions/fingerprints, and expected workspace locations; pause only the dependent work while continuing useful independent work. For option 2, state the intended acquisition actions and destinations before executing them. For option 3, use local caches and `--no-restore`-style build modes where available; treat a missing dependency as a new asset gap instead of triggering an implicit restore.

Treat downloading packages/binaries/artifacts, installing tools or templates, copying from a game installation, extracting, decompiling, dumping, generating interop/dummy assemblies, and launching a first run that generates them as asset acquisition. Perform those actions only after the user selects option 2 or explicitly requests the specific action. Keep normal read-only inspection of user-scoped project files, logs, configuration, file layout, versions, and hashes available under option 3. Treat reading public official documentation as information lookup rather than asset acquisition unless the user has forbidden web access.

Use reverse-engineered or decompiled assets already supplied by the user or already present in the workspace under option 3. Do not seek replacements or newer copies automatically. Scope option 2 to the current task and acquire only the minimum needed; follow all runtime approval requirements and keep proprietary artifacts out of source control and release archives.

Before generating analysis output, resolve the corresponding `<mod-project-root>` rather than defaulting to the repository root. Keep two distinct in-project locations:

- **Analysis** — store the compact, reviewable, version-controlled Markdown record at `<mod-project-root>/analysis/<game-version>/<target-slug>.md`.
- **Analysis assets** — store costly, bulky, proprietary, or generated inputs and outputs at `<mod-project-root>/.assets/<game-version>/<tool>/`. This includes decompiler output, metadata exports, generated wrappers/stubs, symbol/address maps, reusable utilities, and Ghidra projects/databases. Record tool versions in the Markdown analysis instead of adding another directory level.

Ensure the corresponding Mod project's `.gitignore` excludes `/.assets/`; add the narrow rule when repository policy permits and it is absent. Do not ignore `/analysis/`. Use temporary storage only for bounded scratch data that is cheap to reproduce; promote every reusable result into the in-project analysis-assets directory and link it from the analysis record before cleanup or handoff.

Complete this step when the asset inventory, selected/default mode, missing items, and resulting validation limits are visible to the user.

## 3. Analyze before target-dependent work

- Search source and compatible analysis records before invoking reverse-engineering tools. Existing source and records precede the three tool levels and do not justify repeating analysis.
- Read [analysis.md](references/analysis.md) and [tooling.md](references/tooling.md) when target discovery or reverse-engineered evidence is needed. Before invoking an analysis tool, read its command card in [tool-usage.md](references/tool-usage.md).
- Start at **shallow** inspection. Escalate to **intermediate** only when signatures, metadata, stubs, and wrappers cannot answer the named question. For IL2CPP, prefer `rodroidmods/il2cpp-dumper-rs` when the needed representation is original native instructions combined with type, method, field, annotation, or CFG context; use Cpp2IL when reconstructed IL/IR is specifically more useful. Escalate to **deep** only when bounded intermediate output remains insufficient for native xrefs, interactive data-flow work, ABI, optimization/inlining, independently validated function boundaries, or a native detour.
- Do not run or pre-plan all three levels as a routine pipeline. Installed tool availability is not an escalation reason. Evaluate the current level's actual output before selecting the next level; at every escalation, record the unanswered question, the evidence gap, and why the next level can answer it.
- Create or update a versioned analysis record whenever the task discovers target-specific facts, invokes a reverse-engineering tool, creates costly/reusable output, establishes a compatibility bound, or rejects a plausible approach. Use [analysis-record-template.md](assets/analysis-record-template.md) and follow [analysis.md](references/analysis.md).
- Treat the compact Markdown analysis record as the required reusable index. Raw tool output, an evidence directory, or a Ghidra project supports the record but never substitutes for it.
- In every plan and handoff that invokes a tool level, name both in-project locations explicitly: analysis record `<mod-project-root>/analysis/<game-version>/<target-slug>.md` with schema `unity-modding-analysis/v1`, and analysis assets under `<mod-project-root>/.assets/<game-version>/<tool>/`.
- Do not require a new record for a load-only/configuration scaffold or a mechanical change that produces no target knowledge. When exact-fingerprint source or an existing record fully proves the target, cite and reuse it instead.

Analysis may be a bounded phase inside an implement, extend, repair, or migrate task; it does not require a separate user request. Complete this step when the required target facts are evidenced at the lowest sufficient level and reusable knowledge has been recorded or an explicit no-record exception applies.

## 4. Route by task class

### Analyze or discover a target

- Read [analysis.md](references/analysis.md) and [tooling.md](references/tooling.md).
- State the exact analysis question and stop boundary. Do not create, patch, deploy, or modify runtime configuration unless the user expands the task.
- Search for a reusable analysis record for the exact fingerprint before running tools. Reuse compatible evidence and preserve rejected hypotheses so later agents do not repeat the same work.
- Prefer installed, version-identifiable tools over custom parsers. Record every tool's version, relevant invocation, input fingerprint, output location, and limitations.
- Follow the shallow/intermediate/deep routing in [tooling.md](references/tooling.md). For IL2CPP, inspect exact-fingerprint BepInEx interop assemblies or Il2CppInspectorRedux shim DLLs/C# stubs first. At the intermediate level, use `rodroidmods/il2cpp-dumper-rs` for per-type native disassembly enriched with metadata names, field references, annotations, and CFG; use Cpp2IL instead when recovered IL/IR is the requested representation. Use Ghidra with compatible Il2CppInspectorRedux-generated scripts only at the deep level. Do not open or prepare Ghidra merely because it is installed.
- Create or update a versioned analysis record from [analysis-record-template.md](assets/analysis-record-template.md) at `<mod-project-root>/analysis/<game-version>/<target-slug>.md`.
- Record signatures, locators, call timing, candidate seams, compatibility bounds, and an evidence ledger. Label each material statement **Observed**, **Inferred**, or **Pending**.

Complete this branch when the requested question is answered to the available evidence boundary, reusable evidence is saved under the exact build/tool versions, and every unresolved claim has a concrete next action. Stop there unless implementation was also requested.

### Create a project

- Read [loaders.md](references/loaders.md) and preserve any loader choice already provided.
- Determine backend, loader/version, OS/architecture, target framework, plugin identity, and deployment contract from existing assets.
- When facts are missing, run the asset gate. Under option 3, create a clearly labeled configurable scaffold instead of acquiring or reverse-engineering missing game assets.
- Reuse a compatible versioned analysis record when one exists.
- Build a load-only plugin first, then add configuration, logging, lifecycle cleanup, and feature seams.

Complete this branch when the project builds with available dependencies and its unresolved target-specific inputs are explicit.

### Implement a new feature

- Build the current project when one exists and capture the feature's expected observable behavior.
- Reuse a compatible versioned analysis record when one exists; revalidate only facts affected by the current fingerprint.
- Prefer existing source interfaces, public game APIs, events, configuration, and established project abstractions.
- Read [patching.md](references/patching.md) only when the feature requires a runtime patch. Gate any missing target evidence as an asset choice.
- Implement the smallest end-to-end slice and test feature-disabled behavior.

Complete this branch when the feature builds and its tests or runtime markers prove the requested behavior, with unavailable runtime proof marked pending.

### Extend or modify an existing feature

- Identify the feature's current contract, configuration, hooks, tests, and compatibility bounds.
- Reproduce the existing behavior before editing and preserve established loader and reference choices.
- Change the narrowest seam, retain backward-compatible configuration where required, and test both old and new behavior.

Complete this branch when the changed behavior and every affected prior behavior have evidence.

### Repair a failure

- Establish one red signal from build output, loader logs, a stack trace, or a minimal reproduction.
- Read [debugging.md](references/debugging.md), start at the first red layer, and change one variable at a time.
- Use source, logs, and existing references first. When diagnosis reaches a missing decompiler, interop, metadata, or native-analysis boundary, rerun the asset gate before crossing it.

Complete this branch when the root cause is evidenced, the original signal is green, and a regression check covers the failure.

### Migrate a project

- Capture separate source and destination fingerprints: game build, backend, loader, target framework, packages, generated references, and deployment layout.
- Update loader/project/package contracts before changing feature logic.
- Treat new or regenerated IL2CPP interop and newly decompiled game references as missing assets; apply the selected asset mode.
- Revalidate each target and feature only after the destination project loads.

Complete this branch when the destination build loads, supported features pass, rollback is documented, and unresolved porting work is listed.

## 5. Capture the required fingerprint

When a user-scoped game directory already exists, use the read-only probe if it helps the selected branch:

```bash
python3 <skill-dir>/scripts/inspect_unity_game.py <game-root> --json
```

Record only what the task needs from:

- game/build marker, OS, architecture, and Unity version;
- scripting backend: Mono, IL2CPP, conflicting, or unknown;
- loader/version, project target framework, and packages;
- available source or game-code references;
- loader log, deployment directory, and runtime access;
- for a patch, target type, full method signature, and existing evidence;
- analysis schema/revision and tool versions when reusing a prior analysis record.

Mark unresolved fields without acquiring assets under option 3. Gate only the work that depends on them.

Complete this step when every required fingerprint field is evidenced or explicitly unresolved and its consequence is stated.

## 6. Load only the matching technical branch

- Read [loaders.md](references/loaders.md) for project creation, loader selection, bootstrap, or migration.
- For a Mono fingerprint, read [mono.md](references/mono.md) before choosing framework references or managed patch techniques.
- For an IL2CPP fingerprint, read [il2cpp.md](references/il2cpp.md) before using generated wrappers, class injection, or native signatures.
- Read [patching.md](references/patching.md) before any Harmony, HarmonyX, transpiler, reflection, or native-detour change.
- Read [debugging.md](references/debugging.md) when a build, load, patch, or crash signal is red.
- Read [analysis.md](references/analysis.md) when producing or updating reusable target knowledge.
- Read [tooling.md](references/tooling.md) before installing a tool, writing a parser, or crossing from wrapper-level inspection into native analysis. Read [tool-usage.md](references/tool-usage.md) before invoking `inspect_unity_game.py`, `ilspycmd`, `rodroidmods/il2cpp-dumper-rs`, Cpp2IL, Il2CppInspectorRedux, or Ghidra.
- Read [ghidra.md](references/ghidra.md) only after [tooling.md](references/tooling.md) permits deep-level escalation and the analysis record contains the reason.

Apply the asset mode while following every reference; a reference never grants acquisition authority.

## 7. Advance through gated implementation stages

Do not combine stages unless an existing analysis record proves the earlier stage against the exact fingerprint:

1. **Load-only** — make the plugin load with zero hooks and emit one marker containing plugin version, fingerprint, loader, backend, and hook count `0`.
2. **Resolve-only** — build a hook manifest and resolve every target and patch method without applying hooks. Validate exact overloads, parameter names or supported index mappings, patch signatures, hard/optional status, and rollback owner.
3. **Marker-only** — apply one narrow, harmless hook; prove expected call count and thread with feature behavior disabled.
4. **Behavior** — add the smallest requested behavior only after the marker is green. Add later hooks one at a time unless the manifest proves they form one atomic hard contract.

- Abort before registration when any hard manifest entry is null, ambiguous, version-incompatible, or signature-incompatible. Optional entries must fail locally without aborting unrelated features.
- Prefer the least invasive stable seam: supported API or event, then Postfix, Prefix, a narrowly anchored managed IL rewrite, and finally a native detour.
- Keep loader bootstrap, target discovery, hook logic, and feature logic separate.
- Keep Unity object access on the Unity main thread unless the observed API explicitly permits otherwise.
- Make registration idempotent and release owned hooks, callbacks, objects, and native allocations through the loader lifecycle.
- Put user-tunable behavior behind configuration. Scope broad observations by instance, action ID, thread, or a bounded time window; do not leave global gameplay hooks producing uncorrelated noise.

Complete this step only when the current stage has its own evidence. Record failed and rejected approaches in the analysis record before changing direction.

## 8. Prove the result

Run the applicable checks against the exact fingerprint:

1. Build with pinned or user-approved dependencies.
2. Inspect output so game, Unity, loader, and generated reference assemblies are not copied as mod-owned dependencies.
3. Deploy only explicit mod outputs when runtime testing is authorized.
4. Prove load, requested behavior, one restart, feature-disabled behavior, rollback, and a neighboring behavior.
5. Test each advertised mode separately. Do not infer an untested mode from a symmetric implementation.
6. Verify that the version reported by source, assembly metadata, runtime marker, configuration header, documentation, and artifact name agrees.
7. Report every check blocked by the selected asset mode or unavailable runtime access as **Pending**.

Claim only the validation actually performed. A missing marker in one execution path is not proof that a target is unused; require representative positive and negative paths before excluding it.

## Handoff

Report the task class, selected asset mode, available and missing assets, fingerprint, highest analysis level used and every escalation reason, analysis schema/revision or the applicable no-record exception, tool versions, files changed, chosen implementation seam, build/deployment commands, validation evidence, compatibility bounds, pending checks, and reversible disable/uninstall procedure.

Separate material claims into **Observed**, **Inferred**, and **Pending**. List every advertised mode with its actual test result. Never describe a parser, address map, hook, restart, rollback, or compatibility bound as complete merely because an intermediate structure looked plausible or a build succeeded.

Keep proprietary game binaries, metadata, generated wrappers, decompiler projects/databases, and decompiled source out of source control and release archives. Preserve reusable copies under the corresponding Mod project's ignored `.assets/` directory rather than disposable temporary storage.
