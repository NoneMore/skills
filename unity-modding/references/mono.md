# Mono Branch

Use this branch only when the fingerprint identifies a Unity Mono player.

## Confirm the backend

Strong Mono evidence includes game assemblies such as `Assembly-CSharp.dll` under a `Managed` directory together with a Mono runtime. A `Managed` directory alone is not decisive because IL2CPP players can ship managed support assemblies.

If Mono and IL2CPP signals coexist, compare the executable's loaded modules or a successful loader log before choosing references.

## Choose the target framework

Use this priority order:

1. Preserve the target framework of a working mod project or official loader template for the installed version.
2. Inspect the game's already available `netstandard.dll`, `mscorlib.dll`, Unity version, and loader requirements.
3. Validate the choice by compiling a minimal loader entry against exact references.

Avoid raising the target framework merely to satisfy a convenience API; the game runtime must be able to load the compiled assembly.

## Build a clean reference set

- Reference the loader and patching assemblies from pinned packages or the exact loader installation.
- Reference only the Unity modules and game assemblies used by the mod.
- Exclude `mscorlib`, `netstandard`, and broad `System.*` copies from local game references unless the pinned template explicitly requires them.
- Keep game assemblies out of build output and source control.
- Prefer repository source, public APIs, and user-supplied target evidence. If a patch target cannot be resolved, list the exact game assembly or decompiler output as a missing asset and apply the selected asset mode.
- Under asset mode 2, decompile only the exact assemblies needed for the requested target and record their hashes or game build. Keep the outputs outside source control.

## Patch managed code

- Resolve the target by declaring type, method name, argument types, static/instance status, generic arity, and return type.
- Prefer Prefix or Postfix patches with minimal injected arguments.
- Use reflection accessors for private members only after a public seam is unavailable.
- Use a transpiler only when existing or user-authorized IL evidence provides a distinctive semantic instruction pattern; assert the expected match count.
- When compiler-generated state machines, lambdas, or properties hide behavior, request emitted IL through the asset gate before inspecting it.

Apply the shared hook rules in [patching.md](patching.md).

## Unity lifecycle and threads

- Use the loader's Unity component lifecycle only if the exact entry type provides it.
- Register scene-dependent behavior after the target scene or singleton is ready.
- Marshal work from file, network, or timer callbacks onto the Unity main thread before touching Unity objects.
- Cache stable method metadata, but re-resolve scene objects after scene changes.

## Mono proof

Require all of the following:

- the plugin assembly loads without target-framework or binding errors;
- every required patch target resolves to exactly one managed method;
- the hook marker fires at the expected count and lifecycle phase;
- unpatching or disabling restores baseline behavior after restart.

Start at <https://docs.bepinex.dev/> and select documentation matching the installed BepInEx version before applying its target-framework and local-reference guidance.
