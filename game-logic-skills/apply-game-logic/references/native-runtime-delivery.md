# Native Runtime Delivery

Load this reference for retained native runtime mechanisms that write process memory or install/replace executable code. For gameplay changes, it complements `change-design.md`. It does not replace mechanic recovery, the main Skill's locator policy, or durable application provenance.

## Fail closed on material assumptions

Use the native locator and target-version rules from the main Skill. Prefer symbolic or site-relative destinations inside the retained implementation when they avoid re-encoding an address.

A retained runtime mutation should also verify the material state assumptions that make the write or hook safe, such as expected original bytes/value/state and pointer, object-lifetime, or container assumptions before dereference.

Refuse to mutate when a material target, locator, or original-state assumption no longer matches. Do not broaden compatibility merely because a locator happens to resolve on another build.

## Preserve the machine contract

For injected code or instruction replacement, preserve the behavior the surrounding code still relies on.

Check the material invariants for the hook site, including complete instruction boundaries, replay of overwritten semantics, correct return state, required registers and flags, floating-point/vector state, stack balance, and shared-state ownership when relevant.

Do not add a dynamic hook merely because the runtime surface makes one convenient. Use the smallest mechanism that preserves the requested behavioral scope.

## Treat restoration as implementation

The disable or rollback path is part of a retained runtime mutation. Restore the documented original code or mutable state and release resources owned by the runtime mechanism where applicable.

If disabling the mechanism cannot undo gameplay state already generated while it was active, state that limitation explicitly rather than implying full restoration.

## Match validation to the claim

Validate the exact retained implementation, not only an equivalent prototype, harness, or alternate runtime representation.

Keep implementation/tool acceptance, execution, target behavior, and broader scope/lifecycle evidence distinct. These are checks, not a linear ladder:

- **Implementation check** — the retained implementation is internally consistent, material guards/restoration are present, and the selected runtime surface accepts it when that can be checked directly.
- **Execution check** — nontrivial injected logic is exercised with the material branches and machine-state invariants needed by the claim.
- **Target smoke test** — control, modified, and restored behavior are compared in the supported target build when the claim depends on target behavior.
- **Scope/lifecycle validation** — broader scenario or lifecycle coverage claimed for the artifact is exercised. Existing mechanic evidence may support semantic scope such as ownership or fan-out, but application-level lifecycle claims such as scene transitions, save/reload, or object recreation require application evidence.

Report the checks actually completed and the important gaps. Tool acceptance does not prove hook behavior. Controlled execution does not prove in-game behavior. One target scenario does not prove cross-scenario or cross-build compatibility.

Use the cheapest checks that support the claim. A simple guarded data edit does not need injected code or a synthetic execution harness when direct target comparison is safer and more informative.

For nontrivial injected logic, static or assembler acceptance alone is insufficient: require execution evidence covering every material branch and machine-state invariant needed by the claim. If the required execution or target environment is unavailable, deliver the retained implementation only with the missing validation named explicitly rather than calling the unsupported claim complete.

## Completion

Before calling a retained native runtime delivery complete, verify that:

- the retained locator satisfies the main Skill's native locator policy;
- material target, locator, original-state, and any identified safety-critical runtime assumptions required before mutation or dereference fail closed;
- restoration is implemented for code, mutable state, and mechanism-owned resources where applicable;
- nontrivial injected logic has execution evidence for the material branches and machine-state invariants required by the claim;
- validation applies to the exact retained implementation being delivered;
- any claimed application lifecycle coverage is supported by application-level evidence rather than mechanic evidence alone;
- reported compatibility and validation scope do not exceed the evidence;
- retained artifacts satisfy the normal application provenance and rollback requirements.