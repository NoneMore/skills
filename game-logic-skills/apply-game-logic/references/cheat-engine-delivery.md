# Cheat Engine Delivery

Load this reference only when the requested deliverable is a Cheat Engine table or Auto Assembler script, or Cheat Engine has already been selected as the retained runtime-change surface. For gameplay changes, it complements `change-design.md`. It does not replace mechanic recovery or general application validation.

## Keep one authoritative implementation

When Auto Assembler is material to the change, designate one authoritative script source. That source may live in a standalone file or in the table itself.

If both a standalone script and a `.CT` exist, derive one from the other or verify that the embedded script round-trips exactly. Do not maintain two independent copies of the same implementation.

Use the normal durable-application rules for target identity, consumed mechanic knowledge, validation evidence, and rollback. Do not duplicate that provenance contract here.

## Fail closed on the target

A reusable CE artifact should guard the assumptions that make the mutation safe:

- exact executable/module identity and architecture when material;
- the stable native locator required by the main Skill rather than a launch-specific address;
- expected original bytes/value/state before mutation when practical;
- pointer, object-lifetime, or container assumptions before dereference when they affect correctness.

If a unique signature is also used, treat uniqueness only as evidence within the supported target scope, not as proof of cross-version compatibility. Refuse to enable when a material guard no longer matches.

## Preserve the overwritten machine contract

For injected code or instruction replacement, preserve the behavior the surrounding code still relies on.

Check the material invariants for the hook site, such as complete instruction boundaries, replay of overwritten semantics, correct return address, required registers and flags, floating-point/vector state, stack balance, and shared-state ownership.

Do not add a dynamic hook merely because it is easy to express in CE. Use the smallest mechanism that preserves the requested behavioral scope.

The disable path is part of the implementation. Restore the documented original code or mutable state, unregister symbols, and release owned allocations where applicable. If generated gameplay state cannot be undone by disabling the script, say so explicitly.

## Report validation checks

Keep packaging, assembly, execution, and gameplay validation distinct. These are checks, not a linear ladder:

- **Package check** — the table/script parses, authoritative source is synchronized, and required guards/restoration logic are present.
- **CE assembly check** — the actual CE assembler accepts the shipped enable and disable implementation.
- **Synthetic execution** — nontrivial hook logic is exercised in a controlled process or harness, including material branches and machine-state invariants.
- **Target smoke test** — control and modified behavior are compared in the supported game build.
- **Scope/lifecycle validation** — broader scenario or lifecycle coverage claimed for the artifact is exercised. Existing mechanic evidence may support semantic scope such as ownership or fan-out, but application-level lifecycle claims such as scene transitions, save/reload, or object recreation require application evidence.

Report the checks actually completed and the important gaps. Assembly success does not prove hook behavior. Synthetic execution does not prove in-game behavior. One in-game scenario does not prove cross-scenario or cross-build compatibility.

Use the cheapest checks that can support the claim. A simple guarded data edit does not need a synthetic execution harness when a direct target comparison is safer and more informative.

For a shipped Auto Assembler implementation, actual CE must accept both enable and disable paths before calling the reusable artifact complete. For nontrivial injected logic, assembly alone is insufficient: require execution evidence covering the material branches and machine-state invariants needed by the claim. If the required CE or execution environment is unavailable, deliver the artifact as an unvalidated draft and name the missing checks rather than calling it complete.

## Completion

Before calling a reusable CE delivery complete, verify that:

- the requested user-facing table/script exists and its authoritative implementation is identifiable;
- duplicate script representations, if any, are synchronized;
- material target and original-state guards fail closed;
- shipped Auto Assembler enable and disable paths pass the actual CE assembly check;
- nontrivial injected logic exercises every material branch required by the claim and verifies the relevant machine-state invariants;
- any claimed application lifecycle coverage is supported by application-level evidence rather than mechanic evidence alone;
- the reported compatibility and validation scope does not exceed the evidence;
- retained artifacts satisfy the normal application provenance and rollback requirements.
