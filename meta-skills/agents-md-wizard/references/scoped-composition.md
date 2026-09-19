# Scoped composition

Use this reference only when the active harness or governing context establishes broader+narrower instruction composition and the inline four-way model is not enough.

## Resolve the effective chain

Before local interviewing or drafting:

1. identify the exact target scope;
2. resolve which broader and local artifacts are applicable and in what order;
3. read the applicable chain from broadest to nearest scope as required by the harness;
4. summarize the effective inherited contract relevant to the target;
5. inspect the local scope for durable behavioral differences.

Do not infer this chain from directory nesting alone, and do not ask the user to restate a broader rule you can read.

## Treat a local file as a delta

Under overlay composition:

```text
broader effective contract + local delta = local effective contract
```

Classify every local candidate:

- **inherit** — unchanged broader behavior; omit it locally;
- **extend** — add behavior needed only here;
- **narrow** — specialize a broader rule without changing its purpose;
- **override** — intentionally replace broader behavior for this scope.

If a candidate cannot be classified, it is probably background information rather than a local instruction.

A useful local file may be only a few lines. Avoid shadow copies of workspace-wide mission, shared validation, style guidance, or lifecycle rules that still apply unchanged.

## Overrides

For an override, identify the exact broader behavior being changed and the grounded reason this scope differs. Write the positive local behavior, not a vague exception such as “the parent rule does not apply.”

Ask a separate policy question when the desired local behavior remains ambiguous. If maintained workspace evidence clearly establishes the divergence, present it as an evidenced recommendation in the ordinary pre-write review; do not write the override until the user approves the proposal.

## Refresh and drift

A local refresh must consider both:

- **local drift** — the subtree changed;
- **broader drift** — an ancestor rule changed, making local text redundant, conflicting, or misplaced.

Re-read the applicable chain and classify existing local lines as: still-needed local delta; now inherited and removable; stale; conflicting; or better promoted to a broader scope.

Scoped authoring is complete when every local line changes behavior specifically in that scope, unchanged broader policy is not duplicated, intentional overrides are explicit and grounded, and the composed instructions form one coherent effective contract.
