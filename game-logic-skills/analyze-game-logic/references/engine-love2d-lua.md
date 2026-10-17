# Windows LÖVE / Love2D Lua Engine Adapter

Use this adapter after the material Windows boundary is identified as LÖVE-hosted
Lua. Generic scope, evidence, validation, persistence, and native escalation stay
in `SKILL.md`; this reference contains only LÖVE-specific tracing deltas.

## 1. Applicability and detection

Strong packaging evidence is a `.love` ZIP with root `main.lua`, or a structurally
valid Windows PE that is also a ZIP with root `main.lua`. A source directory or
generic ZIP with root `main.lua` is only a candidate; corroborate it with material
LÖVE-specific evidence such as `conf.lua`, LÖVE API use, or runtime strings/DLLs
before classifying the boundary as LÖVE-hosted Lua. None of these container signals
prove gameplay ownership.

Stop this adapter when the unresolved mechanic crosses a material C module, FFI
call, or other opaque native boundary.

## 2. Implementation model

```text
source / .love / fused PE
  -> main.lua / conf.lua
  -> effective module origin
  -> effective scheduler / thread
  -> authoritative Lua transition
  -> native boundary when material
```

Two LÖVE behaviors can invalidate the obvious source path:

- `love.filesystem` mounts, identity/search settings, or require-path changes can
  make a loaded module differ from the archive copy.
- custom `love.run` logic or a worker thread can make `love.update(dt)` only a
  dispatcher or consumer.

### Gameplay semantic mapping

- Bootstrap: root `main.lua`, `conf.lua`, and `love.conf`.
- Scheduling/dispatch: `love.run`, callbacks, framework loops, queues, and worker
  threads.
- State: Lua/module/object state, Channels, save-loaded values, and LÖVE userdata.
- Persistence: keep module/filesystem resolution distinct from gameplay save
  state.
- Randomness: distinguish shared random APIs from independent
  `RandomGenerator` instances when material.

## 3. Semantic anchors

Prefer `main.lua`/`conf.lua`, custom `love.run`, the material callback/dispatcher,
`require(...)` plus material `setRequirePath`/`setCRequirePath`/`mount`/identity
configuration, worker/Channel endpoints, and explicit Lua-to-native calls.

Callback presence and lexical `require` edges locate candidates; they do not prove
ownership or effective module resolution.

## 4. Runtime values and threads

Use ordinary Lua semantics until evidence crosses a native boundary. Determine
shared versus per-instance module state from construction/data flow. LÖVE worker
threads use separate Lua environments, so trace worker source and Channel/shared
userdata edges when they are material.

## 5. Recommended tracing workflow

Classify the container, corroborate the LÖVE boundary when packaging is ambiguous,
expose only the needed readable Lua, start from the strongest mechanic anchor,
resolve module origin/scheduler/thread only when it can change the claim, then
follow the path to the authoritative transition. For fused PEs, rely on valid PE +
ZIP structure rather than a `PK` string or runtime name.

## 6. Static-analysis guidance

Prefer readable Lua over native escalation. Lexical require/API inventories are
search hints because runtime path changes and dynamic loading can invalidate them.
Treat recovered bytecode/decompiled Lua as reconstructed evidence.

## 7. Runtime-observation guidance

If a material LÖVE-specific relation remains ambiguous, observe only the effective
module origin, scheduler, worker/Channel edge, or Lua side of the native
transition needed to close it.

## 9. Version-sensitive assumptions

Revalidate material target-version behavior for `love.run`, filesystem/search and
mount semantics, thread/Channel behavior, and Lua/LuaJIT details when bytecode or
native boundaries matter.

## 10. Common failure modes

- Classifying a generic `main.lua` source tree or ZIP as LÖVE without corroboration.
- Escalating a fused PE to native analysis before checking its appended Lua.
- Treating an archive member or lexical require as the effective module.
- Treating `love.update` or a Channel consumer as the scheduler/computation owner.
- Extending Lua assumptions across an opaque native call.

## 11. Evidence checklist

Record only material LÖVE deltas: fused-container provenance, nontrivial effective
module origin, scheduler/thread relation, and any decisive Lua-to-native
transition.

## 12. Bundled tool

`scripts/love2d_triage.py` mechanically inventories source directories, `.love`
archives, generic ZIP candidates, and fused Windows executables; hashes file
targets; and reports lexical resolution/scheduler/thread/native hints. Container
classification narrows search and does not by itself prove LÖVE identity, runtime
ownership, or effective resolution. Use `--self-test` for deterministic classifier
regressions.
