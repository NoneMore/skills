# Cheat Engine Delivery

Load this reference only when the requested deliverable is a Cheat Engine table or Auto Assembler script, or Cheat Engine has already been selected as the retained runtime-change surface. It complements `change-design.md`; it does not replace mechanic recovery or general application validation.

## Keep one authoritative implementation

When Auto Assembler is material to the change, designate one authoritative script source. That source may live in a standalone file or in the table itself.

If both a standalone script and a `.CT` exist, derive one from the other or verify that the embedded script round-trips exactly. Do not maintain two independent copies of the same implementation.

Use the normal durable-application rules for target identity, consumed mechanic knowledge, validation evidence, and rollback. Do not duplicate that provenance contract here.

## Fail closed on the target

A reusable CE artifact should guard the assumptions that make the mutation safe:

- exact executable/module identity and architecture when material;
- stable module + RVA or a validated unique signature rather than a launch-specific address;
- expected original bytes/value/state before mutation when practical;
- pointer, object-lifetime, or container assumptions before dereference when they affect correctness.

A unique signature is a locator inside the supported evidence scope, not proof of cross-version compatibility. Refuse to enable when a material guard no longer matches.

## Preserve the overwritten machine contract

For injected code or instruction replacement, preserve the behavior the surrounding code still relies on.

Check the material invariants for the hook site, such as complete instruction boundaries, replay of overwritten semantics, correct return address, required registers and flags, floating-point/vector state, stack balance, and shared-state ownership.

Do not add a dynamic hook merely because it is easy to express in CE. Use the smallest mechanism that preserves the requested behavioral scope.

The disable path is part of the implementation. Restore the documented original code or mutable state, unregister symbols, and release owned allocations where applicable. If generated gameplay state cannot be undone by disabling the script, say so explicitly.

## Name the validation level

Keep packaging, assembly, execution, and gameplay validation distinct:

1. **Package check** — the table/script parses, authoritative source is synchronized, and required guards/restoration logic are present.
2. **CE assembly check** — the actual CE assembler accepts the shipped enable/disable implementation.
3. **Synthetic execution** — nontrivial hook logic is exercised in a controlled process or harness, including material branches and machine-state invariants.
4. **Target smoke test** — control and modified behavior are compared in the supported game build.
5. **Scope validation** — broader scenario, scene, save/reload, or other claimed coverage is exercised or already supported by mechanic evidence.

State the highest completed level and the important gaps. Assembly success does not prove hook behavior. Synthetic execution does not prove in-game behavior. One in-game scenario does not prove cross-scenario or cross-build compatibility.

Use the cheapest validation level that can support the claim. A simple guarded data edit does not need a synthetic execution harness when a direct target comparison is safer and more informative.

## Completion

Before calling a reusable CE delivery complete, verify that:

- the requested user-facing table/script exists and its authoritative implementation is identifiable;
- duplicate script representations, if any, are synchronized;
- material target and original-state guards fail closed;
- enable and disable/restoration behavior have been checked at the claimed validation level;
- nontrivial injected logic has enough execution coverage to catch scope leakage or machine-state corruption;
- the reported compatibility and validation scope does not exceed the evidence;
- retained artifacts satisfy the normal application provenance and rollback requirements.
