# Reliability design

Use this guidance when failure behavior, recovery, availability, or degradation can materially change the design. This lens owns how system behavior should remain bounded under failure; use [distributed-state.md](distributed-state.md) when the core question becomes correctness across independent state or ordering boundaries, and [operability.md](operability.md) when recovery depends on operator diagnosis or control.

## Start from failure assumptions

Model the failures whose consequences matter before choosing mechanisms. For each material failure, establish what becomes unavailable, slow, partitioned, duplicated, reordered, or corrupted; how the failure becomes observable; the blast radius and invariants that must still hold; what useful behavior can continue; and how recovery occurs.

Do not require a system to survive every imaginable failure. Redundancy, retries, failover, and degradation paths earn their complexity only when they contain a plausible failure with material consequences.

## Make recovery semantics explicit

Retries are safe only when repeated execution is acceptable or duplicate effects are prevented. Timeouts and retry budgets should bound work rather than amplify an unhealthy dependency. Redundancy improves reliability only when the redundant paths do not share the failure that matters.

Prefer graceful degradation when reduced service can preserve important invariants. If recovery can lose, duplicate, or reorder state, make that consequence explicit and use [distributed-state.md](distributed-state.md) when ownership or consistency becomes the real design question.

Reliability targets such as RTO, RPO, or availability matter when they constrain the design; do not invent them as ceremony.
