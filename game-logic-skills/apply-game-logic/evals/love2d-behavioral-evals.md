# Windows LÖVE Application Behavioral Evals

These scenarios supplement the shared `behavioral-evals.md` with Windows
LÖVE/Lovely delivery cases. They protect application correctness and scope rather
than a particular manifest shape. Record each required assertion as PASS or FAIL.

## 1. Shared owner uses a recovered narrow caller/context

A confirmed LÖVE finding shows that player and non-player actors share one update
function, while an already-recovered caller/context relation can distinguish the
player path. The requested retained change is player-only and is delivered with
Lovely.

Required assertions:
- did not patch the shared formula globally and call the result player-only
- used the recovered player-specific caller/context or returned only the missing
  narrowing relation to analysis
- kept nontrivial mod behavior in mod-owned Lua and the game-side integration
  narrow when practical
- treated Lovely as delivery rather than as the source of the intervention
  decision
- validated at least one non-player/shared consumer capable of exposing leakage

## 2. First-match settings do not identify an ambiguous semantic site

The candidate target string appears three times in one Lovely patch target, and
only one occurrence is the recovered mechanic site.

Required assertions:
- did not use `times = 1` or first-match behavior as proof of target identity
- refined the source/context anchor until the recovered semantic site was
  distinguishable, or stopped for the missing relation
- retained the expected target buffer and match/cardinality assumptions with the
  mod
- did not broaden to a regex solely to hide unresolved target ambiguity

## 3. Text matching after source drift does not prove compatibility

A newer game build still matches the proposed Lovely pattern, but the shipped
artifact or material source identity differs from the finding consumed by the
mod.

Required assertions:
- did not call the mod compatible merely because the text patch still matched
- identified the material semantic relation and scope facts requiring narrow
  revalidation
- reused unaffected application work after that relation was revalidated rather
  than restarting broad reverse engineering
- preserved the newly supported target identity in retained provenance

## 4. Generated mod files without runtime acceptance remain a draft

The authoritative `lovely.toml` and mod-owned Lua are generated successfully, but
the supported Windows target/Lovely runtime is unavailable for execution.

Required assertions:
- retained the output as an **unvalidated Lovely mod draft**
- did not call delivery complete from file generation or static patch review
  alone
- named actual Lovely load, patch acceptance, material gameplay exercise, and
  scope validation as missing checks as applicable
- kept rollback/disable instructions consistent with what was actually validated

## 5. Patched-source dump proves delivery, not gameplay semantics

Lovely loads and its dump shows the intended mod call inserted at the recovered
source location, but no gameplay scenario has yet tested actor-local scope.

Required assertions:
- used the dump/log as evidence that the expected source was emitted/applied
- did not promote that evidence into a player-only or behavior-correct claim
- exercised the material gameplay path and a sibling/shared consumer before
  claiming actor-local scope

## 6. Compatibility is limited to the tested mod set

The produced mod passes validation with the target game and selected Lovely
version. Other Lovely mods are installed in a different user's environment but
were not part of the tested baseline.

Required assertions:
- claimed compatibility only for the exact game/Lovely/mod set actually tested
- did not use patch priority/order as proof of compatibility with untested mods
- treated coexistence with specifically requested third-party mods as a new
  material compatibility constraint
- recorded the tested mod set and versions when compatibility was part of the
  retained claim
