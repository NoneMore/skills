# Native Runtime Delivery

Load this reference for retained native runtime mechanisms that write process memory or install/replace executable code. Gameplay mechanism selection remains owned by `change-design.md`; native locator policy remains owned by the main Skill.

## Guard mutation

For code/instruction replacement, verify the expected original bytes before mutation.

For mutable runtime data, guard only preconditions material to a safe, semantically correct write, such as an expected current value when the operation depends on it, pointer validity, object lifetime, or container identity. Do not require an exact prior value merely because the write is retained.

If a material precondition fails, refuse the mutation rather than broadening compatibility, substituting a nearby site, or weakening the guard.

## Preserve and restore the machine contract

Injected/replaced code must preserve the material surrounding contract: complete instruction boundaries, overwritten semantics, return state, required registers/flags, floating-point or vector state, and stack balance when relevant. Prefer symbolic or site-relative control-flow destinations when they avoid re-encoding an address.

Disable/rollback must restore the documented original code or mutable state and release mechanism-owned resources where applicable. State explicitly when gameplay state already produced while active cannot be undone.

## Validate the retained implementation

Validate the exact retained implementation, not only an equivalent prototype, harness, or alternate runtime representation. Keep runtime-surface acceptance, injected-logic execution, target behavior, and broader lifecycle coverage as distinct claims, using the cheapest direct evidence for each.

For nontrivial injected control flow, execute the material branches required by the claim. Verify machine-contract invariants with static/disassembly or assembler evidence when that directly proves the property; require runtime evidence only for properties that depend on live execution.

A simple data edit needs no injected code or synthetic execution harness when direct target comparison is sufficient. If required validation is unavailable, name the gap and limit the completion claim accordingly.
