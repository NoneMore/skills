# Godot Recovery with GDRETools

Load this reference only when a Godot mechanic cannot be closed from already
readable project/source artifacts and exported-package recovery or binary
resource conversion is material. GDRETools is an external dependency, not a
bundled helper and not evidence of gameplay ownership by itself.

Upstream project: [GDRETools/gdsdecomp](https://github.com/GDRETools/gdsdecomp).

## Use current tool behavior, not cached CLI recipes

GDRETools evolves independently from this skill. Before relying on a command or
option, record the installed GDRETools version and consult that installation's
current help. Prefer the tool's own version/help output over commands copied from
old notes or examples.

The upstream tool currently provides project recovery from Godot export
artifacts, GDScript decompilation, PCK inspection/extraction/creation, and
binary/text resource conversion. Treat exact flags, supported bytecode
revisions, and recovery limitations as live tool state.

## Recover only what the claim needs

Use the smallest mechanical step that exposes the unresolved relation:

1. Identify and hash the original target artifact before recovery.
2. Inspect the package/file listing when path discovery is enough.
3. Recover only material scripts when the question is script-local.
4. Convert or recover the specific scene/resource layer when configuration,
   signal wiring, or serialized overrides are material.
5. Perform full project recovery only when the mechanic genuinely depends on a
   broader scene/resource graph or narrower recovery cannot close the relation.

Write recovery output to a separate working directory. Analysis should not
modify the installed game artifact.

When recovery reports a detected Godot/bytecode version, retain that information
with any reusable finding. If version auto-detection is uncertain and an override
must be forced, treat semantic conclusions that depend on correct decompilation
as a working hypothesis until independently corroborated.

## Interpret recovered output conservatively

A recovered `.gd` file is reconstructed source, not proof of the exact original
source text. A recovered `project.godot`, scene, or resource likewise proves what
the recovery tool reconstructed from the export artifact, not automatically how
the shipped runtime used every value.

Corroborate material relations using the scene/resource graph, callers/signals,
effective serialized values, and runtime behavior when the core workflow
requires it. Keep the original artifact hash and recovery provenance so the
result remains version-scoped.

GDRETools can recover GDScript across multiple Godot generations, but a recovered
project may still differ from the shipped environment because of missing plugins,
imports, native extensions, export-only behavior, or engine-version differences.
Do not promote "the recovered project runs" to proof that all target behavior is
identical.

## Respect implementation boundaries

GDRETools recovery can expose where a GDScript path enters C#/.NET,
GDExtension/GDNative, or another native component. That transition is evidence
for a new boundary, not a reason to infer the opaque implementation from the
GDScript side.

Do not expect GDExtension/GDNative implementations to become GDScript simply
because the surrounding project was recovered. Continue with the appropriate
core/native workflow only when the unresolved fact actually lies beyond that
transition.

## Encrypted or protected artifacts

Use an encryption key only when it is already legitimately available and its use
is authorized for the local target. If proceeding would require recovering,
extracting, guessing, or bypassing a key or protection mechanism, stop that
recovery path.

A custom decryptor is acceptable only when the user is authorized to access the
content and the required scheme/key material is already available; do not use
this workflow to derive secrets. This keeps tool capability separate from the
core prohibition on DRM/licensing/protection bypass.

## Evidence to retain when material

Record only what affects reproducibility or confidence:

- original target path/hash and detected Godot/export form;
- GDRETools version and the bounded recovery action used;
- recovery log details that determine engine/bytecode interpretation;
- recovered `res://` locators used by the finding;
- any forced version/bytecode override or recovery warning;
- unresolved C#/.NET, GDExtension/GDNative, encryption, or native boundaries.

Do not preserve complete recovered projects merely for bookkeeping when the
normal project-knowledge persistence triggers do not apply.