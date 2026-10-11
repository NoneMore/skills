# Cheat Engine Delivery

Load this reference when the requested deliverable is a Cheat Engine table or Auto Assembler script, or Cheat Engine is the retained runtime surface. When the artifact writes process memory or installs/replaces executable code, `native-runtime-delivery.md` remains the source of truth for guarded mutation, hook correctness, restoration, and execution evidence.

For gameplay changes, this reference complements `change-design.md`. It does not replace mechanic recovery, general application validation, or durable application provenance.

## Keep one authoritative source per Auto Assembler feature

When Auto Assembler is material to the change, designate one authoritative script source for each independently shipped feature. That source may live in a standalone file or in the table itself.

If both a standalone script and a `.CT` exist for the same feature, derive one from the other or verify that the embedded script round-trips exactly. Do not maintain two independent copies of the same implementation.

Use the normal durable-application rules for target identity, consumed mechanic knowledge, validation evidence, and rollback. Do not duplicate that provenance contract here.

## Keep CE-specific target claims narrow

Use the native locator policy from the main Skill and the fail-closed mutation requirements from `native-runtime-delivery.md` when the CE artifact mutates the target.

If an AoB/signature is also used, treat uniqueness only as evidence within the supported target scope. A unique match does not prove cross-version compatibility.

## Require CE-native acceptance

For a shipped `.CT`, actual Cheat Engine must load the delivered table. For each shipped Auto Assembler feature material to the requested behavior, exercise the activation and deactivation paths the artifact exposes on the supported target; when the feature has enable and disable paths, check both before calling the CE deliverable complete.

CE acceptance is only a delivery check. It does not prove that injected logic executes correctly, that target behavior changed as intended, or that the artifact survives broader lifecycle events. Use `native-runtime-delivery.md` and the main Skill for those claims.

If Cheat Engine is unavailable, the artifact may still be delivered as an unvalidated draft, but name the missing CE acceptance check explicitly.

## Clean up CE-owned resources

The disable path should unregister CE symbols and release CE-owned allocations where applicable, in addition to the restoration requirements owned by `native-runtime-delivery.md`.

Do not imply that disabling a CE script reverses gameplay state already generated while the script was active when that state is not actually restorable.

## Completion

Before calling a reusable CE delivery complete, verify that:

- the requested user-facing table/script exists and, when Auto Assembler is material, each shipped Auto Assembler feature has an identifiable authoritative source;
- duplicate script representations, if any, are synchronized;
- actual Cheat Engine accepts the shipped delivery surface required by the artifact, including table loading and enable/disable when applicable;
- CE-owned symbols and allocations are cleaned up where applicable;
- AoB/signature evidence is not presented as broader compatibility proof;
- any native runtime mutation also satisfies `native-runtime-delivery.md`;
- retained artifacts satisfy the normal application provenance and rollback requirements.
