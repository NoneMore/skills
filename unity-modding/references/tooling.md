# Tool Selection

Prefer an existing, version-identifiable tool over a custom parser. Use a custom parser only after existing tools cannot answer the bounded question, the failure is recorded, and the user accepts the extra implementation scope.

## Discover tools first

1. Inventory project-local tools, installed commands, global .NET tools, debugger integrations, and loader-provided outputs.
2. Capture `--version`, assembly/file version, release tag, or commit. Do not record only a product name.
3. Check the tool against the exact Unity, loader, backend, OS, and architecture fingerprint.
4. If the user asks to find a tool, consult its official documentation or repository before writing code or guessing flags.
5. Apply the asset gate before downloading or installing. Information lookup alone is not acquisition.

Record the selected tool, version, relevant invocation/configuration, input hashes, output path, and limitations in the versioned analysis record.

## Preserve expensive analysis

Choose a persistent analysis root outside the mod repository before importing or generating assets. Follow the user's existing workspace layout; otherwise propose a location and include the game/build fingerprint and tool version in its path. Keep Ghidra projects, decompiler databases, metadata exports, generated wrappers, address/symbol maps, and reusable analysis utilities there. They are reusable evidence, not temporary files.

Use an OS temporary directory only for downloads awaiting validation, unpacking, transient conversion files, and isolated experiments that are cheap to reproduce. If a scratch result becomes useful, move or regenerate it in the persistent analysis root and update the analysis record before ending the task. Never delete the only useful analysis copy during cleanup.

## Integrate Ghidra with an Agent

Use a persistent Ghidra project as the source of analysis state. Prefer this stack, in order:

1. Use Ghidra's `analyzeHeadless` for deterministic import, initial auto-analysis, and repeatable pre/post scripts.
2. Use official PyGhidra as the stable automation layer for opening the persistent project, running bounded analysis, and accessing the Ghidra API from CPython.
3. Use a pinned, approved Ghidra MCP implementation only as an optional structured Agent interface. Do not require GUI automation or bind the workflow to one community MCP implementation.

Prefer high-level, bounded operations such as resolving a function by name/token/RVA, decompiling one function, returning callers/callees/xrefs/P-code, reading types, batching compact function context, and exporting evidence. Do not stream a whole-program decompilation into model context.

Keep MCP read-only by default. Require explicit task authority for renames, type changes, comments, imports, patches, or script execution; apply state changes in transactions when supported and record the before/after values. Bind local integrations to stdio or loopback only unless the user explicitly authorizes and secures remote access. Restrict exposed tools with allowlists or lazy loading rather than presenting a broad arbitrary-script surface.

Make every response identify the open program and analysis state: native input hash, build ID, Ghidra version, project path, program name/address space, image base, and relevant metadata/importer or script versions. Reject a request when its expected fingerprint differs from the open project. Treat metadata-derived IL2CPP names, types, and addresses as candidate annotations until representative entries agree with the native listing or runtime evidence.

Record MCP/PyGhidra implementation and version, transport, endpoint scope, allowed write capabilities, project persistence, and mutation log location in the analysis record. Avoid MCP modes that discard the only project at session end; if a tool defaults to ephemeral projects, configure a persistent destination or export/promote the useful project before shutdown.

## Route by question

| Question | Prefer | Guardrail |
| --- | --- | --- |
| Browse managed or loader-generated interop types, methods, tokens, overloads, and parameter names | An already installed ILSpy GUI or `ilspycmd`, or another trusted metadata browser already used by the project | Treat generated interop as a signature surface, not a managed implementation body. Do not load untrusted target assemblies merely to enumerate metadata. |
| Inspect IL2CPP native method bodies, data flow, cross-references, or control flow, especially for recent Unity builds | A version-pinned persistent Ghidra project imported from the exact native binary, automated through `analyzeHeadless` or PyGhidra; add metadata-derived names/types with a compatible loader or script | Prefer this route for native analysis. Record image base, import settings, processor/language, scripts/extensions and versions, input hashes, and analysis options. Use an approved MCP for bounded Agent queries when available. Keep the Ghidra project outside source control but do not treat it as disposable. |
| Recover IL2CPP metadata, approximate managed structure, or method mappings when exact-version compatibility is demonstrated | A pinned Cpp2IL release and its documented output formats | Treat Cpp2IL as an optional metadata/structure aid, not the default native decompiler. Recent Unity/metadata formats may be unsupported or partially supported; a successful run or generated assembly alone is not proof of correct method bodies, mappings, or cross-references. Validate representative outputs against metadata, Ghidra, or runtime evidence. |
| Generate address maps or Ghidra/debugger scaffolding when a compatible exporter is available | A version-compatible Il2CppInspector or other approved metadata tool | Treat every exporter as compatibility-sensitive; verify the exact Unity/metadata version and validate representative addresses before relying on bulk output. |
| Observe a native call stack or live control flow | The debugger already available to the user, with symbols/address maps generated by an approved tool | Do not implement an in-plugin stack walker for a one-off diagnostic unless the debugger cannot answer the bounded question and reusable runtime stack capture is itself requested. |
| Inspect exact loader bootstrap and lifecycle APIs | The installed loader assemblies, templates, and version-matched official documentation | Do not copy an example from another loader major or backend. |

Primary project sources:

- ILSpy and `ilspycmd`: <https://github.com/icsharpcode/ILSpy>
- Ghidra: <https://github.com/NationalSecurityAgency/ghidra>
- PyGhidra: <https://github.com/NationalSecurityAgency/ghidra/tree/master/Ghidra/Features/PyGhidra>
- Cpp2IL: <https://github.com/SamboyCoding/Cpp2IL>
- Il2CppInspector: <https://github.com/djkaty/Il2CppInspector>

## Stop unproductive exploration

Before crossing from wrapper-level inspection into native analysis, state:

- the exact unanswered question;
- why current evidence and existing tools cannot answer it;
- the minimum additional artifact or tool output needed;
- the fallback if the attempt fails.

After two incompatible or failed approaches to the same subproblem, stop. Record them as rejected approaches, present the remaining tool/acquisition choices, and continue only work that is still independently useful.
