# Tool Selection

Prefer an existing, version-identifiable tool over a custom parser. Use the lowest intervention level that can answer the bounded question. Use a custom parser only after the three-level route cannot answer it, the failure is recorded, and the user accepts the extra implementation scope.

## Discover tools first

1. Inventory project-local tools, installed commands, global .NET tools, debugger integrations, and loader-provided outputs.
2. Capture `--version`, assembly/file version, release tag, or commit. Do not record only a product name.
3. Check the tool against the exact Unity, loader, backend, OS, and architecture fingerprint.
4. If the user asks to find a tool, consult its official documentation or repository before writing code or guessing flags.
5. Apply the asset gate before downloading or installing. Information lookup alone is not acquisition.

Record the selected tool, version, relevant invocation/configuration, input hashes, output path, and limitations in the versioned analysis record.

Before invoking `inspect_unity_game.py`, `ilspycmd`, Cpp2IL, Il2CppInspectorRedux, or Ghidra, read the matching command card in [tool-usage.md](tool-usage.md). Run the installed binary's help before copying a command, include every required positional input, and validate the expected artifact after execution. Treat an empty stdout/output directory as a failed or incomplete invocation even when the exit code is zero.

## Use three intervention levels

Repository source and a compatible existing analysis record come before these levels. They are reusable evidence, not a fourth tool level.

| Level | Mono | IL2CPP | What it can prove | Guardrail |
| --- | --- | --- | --- | --- |
| **Shallow** | Use `ilspycmd` on the exact managed game assembly. | Use `ilspycmd` on exact-fingerprint BepInEx-generated interop assemblies or Il2CppInspectorRedux-generated .NET shim/Dummy DLLs; use Il2CppInspectorRedux C# stubs when pointer metadata or a source-shaped index is clearer. | Assemblies, types, fields, properties, method names, overloads, signatures, tokens, and metadata-provided locators. Mono IL can also expose managed method bodies and call sites. | Treat BepInEx interop, shim/Dummy DLLs, and C# stubs as structural/signature surfaces, not IL2CPP managed implementations. Use BepInEx interop assemblies as build references only when they match the installed loader and build pair; keep Redux browse artifacts analysis-only. |
| **Intermediate** | Normally unnecessary because exact Mono assemblies contain managed IL; use only when a separate native component is the bounded target. | Use a version-compatible Cpp2IL recovered IL/IR, mapping, or method output together with the exact `global-metadata.dat` and native/metadata pair. | Candidate method identity, address mapping, basic blocks, calls, constants, and control flow. | Cpp2IL recovery output is reconstructed, not original source or an exact native assembly listing. Keep the native module and metadata as one fingerprinted pair. Record unsupported instructions, failed mappings, and optimizer ambiguity. |
| **Deep** | Use only for a native engine/plugin target that managed IL cannot explain. | Import the exact native binary into a persistent Ghidra project and apply the compatible Il2CppInspectorRedux-generated Ghidra script plus its companion metadata/type files. | Native decompilation, xrefs, callers/callees, data flow, globals, layout, ABI, optimization/inlining effects, and native-detour evidence. | Pin Ghidra and Il2CppInspectorRedux versions and record image base, import/analysis settings, script package, hashes, and representative address validation. Keep the project persistently under the ignored in-project `.assets/<game-version>/ghidra/` directory. |

Treat the levels as serial checkpoints, not a list of tools to prepare in advance. Installed tool availability does not justify escalation. Start shallow even when implementation is the final goal. Escalate only as follows:

1. Move to intermediate when shallow artifacts cannot answer a named IL2CPP method-body, call-order, constant, control-flow, or method-address question and reconstructed Cpp2IL evidence can answer it.
2. Move to deep when intermediate output is absent, incompatible, ambiguous, or insufficient for native xrefs, data flow, ABI, optimization/inlining, or a native detour.
3. Move directly to deep after recording the reason when the requested evidence is inherently an exact native instruction listing or bytes at a validated RVA; do not repeatedly ask Cpp2IL to turn reconstruction output into original disassembly.
4. Stop at the first level that answers the question to the required confidence. Do not generate the next level merely because the tool is available.

At each escalation, add the unanswered question, evidence gap, attempted level/output, and expected proof from the next level to the analysis record.

Before invoking any level, resolve `<mod-project-root>`, choose the Markdown record path from [analysis.md](analysis.md), and copy the template if no compatible record exists. Every execution plan and handoff involving a tool level must explicitly name schema `unity-modding-analysis/v1`, analysis path `<mod-project-root>/analysis/<game-version>/<target-slug>.md`, and asset path `<mod-project-root>/.assets/<game-version>/<tool>/`. Update the record with the current result before escalating or handing off. Raw output directories, screenshots, exports, and analysis databases are analysis assets; they support but never replace the analysis record.

### Gate deep analysis

Do not generate an Il2CppInspectorRedux Ghidra export, create/import a Ghidra project, or include Ghidra as an immediate next action until one of these is recorded:

- the actual Cpp2IL output for the bounded target is incompatible, incomplete, ambiguous, or contradicts the exact metadata mapping;
- Cpp2IL cannot process the exact fingerprint, with the attempted version and failure captured;
- the requested proof inherently requires native xrefs, data flow, globals, layout, ABI, optimization/inlining analysis, or a native detour.
- the requested proof is the exact native assembly or bytes for a mapped method, which Cpp2IL recovered IL/IR and decompiled pseudocode cannot provide.

A request about a candidate branch, constant, direct call, or basic control flow belongs to intermediate analysis first. Mention Ghidra only as a conditional fallback until the intermediate result demonstrates the deep-level need.

## Preserve expensive analysis

Use `<mod-project-root>/.assets/<game-version>/<tool>/` as the persistent location before importing or generating analysis assets. Keep Ghidra projects, decompiler databases, metadata exports, generated wrappers, address/symbol maps, and reusable analysis utilities under the corresponding tool directory. Ensure the Mod project's `.gitignore` excludes `/.assets/`. These files are reusable evidence, not temporary files and not version-controlled analysis.

Use an OS temporary directory only for downloads awaiting validation, unpacking, transient conversion files, and isolated experiments that are cheap to reproduce. If a scratch result becomes useful, move or regenerate it in the in-project `.assets/` tree and update the Markdown analysis before ending the task. Never delete the only useful analysis asset during cleanup.

## Enter deep Ghidra analysis only after the gate

Do not read or apply the Ghidra workflow while shallow or intermediate analysis remains sufficient. After the deep-analysis gate above is satisfied and recorded, read [ghidra.md](ghidra.md). Until then, keep Ghidra and Il2CppInspectorRedux Ghidra exports out of the immediate plan and name them only as a conditional fallback.

## Route common questions

| Question | Level and tool | Guardrail |
| --- | --- | --- |
| Browse Mono types, methods, emitted IL, overloads, or parameter names | Shallow: `ilspycmd` on the exact managed assembly | Record the assembly hash and decompiler version. Avoid bulk decompilation when a type or method is sufficient. |
| Browse IL2CPP types, fields, methods, tokens, overloads, pointer metadata, or parameter names | Shallow: `ilspycmd` on matching BepInEx interop or Il2CppInspectorRedux shim/Dummy DLLs; use Redux C# stubs as needed | These outputs reconstruct structure and locators, not original managed bodies. Do not infer implementation behavior from placeholder bodies. |
| Inspect an IL2CPP method's approximate recovered behavior, constants, calls, or basic control flow | Intermediate: compatible Cpp2IL recovered IL/IR or method output plus exact metadata mappings | Validate representative method identity and address mapping. Mark gaps and unsupported instructions instead of filling them by inference. Do not call reconstructed output original disassembly. |
| Inspect exact IL2CPP native instructions or bytes | Deep: Ghidra Listing at a metadata-validated RVA | Keep the Listing separate from decompiler pseudocode. Record the direct-to-deep reason; do not retry Cpp2IL recovery formats for this representation. |
| Inspect IL2CPP native data flow, cross-references, globals, optimized/inlined behavior, or ABI | Deep: persistent Ghidra project annotated by compatible Il2CppInspectorRedux-generated scripts and companion data | Record all import and analysis state. Validate representative imported addresses before relying on bulk names/types. |
| Observe a native call stack or live control flow | The debugger already available to the user, with symbols/address maps generated by an approved tool | Do not implement an in-plugin stack walker for a one-off diagnostic unless the debugger cannot answer the bounded question and reusable runtime stack capture is itself requested. |
| Inspect exact loader bootstrap and lifecycle APIs | The installed loader assemblies, templates, and version-matched official documentation | Do not copy an example from another loader major or backend. |

Primary project sources:

- ILSpy and `ilspycmd`: <https://github.com/icsharpcode/ILSpy>
- Cpp2IL: <https://github.com/SamboyCoding/Cpp2IL>
- Il2CppInspectorRedux: <https://github.com/LukeFZ/Il2CppInspectorRedux>

## Stop unproductive exploration

Before escalating to the next intervention level, state:

- the exact unanswered question;
- why current evidence and existing tools cannot answer it;
- the minimum additional artifact or tool output needed from the next level;
- the fallback if the attempt fails.

After two incompatible or failed approaches to the same subproblem, stop. Record them as rejected approaches, present the remaining tool/acquisition choices, and continue only work that is still independently useful.
