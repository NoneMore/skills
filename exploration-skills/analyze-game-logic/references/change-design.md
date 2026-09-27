# Gameplay Change Design

Load this reference only when the user asks to design, apply, or validate a local
offline gameplay change. Analysis remains mechanic-first: establish behavioral
scope before optimizing implementation convenience.

## Establish scope before mechanism

Determine whether the candidate value, object, definition, field, or call path is
shared across actors, sides, event sources, or gameplay contexts. Treat unresolved
ownership/fan-out as **Unknown**. Reversible does not mean narrowly scoped.

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
may be used as scoped analysis techniques when permitted. Document what changes,
where it changes, how it is version-guarded, and how to restore the control state.

## Version and address guards

Bind the change to the exact target version/build/hash. For native interventions,
record stable `module + RVA` locators and verify VA/RVA/file-offset/runtime-address
conversion against the original binary or loaded module before use.

Do not rely on a raw virtual address across launches or builds. If a signature or
pattern is used for relocation, validate that it resolves uniquely and still maps
to the recovered semantic site before applying the change.

## Destructive changes

Before any destructive patch, record:

- exact target file/module hash;
- original bytes or original file content;
- replacement bytes/files;
- file-offset or RVA mapping when applicable;
- expected behavioral effect and known shared-use risks;
- restoration procedure.

Keep the authoritative patch/mod source and provenance in the analysis project.
Installed game files remain read-only unless destructive modification was
explicitly authorized.

## Validate the intended scope

Use [runtime-validation.md](runtime-validation.md) when runtime behavior is
material. Compare control and modified behavior and exercise only the edge cases
that can reveal scope leakage: other actors/sides, alternate event sources,
pause/death/loading, scene transitions, save/reload, or difficulty/state variants.

A successful change in one scenario establishes only that scenario until the
claimed ownership/fan-out scope is also evidenced.
