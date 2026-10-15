# Lean Performance Optimization

Use when proof elaboration, tactic execution, or builds are materially slow. Measure or localize the cost before changing code; a merely long-looking proof is not automatically a performance problem.

## Diagnose first

Determine whether the cost is primarily:

- broad simplification or proof search;
- typeclass synthesis;
- definitional reduction / unification of large terms;
- one expensive tactic or theorem application;
- repeated elaboration of the same complex expression;
- project/build scope rather than the proof itself.

When the source of cost is unclear, profile the smallest target that can distinguish candidate causes: one theorem/tactic region, one module, or one relevant trace class. Verify profiler/trace option names against the active Lean toolchain rather than caching version-specific spellings.

## Common remedies

### Narrow automation

Replace broad automation with the smallest explicit lemma set or solver that closes the intended goal. `simp only [...]` can be useful when a stable small normalization set is known; it is not mechanically superior to every terminal `simp`.

### Make expensive inference explicit

Pin important polymorphic arguments, structures, or instances when repeated inference is the bottleneck. Do this at the smallest useful boundary rather than making every argument explicit.

### Split elaboration boundaries

A small named helper can prevent one giant nested term from forcing Lean to solve all constraints at once. Extract helpers when they create a meaningful checked boundary, not merely to shorten a line.

### Control definitional unfolding

If a large definition is repeatedly unfolded during unification, a deliberately opaque/irreducible boundary or a theorem stated over a stable wrapper can reduce elaboration work. This changes reducibility behavior and should be justified by an observed bottleneck, not used as a default pattern.

### Prefer direct results over repeated search

Replace expensive search tactics with known lemmas once the desired result is identified, especially in hot or repeatedly elaborated code.

## Measurement loop

1. reproduce the slowdown on the smallest useful target;
2. record a baseline;
3. enable the narrowest useful timing/profile/trace when localization is still uncertain;
4. identify the dominant tactic, reduction, or synthesis region;
5. change one mechanism;
6. rerun the same measurement and semantic verification gate;
7. keep the change only if it improves the requested performance property without unacceptable readability/API cost.

When available, compare wall-clock observations with heartbeats or another deterministic work counter to separate machine noise from elaboration complexity. Whole-project timing is useful for regression impact but poor for locating a proof hotspot.

Do not raise heartbeat/recursion limits until you know the work is legitimate and restructuring is not the better fix.
