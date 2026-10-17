# Windows LÖVE Analysis Behavioral Evals

These scenarios supplement the shared `behavioral-evals.md` with Windows
LÖVE/Lua boundary cases. They protect user-visible analysis behavior rather than
one helper implementation. Record each required assertion as PASS or FAIL.

## 1. Fused Windows executable recovers Lua before native escalation

An authorized offline Windows `game.exe` is a standard fused LÖVE executable with
a structurally valid appended `.love` archive containing root `main.lua` and the
material mechanic in readable Lua.

Required assertions:
- classified the PE plus appended `.love` structurally rather than from a `PK`
  string or runtime DLL name alone
- recovered only the readable payload/source needed for the mechanic and retained
  target/payload provenance
- loaded the LÖVE adapter after the Lua boundary became material
- stayed at Lua/source level while it closed the mechanic
- did not begin PE/native reverse engineering merely because the shipped artifact
  was an executable

## 2. Custom love.run controls scheduling claims

Recovered Lua defines `love.update(dt)` but also overrides `love.run` with a
fixed-step accumulator that can call the gameplay update zero, one, or multiple
times per rendered frame.

Required assertions:
- detected and followed the custom `love.run` before making timing claims
- did not equate rendered frames with simulation steps
- preserved the actual accumulator/update ordering material to the mechanic
- kept any unresolved target-version/runtime timing detail explicit rather than
  substituting a frozen default main loop

## 3. Effective module resolution beats archive presence

The shipped `.love` contains `rules.lua`, while material filesystem/require
configuration causes `require("rules")` to resolve to a different effective copy
from a mounted or save-backed path.

Required assertions:
- did not call the archive copy authoritative solely because it existed
- recovered only the path/search/identity relation needed to determine the
  effective module origin
- preserved the distinction between code/data shadowing and gameplay save
  persistence
- traced the mechanic from the effective module actually consumed by the target

## 4. Worker thread owns the material computation

`love.update` only receives a value from a Channel. The formula and material
computation run in Lua supplied to `love.thread.newThread` and the result is sent
back to the main thread.

Required assertions:
- traced the worker source and Channel edge rather than stopping at the consumer
- distinguished computation ownership from main-thread consumption
- did not assume ordinary Lua variables/functions were shared across thread
  environments
- resolved shared LÖVE userdata only when it was material to ownership or scope

## 5. Lua to native transition stops LÖVE assumptions

A recovered Lua callback calls a C module or FFI/native function and the
unresolved authoritative mutation lies beyond that call.

Required assertions:
- preserved the effective Lua caller, arguments/state relation, and transition
  evidence
- identified the native implementation as the unresolved material boundary
- did not invent LuaJIT/private VM layouts, native calling conventions, or C-side
  gameplay semantics
- continued with the shared core/native workflow only because the decisive
  relation lay beyond the Lua boundary

## 6. Mechanical triage hints are not semantic proof

`love2d_triage.py` reports a custom `love.run`, several lexical `require` edges,
thread creation, RNG use, and adjacent DLL candidates.

Required assertions:
- treated the helper output as inventory/search hints and provenance rather than
  gameplay ownership evidence
- resolved only the indicators material to the requested mechanic
- did not infer effective module origin from a lexical `require` edge when path
  customization could change resolution
- did not classify a DLL candidate as the mechanic owner without transition/data
  flow evidence
