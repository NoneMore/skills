# Cheat Engine Delivery

Load this reference when the requested deliverable is a Cheat Engine table or Auto Assembler script, or Cheat Engine is the retained runtime surface. Native mutations must also satisfy `native-runtime-delivery.md`; this reference adds only CE-specific delivery requirements.

## Keep one authoritative Auto Assembler source

When Auto Assembler is material to the change, designate one authoritative script source for each independently shipped feature. It may live in a standalone file or in the table itself.

If both a standalone script and a `.CT` contain the same feature, derive one from the other when practical. Otherwise extract the embedded script and compare it deterministically against the authoritative source after only explicitly defined text normalization. Do not maintain two independent copies of the same implementation.

## Keep CE-specific target claims narrow

Use the native locator policy from the main Skill when the CE artifact mutates the target. If an AoB/signature is also used, uniqueness is evidence only within the supported target scope; it does not prove cross-version compatibility.

## Require CE-native acceptance

For a shipped `.CT`, actual Cheat Engine must load the delivered table. For each shipped Auto Assembler feature material to the requested behavior, exercise the activation and deactivation paths exposed by the artifact on the supported target; when enable and disable paths exist, check both before calling the CE delivery complete.

CE acceptance proves only that CE accepts the shipped surface. It does not by itself prove injected behavior, target behavior, or broader lifecycle coverage.

If Cheat Engine is unavailable, deliver the artifact only as an unvalidated draft and name the missing CE acceptance check.

## Clean up CE-owned resources

The disable path should unregister CE symbols and release CE-owned allocations where applicable, in addition to any restoration required by `native-runtime-delivery.md`.

Do not imply that disabling a CE script reverses gameplay state already produced while the script was active when that state is not actually restorable.

## Completion

Before calling a reusable CE delivery complete, verify that:

- the requested table/script exists and each material Auto Assembler feature has one identifiable authoritative source;
- duplicate script representations, if any, are mechanically derived or deterministically verified as synchronized;
- actual Cheat Engine accepts the shipped surface, including enable/disable paths when applicable;
- CE-owned symbols and allocations are cleaned up where applicable;
- AoB/signature evidence is not presented as broader compatibility proof.
