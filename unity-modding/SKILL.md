---
name: unity-modding
description: Source-first Unity Mono and IL2CPP modding. Use when creating projects, implementing or extending features, repairing or migrating BepInEx or MelonLoader plugins, choosing managed or interop references, applying Harmony/HarmonyX or native hooks, or diagnosing loader, metadata, stripping, and ABI failures.
---

# Unity Mono / IL2CPP Modding

Work **source-first**. Treat the repository and user-supplied assets as authoritative; acquire reverse-engineered assets only under an explicit asset choice. Build backend-specific work from a **fingerprint**, not assumptions.

## 1. Bound and classify the task

- Work only on a game or build the user is authorized to modify.
- For multiplayer or anti-cheat titles, keep work inside an officially supported mod environment or a developer-provided offline test build. Keep hooks local and exclude bypass, evasion, and unfair-advantage behavior.
- Inspect the existing repository and user-provided files before choosing a loader, package version, target framework, reference set, or deployment layout.
- Classify the request as one or more of: **create**, **implement**, **extend**, **repair**, or **migrate**.
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

Use reverse-engineered or decompiled assets already supplied by the user or already present in the workspace under option 3. Do not seek replacements or newer copies automatically. Scope option 2 to the current task and acquire only the minimum needed; follow all runtime approval requirements and keep proprietary artifacts outside source control and release archives.

Complete this step when the asset inventory, selected/default mode, missing items, and resulting validation limits are visible to the user.

## 3. Route by task class

### Create a project

- Read [loaders.md](references/loaders.md) and preserve any loader choice already provided.
- Determine backend, loader/version, OS/architecture, target framework, plugin identity, and deployment contract from existing assets.
- When facts are missing, run the asset gate. Under option 3, create a clearly labeled configurable scaffold instead of acquiring or reverse-engineering missing game assets.
- Build a load-only plugin first, then add configuration, logging, lifecycle cleanup, and feature seams.

Complete this branch when the project builds with available dependencies and its unresolved target-specific inputs are explicit.

### Implement a new feature

- Build the current project when one exists and capture the feature's expected observable behavior.
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

## 4. Capture the required fingerprint

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
- for a patch, target type, full method signature, and existing evidence.

Mark unresolved fields without acquiring assets under option 3. Gate only the work that depends on them.

Complete this step when every required fingerprint field is evidenced or explicitly unresolved and its consequence is stated.

## 5. Load only the matching technical branch

- Read [loaders.md](references/loaders.md) for project creation, loader selection, bootstrap, or migration.
- For a Mono fingerprint, read [mono.md](references/mono.md) before choosing framework references or managed patch techniques.
- For an IL2CPP fingerprint, read [il2cpp.md](references/il2cpp.md) before using generated wrappers, class injection, or native signatures.
- Read [patching.md](references/patching.md) before any Harmony, HarmonyX, transpiler, reflection, or native-detour change.
- Read [debugging.md](references/debugging.md) when a build, load, patch, or crash signal is red.

Apply the asset mode while following every reference; a reference never grants acquisition authority.

## 6. Implement a tracer slice

- First make the plugin load and emit one fingerprinted startup marker when runtime testing is in scope.
- Add one narrow hook marker before feature behavior when a patch is required.
- Prefer the least invasive stable seam: supported API or event, then Postfix, Prefix, a narrowly anchored managed IL rewrite, and finally a native detour.
- Keep loader bootstrap, target discovery, hook logic, and feature logic separate.
- Keep Unity object access on the Unity main thread unless the observed API explicitly permits otherwise.
- Make registration idempotent and release owned hooks, callbacks, objects, and native allocations through the loader lifecycle.
- Put user-tunable behavior behind configuration and log compatibility failures without per-frame noise.

Complete this step when the smallest available slice builds and each accessible execution boundary has one observable marker.

## 7. Prove the result

Run the applicable checks against the exact fingerprint:

1. Build with pinned or user-approved dependencies.
2. Inspect output so game, Unity, loader, and generated reference assemblies are not copied as mod-owned dependencies.
3. Deploy only explicit mod outputs when runtime testing is authorized.
4. Prove load, requested behavior, one restart, feature-disabled behavior, rollback, and a neighboring behavior.
5. Report every check blocked by the selected asset mode or unavailable runtime access as pending.

Claim only the validation actually performed.

## Handoff

Report the task class, selected asset mode, available and missing assets, fingerprint, files changed, chosen implementation seam, build/deployment commands, validation evidence, compatibility bounds, pending checks, and reversible disable/uninstall procedure.

Keep proprietary game binaries, metadata, generated wrappers, and decompiled source out of the mod repository and release archive.
