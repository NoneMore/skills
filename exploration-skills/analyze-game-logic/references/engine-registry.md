# Engine Adapter Registry

Use this registry only after the implementation boundary has been detected from
evidence. Load a single matching adapter when possible; do not preload unrelated
engine references.

| Detected boundary | Adapter | Optional bundled tooling | Status |
| --- | --- | --- | --- |
| GameMaker YYC | [engine-gamemaker-yyc.md](engine-gamemaker-yyc.md) | `scripts/yyc_triage.py` | bundled |
| GameMaker VM | none | none | core workflow only |
| Unity Mono | none | none | core workflow only |
| Unity IL2CPP | none | none | core workflow only |
| Unreal native code | none | none | core workflow only |
| Web / JavaScript bundle or local Node.js logic | [engine-web-javascript.md](engine-web-javascript.md) | `scripts/web_js_triage.py` | bundled |
| Other embedded/custom runtime | none | none | core workflow only |

## Adding an adapter

Engine knowledge is an extension of the core protocol, not a new core workflow.
To add support for another engine/runtime boundary:

1. Copy the structure in
   [engine-adapter-contract.md](engine-adapter-contract.md) into a new focused
   file named `engine-<engine-or-boundary>.md`.
2. Add one row to this registry describing the detection boundary, adapter, and
   optional bundled tool.
3. Add deterministic helper scripts under `scripts/` only when they automate
   repeatable mechanical triage. Keep interpretation and version-sensitive
   knowledge in the adapter.
4. Do not add engine-specific ABI, layout, metadata, naming, or tooling rules to
   `SKILL.md` unless they are genuinely cross-engine invariants.
5. Keep adapter links shallow: adapters may link to focused supporting references,
   but avoid deep reference chains.

A new adapter should be removable without changing the meaning of the core
workflow. If adding an engine requires broad edits to `SKILL.md`, first check
whether engine-specific knowledge has leaked into the core protocol.
