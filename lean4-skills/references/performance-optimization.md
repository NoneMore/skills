# Lean Performance Optimization

Use when elaboration, tactic execution, or builds are materially slow. Measure or localize the cost before changing code; a merely long-looking proof is not automatically a performance problem.

## Diagnose first

Determine whether the cost is primarily:

- broad simplification or proof search;
- typeclass synthesis;
- definitional reduction / unification of large terms;
- one expensive tactic or theorem application;
- repeated elaboration of the same complex expression;
- project/build scope rather than the proof itself.

Use available profiling facilities or focused timing/traces when the source of cost is unclear. See [profiling-workflows.md](profiling-workflows.md).

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

## Optimization loop

1. establish a verified baseline;
2. localize the cost;
3. change one mechanism;
4. re-measure and re-verify;
5. keep the change only if it improves the requested performance property without unacceptable readability/API cost.

Do not raise heartbeat/recursion limits until you know the work is legitimate and restructuring is not the better fix.
