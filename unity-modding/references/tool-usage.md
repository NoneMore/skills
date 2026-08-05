# Analysis Tool Usage

Read the matching card before invoking an analysis tool. Treat every command as a template: resolve the executable and input paths, run the installed version's help first, and replace every angle-bracket placeholder. Never run a copied template with unresolved placeholders.

For every tool run, save the command, version, input fingerprint, output location, exit status, and a short output validation in the analysis record. A zero exit code without the expected artifact is not success.

## Common preflight

1. Resolve the exact executable; do not assume it is on `PATH`.
2. Run `<tool> --version` and `<tool> --help`. When either switch is unsupported, capture the executable file or assembly version and the help command that does work.
3. Check that every required input exists and belongs to the same game fingerprint.
4. Create the tool-specific directory under `<mod-project-root>/.assets/<game-version>/<tool>/`.
5. State the one question the run must answer and the expected output file or stdout content.
6. After the run, inspect file count, sizes, logs, and one representative target. Treat empty stdout, an empty output directory, placeholder bodies, and unmapped addresses as failures or limitations, not evidence.

## `inspect_unity_game.py`

Use the bundled read-only probe to classify a Unity installation before choosing backend-specific tools.

```bash
python3 <skill-dir>/scripts/inspect_unity_game.py <game-root> --json
```

- Require the positional `<game-root>`; `--json` only selects the output format.
- Accept a game root, a Unity `*_Data` directory, or an executable path.
- Expect JSON on stdout containing `backend`, `architecture`, `unity_version`, loader evidence, and—when IL2CPP is found—the native/metadata build pair and hashes.
- Do not treat `unknown` or `conflicting` as a backend choice. Resolve it with loader logs or loaded-module evidence.

## `ilspycmd`

Use `ilspycmd` only on managed .NET assemblies: Mono game assemblies, loader assemblies, BepInEx interop assemblies, or Il2CppInspectorRedux shim/Dummy DLLs. It does not disassemble `GameAssembly.dll` or `libil2cpp.so`.

First capture the local syntax because options can change between ILSpy versions:

```bash
ilspycmd --version
ilspycmd --help
```

Use these common forms when the installed help confirms them:

```bash
# List type names before choosing a fully qualified type.
ilspycmd -l c <assembly.dll>

# Decompile one type as C# to stdout.
ilspycmd -t <Namespace.TypeName> <assembly.dll>

# Emit managed IL for one type to stdout.
ilspycmd --ilcode -t <Namespace.TypeName> <assembly.dll>

# Decompile a whole assembly as a project. -p requires -o.
ilspycmd -p -o <output-directory> <assembly.dll>
```

- Always supply the assembly positional argument. `-t` selects a type; it does not replace the assembly argument.
- Pass a fully qualified type name to `-t`, including the namespace and the installed version's syntax for nested or generic types. Discover it with `-l` instead of guessing.
- Expect decompilation on stdout when `-o` is omitted. Capture stdout explicitly through the execution tool; do not report “no result” merely because no file was created.
- Use `-r <dependency-directory>` only when the installed help supports it and unresolved dependencies materially affect the output.
- For a bulk project, require both `-p` and `-o`, then verify that the directory contains non-empty source files and a project file.
- On Mono, C# and `--ilcode` can expose real managed bodies. On IL2CPP interop/shim DLLs, expect wrapper or placeholder bodies only; use them for structure, signatures, tokens, and locators, never as proof of the original implementation.

If stdout is empty, check the exit code and stderr, confirm the assembly argument, list the type names, retry once with the exact listed type, and stop. Do not cycle through guessed flag orders or write a replacement metadata parser merely because the invocation was incomplete.

## Cpp2IL

Use Cpp2IL on an exact IL2CPP game build to obtain metadata-aware mappings, Dummy DLLs, or the specific output format exposed by the installed build. Cpp2IL's CLI and output formats vary substantially by release; never copy flags from another release without querying the binary.

Start with capability discovery:

```bash
<cpp2il> --help
<cpp2il> --list-output-formats
<cpp2il> --list-processors
```

For current builds whose help advertises these options, use this shape:

```bash
<cpp2il> \
  --game-path <game-root> \
  --output-as <format-from-list-output-formats> \
  --output-to <mod-project-root>/.assets/<game-version>/cpp2il/<run-name> \
  --verbose
```

- Require `--game-path`; add `--exe-name <name>` only when automatic executable detection is ambiguous and the installed help exposes it.
- Select `--output-as` only from the current binary's `--list-output-formats` output. Do not assume old switches such as `--analysis-level`, `--skip-analysis`, or `--dump-method-addresses` still exist.
- Use a Dummy DLL or metadata-oriented output for structure and address mapping. Use an IL-recovery format only when approximate recovered managed IL is the named evidence needed.
- Treat recovered CIL, ISIL, control-flow graphs, or decompiled C# as reconstruction. They are not the compiler's original C# and are not the original native assembly listing.
- When the question asks for exact native instructions or bytes at a mapped RVA, stop trying additional IL-recovery settings. Use Cpp2IL only to establish the method identity/RVA if it can, then enter the deep native-disassembly route in [ghidra.md](ghidra.md) with that recorded reason.
- Validate at least one method identity, token/RVA mapping, architecture, and non-empty output. Record unsupported instructions and analysis failures verbatim instead of filling gaps with plausible pseudocode.

After one capability-correct run fails, retry once only when the log identifies a concrete compatibility or input correction. Otherwise record the incompatibility and escalate or stop; do not repeatedly switch recovery formats hoping to obtain exact disassembly.

## Il2CppInspectorRedux

Use Il2CppInspectorRedux for structural exports and address maps: C# stubs, shim DLLs, JSON metadata, C++ scaffolding, or companion files for a disassembler. It is not a decompiler and does not recover original method bodies.

The repository has legacy and Redux frontends, and release executable names can differ. Resolve the CLI binary and run:

```bash
<inspector-cli> --version
<inspector-cli> --help
```

For a Windows/Linux/macOS native binary plus metadata, use the options shown by the installed CLI. Current documented option names use this shape:

```bash
# Generate only C# stubs, shim DLLs, and JSON address metadata.
<inspector-cli> \
  --bin <GameAssembly.dll-or-libil2cpp.so> \
  --metadata <global-metadata.dat> \
  --select-outputs \
  --cs-out <output-root>/types.cs \
  --dll-out <output-root>/dll \
  --json-out <output-root>/metadata.json

# Generate the Ghidra script and its required companion outputs.
<inspector-cli> \
  --bin <native-binary> \
  --metadata <global-metadata.dat> \
  --select-outputs \
  --py-out <output-root>/il2cpp.py \
  --json-out <output-root>/metadata.json \
  --cpp-out <output-root>/cpp \
  --script-target Ghidra
```

- Keep the native binary and `global-metadata.dat` from the same build. For APK/AAB/XAPK/IPA/Zip inputs, follow the installed help because separate metadata input may be ignored.
- Use `--select-outputs`; otherwise documented builds generate all outputs by default, creating unnecessary bulk artifacts.
- Preserve the generated Python script, JSON metadata, and C++ type header together for a Ghidra import. Generating only `il2cpp.py` is incomplete.
- Pass `Ghidra` with the documented case when using `--script-target`.
- Provide `--unity-version <version>` only when evidenced, or use the installed version's asset-based detection option. Do not guess a Unity version to force parsing.
- For ordinary browsing, inspect generated C# stubs or shim DLLs and `metadata.json`. Do not mistake empty/placeholder method bodies for implementation behavior.
- Validate that `metadata.json` parses, shim DLLs are non-empty, and one known method has a plausible token/address before trusting the bulk export.

If the installed Redux CLI rejects the documented flags, do not silently switch to a similarly named legacy executable. Capture the executable path/version and its own `--help`, then adapt only the option names it advertises.

## Ghidra and PyGhidra

Use Ghidra only after the deep-analysis gate in [tooling.md](tooling.md) is satisfied. Read [ghidra.md](ghidra.md) completely before import or mutation.

- Use the exact native binary and a persistent project under `<mod-project-root>/.assets/<game-version>/ghidra/`.
- Import all Il2CppInspectorRedux companion files together; a Python script without its JSON and type header is not a usable export.
- Resolve one method by imported name/token/RVA, verify its address against the metadata mapping, and obtain the native **Listing** when exact assembly is requested. Treat the decompiler's C-like view as a separate inferred representation.
- Record image base, language/processor, analysis settings, program identity, and all script versions. A wrong image base can make every imported address look valid but point to the wrong bytes.
- Prefer bounded queries for one function, its xrefs, callers/callees, P-code, or listing. Do not bulk-decompile the whole binary.

## Choose the representation deliberately

| Requested evidence | Use | Do not substitute |
| --- | --- | --- |
| Managed Mono C# body | `ilspycmd -t` | IL2CPP stub C# |
| Managed Mono IL | `ilspycmd --ilcode -t` | Cpp2IL recovered IL |
| IL2CPP types, signatures, tokens, addresses | BepInEx interop or Il2CppInspectorRedux exports; browse DLLs with `ilspycmd` | Placeholder bodies |
| Approximate IL2CPP body/control flow | A compatible Cpp2IL recovery/IR output | Claims of original source or exact native instructions |
| Exact IL2CPP native assembly/bytes | Ghidra Listing at a validated RVA, after the deep gate | Cpp2IL pseudocode, recovered CIL, or Ghidra decompiler C |
| IL2CPP native xrefs, data flow, ABI | Annotated persistent Ghidra project | Shim DLL metadata alone |
