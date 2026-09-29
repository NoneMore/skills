# Gameplay Change Design

Load this reference only when the user asks to design, apply, or validate a local
offline gameplay change. The recovered mechanic is the input contract: establish
behavioral scope before optimizing implementation convenience.

## Establish scope before mechanism

Determine whether the candidate value, object, definition, field, or call path is
shared across actors, sides, event sources, or gameplay contexts. Treat unresolved
ownership/fan-out as **Unknown**. Reversible does not mean narrowly scoped.

If ownership/fan-out is material but absent from the input mechanic record, return
that narrow question to `$analyze-game-logic` before choosing a change
mechanism.

When the intended effect is narrow, prefer a candidate whose ownership or caller
path naturally matches that scope over a globally shared hook that requires
special-case filtering.

## Prefer the least invasive acceptable mechanism

Among changes with acceptable behavioral scope, prefer in order:

1. an existing game configuration or supported mod interface;
2. a reversible runtime data change with version/value guards;
3. a hook limited to one caller or event source;
4. a hook on shared logic with documented filtering and side effects;
5. destructive modification of original installed files only with explicit
   authorization.

Runtime writes, hooks, injected instrumentation, and reversible mod techniques
may be used when permitted. Document what changes, where it changes, which
recovered finding/locator it depends on, how it is version-guarded, and how to
restore the control state.

## Version and address guards

Bind the change to the exact target version/build/hash. For native interventions,
record stable `module + RVA` locators and verify VA/RVA/file-offset/runtime-
address conversion against the original binary or loaded module before use.

Do not rely on a raw virtual address across launches or builds. If a signature or
pattern is used for relocation, validate that it resolves uniquely and still maps
to the recovered semantic site before applying the change.

If the installed target no longer matches the version/hash that supports the
mechanic record, stop and revalidate the material relation with
`$analyze-game-logic`.

## Destructive changes

Before any destructive patch, record:

- exact target file/module hash;
- original bytes or original file content;
- replacement bytes/files;
- file-offset or RVA mapping when applicable;
- expected behavioral effect and known shared-use risks;
- restoration procedure.

For every retained or deployed change, follow
[application-artifacts.md](application-artifacts.md): store the authoritative
patch/mod source and a `gameplay-application-record` in the existing game-logic
project store and register them in `artifacts/manifest.json`. When a retained
artifact consumes a finding that exists in the current project store, record that
dependency through `consumes_finding_refs`, never `finding_refs`; application
artifacts are not evidence for the mechanic they consume. Record the
original/control state or a registered backup before destructive modification so
a later session can reconstruct rollback without conversational memory.

Installed game files remain read-only unless destructive modification was
explicitly authorized.

## Validate the intended scope

Follow the application validation rules in `SKILL.md`. Compare control and
modified behavior and exercise only the edge cases that can reveal scope leakage:
other actors/sides, alternate event sources, pause/death/loading, scene
transitions, save/reload, or difficulty/state variants.

A successful change in one scenario establishes only that scenario until the
claimed ownership/fan-out scope is also evidenced. If the modified behavior
contradicts the recovered mechanic model rather than merely the intended change,
return the discrepancy to `$analyze-game-logic` instead of adding ad hoc
filters.
