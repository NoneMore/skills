# Target Discovery and Patching

Treat every patch as a compatibility contract between one mod version and one target fingerprint.

## Prove the target

Collect the target from repository source, public API, or an exact user-supplied artifact, not memory or an unversioned web snippet:

- assembly/module and declaring type;
- method name and metadata token, RVA, or other stable locator when available;
- static/instance status, visibility, generic arity, parameter types, and return type;
- caller and call timing relevant to the requested behavior;
- hash or build marker for the inspected artifact.

When available evidence cannot prove the target, list the exact decompiler, interop, metadata, or native-analysis asset required and apply the asset gate. Under asset mode 2, acquire only evidence for the requested target.

For obfuscated games, use existing or user-authorized structural evidence such as call relationships, field types, constants, and control flow. Keep fragile names behind one resolver.

Accept a resolver only when it returns exactly one target and rejects an incompatible build with a clear log message.

## Use the hook ladder

Choose the first rung that can express the behavior:

1. Supported game API, event, configuration, or composition.
2. Postfix for observing completion or adjusting a result without suppressing original behavior.
3. Prefix for validating/changing inputs or deliberately replacing original behavior.
4. Managed transpiler for a narrow IL edit with a checked semantic anchor.
5. Native detour for an evidenced IL2CPP/native target with a complete ABI contract.

Prefer a Finalizer only when exception observation or translation is the feature; avoid hiding failures that the game or other mods need to see.

Harmony's official patch model and constraints are documented at <https://harmony.pardeike.net/articles/patching.html>. Match Harmony or HarmonyX details to the package actually referenced by the loader.

## Define the patch contract

Before coding, state:

- trigger: which call activates the patch;
- inputs: which arguments, instance, fields, or state are read;
- effect: what changes and what remains delegated to the original;
- count: expected calls per scene, action, or frame;
- timing: loader phase, scene phase, and thread;
- coexistence: ordering or interaction with other patches;
- rollback: how registration and owned state are removed.

Keep patch methods small. Move feature logic into ordinary testable C# methods.

## Preserve coexistence

- Use a unique Harmony owner ID and unpatch only that owner.
- Avoid broad `PatchAll` when compatibility checks must gate individual targets.
- Apply priorities or before/after relationships only for a demonstrated conflict.
- Preserve original behavior by default; skip it only when replacement is the explicit contract.
- Avoid per-frame reflection, allocations, disk I/O, and repeated logging.
- Guard reentrancy when patched code can call the target again.
- Keep shared state synchronized and clear it during teardown.

## Make failure loud and local

- Validate target count before applying hooks.
- Log the resolved signature and target evidence once.
- Assert transpiler match counts before emitting modified IL.
- Catch exceptions at the loader boundary where they can be logged; keep native callbacks from unwinding managed exceptions across the ABI boundary.
- Disable only the affected feature when optional targets are missing. Refuse startup when a hard compatibility contract fails.

## Test the seam

Prove a hook with a harmless marker before changing behavior. Then test:

- expected call count and thread;
- original behavior when the feature is disabled;
- boundary inputs and null/destroyed instances;
- another mod patching the same method when that ecosystem is in scope;
- one cold restart and one clean uninstall.
