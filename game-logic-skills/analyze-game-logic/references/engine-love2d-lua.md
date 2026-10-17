# Windows LÖVE / Love2D Lua Engine Adapter

This adapter covers authorized offline Windows LÖVE games whose material gameplay
logic is implemented in Lua hosted by LÖVE. It includes shipped source
directories, `.love` archives, and standard Windows fused executables whose
appended `.love` payload can be recovered structurally. Apply the core evidence,
version-scope, and project-knowledge rules from `SKILL.md`; this file supplies
LÖVE-specific packaging, lifecycle, module-resolution, threading, and tracing
semantics.

Treat material C modules, LuaJIT/private VM internals, FFI/native libraries, and
other opaque native implementations as separate boundaries. Preserve the
Lua-side caller and transition evidence, then continue with the shared core/native
workflow rather than extending Lua assumptions across the boundary.

## 1. Applicability and detection

Use mutually supporting indicators and prefer structural evidence over names or
runtime strings.

Strong indicators include:

- a source directory with a root `main.lua` consistent with a LÖVE game;
- a valid `.love` ZIP archive with root `main.lua`;
- a Windows PE executable with a structurally valid appended `.love`/ZIP payload
  whose root contains `main.lua`.

Supporting indicators include `conf.lua`, LÖVE runtime/version strings, adjacent
LÖVE/runtime DLLs, and recovered Lua using LÖVE APIs. Do not classify a material
gameplay boundary as LÖVE-hosted Lua from a DLL name, PE string, or executable
identity alone.

A LÖVE title does not prove that the material mechanic is implemented in Lua. If
recovered Lua delegates the unresolved state transition to a C module, FFI call,
or other native implementation, stop LÖVE-specific assumptions at that call.

This adapter does not own generic Windows installer or launcher unpacking. If an
MSI, NSIS/Inno-style installer, third-party launcher, or other outer package
blocks access to the installed game directory or actual `.love` payload, use an
appropriate external recovery path to expose the game artifact first, then resume
this adapter. Do not turn LÖVE triage into a general installer framework.

## 2. Implementation model

A useful shipped-game model is:

```text
Windows shipped artifact
        |
        +-- source directory
        +-- .love ZIP
        `-- fused PE + appended .love
                |
                v
        conf.lua / boot configuration
                |
                v
        main.lua / bootstrap
                |
                v
        effective filesystem + module graph
                |
                v
        actual scheduler
        +-- target-version default love.run
        `-- custom love.run
                |
                v
        callbacks / framework dispatch / worker threads
                |
                v
        effective state owner
                |
                v
        authoritative gameplay mutation
                |
                `-- native transition when material
```

The key LÖVE-specific concept is the **effective implementation**: the source,
module, value, callback, or state that actually controls the mechanic after
filesystem search order, mounts, require-path changes, runtime assignment, and
scheduling are accounted for. A file present in the shipped archive is not by
itself proof that it is the implementation loaded or consumed at runtime.

### Gameplay semantic mapping

Validate mappings against the target LÖVE/runtime version and recovered game:

- **Bootstrap/configuration:** `conf.lua`, `love.conf`, and `main.lua` are strong
  bootstrap anchors. Configuration can affect enabled modules, identity, and
  other runtime behavior before ordinary game code executes.
- **Scheduler/update:** establish whether `love.run` is overridden before using
  `love.update(dt)` as evidence about simulation cadence. A custom main loop,
  fixed-step accumulator, framework dispatcher, or worker can define the
  material timing domain.
- **Triggers:** LÖVE input/event callbacks, timers implemented by game/framework
  code, direct calls, queues, and framework dispatchers are caller/trigger
  anchors. Callback entry proves dispatch, not mechanic ownership.
- **State owners:** module locals, returned module tables, objects/classes, ECS
  components, state managers, closures, globals, save-loaded values, Channels,
  and shared LÖVE userdata are candidates. Establish owner and fan-out from data
  flow and lifecycle, not declaration style alone.
- **Persistence:** distinguish code/data resolution through `love.filesystem`
  from gameplay save persistence. A save-directory file can shadow source
  without being saved gameplay state; conversely a save file can own persistent
  state without participating in module resolution.
- **Randomness:** distinguish `math.random`, `love.math` random APIs,
  `RandomGenerator` instances/state, and custom RNG. Do not infer a shared RNG
  stream when the implementation uses independent generator objects.
- **Presentation:** `love.draw`, graphics, audio, and effects are usually
  observers, but follow data flow before declaring them presentation-only.

## 3. Semantic anchors

Prefer anchors that expose effective control and loading relationships:

- root `conf.lua` and `main.lua`;
- a custom `love.run` definition;
- `love.load`, `love.update`, `love.draw`, and material input/event callbacks;
- `require(...)` calls and the modules they actually resolve to;
- `love.filesystem.setRequirePath`, `setCRequirePath`, `mount`, `setIdentity`,
  and identity/priority configuration affecting source resolution;
- framework/state/ECS registration and dispatch tables;
- `love.thread.newThread`, thread source entrypoints, and Channel creation/use;
- `math.random`, `love.math` random APIs, and `RandomGenerator` creation/state;
- save/load serialization paths;
- native module loads, FFI/native-library loads, or other explicit opaque
  transitions.

Before treating a Lua file, configuration value, or module as authoritative,
establish its effective origin when save/source shadowing, mounts, or require
path customization can materially change the result.

Do not use callback presence as ownership proof. In particular,
`love.update(dt)` can be only a dispatcher or Channel consumer while the material
computation lives in another module or thread.

## 4. ABI, runtime values, and object model

Stay at Lua/LÖVE semantics while they close the mechanic. Track ordinary Lua
values, tables, closures, module state, metatable/class conventions, and LÖVE
userdata through observed code rather than assuming one object framework.

For module-backed state, establish whether `require` returns a shared module
singleton or whether callers construct per-instance state after loading it.
Likewise, a global or module-local table can intentionally fan out across scenes
or actors; do not call a field actor-local solely because it is reached through
an actor method.

LÖVE worker threads run separate Lua environments. Ordinary Lua variables and
functions are not implicitly shared across those environments. When a mechanic
crosses a thread boundary, trace the thread source plus Channels and any shared
LÖVE userdata needed to establish who computes, who communicates, and who owns
or mutates the authoritative state. A Channel consumer is not evidence that the
consumer owns the computation.

Do not invent LuaJIT GC layouts, VM bytecode structures, FFI object layouts,
native calling conventions, or private LÖVE runtime offsets. Preserve the
Lua-side transition evidence and continue outside this adapter when those details
become material.

## 5. Recommended tracing workflow

For shipped Windows targets, prefer:

```text
classify source/.love/fused PE
  -> expose the minimum readable game source
  -> identify conf.lua + main.lua bootstrap
  -> establish custom/default love.run scheduling when material
  -> resolve the relevant effective module/source origin
  -> follow callback/framework/thread dispatch to the state owner
  -> locate the decisive state read/write
  -> resolve reset, persistence, sharing, and RNG only when material
  -> stop at a native boundary or validate the Lua mechanic as required
```

For a fused executable, recover the appended `.love` from ZIP/container
structure. Do not treat the first `PK` byte sequence or a LÖVE-related PE string
as sufficient proof of payload start or gameplay ownership.

For module-driven mechanics, resolve the material `require` against the effective
search configuration before citing an archive member as the implementation. If
runtime save state or a mounted path could shadow that module and the distinction
can change the mechanic, inspect only the material runtime/environment state
needed to close that relation.

For scheduling-sensitive mechanics, check for custom `love.run` before converting
`dt`, counters, or callback frequency into a timing claim. Treat target-version
default scheduler behavior as recoverable runtime knowledge rather than copying a
frozen default loop into this adapter.

For thread-driven mechanics, trace the worker source and communication edge rather
than stopping at the main-thread callback that consumes the result.

## 6. Static-analysis guidance

Search readable Lua and configuration before escalating. Prefer module/caller
relationships, state mutation, and bootstrap/scheduler structure over broad text
scanning.

For `.love` or standard fused Windows targets, use the smallest mechanical
container recovery needed to expose relevant source while preserving the input
hash and recovered payload provenance. Do not rewrite installed game files.

Treat simple lexical `require` scans and API-name inventories as triage hints.
Dynamic module names, modified require paths, mounts, loader wrappers, generated
code, and runtime assignment can invalidate a purely lexical graph. Resolve only
the paths material to the mechanic rather than attempting an exhaustive Lua
program analysis.

If shipped Lua is bytecode or otherwise unreadable, identify the Lua/LuaJIT and
version evidence that is actually available and use a suitable recovery
capability only when needed. Recovered/decompiled Lua is reconstructed evidence,
not guaranteed original source. Successful recovery does not establish gameplay
ownership.

## 7. Runtime-observation guidance

Useful read-only observation points include:

- entry/exit of the recovered mechanic function or caller;
- the actual `love.run`/framework scheduling path when timing is material;
- before/after the authoritative state mutation;
- the effective module origin when static resolution remains ambiguous;
- Channel send/receive and worker entry when thread ownership is material;
- RNG state/value flow when effective randomness is material;
- save/load/reset paths when persistence is material.

Prefer game/framework-visible logging or other minimally invasive Lua-level
observation where practical. Do not escalate to native hooks merely because the
host executable is a PE when the Lua layer already closes the claim.

## 9. Version-sensitive assumptions

Revalidate per target rather than hard-coding:

- declared target LÖVE version versus shipped/runtime LÖVE version evidence;
- `love.run` contract and default scheduling behavior for the target runtime;
- filesystem identity/search precedence and any `appendidentity` behavior;
- require/C-require paths and mount behavior;
- thread/Channel API and runtime behavior material to the claim;
- random API/state behavior material to the mechanic;
- fused executable/container details;
- Lua versus LuaJIT runtime/version and any bytecode recovery assumptions;
- third-party framework/state-manager behavior.

Keep declared target version and runtime-version evidence distinct. A `conf.lua`
version declaration is not by itself proof of the exact runtime embedded in a
shipped executable.

## 10. Common failure modes

- Treating a Windows PE as a native-only target before checking for a recoverable
  fused `.love` payload.
- Classifying gameplay as LÖVE-hosted Lua from `love.dll` or strings alone.
- Treating an archive member as the effective module without checking material
  save/source shadowing, mounts, or require-path customization.
- Assuming `love.update(dt)` defines the actual simulation cadence when a custom
  `love.run`, framework scheduler, fixed-step loop, or worker controls timing.
- Treating a callback or Channel consumer as the mechanic owner.
- Treating save-directory presence as proof of gameplay persistence.
- Treating a shared module/global as instance-local without fan-out evidence.
- Treating multiple generated/recovered source views as independent mechanic
  evidence.
- Extending Lua semantics across C modules, FFI/native calls, LuaJIT internals,
  or other opaque native boundaries.
- Turning the adapter or helper into a generic Windows installer/launcher
  unpacker.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- exact Windows target and shipped artifact hash;
- container classification and recovered `.love` provenance when applicable;
- declared target LÖVE version and distinct runtime-version evidence when known;
- effective Lua path/module locator and the resolution facts material to it;
- `love.run`/scheduler relation when timing depends on it;
- callback/framework/thread caller path;
- module/global/object/thread owner and fan-out/lifetime relation;
- Channel/shared-userdata transition when worker computation is material;
- RNG source/state relation when randomness is material;
- explicit Lua-to-native transition evidence when the decisive mutation lies
  beyond this adapter.

## 12. Bundled tools

`scripts/love2d_triage.py` is a read-only Windows LÖVE triage helper. It accepts a
source directory, `.love` archive, or Windows executable; hashes the target;
classifies supported containers; structurally exposes a standard fused `.love`
payload when present; inventories Lua/config inputs; and reports conservative
bootstrap, require/path, threading, RNG, and native-transition indicators.

The helper does not execute the game, inspect ambient `%APPDATA%` by default,
interpret mechanics, establish ownership, or patch source/runtime state. Its
module edges and API indicators are search hints rather than gameplay evidence.
Use explicit runtime/environment inspection only when effective resolution is
material to the current claim.