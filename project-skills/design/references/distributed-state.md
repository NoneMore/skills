# Distributed state

Use this guidance when authoritative state, replicas, caches, messages, or concurrent writers cross a process or asynchronous boundary. This lens owns correctness semantics across independent state and ordering boundaries; use [reliability.md](reliability.md) when the primary question is service behavior under failure, and [operability.md](operability.md) when the primary question is human or tooling intervention.

## Establish ownership and guarantees

Before choosing replication, queues, caches, or coordination mechanisms, identify the authoritative owner of each material fact. A cache, index, replica, or event stream is not a source of truth merely because it stores data. If multiple writers can be authoritative, define the conflict semantics rather than letting the topology decide them accidentally.

Describe guarantees in domain terms: which reads may be stale, which writes may race, what ordering matters, which duplicates or losses are possible, and which invariants cross boundaries. Labels such as "eventual consistency" are not substitutes for the behavior callers must understand.

## Design divergence and reconciliation

Assume asynchronous copies can diverge. When divergence matters, decide how it is detected, which side wins or how conflicts are resolved, and how repair occurs. Idempotency, deduplication, compensation, and stronger coordination earn their cost only where the corresponding duplicate, partial-execution, or conflict risk is real.

Make message semantics explicit when they affect behavior: a durable fact, a request to act, and a best-effort notification imply different ownership and recovery expectations. Do not infer guarantees from the transport that the domain has not actually chosen.

Choose infrastructure after the required ownership and consistency semantics are clear enough to evaluate it.
