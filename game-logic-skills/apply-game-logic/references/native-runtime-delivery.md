# Native Runtime Delivery

Load this reference for retained native runtime mechanisms that write process memory or install/replace executable code. For gameplay changes, mechanism selection remains owned by `change-design.md`; locator policy remains owned by the main Skill.

## Guard only material mutation assumptions

Use the main Skill's target-version and native-locator rules.

For code or instruction replacement, verify the expected original bytes before mutation so the artifact fails closed when the site has drifted.

For mutable runtime data, verify only the preconditions material to a safe and semantically correct write. These may include an expected current value when the operation depends on it, plus pointer validity, object lifetime, container identity, or comparable runtime assumptions before dereference. Do not require an exact prior value merely because the write is retained.

Refuse to mutate when a material precondition fails. Do not broaden compatibility, substitute a nearby site, or weaken a guard merely to make the mutation proceed.

## Preserve the machine contract

For injected code or instruction replacement, preserve the surrounding behavior that remains part of the contract. Identify the material invariants for the hook site, such as complete instruction boundaries, overwritten semantics, return state, required registers or flags, floating-point/vector state, and stack balance when relevant.

Prefer symbolic or site-relative control-flow destinations when they avoid re-encoding an address.

## Treat restoration as implementation

The disable or rollback path is part of a retained runtime mutation. Restore the documented original code or mutable state and release resources owned by the runtime mechanism where applicable.

If disabling the mechanism cannot undo gameplay state already produced while it was active, state that limitation explicitly.

## Validate the retained implementation

Validate the exact retained implementation rather than only an equivalent prototype, harness, or alternate runtime representation.

Keep runtime-surface acceptance, execution of injected logic, target behavior, and broader lifecycle coverage as distinct claims. Use the cheapest direct evidence that supports each claim instead of manufacturing a validation ladder.

For nontrivial injected control flow, execute the retained implementation across the material branches required by the claim. Verify machine-contract invariants with the evidence best suited to each invariant; static/disassembly or assembler evidence is sufficient when it directly proves the property, while runtime evidence is required for properties that depend on live execution.

A simple guarded data edit does not need injected code or a synthetic execution harness when direct target comparison is sufficient. If a required environment is unavailable, name the missing validation and limit the completion claim accordingly.

## Completion

Before calling a retained native runtime delivery complete, verify that:

- its retained locator follows the main Skill's native locator policy, and any implementation-local symbolic or site-relative form maps unambiguously to that site;
- code/instruction replacement fails closed on unexpected original bytes, while mutable-data writes guard only the runtime preconditions material to safe/correct mutation;
- injected/replaced code preserves the material machine contract;
- restoration and mechanism-owned resource cleanup are implemented where applicable;
- validation exercised the exact retained implementation, including material injected-control-flow branches when present;
- any missing execution, target, or lifecycle evidence is reported as a limitation rather than promoted into a broader claim.
