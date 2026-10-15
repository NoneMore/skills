# Lean Profiling

Use when a Lean file, declaration, or tactic is materially slow and the source of cost is not already clear.

## Narrow the measurement

Prefer the smallest profile that can distinguish candidate causes:

- one theorem/tactic region;
- one module/target;
- one trace class such as simplification, typeclass synthesis, elaboration, or compiler specialization.

Whole-project timing is useful for regression impact but poor for locating a proof hotspot.

## Lean profiler/traces

The active Lean toolchain provides profiler and trace options that can attribute expensive elaboration work. Option names and output formats can evolve, so verify them against the installed version before scripting around them.

When supported, compare wall-clock information with heartbeats or other deterministic work counters to separate machine noise from elaboration complexity.

## Workflow

1. reproduce the slowdown on a focused target;
2. record a baseline;
3. enable the narrowest useful profile/trace;
4. identify the dominant tactic, reduction, or synthesis region;
5. apply one targeted change from [performance-optimization.md](performance-optimization.md);
6. rerun the same measurement and semantic verification gate.

Record enough of the baseline and after-state to justify that the optimization helped the requested property. Do not infer a performance win solely from fewer source lines.
