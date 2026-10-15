# Lean Compiler Internals

Use when the task concerns compiler attributes, specialization, generated code, or compiler-pass behavior. These APIs can drift across Lean versions; verify names and option availability against the active toolchain before making compatibility claims.

## Optimization attributes

Prefer source/algorithmic improvements before compiler knobs.

- `@[inline]`, related inline controls, and specialization attributes can affect generated code and compile time; use them only with an observed reason.
- `@[csimp]` is proof-backed replacement: the rewrite theorem is part of the trust story.
- `@[implemented_by ...]` selects a compiled implementation without proving equivalence to the logical definition. Treat it as a trusted-code boundary and test runtime behavior explicitly.

Do not describe an unsafe compiled implementation as logically certified merely because the wrapper theorem or definition elaborates.

## Diagnostics

When investigating specialization or compiler passes:

1. establish a baseline;
2. enable the narrowest relevant compiler trace/options supported by the toolchain;
3. change one attribute/pass boundary;
4. compare generated/compiler behavior;
5. retain the change only when the intended effect is observed.

For ordinary proof elaboration slowness, start with [performance-optimization.md](performance-optimization.md) rather than compiler internals.

## Custom passes

Compiler-pass APIs are advanced and version-sensitive. Keep pass installation local and narrowly scoped during experiments, validate phase assumptions, and run type/invariant checks supported by the active compiler before broadening a transformation.

Prefer current Lean source/reference documentation over cached API spellings when a compiler-internal name is uncertain.
