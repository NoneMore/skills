# Debugging Matrix

Start from the first red layer. Preserve the original signal while testing one variable at a time.

When a row requires an unavailable log, assembly, generated wrapper, decompiler output, metadata file, or native-analysis result, stop at that boundary and repeat the three-option asset check. Continue with existing evidence by default.

## Layered triage

| Signal | Inspect first | Proof of resolution |
| --- | --- | --- |
| Loader never starts | Correct game root, executable, OS/architecture build, bootstrap/proxy files, permissions, launch method | Loader creates a fresh startup log for one cold launch |
| Loader starts; plugin absent | Plugin directory, metadata, backend, target framework, dependency graph, assembly-load exceptions | Loader enumerates the plugin ID and startup marker once |
| `BadImageFormat` or immediate load failure | x86/x64/ARM mismatch, managed/native mix-up, wrong backend package | Minimal plugin loads on the same fingerprint |
| `FileNotFound` / `TypeLoad` / `MissingMethod` | Copied framework DLLs, wrong loader major, wrong Unity/game references, stale package cache | Clean output contains only intended dependencies and loads |
| Target resolves zero or many methods | Full signature, overloads, generic arity, obfuscation, game update, stripping | Resolver logs exactly one evidenced target |
| Hook applies but never fires | Wrong overload/instance, lifecycle timing, inlining, native wrapper mismatch, caller path | Harmless marker fires at the expected action and count |
| IL2CPP wrapper/binding error | Stale generated interop, mismatched metadata/native pair, unsupported generic or conversion | Regenerated wrappers load and target resolves for current hashes |
| Native access violation | ABI/calling convention, hidden parameters, bad address, object/delegate lifetime, wrong thread | Minimal detour survives repeated calls and a cold restart |
| Freeze or runaway recursion | Reentrancy, lock ordering, main-thread blocking, patch calling its own target | Marker proves bounded calls without frame stalls |
| Works once or duplicates after reload | Static state, repeated registration, missing teardown, persistent injected object | Hook count remains one across supported reload/restart paths |
| Feature works but other behavior breaks | Over-broad target, original skipped, mutable shared state, patch ordering | Neighboring behavior passes with the feature enabled |

## Collect a minimal evidence bundle

Use already available evidence first. List unavailable items in the asset check and acquire them only under the selected mode:

- exact game and loader versions;
- backend, OS, and architecture;
- clean loader log from process start through the failure;
- build output with warnings and full exception chain;
- project file and resolved package/reference list;
- target signature plus decompiler or interop evidence;
- IL2CPP native-module and metadata hashes when applicable;
- reproduction steps and expected versus observed marker.

Redact account names, tokens, and unrelated personal paths before sharing logs.

## Run controlled experiments

1. Return to a minimal plugin that only logs startup.
2. Resolve and validate the complete hook manifest without applying a hook.
3. Apply one marker-only hook with feature behavior disabled.
4. Add the smallest feature logic without optimization.
5. Reintroduce additional hooks and integrations one at a time.

Keep each experiment on the same fingerprint. If the fingerprint changes, discard cached conclusions and generated IL2CPP interop inputs.

For shared or global targets, correlate logs to the initiating instance/action and a bounded scope. Disable broad logging after the required event is captured. Do not treat calls from unrelated gameplay systems as evidence for the feature under test.

Keep a hypothesis ledger in the versioned analysis record. Mark direct signals **Observed**, causal explanations **Inferred**, and missing experiments **Pending**. Preserve rejected hypotheses and the evidence that rejected them.

## Build artifact inspection

Inspect the final output directory and archive. Flag:

- Unity or game assemblies copied beside the plugin;
- loader contract assemblies bundled accidentally;
- mixed Harmony/HarmonyX versions;
- architecture-specific native files for another platform;
- symbols or configuration files containing private paths;
- stale DLLs from prior builds.

Accept the artifact only when every file has a named owner and runtime purpose, and its source version, assembly metadata, runtime marker, configuration header, documentation, and artifact name agree.
