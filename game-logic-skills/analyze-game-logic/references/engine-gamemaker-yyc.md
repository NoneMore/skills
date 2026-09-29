# GameMaker YYC Engine Adapter

This adapter covers GameMaker games whose GML gameplay logic has been compiled
to native code by YYC. Apply the core evidence and project-knowledge rules from
`SKILL.md`; this file supplies YYC-specific detection, runtime conventions, and
tracing tactics.

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

Validate these YYC search mappings against the target runner/game version:

- **Update/lifecycle:** Begin Step, Step, End Step; Create, Destroy, Clean Up,
  and room/game lifecycle events.
- **Triggers/time:** object events, scripts, alarms, collisions, async callbacks,
  and explicit calls; room steps, alarms, `delta_time`, wall-clock helpers,
  animation/image progression, or custom accumulators.
- **State owners:** instances, globals, structs/arrays/data structures,
  controller objects, and resource/config values surfaced through `RValue`
  operations and variable metadata.
- **Physics/presentation:** collision callbacks, built-in physics, custom
  movement/query code; Draw/GUI, sprite/image, particles, audio, camera, and HUD
  are observers unless data flow shows they own gameplay mutation.
- **Persistence/authority:** save/checkpoint/reset paths plus any networking or
  local-co-op boundaries; determine ownership/authority from data flow rather
  than from presentation or registration paths.

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

When mechanic reconstruction applies, use this YYC-specific path:

```text
semantic anchor / gml_* identity
  -> metadata / registration
  -> runtime ID or function-pointer xrefs
  -> native event/script implementation
  -> decisive state reads/writes
  -> callers, shared-use, and lifecycle paths
  -> controlled runtime validation when material
```

Do not stop at a plausible script body when the claim depends on trigger/source,
state ownership, or lifetime. When registration xrefs dominate, inspect adjacent
parallel tables and function pointers before scanning the entire text segment.

For timers/state machines, trace both refresh/write and decrement/expiry paths,
then establish the actual YYC time domain before converting counters to seconds.

Search for materially distinct sources that may share the same path, such as
damage, death, cutscenes, pause/loading transitions, damage-over-time, reflected
damage, local-coop slots, difficulty, skills, equipment, artifacts, or stats.

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

Useful YYC observation points include native script/event entry, `RValue`
reads/writes, timer refresh/expiry paths, and distinct callers of shared
state-transition functions. Apply the core rules for deciding when runtime
validation is required.

For a Frida write or hook, guard on the strongest available combination of
module identity/size, exact target hash when available, expected original
bytes/value, plausible argument count and runtime-value kind, stable
`module + RVA` or validated signature, and a reversible restore path.

Detaching instrumentation does not necessarily undo a raw memory write; state
restoration limitations must be explicit.

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

Record YYC-specific evidence as applicable:

- `gml_*` or registration identity and the relation that establishes it;
- validated variable-metadata layout and `RValue` kind/interpretation when used;
- stable `module + RVA` plus exact module/build hash for native locators;
- shared-call-site/source discrimination when one generated path serves multiple
  gameplay sources;
- the actual YYC time domain when a timer/counter is interpreted.

All generic mechanic, validation, and provenance evidence follows the core
workflow.

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
