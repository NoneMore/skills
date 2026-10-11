# Cheat Engine Delivery

Load this reference when the requested deliverable is a Cheat Engine table or Auto Assembler script, or Cheat Engine is the retained runtime surface. Native mutations must also satisfy `native-runtime-delivery.md`; this file adds only CE-specific delivery requirements.

## Keep one authoritative Auto Assembler source

Each independently shipped Auto Assembler feature must have one authoritative source, either standalone or table-embedded. If both forms exist for the same feature, derive one from the other when practical; otherwise compare the embedded script deterministically against the authoritative source after only explicitly defined text normalization.

## Keep CE-specific target claims narrow

Use the main Skill's native locator policy. AoB/signature uniqueness is evidence only within the supported target scope; it does not prove cross-version compatibility.

## Require CE-native acceptance

A shipped `.CT` must load in actual Cheat Engine. Exercise each material Auto Assembler activation/deactivation path exposed by the artifact on the supported target, including both enable and disable when present, before calling the CE delivery complete.

CE acceptance proves only that CE accepts the shipped surface. If CE is unavailable, deliver only an unvalidated draft and name the missing check.

## Clean up CE-owned resources

Disable must unregister CE symbols and release CE-owned allocations where applicable, in addition to native restoration. Do not imply that disable reverses gameplay state already produced while active when that state is not actually restorable.
