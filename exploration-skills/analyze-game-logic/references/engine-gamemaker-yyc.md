# GameMaker YYC Engine Adapter

This adapter covers GameMaker games whose GML gameplay logic has been compiled
to native code by YYC. Apply the core evidence and project-knowledge rules from
`SKILL.md`; this file supplies YYC-specific detection, runtime conventions, and
tracing tactics.

## Contents

1. [Applicability and detection](#1-applicability-and-detection)
2. [Implementation model](#2-implementation-model)
   - [Gameplay semantic mapping](#gameplay-semantic-mapping)
3. [Semantic anchors](#3-semantic-anchors)
4. [ABI, runtime values, and object model](#4-abi-runtime-values-and-object-model)
5. [Recommended tracing workflow](#5-recommended-tracing-workflow)
6. [Static-analysis guidance](#6-static-analysis-guidance)
7. [Runtime-observation guidance](#7-runtime-observation-guidance)
8. [Modification-point selection](#8-modification-point-selection)
9. [Version-sensitive assumptions](#9-version-sensitive-assumptions)
10. [Common failure modes](#10-common-failure-modes)
11. [Evidence checklist](#11-evidence-checklist)
12. [Bundled tools](#12-bundled-tools)

## 1. Applicability and detection

Treat YYC as a native-code target. Game logic is compiled into the executable or
native modules; `data.win` still supplies resources and metadata but is not a
normal GML bytecode analysis target.

Use multiple mutually supporting indicators, for example:

- a GameMaker-style `data.win` beside the executable;
- YoYo Games or GameMaker runner strings/import patterns;
- native strings beginning with `gml_Script_` or `gml_Object_`;
- large amounts of generated native code and `RValue` helper calls;
- script/event registration tables that point into native code.

Do not classify a build as YYC from `data.win` alone. Distinguish it from VM
bytecode, older runners, extensions, and unrelated embedded runtimes.

## 2. Implementation model

In a YYC build, gameplay scripts/events are represented by generated native
functions. Resources and metadata may still live in `data.win`, while executable
code, generated helper calls, registrations, and runtime state access live in
the native image.

A useful conceptual split is:

```text
data.win / resource metadata
        +
script/event/variable registration metadata
        -> native generated functions
        -> runner helpers and runtime state
```

Do not treat the resource container as the primary bytecode target when the
logic is native.

### Gameplay semantic mapping

Use these YYC conventions to map the cross-engine gameplay model onto likely
implementation sites. Treat them as search guidance and validate them against
the target runner/game version.

- **Simulation/update:** object Begin Step, Step, and End Step events commonly
  own per-step gameplay updates. Draw/GUI events are normally presentation paths
  unless data flow proves they also mutate authoritative gameplay state.
- **Entity/object lifecycle:** object Create establishes instance state; Destroy
  and Clean Up participate in teardown; room/game lifecycle events can create,
  reset, or replace controller/global state.
- **Time:** mechanics may use room steps, alarms, `delta_time`, wall-clock
  helpers, animation/image progression, or custom accumulators. Establish which
  domain advances during pause, slow motion, loading, and room transitions.
- **Events and dispatch:** generated object event functions, scripts, alarms,
  collision events, async callbacks, and explicit script calls can all trigger a
  mechanic. Trace shared scripts back to the concrete event/caller that supplies
  the source-specific context.
- **Gameplay state:** state may live on instances, globals, structs/arrays/data
  structures, controller objects, or resource/config values surfaced through
  generated `RValue` operations and variable metadata.
- **Persistence/reset:** save/checkpoint formats are game-specific. Determine
  which runtime values are serialized, reconstructed from defaults, or reset by
  death, room restart/change, and new-game flows rather than assuming all global
  or controller state persists.
- **Physics/spatial rules:** collision events, built-in physics integration, and
  custom movement/query scripts can represent different simulation domains; do
  not infer one from the presence of the other.
- **Presentation:** Draw/GUI, sprite/image state, particles, audio, camera, and
  HUD updates can expose the mechanic without owning its mutation.
- **Authority:** for an authorized offline build, the relevant local simulation
  path is normally the authority for the analyzed mechanic. Networking
  extensions or local-coop code can still create multiple sources/actors that
  must be discriminated.

Map the recovered implementation back to the mechanic chain from
`gameplay-semantics.md`: trigger, eligibility, inputs, computation/RNG,
authoritative mutation, secondary effects, presentation, and lifetime/reset.

## 3. Semantic anchors

YYC builds frequently retain diagnostic frame strings such as:

```text
gml_Script_playerDamage
gml_Object_obj_player_Create_0
gml_Object_obj_controller_Step_0
```

These may appear in a function prologue even when IDA names the function
`sub_*`. Use them as identity evidence, then confirm with callers, state access,
and behavior.

Also inspect:

- script registration wrappers and function-pointer tables;
- object event tables;
- internal variable-name strings;
- built-in/generated helper names such as `RValue_*`, `YYC_*`, and
  `gm_builtin_*` when symbols survive.

A `gml_*` string proves association, not necessarily implementation. Tiny string
accessors, registration thunks, metadata descriptors, and the actual script body
can all reference related names.

### Variable-name metadata as a two-hop anchor

Internal variable names often lead to metadata rather than directly to gameplay
code. One observed layout is:

```c
struct VariableEntry {
    const char *name;  // +0x00
    int id;            // +0x08, initialized at runtime
    int reserved;      // +0x0C
};
```

Generated code can read the runtime ID field and ask a global/instance variable
container for the corresponding value. Prefer:

```text
semantic variable-name string
  -> data xref to candidate metadata entry
  -> code xrefs to candidate ID field
  -> functions that read or write the actual variable
```

Do not hard-code a 16-byte stride or `+0x08` ID offset across games. Validate a
candidate layout with multiple known names and coherent field xrefs.

## 4. ABI, runtime values, and object model

### Common native script shape

A common x64 YYC script shape is conceptually:

```c
RValue *script(
    YYObjectBase *self,
    YYObjectBase *other,
    RValue *result,
    int argc,
    RValue **argv
);
```

On Windows x64, the first four parameters arrive in `RCX`, `RDX`, `R8`, and
`R9`; the fifth is stack-passed. Generated wrappers and event functions may
differ.

Confirm the ABI from several call sites before applying a type. Strong
indicators include:

- writing an undefined/default value into `result`;
- checking `argc` before reading `argv`;
- copying or releasing 16-byte runtime values;
- accesses to `self` or `other` through generated instance-variable helpers.

Treat this signature as a version-sensitive convention, not a universal
declaration.

### `RValue` interpretation

YYC commonly moves values in 16-byte records. A useful conceptual layout is:

```c
struct RValue {
    uint64_t payload;
    uint32_t flags_or_aux;
    uint32_t kind;
};
```

The payload may represent a `double`, integer, pointer, string/object reference,
or tagged asset value. Exact kind values and ownership rules vary by runtime.

Before decoding or changing a candidate value:

1. Read the full record, not only the first eight bytes.
2. Inspect how generated code tests the kind/tag field.
3. Compare with nearby known values.
4. Confirm how the consumer interprets it.
5. Audit all xrefs to determine whether the value is shared.

Do not interpret every payload as a `double`. Reference-counted values may
require retain/release behavior; never overwrite them speculatively.

## 5. Recommended tracing workflow

Start by sketching the target mechanic with the core gameplay semantic model,
then use this YYC-specific progression to map each stage to implementation:

```text
player-visible behavior and reproduction
  -> trigger/event and likely state owner
  -> semantic strings, variable names, or gml_* identities
  -> metadata/registration entries
  -> runtime ID or function-pointer xrefs
  -> native event/script implementation
  -> eligibility, inputs, formula/transition/RNG
  -> authoritative state write
  -> callers, secondary sources, and shared-use audit
  -> expiry/reset/persistence and presentation paths
  -> controlled runtime validation
```

Do not stop after recovering a plausible script body. Close the mechanic loop:
show which event triggers it, which state it owns or mutates, which other sources
share the path, and how the state expires or survives lifecycle transitions.

When registration xrefs dominate, inspect adjacent parallel tables and function
pointers before scanning the entire text segment.

For timers/state machines, trace both the refresh/write path and the
decrement/expiry path. Determine whether time is expressed in room steps, Step
events, milliseconds, `delta_time` microseconds, alarms, real-time clocks,
animation frames, or a paused/scaled clock.

Search for special sources that may share the same refresh/transition function,
including damage, death, cutscenes, pause/loading transitions, damage-over-time,
reflected damage, local-coop slots, difficulty, skills, equipment, artifacts,
or stats. Convert steps to seconds only after the effective update rate is
established.

## 6. Static-analysis guidance

For large generated functions, analyze basic blocks around decisive field
accesses/calls first. Generated exception cleanup and runtime-value lifetime code
can obscure a short GML operation.

When decompiler output is noisy:

- identify runtime-value copy, release, arithmetic, compare, and conversion
  helpers;
- collapse lifetime-management blocks mentally;
- follow value-producing calls and final assignments;
- use instruction-level views around decisive calls;
- verify constants from raw bytes;
- prefer metadata/function-pointer xrefs over broad instruction scans.

Do not stop at UI/draw functions merely because they reference the right text or
variable name.

## 7. Runtime-observation guidance

Use narrow runtime observation to validate identities, values, call counts,
state transitions, units, and source discrimination before writing memory.

When the game can be observed safely at runtime, normally validate before
confirming YYC claims that depend on:

- converting Step/event counts or timer fields into seconds or other wall-clock
  units;
- distinguishing which of several callers/events refreshes or consumes shared
  state in the reproduced gameplay path;
- state persistence/reset behavior across pause, death, room transitions,
  loading, cutscenes, or save/reload;
- the causal scope of a static `RValue`, instance/global variable, or shared
  refresh/transition function selected as a modification point.

Apply the evidence-independence definition from `SKILL.md` §5; do not count
alternate renderings or metadata wrappers as separate checks.

For a Frida write or hook, guard on the strongest available combination of:

- module name and image size;
- exact game/build hash documented with the analysis when in-process hashing is
  impractical;
- expected original bytes or value;
- plausible argument count and runtime-value kind;
- stable `module + RVA` or a validated signature;
- a reversible restore path.

Detaching an instrumentation script does not necessarily undo a raw memory
write. State restoration limitations should be stated explicitly.

## 8. Modification-point selection

Prefer the narrowest YYC state representing the requested behavior:

1. Change a uniquely referenced static numeric runtime value when it controls
   only the intended source.
2. Intercept one call site or discriminate by return address when a shared
   callee receives different values from different sources.
3. Hook the shared script only when all sources should change together.
4. Modify a live global/instance runtime value only after confirming type,
   ownership, and lifetime.

Shared refresh functions are a common source of overly broad changes. Audit all
callers before choosing the hook point.

## 9. Version-sensitive assumptions

Revalidate per runner/game version rather than hard-coding:

- native script/event ABI details and wrapper shapes;
- variable metadata entry size and runtime-ID offset;
- `RValue` tag/kind values, ownership, and lifetime rules;
- generated helper names or which symbols survive;
- registration table formats and pointer relationships;
- runner timing behavior and room/update-rate assumptions.

Record observed layouts as version-scoped findings, not universal GameMaker
facts.

## 10. Common failure modes

- Searching only UI text and stopping at a draw function.
- Treating a Step/Alarm/script function as the whole mechanic without mapping
  its trigger, authoritative mutation, and reset/lifetime path.
- Treating every xref to a `gml_*` string as the implementation function.
- Broad-scanning huge instruction ranges before following metadata xrefs.
- Assuming one observed variable-table layout applies to every YYC runtime.
- Decoding an `RValue` payload without validating its tag/kind.
- Calling a frame/step count seconds without confirming update rate.
- Hooking a shared refresh function and unintentionally changing cutscene,
  transition, damage, or other behavior.
- Treating decompiler-generated cleanup/lifetime code as gameplay logic.
- Recording raw VA without `module + RVA` and exact version/hash.
- Patching the installed executable before reversible runtime validation.

## 11. Evidence checklist

Before claiming a YYC mechanic is understood, record as applicable:

- player-visible mechanic trigger, authoritative state owner, and relevant
  lifetime/reset path;
- script/event identity and how it was established;
- relevant variable names and metadata-field evidence;
- read/write/expiry functions and call paths;
- raw constant bytes plus interpreted value and type/tag evidence;
- relevant constant/function xrefs and shared-use audit;
- timer/formula units and update-rate evidence;
- stable `module + RVA` locations;
- exact game/build/module hash;
- runtime test procedure and result when performed;
- special paths and known limitations;
- whether a proposed change affects one source or shared behavior.

## 12. Bundled tools

Use `scripts/yyc_triage.py` inside an already-open IDA database. It is read-only:
it does not rename, comment, patch, or save the database. The helper is written
for Python 3.8+ syntax and should be run under an IDAPython environment that
meets that requirement.

Capabilities:

- find semantic strings supplied with `--term`;
- list direct string xrefs and containing functions;
- probe a configurable candidate variable-ID field next to a data xref;
- list `gml_Script_*` and `gml_Object_*` markers;
- decode a candidate 16-byte runtime value without changing it;
- print addresses as VA and `module + RVA`;
- bound strings, xrefs per anchor, and total emitted records independently so a
  large IDB cannot flood tool/model output.

Useful output controls are `--max-strings`, `--max-xrefs-per-anchor`, and
`--max-total-records`. The legacy `--limit` option remains as a compatibility
shorthand for the first two limits.

Headless example against a copied target or existing analysis database:

```text
idat -A -S"yyc_triage.py --term killtimer --term duration" copied-target.exe
```

IDA 9.x normally names the console executable `idat`; older installations may
use `idat64`.

Interactive IDA use: run the script without arguments and enter comma-separated
search terms when prompted.

Treat descriptor-field probes and decoded values as hypotheses until table
layout and runtime-value interpretation are validated manually. The script is a
mechanical triage helper, not a semantic oracle.
