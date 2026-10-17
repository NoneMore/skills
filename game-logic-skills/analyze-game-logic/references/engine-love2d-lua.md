# Windows LÖVE / Love2D Lua Engine Adapter

Use this adapter after the material implementation boundary is identified as Lua
hosted by LÖVE on Windows. Inherit generic scope, evidence, validation, and
persistence rules from `SKILL.md`; keep this reference to LÖVE-specific facts that
can change tracing.

## 1. Applicability and detection

Strong indicators are:

- a source directory with root `main.lua`;
- a valid `.love` ZIP with root `main.lua`;
- a Windows PE with a structurally valid appended ZIP whose root contains
  `main.lua`.

`conf.lua`, LÖVE runtime strings/DLLs, and LÖVE API use are supporting evidence,
not sufficient classification by themselves. A LÖVE title also does not prove
that the requested mechanic remains in Lua: stop this adapter at a material C
module, FFI call, or other opaque native implementation.

Generic installer or launcher unpacking is outside this adapter. Expose the
installed game artifact first, then resume here.

## 2. Implementation model

For tracing purposes, the LÖVE-specific path is:

```text
source / .love / fused PE
  -> conf.lua + main.lua
  -> effective filesystem/module origin
  -> effective scheduler
  -> callback/framework/thread path
  -> authoritative Lua state transition
  -> native boundary when material
```

Two LÖVE details frequently change the obvious answer:

- `love.filesystem` mounts, identity/search settings, or require-path changes can
  make the effective module differ from the copy visible in the shipped archive.
- a custom `love.run` or worker thread can make `love.update(dt)` a dispatcher or
  consumer rather than the material scheduler/computation owner.

### Gameplay semantic mapping

- Bootstrap: `conf.lua`, `love.conf`, and root `main.lua`.
- Scheduling: target-version `love.run`, custom `love.run`, framework loops, and
  worker threads.
- Dispatch: LÖVE callbacks, direct calls, queues, and framework/state dispatch.
- State: Lua locals/tables/closures, module singletons, objects/ECS state,
  Channels, save-loaded values, and LÖVE userdata.
- Persistence: distinguish filesystem/module resolution from gameplay save state.
- Randomness: distinguish global random APIs from independent
  `RandomGenerator` instances when randomness is material.

## 3. Semantic anchors

Prefer anchors that can establish effective control:

- `main.lua`, `conf.lua`, and a custom `love.run`;
- the material LÖVE callback or framework dispatcher;
- `require(...)` plus any material `setRequirePath`, `setCRequirePath`, `mount`,
  or identity configuration;
- `love.thread.newThread` and Channel endpoints when a worker is material;
- the Lua call that crosses into a C module, FFI library, or other native code.

Callback presence and lexical `require` edges are locating hints, not ownership or
effective-module proof.

## 4. Runtime values and threads

Use ordinary Lua semantics unless evidence crosses a native boundary. Establish
whether module state is shared or per-instance from construction and data flow,
not naming.

LÖVE worker threads have separate Lua environments. Trace worker source and
Channel/shared-userdata edges when a mechanic crosses that boundary; a
main-thread Channel consumer does not own the worker computation.

## 5. Recommended tracing workflow

1. Classify source, `.love`, or a standard fused PE and expose only the readable
   source needed for the mechanic.
2. Start from `main.lua`/`conf.lua` and the strongest mechanic anchor.
3. Resolve effective module origin or scheduler only when it can change the
   interpretation.
4. Follow the material callback/framework/thread path to the authoritative state
   transition.
5. Stop at a native boundary when the unresolved relation is beyond Lua.

For fused executables, recover the appended archive structurally; do not use the
first `PK` string or a LÖVE-related DLL/string as the payload boundary.

## 6. Static-analysis guidance

Prefer readable Lua over native escalation. Treat lexical require/API inventories
as search hints because runtime path changes, mounts, generated names, or dynamic
loads can invalidate them.

If shipped Lua is bytecode or otherwise unreadable, recover only the material view
needed to continue and keep recovered source distinct from original source.

## 7. Runtime-observation guidance

When static evidence cannot resolve a material LÖVE-specific relation, useful
observation points are the actual scheduler path, effective module origin,
worker/Channel boundary, or the Lua side of a native transition. Generic runtime
validation rules remain in `SKILL.md`.

## 9. Version-sensitive assumptions

Revalidate only details material to the claim:

- shipped/runtime LÖVE version versus any declared target version;
- default `love.run` behavior;
- filesystem identity/search, require paths, and mount behavior;
- thread/Channel behavior;
- Lua versus LuaJIT details when bytecode/native boundaries matter.

## 10. Common failure modes

- Treating a fused PE as native-only before checking for an appended `.love`.
- Treating an archive member as effective code despite material path shadowing.
- Equating rendered frames or `love.update` calls with simulation steps despite a
  custom scheduler.
- Treating a callback or Channel consumer as the state/computation owner.
- Extending Lua assumptions across an opaque native call.

## 11. Evidence checklist

Add only the LÖVE-specific facts material to the finding:

- container/payload provenance for a fused executable;
- effective Lua module/source origin when resolution is nontrivial;
- scheduler relation when timing depends on it;
- worker/Channel relation when computation crosses a thread;
- explicit Lua-to-native transition when the decisive relation leaves Lua.

## 12. Bundled tool

`scripts/love2d_triage.py` is a read-only helper for source directories, `.love`
archives, and standard fused Windows executables. It classifies containers,
hashes file targets, inventories Lua/config/native candidates, and reports a small
set of lexical hints. Its output narrows search; it does not establish mechanic
ownership or effective runtime resolution.
