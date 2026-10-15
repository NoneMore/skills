# Operability

Use this guidance when production diagnosis, repair, or operational control can materially change the architecture.

## Treat operations as an interface

Operators and support tooling are callers with real information needs. Important failures should expose enough evidence to identify the violated behavior and responsible boundary without requiring global system knowledge. Prefer telemetry tied to meaningful invariants, state transitions, and service behavior over exhaustive instrumentation whose diagnostic value is unclear.

Keep diagnostic and administrative interfaces narrow and internal unless ordinary callers genuinely need them. Do not enlarge a public interface merely to make production debugging convenient.

## Design repair, not only detection

For failures that plausibly require intervention, establish the smallest safe repair surface that the consequences justify. Actions such as drain, replay, reconcile, disable, inspect, or backfill should have bounded scope and clear safety semantics when they are needed, rather than existing as a generic control plane by default.

Favor locality: evidence, controls, and operational ownership should remain near the component or domain boundary that can explain the behavior. If a common incident requires coordinated manual edits across unrelated parts of the system, treat that spread as a design signal.

Operational machinery earns its cost by reducing a concrete diagnosis or recovery burden, not merely because future operations are imaginable.
