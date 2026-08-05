# IL2CPP Branch

Use this branch only when the fingerprint identifies a Unity IL2CPP player.

## Confirm the backend and build pair

Strong IL2CPP evidence includes native game code such as `GameAssembly.dll`, `libil2cpp.so`, or a platform equivalent together with `global-metadata.dat`. Record hashes for the native module and metadata file as one inseparable build pair.

Match the loader distribution to backend, OS, process architecture, and loader version. Treat first-run interop generation as asset acquisition; run it only under asset mode 2 or when the user explicitly requests it.

Unity describes IL2CPP as managed assemblies converted to C++ and then compiled and linked as native code: <https://docs.unity3d.com/Manual/scripting-backends-il2cpp.html>.

## Use generated shallow artifacts as a cache

- Inspect existing BepInEx-generated interop assemblies for the exact build pair with `ilspycmd`; reference them from the mod only when they match the installed loader and runtime.
- Use Il2CppInspectorRedux-generated .NET shim/Dummy DLLs or C# stubs as analysis-only structural views. Do not substitute them for loader-generated runtime interop references.
- When wrappers are missing or stale after a game or generator update, present the asset check. Regenerate through the loader's supported mechanism only under asset mode 2.
- Keep generated game wrappers used as analysis assets under the corresponding Mod project's ignored `.assets/<game-version>/<generator>/` directory and out of release archives.
- Resolve types and methods from existing wrappers and user-supplied evidence first. Treat new native/metadata analysis as reverse-asset acquisition.
- Record the loader/generator version with the build pair so another machine can reproduce the reference set.

Generated interop assemblies, shim/Dummy DLLs, and C# stubs describe a structural or callable surface; they do not turn the native game back into ordinary managed IL and their placeholder bodies do not prove behavior.

## Escalate native analysis deliberately

1. Start shallow with exact-fingerprint BepInEx interop or Il2CppInspectorRedux shim DLLs/C# stubs.
2. Use compatible Cpp2IL recovered IL/IR, mapping, or method output with the exact metadata pair when the unanswered question concerns approximate behavior, calls, constants, control flow, or method identity/address.
3. Use a persistent Ghidra project annotated by compatible Il2CppInspectorRedux-generated scripts and companion data when intermediate evidence is insufficient or the question requires exact native instructions, native xrefs, data flow, ABI, optimization/inlining, or a native detour.

Follow [tooling.md](tooling.md) for escalation evidence and persistence requirements. Stop at the first sufficient level.

## Write interop-aware code

- Use loader-provided conversions for IL2CPP strings, arrays, delegates, collections, and objects.
- Keep managed delegates and wrapper objects alive for as long as native code can call them.
- Register injected types before adding them as Unity components, using the API from the pinned loader/interop version.
- Resolve overloads explicitly. Treat generic methods, stripped members, and shared generic implementations as high-risk targets.
- Check wrapper objects for destroyed native instances before dereferencing them.
- Perform Unity API calls on the main thread.

## Choose hooks that exist at runtime

- Prefer loader-supported HarmonyX or interop hooks that resolve the wrapper to a native target.
- Use Prefix/Postfix semantics when the loader supports them for that target.
- Treat managed-IL transpilers as unavailable for native IL2CPP method bodies unless the exact framework documents a supported transformation path.
- Use a native detour only after wrapper-level hooks cannot express the change and existing or user-authorized reverse evidence independently proves the function address and signature.

For a native detour, record:

- module and relative virtual address or symbol resolution method;
- architecture and calling convention;
- complete parameter and return ABI, including hidden instance or return-buffer parameters;
- original function pointer and detour lifetime;
- thread, GC, and exception boundary behavior.

Apply the shared hook rules in [patching.md](patching.md).

## IL2CPP proof

Require all of the following:

- interop assemblies match the current build pair, or their generation is explicitly marked pending under the selected asset mode;
- the plugin loads without wrapper or native binding errors;
- every required hook target identifies one native method and logs stable evidence;
- the hook survives repeated calls and one cold restart without access violations;
- disabling the plugin restores baseline behavior.

Use the version-matched BepInEx IL2CPP installation guide when applicable: <https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html>.
