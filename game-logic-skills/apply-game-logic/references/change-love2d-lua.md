# Windows LÖVE / Love2D Lua Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Windows
LÖVE/Lua mechanic to an authorized local/offline gameplay change. Select the
mechanism class first with [change-design.md](change-design.md); this guide only
refines the Lua-level intervention from already-recovered ownership, scheduling,
module-resolution, threading, and scope facts.

For retained Windows mods in this v1 surface, deliver the selected Lua-level
intervention through [lovely-delivery.md](lovely-delivery.md). Directly repacking
`.love` archives, rebuilding fused executables, or overwriting shipped Lua files
is outside the normal retained application path.

## Refine the intervention from recovered scope

Choose the narrowest semantic point whose recovered fan-out matches the requested
behavior:

- target an effective Lua value/function/state owner directly when its consumers
  are already within the requested scope;
- when the underlying owner/function is shared, prefer an evidenced caller,
  event, actor, state, or context boundary that narrows the effect to the
  requested scope;
- preserve recovered custom `love.run`, fixed-step/framework scheduling, module
  singleton, save-loaded state, and lifecycle relations when they affect where a
  change can safely occur;
- preserve recovered worker-thread/Channel ownership rather than patching the
  main-thread consumer merely because it is easier to reach;
- preserve recovered RNG source/state distinctions when the requested change
  depends on random behavior;
- preserve the effective module/source origin established by analysis rather than
  retargeting to a shadowed or inactive archive copy.

The loader does not choose the gameplay intervention point. Recovered mechanic
ownership and scope do.

If a relation needed to distinguish a narrow point is missing or stale, return
only that relation to `$analyze-game-logic`. Do not compensate for missing scope
knowledge with a broader patch plus ad hoc filters.

## Bind the semantic target

Keep target/version evidence separate from the semantic site the mod consumes.
For a retained LÖVE change record, preserve as material:

- the shipped target/build/hash evidence consumed by the finding;
- the effective Lua source/buffer/module path;
- the recovered function/caller/state relation identifying the intervention;
- the ownership/fan-out facts establishing requested scope;
- the expected source relation or value used to locate/guard the site;
- scheduler/thread/RNG/persistence facts only when they affect correctness.

A successful text match in a later build is not proof that the mechanic relation
or scope is unchanged. When the target drifts, revalidate only the material
semantic relation before reusing the intervention.

## Keep game-side integration thin

When the selected intervention needs nontrivial mod logic, keep that behavior in
mod-owned Lua and make the game-side integration as small as the recovered seam
allows. Prefer a thin call into mod-owned code over injecting a large replacement
implementation into the target function.

Do not force all changes through one patch style. A retained mod may combine a
small game-side integration patch with a separately injected module when that
keeps the authoritative mod logic local and the target seam narrow.

## Respect native boundaries

A Lovely-delivered Lua patch remains on this application path even though Lovely
itself uses native process integration internally. Do not route to the shared
native delivery contract solely because the loader is implemented natively.

If the retained mod itself writes process memory, installs/replaces executable
machine code, or materially depends on LuaJIT/private native layouts, use the
recovered transition evidence and the shared native runtime delivery contract for
that application path.

## Validate Love-specific scope

Under the main Skill's validation rules, exercise only material edges capable of
exposing the claimed scope, such as:

- a sibling/shared module consumer when the requested effect is actor-local;
- a second caller/event source when the patched function is shared;
- a custom scheduler/fixed-step edge when timing is part of the claim;
- a worker/main-thread boundary when computation ownership is material;
- save/reload/reset behavior when retained state is part of the claim;
- an independent RNG stream or shared generator when randomness scope matters.

If validation shows that the effective module, owner, caller, scheduler, thread,
or other mechanic relation differs from the consumed finding, return that
specific discrepancy to `$analyze-game-logic` instead of widening the patch.