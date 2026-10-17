# Lovely Injector Delivery for Windows LÖVE Mods

Load this reference when a retained Windows LÖVE/Lua gameplay change selected by
[change-love2d-lua.md](change-love2d-lua.md) is delivered through Lovely
Injector. This guide adds Lovely-specific packaging, target binding, patch
selection, acceptance, compatibility, and rollback requirements. It does not
select the gameplay-change mechanism or semantic intervention point.

Lovely's patch syntax and loader implementation are version-sensitive external
state. Use the actual selected Lovely version and its current documentation for
exact manifest/patch syntax rather than treating examples here as a frozen API.

## Keep loader and mechanic decisions separate

Lovely determines how mod code reaches the LÖVE runtime. The consumed mechanic
finding and `change-love2d-lua.md` determine where behavior should change.

Do not move an intervention to a broader or easier-to-match source location merely
because Lovely can patch it conveniently. Preserve the recovered owner, caller,
scheduler, thread, and fan-out relations that justified the selected semantic
site.

A Lovely-delivered Lua modification remains a Lua-level application path even
though Lovely uses native process integration internally. Enter the shared native
runtime delivery contract only when the retained mod itself writes process
memory, installs/replaces executable machine code, or depends materially on
private native/LuaJIT layouts.

## Organize authoritative mod code locally

Prefer mod-owned Lua modules for nontrivial behavior and keep game-side source
patches thin. A typical retained artifact may contain a Lovely patch manifest plus
one or more mod-owned Lua files; do not duplicate the authoritative behavior in
both the manifest payload and a separate module unless the duplication has a
concrete delivery need.

Use Lovely patch surfaces by role rather than a global ranking:

- **module patches** are appropriate for injecting independent mod-owned Lua that
  should remain isolated and reusable;
- **pattern patches** are appropriate for establishing a narrow integration seam
  at an evidenced target source location;
- **regex patches** are appropriate only when a stable target cannot be expressed
  adequately with the simpler pattern patch;
- **copy patches** are appropriate for bootstrap or genuinely
  position-independent bulk injection, not as the default way to replace a
  mechanic implementation.

Complex retained mods may legitimately combine a module patch with one or more
small pattern patches.

## Bind every patch to the recovered semantic target

For each game-side patch, retain enough information to distinguish the intended
site from other textually similar locations:

- target game/build and material hash evidence;
- target Lua buffer/source path as Lovely sees it;
- the recovered semantic function/caller/state relation;
- a source anchor/context tied to that relation;
- the expected match cardinality needed for the chosen patch;
- any material original value or surrounding state used as a guard.

`times = 1` or an equivalent first-match setting is not a substitute for proving
that the first match is the recovered semantic target. If a proposed anchor has
multiple plausible matches, refine the anchor or return the missing relation to
analysis rather than silently choosing one.

A patch that still matches after a game update is not automatically compatible.
When shipped target identity or material source identity drifts, revalidate only
the semantic relation and scope facts the patch depends on before calling the mod
compatible with the new target.

## Keep Lovely version provenance explicit

Record the Lovely version used to build/test the retained mod. Do not rely on
Lovely manifest fields that are unsupported or non-enforcing as compatibility
boundaries. Treat patch-format details, Windows loader filename, and matching
semantics as version-sensitive external behavior and verify them against the
selected Lovely release when material.

Do not pin the Skill to one Lovely version. A later session should be able to tell
which loader version produced and validated the retained result without requiring
conversation history.

## Require Lovely-native acceptance

A retained mod is not delivery-complete merely because its files were generated.
Before calling delivery complete, when the supported target/runtime is available:

1. verify the target identity still satisfies the consumed mechanic evidence;
2. install/use the selected Lovely version on the supported Windows target;
3. confirm Lovely loads and the mod/patch files are accepted without material
   loader or patch errors;
4. verify the intended target patch applies at the recovered semantic site;
5. inspect Lovely's patched-source dump and logs when they materially help confirm
   the emitted source and target selection;
6. exercise the requested gameplay path under the main Skill's validation rules;
7. exercise the minimum sibling/caller/lifecycle/thread/RNG edge capable of
   exposing scope leakage for the claim being made;
8. disable or remove the produced mod, restart when required, and confirm the
   claimed control behavior is restored.

Patched-source dumps and loader logs prove delivery facts, not gameplay semantics.
They can show what source Lovely emitted or whether a patch loaded; they do not by
themselves prove player-only scope, timing correctness, persistence, or other
behavioral claims.

If the supported target or Lovely runtime is unavailable, retain the output as an
**unvalidated Lovely mod draft** and name actual Lovely load plus material
Gameplay validation as missing acceptance checks.

## Keep rollback proportional

Do not require hot unload solely to call a retained Lovely mod reversible. A
remove/disable plus game restart lifecycle is sufficient when that is the actual
rollback claim and validation confirms control behavior returns.

If the mod claims in-session disable, live restoration, config reload, or another
stronger control path, exercise that path before claiming it works.

Direct modification of shipped `.love` archives, fused executables, or shipped
Lua files is outside this normal retained delivery surface. Do not silently fall
back to destructive installed-content modification when Lovely cannot express the
selected intervention; report the delivery limitation and reopen mechanism choice
only if the user explicitly expands scope.

## Scope compatibility claims to the tested mod set

Do not promise compatibility with arbitrary Lovely mods. Lovely can load multiple
patches whose ordering and target overlap can materially change behavior, but
priority/order alone does not prove compatibility.

By default, validate against the exact baseline consisting of the supported game,
the selected Lovely version, and the produced mod. If coexistence with named mods
is a user requirement, treat that exact mod set and versions as a material
compatibility constraint and validate the interactions capable of changing the
selected target or behavior.

## Retain provenance with the mod

For a retained mod, follow [application-artifacts.md](application-artifacts.md).
Keep the authoritative mod source/configuration together with:

- supported target/build and material hashes;
- the consumed mechanic finding;
- Lovely version;
- semantic patch target and guards/cardinality assumptions;
- actual validation performed and compatibility scope;
- rollback/disable procedure;
- remaining unknowns or unvalidated acceptance steps.

The deployed result should be reconstructable and reviewable without depending on
chat history or on a generated patched-source dump as the authoritative mod
source.