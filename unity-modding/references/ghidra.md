# Deep Ghidra Analysis

Read this reference only after [tooling.md](tooling.md) permits deep-level escalation and the versioned analysis record contains the unanswered question, intermediate result or incompatibility, and escalation reason.

## Build the annotated persistent project

Use a persistent Ghidra project as the source of analysis state. Import the exact native binary and apply a version-compatible Il2CppInspectorRedux Ghidra export—script, metadata/address map, and type header or the equivalent companion files emitted by the pinned release—to the exact native/metadata pair. Validate representative names and addresses against the native listing before trusting the bulk import.

Record the native and metadata hashes, build ID, Ghidra version, project path, program name/address space, image base, import settings, processor/language, analysis options, and Il2CppInspectorRedux/export versions. Reject work when the expected fingerprint differs from the open project. Treat imported names, types, and addresses as candidate annotations until representative entries agree with native listing or runtime evidence.

## Integrate Ghidra with an Agent

Prefer this automation stack, in order:

1. Use Ghidra's `analyzeHeadless` for deterministic import, initial auto-analysis, and repeatable pre/post scripts.
2. Use official PyGhidra as the stable automation layer for opening the persistent project, running bounded analysis, and accessing the Ghidra API from CPython.
3. Use a pinned, approved Ghidra MCP implementation only as an optional structured Agent interface. Do not require GUI automation or bind the workflow to one community MCP implementation.

Prefer high-level, bounded operations such as resolving a function by name/token/RVA, decompiling one function, returning callers/callees/xrefs/P-code, reading types, batching compact function context, and exporting evidence. Do not stream a whole-program decompilation into model context.

Keep MCP read-only by default. Require explicit task authority for renames, type changes, comments, imports, patches, or script execution; apply state changes in transactions when supported and record the before/after values. Bind local integrations to stdio or loopback only unless the user explicitly authorizes and secures remote access. Restrict exposed tools with allowlists or lazy loading rather than presenting a broad arbitrary-script surface.

Record the MCP/PyGhidra implementation and version, transport, endpoint scope, allowed write capabilities, project persistence, and mutation log location. Avoid modes that discard the only project at session end; configure a persistent destination or export/promote the useful project before shutdown.

Primary project sources:

- Ghidra: <https://github.com/NationalSecurityAgency/ghidra>
- PyGhidra: <https://github.com/NationalSecurityAgency/ghidra/tree/master/Ghidra/Features/PyGhidra>
- Il2CppInspectorRedux: <https://github.com/LukeFZ/Il2CppInspectorRedux>
