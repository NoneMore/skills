# Loader Selection and Bootstrap

Use the installed loader as part of the target fingerprint. Loader family, major version, backend, OS, and architecture jointly determine the API and package graph.

## Select from evidence

1. Prefer the loader already present in the game or repository.
2. Match examples and official documentation to the installed major version. Treat BepInEx stable and BepInEx master documentation as different API surfaces.
3. For a new setup, compare the game's community convention, supported OS/architecture, backend support, and release status. Treat loader/template/package installation as missing assets and apply the selected asset mode.
4. Use one loader's bootstrap and dependency set. Share feature code through a loader-neutral project only when the repository already needs multiple loaders.

Useful primary sources:

- BepInEx installation and development: <https://docs.bepinex.dev/>
- BepInEx templates: <https://github.com/BepInEx/BepInEx.Templates>
- MelonLoader releases and documentation links: <https://github.com/LavaGang/MelonLoader>

## Inspect before writing bootstrap code

Capture these facts from the installed files, project, template, or package metadata:

| Fact | Evidence |
| --- | --- |
| Loader family and version | Startup log, core assembly metadata, package lock |
| Backend build | Distribution name plus Mono/IL2CPP probe evidence |
| Entry base class and namespace | Installed template or referenced loader assembly |
| Lifecycle methods | API for that exact loader version |
| Plugin metadata | Existing plugins or official template |
| Plugin directory | Loader configuration and successful startup log |
| Logging/config API | Referenced assembly or pinned docs |

Treat copied snippets as untrusted until they compile against the pinned assemblies.

## Bootstrap rules

- Keep the entry class small: initialize logging/configuration, verify compatibility, register hooks, and report success or a precise failure.
- Delay scene-object lookup until the relevant scene or subsystem exists.
- Keep expensive discovery out of per-frame callbacks.
- Assign a stable unique plugin identifier and version it independently from the game.
- Declare hard dependencies only when the plugin cannot function without them; detect optional integrations at runtime.
- Make initialization idempotent and expose a cleanup path for hooks, callbacks, native allocations, and injected objects.
- For MelonLoader, inspect whether the pinned version automatically applies annotated Harmony patches. Use either its automatic path or one manual `PatchAll` call during process-level initialization, never both.

## Reference discipline

- Use packages or assemblies matching the installed loader version.
- Use user-supplied proprietary references from a local ignored `lib/` or resolve existing references through machine-local MSBuild properties.
- When a required reference is absent, list its exact identity and expected location in the asset check. Copy or extract it from a game installation only under asset mode 2.
- Set local reference copying so game, Unity, and loader contract assemblies do not enter the output directory.
- Include only mod-owned runtime dependencies in distribution archives.
- Build against existing generated IL2CPP interop assemblies from the same game fingerprint. If they are absent or stale, treat generation as asset acquisition and apply the selected mode.

## First proof

Make bootstrap success observable with one line containing:

- plugin identifier and version;
- backend;
- loader version;
- game/build marker;
- hook count after registration.

Accept bootstrap only when authorized runtime testing shows that line once during a cold start and no assembly-resolution error precedes it. Otherwise mark runtime proof pending.
