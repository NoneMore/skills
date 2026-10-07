# Scoped composition

Use this reference only when the active harness actually composes broader and narrower instruction artifacts and the inline **inherit / extend / narrow / override** model is not enough.

## Resolve the effective chain

Before changing a local artifact:

1. identify the exact target scope;
2. resolve applicable instruction artifacts and their order from the active loader semantics;
3. read the applicable chain from broadest to nearest scope;
4. summarize the inherited contract relevant to the target;
5. inspect the local scope for durable behavioral differences.

Do not infer composition from directory nesting alone, and do not ask the user to restate broader policy that can be read from the effective chain.

## Treat a local file as a delta

Under overlay composition:

```text
broader effective contract + local delta = local effective contract
```

Classify each local candidate:

- **inherit** — broader behavior remains correct; omit it locally;
- **extend** — add behavior needed only here;
- **narrow** — specialize a broader rule without changing its purpose;
- **override** — intentionally replace broader behavior for this scope.

If a candidate cannot be classified, it is probably background information rather than a local instruction.

A useful local artifact may be only a few lines. Do not copy workspace-wide mission, shared validation, style guidance, or lifecycle rules merely for convenience.

## Overrides

For an override, identify the exact broader behavior being changed and the grounded reason this scope differs. Write the positive local behavior rather than a vague exception.

If the desired local behavior is materially ambiguous, ask because the answer changes the effective contract. If maintained project authority clearly establishes the divergence and the user already requested the create/update, encode it without adding a separate approval round.

Never silently replace a still-valid human guardrail with a conflicting local rule that the user did not ask to change.

## Refresh and drift

A local refresh must consider both:

- **local drift** — the subtree changed;
- **broader drift** — an ancestor rule changed, making local text redundant, conflicting, or misplaced.

Re-read the applicable chain and classify existing local lines as still-needed local delta, now inherited, stale, conflicting, or better promoted to a broader scope.

Remove a line that became purely inherited when doing so preserves the effective behavior. Stop for a decision only when the refresh would materially change still-valid policy rather than merely deduplicate it.

Scoped authoring is complete when every local line changes behavior specifically in that scope, unchanged broader policy is not duplicated, intentional overrides are grounded, and the composed instructions form one coherent effective contract.
