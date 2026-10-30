# Reusable Game Architecture Knowledge

Use this guidance only when the user requests retained knowledge, the work already spans sessions, or the recovered understanding/evidence would be costly or lossy to reconstruct. A one-off answer needs no persistent artifact system.

## Preserve what helps the next investigation

Treat notes like ordinary architecture documentation, not an immutable result database. Record only the parts material to re-understanding or re-finding a mechanic:

- system/module boundaries, ownership, authority, and how components interact;
- recognizable function entry shapes and surrounding calls, data access patterns, meaningful constants, and variable/field roles;
- state machines, event sequences, data flow, and semantic rules, using compact diagrams or pseudocode when clearer;
- decisive observations, confidence/limitations, a few discriminating checks, and how to repeat verification;
- build/version scope and, if useful, exact addresses, hashes, or locators **clearly marked as build-specific**.

Choose an explanation suited to the mechanism; this is guidance, not a required template or schema. Avoid exhaustive call inventories, raw decompiler dumps, or line-by-line annotations as the long-lived overview. Maintain code-local annotations in the existing analysis workspace rather than duplicating them without benefit.

## Retain evidence without maintenance obligations

Decide whether evidence is worth keeping separately from whether it needs to be maintained. A decompilation slice, trace, or captured tool result can remain a build-scoped snapshot, kept solely for future reading; saving it does not require normalization, registration, synchronization, or routine updates. Living architecture notes may be revised when new understanding makes that useful, but do not silently rewrite historical evidence.

Length or truncation alone does not justify saving raw output. If a material range can be retrieved cheaply again, recover it on demand. If recovering it required repeated partial reads, expensive setup, lossy tool state, or nontrivial reconstruction, retain only the relevant captured ranges or consolidated evidence. Keep enough context to identify the target/build, the covered ranges and any gaps, and how to interpret the capture; never present partial coverage as complete. A retained snapshot is not proof that its claims hold in a later build.

## Reuse across versions

An old architecture note is a map for rediscovery, **not evidence that the new version behaves identically**. Start from structural/semantic recognition clues, identify the current implementation, and revalidate the specific relations that affect the task. Addresses, byte patterns, layout offsets, and even apparent function roles may drift. If the architecture changes, correct the affected explanation and mark unresolved differences rather than silently carrying forward a previous conclusion.

## Keep storage ordinary

Prefer an existing project document; otherwise, one or a few small Markdown notes in an authorized working location outside the installed game are sufficient. Do not require a directory convention, manifest, IDs, links, hashes of every output, migrations, or a bootstrap step. Retain costly or lossy traces, extracted material, and reusable scripts only when their expected reuse earns the cost, with enough context to interpret them later.

Legacy stores can be read as historical material if present but are neither required nor automatically migrated or overwritten. A later agent should be able to understand the system, find candidate implementation paths, see uncertainty, and know what to verify without relying on chat history.
