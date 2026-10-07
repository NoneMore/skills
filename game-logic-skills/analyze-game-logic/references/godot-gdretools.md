# Godot Recovery with GDRETools

Load this reference only when a Godot mechanic cannot be closed from readable
project/source artifacts and exported-package recovery or binary-resource
conversion is material. GDRETools is an external recovery dependency, not
gameplay evidence.

Upstream project: [GDRETools/gdsdecomp](https://github.com/GDRETools/gdsdecomp).

## Use current tool behavior

Record the installed GDRETools version and consult that installation's current
help before relying on commands or options. Treat exact flags, supported bytecode
revisions, and recovery limitations as live tool state rather than cached skill
knowledge. If the installed tool is unavailable or does not support the target,
stop this recovery path rather than inventing or forcing unsupported behavior.

## Recover only what the claim needs

Use the smallest mechanical step that exposes the unresolved relation:

1. Identify and hash the original target artifact.
2. Inspect the package/file listing when path discovery is enough.
3. Recover only material scripts for script-local questions.
4. Convert or recover the specific scene/resource layer when configuration,
   signal wiring, or serialized overrides are material.
5. Recover the full project only when the broader graph is genuinely required.

Write recovery output to a separate working directory rather than modifying the
installed artifact.

Retain detected Godot/bytecode version when material. If auto-detection is
uncertain and a version override is forced, keep conclusions that depend on
correct decompilation as working hypotheses until corroborated.

## Interpret recovered output conservatively

Recovered `.gd`, project, scene, and resource files are reconstructed artifacts,
not proof of exact original source text or shipped runtime behavior. Corroborate
material relations using the recovered graph, callers/signals, effective values,
and runtime behavior when the core workflow requires it.

A recovered project may differ from the shipped environment because of missing
plugins, imports, native extensions, export settings, or engine versions. Its
ability to run does not prove behavioral identity.

## Respect implementation and protection boundaries

If recovery exposes a transition into C#/.NET, GDExtension/GDNative, or native
code, preserve that transition and continue with the appropriate core workflow
only when the unresolved fact lies beyond it.

Use encryption/decryption material only when it is already legitimately
available and authorized for the local target. If recovery would require
deriving, guessing, extracting, or bypassing a key or protection mechanism, stop
that path and follow the core protection boundary.

## Evidence to retain when material

Record only what affects reproducibility or confidence:

- original target path/hash and detected Godot/export form;
- GDRETools version and bounded recovery action;
- recovery details that determine engine/bytecode interpretation;
- recovered `res://` locators used by the finding;
- forced version/bytecode overrides or recovery warnings;
- unresolved managed/native/protection boundaries.

Do not preserve complete recovered projects merely for bookkeeping when normal
project-knowledge persistence triggers do not apply.
