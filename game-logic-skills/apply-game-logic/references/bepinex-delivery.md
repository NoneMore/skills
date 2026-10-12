# BepInEx 5 Regular Plugin Delivery

Load this reference when the retained Unity Mono deliverable is a BepInEx 5
regular plugin under `BepInEx/plugins`. This guide adds only delivery, build,
lifecycle, and acceptance requirements for that surface. It does not select the
gameplay-change mechanism.

This guaranteed delivery surface does not cover BepInEx 6, preloader patchers,
IL2CPP, or direct Unity serialized-content patching.

## Keep one authoritative plugin implementation

Retain the source project and build configuration that produce the shipped plugin
as the authoritative implementation. Reuse an existing project when suitable;
otherwise a compatible project may be created with current BepInEx tooling. The
Skill does not require or bundle a fixed project template.

Target framework, Unity API compatibility, BepInEx 5 dependencies, and material
game-assembly references must match the supported target rather than a
Skill-defined default.

## Bind build inputs to the consumed evidence

For each managed assembly material to the retained implementation, keep its
identity and hash consistent with the finding/mechanic record the application
claims to consume. Successful compilation against a different assembly build does
not preserve that evidence binding merely because the referenced members still
exist.

The project may resolve target assemblies from the installed game, a private
staging directory, or another trustworthy target-matched source. Do not make a
particular reference layout part of the application contract.

Target game assemblies copied or staged for compilation are build inputs, not
implicitly distributable plugin artifacts. Do not package or distribute
proprietary game assemblies merely because the build references them.

If a material build input no longer matches the evidence, stop that delivery path
and rebind or revalidate only the affected relation before claiming compatibility.

## Require BepInEx-native acceptance

A retained BepInEx 5 regular plugin is not delivery-complete merely because it
builds.

Before calling the delivery complete:

- build the authoritative project successfully for the supported target;
- deploy the produced plugin to the target's regular `BepInEx/plugins` surface;
- start the supported target under actual BepInEx 5 and confirm that BepInEx loads
  the retained plugin;
- exercise the material application path; and
- validate the claimed gameplay effect and behavioral scope on that target.

If the supported target or its BepInEx 5 runtime is unavailable, the result may be
a buildable draft, but report it as an **unvalidated BepInEx draft** and name the
missing runtime acceptance check.

## Validate only the restoration lifecycle the plugin claims

Do not require hot unload solely to satisfy delivery.

When the plugin exposes an in-session disable, restoration, cleanup, config
toggle, command, or equivalent control path, exercise that path and verify the
state it claims to restore. If the documented restoration procedure is instead to
disable/remove the plugin and restart the target, state that lifecycle explicitly
and verify it when restoration is part of the retained deliverable's claim.

Removing a plugin, undoing a field change, or removing a patch does not imply that
already-emitted gameplay effects, saves, spawned objects, scene transitions, or
other completed side effects have been reversed. Keep those limits explicit.

## When the selected implementation uses HarmonyX

Apply this section only when the already-selected mechanism is implemented with
HarmonyX. HarmonyX does not make a hook preferable to a narrower direct managed
state change.

Bind the patch to the recovered semantic managed target and exact supported
assembly/build. Preserve any recovered generated-implementation relation rather
than patching a more convenient surface member.

Use plugin-owned patch identity and scope cleanup to the patches owned by this
plugin. A claimed disable or cleanup path must not remove unrelated Harmony
patches from other plugins.

Exercise the material patched path on the supported target. When the plugin claims
in-session patch removal or restoration, exercise that path as part of BepInEx
acceptance.

## Retain delivery provenance

For a retained plugin, follow [application-artifacts.md](application-artifacts.md)
and keep the consumed mechanic input, supported target identity, material assembly
hashes, authoritative project/source, produced plugin artifact, validation result,
and documented restoration/control lifecycle together.
