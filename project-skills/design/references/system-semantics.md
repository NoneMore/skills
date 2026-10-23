# System semantics and boundaries

Use this guidance when failure behavior, cross-boundary state, production intervention, or trust and authority can change a material design decision. These are complementary lenses, not requirements to introduce mechanisms in every area; focus on the consequences relevant to the problem.

## State ownership and reconciliation

### Establish ownership and guarantees

Before choosing replication, queues, caches, or coordination mechanisms, identify the authoritative owner of each material fact. A cache, index, replica, or event stream is not a source of truth merely because it stores data. If multiple writers can be authoritative, define the conflict semantics rather than letting the topology decide them accidentally.

Describe guarantees in domain terms: which reads may be stale, which writes may race, what ordering matters, which duplicates or losses are possible, and which invariants cross boundaries. Labels such as "eventual consistency" are not substitutes for the behavior callers must understand.

### Design divergence and reconciliation

Assume asynchronous copies can diverge. When divergence matters, decide how it is detected, which side wins or how conflicts are resolved, and how repair occurs. Idempotency, deduplication, compensation, and stronger coordination earn their cost only where the corresponding duplicate, partial-execution, or conflict risk is real.

Make message semantics explicit when they affect behavior: a durable fact, a request to act, and a best-effort notification imply different ownership and recovery expectations. Do not infer guarantees from the transport that the domain has not actually chosen.

Choose infrastructure after the required ownership and consistency semantics are clear enough to evaluate it.

## Failure behavior and recovery

### Start from failure assumptions

Model the failures whose consequences matter before choosing mechanisms. For each material failure, establish what becomes unavailable, slow, partitioned, duplicated, reordered, or corrupted; how the failure becomes observable; the blast radius and invariants that must still hold; what useful behavior can continue; and how recovery occurs.

Do not require a system to survive every imaginable failure. Redundancy, retries, failover, and degradation paths earn their complexity only when they contain a plausible failure with material consequences.

### Make recovery semantics explicit

Retries are safe only when repeated execution is acceptable or duplicate effects are prevented. Timeouts and retry budgets should bound work rather than amplify an unhealthy dependency. Redundancy improves reliability only when the redundant paths do not share the failure that matters.

Prefer graceful degradation when reduced service can preserve important invariants. If recovery can lose, duplicate, or reorder state, make that consequence explicit and examine state ownership and consistency when these become material design questions.

Reliability targets such as RTO, RPO, or availability matter when they constrain the design; do not invent them as ceremony.

## Operational diagnosis and intervention

### Treat operations as an interface

Operators and support tooling are callers with real information needs. Important failures should expose enough evidence to identify the violated behavior and responsible boundary without requiring global system knowledge. Prefer telemetry tied to meaningful invariants, state transitions, and service behavior over exhaustive instrumentation whose diagnostic value is unclear.

Keep diagnostic and administrative interfaces narrow and internal unless ordinary callers genuinely need them. Do not enlarge a public interface merely to make production debugging convenient.

### Design repair, not only detection

For failures that plausibly require intervention, establish the smallest safe repair surface that the consequences justify. Actions such as drain, replay, reconcile, disable, inspect, or backfill should have bounded scope and clear safety semantics when they are needed, rather than existing as a generic control plane by default.

Favor locality: evidence, controls, and operational ownership should remain near the component or domain boundary that can explain the behavior. If a common incident requires coordinated manual edits across unrelated parts of the system, treat that spread as a design signal.

Operational machinery earns its cost by reducing a concrete diagnosis or recovery burden, not merely because future operations are imaginable.

## Trust and authority boundaries

### Model authority explicitly

Identify the principals, protected resources, trust boundaries, and which component may act on whose behalf. Separate authentication from authorization, and place enforcement where the information needed to decide is authoritative and bypass can be controlled.

Treat network location or an "internal" service label as a deployment fact, not a sufficient trust model. Cross-tenant, cross-privilege, or delegated operations deserve explicit isolation and authority semantics when their failure would be material.

### Minimize and contain trust

Give components only the authority their responsibilities require, and avoid propagating secrets or ambient credentials beyond the boundary that uses them. Validate untrusted input before it can influence privileged or durable state. Preserve an audit trail where accountability for a material action or decision matters.

Security mechanisms earn their complexity by containing a plausible threat with material consequences; do not stack defensive layers solely because an attack is imaginable. When agents or automation are involved, instructions and prompt text are not authorization boundaries: enforce permissions at the runtime, tool, or resource boundary that controls the action.
