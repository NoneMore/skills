# Lovely Injector Delivery for Windows LÖVE Mods

Load this reference only for a retained Windows LÖVE/Lua gameplay change already
selected by `change-design.md` and refined by `change-love2d-lua.md`. Lovely is a
delivery surface; it does not choose the gameplay intervention point.

Lovely syntax and matching behavior are version-sensitive external state. Use the
selected Lovely release and its current documentation for exact manifest/patch
syntax instead of freezing that API here.

## Bind the patch to the semantic site

Consume the effective source/module and owner/caller relation from the mechanic
finding. For each game-side patch retain only the Lovely-specific binding needed
to distinguish that site:

- the target Lua buffer/source as Lovely sees it;
- a source/context anchor tied to the recovered semantic relation;
- the expected match cardinality or equivalent guard.

A first-match setting such as `times = 1` is not evidence that the first textual
match is the intended semantic site. If the site is ambiguous, refine the anchor
or return the missing relation to analysis rather than broadening the patch.

Keep nontrivial behavior in mod-owned Lua when that makes the game-side patch
smaller. Choose the least expressive Lovely patch form that identifies the site
reliably; obtain exact patch-form syntax from the selected Lovely documentation.

## Keep version and delivery evidence distinct

Record the Lovely version used to build and test the mod. A source pattern still
matching after target drift does not supersede the main Skill's target-binding
rules.

When the supported target/runtime is available, delivery is established by
running the selected Lovely version and confirming that it loads the mod and
applies the intended patch at the bound source site. Lovely logs or patched-source
output can support those delivery facts; they do not replace gameplay validation.

If the runtime is unavailable, keep the result as an **unvalidated Lovely mod
draft** and name actual Lovely load/patch acceptance as the missing delivery
check. The main Skill remains authoritative for gameplay-scope validation and
rollback claims.

## Bound the delivery surface

A Lovely-delivered Lua patch remains a Lua-level application even though Lovely
uses native process integration internally. Use the shared native runtime delivery
contract only when the retained mod itself performs the material native write or
depends on private native layouts.

Do not silently fall back to repacking `.love` archives, rebuilding fused
executables, or overwriting shipped Lua when Lovely cannot express the selected
intervention. Such destructive modification requires a separately selected and
authorized mechanism.

For retained artifacts, follow
[application-artifacts.md](application-artifacts.md) and add only Lovely-specific
state not already covered there: the Lovely version and semantic patch binding.
