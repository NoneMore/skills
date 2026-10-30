# Reusable Game Architecture Knowledge

Use this guidance when the user requests retained material, work spans sessions, or saving understanding/evidence avoids meaningful future recovery cost or loss. An unrequested one-off answer needs no persistent artifact system.

## Preserve what helps the next investigation

Architecture notes should communicate material understanding rather than serve as a result database. They may be maintained overviews or build-scoped historical notes. Record only the parts material to re-understanding or re-finding a mechanic:

- system/module boundaries, ownership, authority, and how components interact;
- recognizable function entry shapes and surrounding calls, data access patterns, meaningful constants, and variable/field roles;
- state machines, event sequences, data flow, and semantic rules, using compact diagrams or pseudocode when clearer;
- decisive observations, confidence/limitations, a few discriminating checks, and how to repeat verification;
- build/version scope and, if useful, exact addresses, hashes, or locators **clearly marked as build-specific**.

Choose an explanation suited to the mechanism; this is guidance, not a required template or schema. Avoid exhaustive call inventories, raw decompiler dumps, or line-by-line annotations as the long-lived overview. Maintain code-local annotations in the existing analysis workspace rather than duplicating them without benefit.

## Retain evidence without maintenance obligations

Decide whether evidence is worth keeping separately from whether it needs to be maintained. A decompilation slice, trace, or captured tool result can remain a build-scoped snapshot, kept solely for future reading; saving it does not require normalization, registration, synchronization, or routine updates. Living architecture notes may be revised when new understanding makes that useful, but do not silently rewrite historical evidence.

An explicit request to save material is sufficient even when it is cheap to regenerate; retain what the user requested without adding bookkeeping. Otherwise, length or truncation alone does not justify saving raw output: recover cheaply retrievable material on demand, but retain valuable evidence when reconstruction requires repeated partial reads, expensive setup, lossy tool state, or nontrivial work. Keep the requested material or the relevant captured ranges/consolidated evidence as appropriate. Identify the target/build, the covered ranges and any gaps, and how to interpret the capture; never present partial coverage as complete. A retained snapshot is not proof that its claims hold in a later build.

## Reuse across versions

An old architecture note is a map for rediscovery, **not evidence that the new version behaves identically**. Start from structural/semantic recognition clues, identify the current implementation, and revalidate the specific relations that affect the task. Addresses, byte patterns, layout offsets, and even apparent function roles may drift. Leave build-scoped historical notes and evidence snapshots unchanged; report material differences and unresolved relations in the current result. Only when an overview is actively being maintained should new evidence lead to a targeted revision. Reading or revalidating old material does not itself require updating it.

## Keep storage ordinary

Prefer existing project documentation for a maintained overview; otherwise, a few small notes or evidence files in an authorized location outside the installed game are sufficient. Tool-generated working outputs may be overwritten or deleted on rerun: preserve any material meant for later passive reading outside helper-managed cleanup paths while it is still available. No directory convention, project-store manifest, IDs, registration graph, hashes of every output, migrations, or bootstrap step is required. Report retained files' locations and material target/build and coverage scope (including gaps) so a later session can find and interpret them; a pointer in existing project documentation is optional.

Legacy stores can be read as historical material if present but are neither required nor automatically migrated or overwritten. A later agent should be able to understand the system, find candidate implementation paths, see uncertainty, and know what to verify without relying on chat history.
