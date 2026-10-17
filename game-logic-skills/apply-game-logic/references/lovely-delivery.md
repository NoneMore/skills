# Lovely Injector Delivery for Windows LÖVE Mods

Load this reference only when a retained Windows LÖVE/Lua gameplay change is
delivered through Lovely Injector. The shared application contract chooses and
validates the gameplay intervention; this file adds only Lovely-specific delivery
requirements.

Lovely syntax and matching behavior are version-sensitive external state. Use the
selected release documentation for exact manifest and patch syntax.

## Bind the semantic site

Bind each game-side patch to the recovered effective Lua source and semantic site
using the Lovely-visible target buffer, a source/context anchor, and the expected
match cardinality or equivalent guard.

A first-match option such as `times = 1` does not establish semantic identity. If
the intended site is still ambiguous, refine the anchor or return the missing
relation to analysis instead of broadening the patch.

## Establish delivery

Record the Lovely version. When the supported target/runtime is available, confirm
that this version loads the mod and applies the patch at the bound source site.
Lovely logs or patched-source output can establish those delivery facts but do not
replace gameplay validation.

Without that runtime check, retain the result as an **unvalidated Lovely mod
draft** and name Lovely load/patch acceptance as the missing delivery evidence.

## Bound the delivery surface

Lovely's native loader does not make a Lua patch a native-runtime application.
Use the shared native delivery contract only when the retained mod itself performs
the material native write or depends on private native layouts.

Do not silently fall back to repacking `.love`, rebuilding fused executables, or
overwriting shipped Lua when Lovely cannot express the selected intervention.

For retained artifacts, [application-artifacts.md](application-artifacts.md)
already owns generic provenance/rollback; add only the Lovely version and semantic
patch binding.
