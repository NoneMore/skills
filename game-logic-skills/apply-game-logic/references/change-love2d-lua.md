# Windows LÖVE / Love2D Lua Change Guidance

Load this reference only after [change-design.md](change-design.md) has selected a
gameplay-change mechanism and the consumed finding places the material
implementation in LÖVE-hosted Lua.

Use the effective Lua source/module and semantic owner/caller recovered by
analysis. When a shared owner would broaden the requested behavior, use an
already-evidenced narrower caller/context or return only that missing relation to
`$analyze-game-logic`. Do not retarget a shadowed archive copy or patch a
main-thread consumer when the finding places the material computation elsewhere.

Preserve a custom scheduler, worker boundary, or RNG source only when it changes
the selected intervention. Generic scope, target binding, validation, provenance,
and rollback rules remain authoritative in the main Skill and
[change-design.md](change-design.md).

For a retained Windows Lua mod delivered through Lovely Injector, load
[lovely-delivery.md](lovely-delivery.md). Keep nontrivial behavior in mod-owned
Lua when that permits a smaller game-side integration seam.

Lovely's native loader implementation does not by itself make the gameplay change
a native-runtime application. Route to the shared native delivery contract only
when the retained mod itself materially writes native process state/code or
depends on private native/LuaJIT layouts.
