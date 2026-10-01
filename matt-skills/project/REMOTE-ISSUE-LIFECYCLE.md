# Remote Issue Lifecycle

## Problem

The remote issue tracker workflow currently models task creation and closure well, but the final resolution phase is underspecified.

Closing a GitHub issue is not always equivalent to resolving an agent task. An issue may be closed because it is completed, duplicated, declined, or moved elsewhere. For agent workflows we need an explicit resolution artifact before closure.

## Proposed lifecycle

Remote issues should expose the following logical states:

```
open -> triaged -> in-progress -> resolved -> closed
```

These states can be represented using existing remote tracker primitives:

- `open`: GitHub issue state
- `triaged`: labels or project fields
- `in-progress`: assignment plus working label
- `resolved`: resolution label and a resolution comment
- `closed`: native issue close operation

## Resolution contract

Before closing a remote issue, the agent should create a final resolution record containing:

```md
## Resolution

What changed and how the issue was addressed.

## Decision

Important tradeoffs or rejected alternatives.

## Verification

How the result was checked.
```

The resolution comment becomes the durable artifact that local issue files currently provide naturally.

## Why not only use `closed`?

`closed` is a transport-level tracker state, not a semantic completion state. Keeping resolution separate allows agents and humans to distinguish:

- completed work
- intentionally not planned work
- duplicate reports
- unresolved conversations

## Future implementation

The remote tracker adapter should add a `resolve` operation that:

1. validates a resolution artifact exists;
2. records the resolution in the issue conversation;
3. applies a resolved marker;
4. optionally closes the issue.

This keeps remote and local trackers aligned while preserving their different storage models.
