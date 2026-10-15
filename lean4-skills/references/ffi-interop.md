# Lean FFI Interop

Use for Lean/C/C++ boundaries, external symbols, exported Lean functions, and Lake link configuration. Treat the foreign boundary as an ABI and trust boundary, not merely syntax.

## Direction

- Lean calling foreign code: use the toolchain's `@[extern]` mechanism with an appropriate declaration.
- Foreign code calling Lean: use `@[export]` on a Lean definition intended as an entry point.

Keep boundary modules small so symbol ownership, initialization, and unsafe assumptions remain inspectable.

## ABI discipline

- Match native widths, ownership, calling convention, and pointer/value layout deliberately.
- Borrowed parameters such as `@&` change runtime ownership behavior; keep Lean and foreign prototypes consistent.
- Use C-layout structures only where the active Lean FFI supports the intended representation; avoid assuming arbitrary Lean structures are C-compatible.
- Prefer byte-oriented buffers plus explicit lengths for raw memory boundaries.

Logical verification in Lean does not prove a foreign implementation is memory-safe or behaviorally equivalent. Test the actual compiled boundary.

## Lake integration

Use the project's Lake configuration to build/link required object or library artifacts. Follow the active toolchain's APIs for external libraries and interpreter/precompiled-module support rather than copying stale build snippets blindly.

## Reverse embedding

When a C/C++ host initializes Lean, treat runtime initialization, module initialization order, reference counting/ownership, and shutdown as part of the interface contract. A function that works when called from a Lean executable may still require additional runtime setup when embedded.

## Completion

A delivered FFI change should elaborate, link, and run through the actual boundary exercised by the user. Report any ABI or lifetime assumptions that are not mechanically checked.
