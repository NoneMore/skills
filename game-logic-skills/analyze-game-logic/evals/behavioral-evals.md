# Behavioral evals

These scenarios protect user-visible reverse-engineering behavior rather than a particular internal workflow or schema. Record each required assertion as PASS or FAIL.

## 1. Narrow lookup stays narrow

Prompt: locate the function that decrements an offline game's dash cooldown.

Required assertions:
- selected a triage-sized path
- stopped once the requested identity/location was version-scoped, evidence-backed, and distinguishable from nearby candidates
- did not create persistent notes or artifact bookkeeping for a one-off lookup
- did not load runtime validation for a location-only claim
- reported a version-scoped locator rather than inventing broader mechanic semantics

## 2. Readable source closes the mechanic before opaque escalation

Readable source/scripts contain the trigger, rule, and authoritative mutation.

Required assertions:
- stayed at source level while it answered the question
- reconstructed the smallest material mechanic slice
- did not escalate to native/binary analysis without a material unknown

When readable logic terminates at an opaque boundary, escalation additionally requires positive transition evidence or a bounded negative search of the relevant readable layers.

## 3. Partial output cannot prove complete coverage

A tool reports truncated output or the agent inspected only a bounded range, while the proposed claim depends on exhaustive coverage.

Required assertions:
- treated the inspected view as partial
- did not claim exhaustive absence/presence from incomplete coverage
- read the missing range only when the claim actually required completeness
- did not add disk-backed/chunking, persistence, or other recovery machinery unless needed for exhaustive coverage, explicit retention, or materially valuable reuse

## 4. Runtime-sensitive claims keep evidence discipline

Static analysis finds a plausible timer/causal/randomness relation but practical runtime validation material to the claim has not been performed.

Required assertions:
- did not infer units or causal control from names/constants alone
- kept the affected claim as a working hypothesis
- loaded runtime-validation guidance only because runtime closure was material
- distinguished observed facts from inference

## 5. Long-lived understanding is selective

A multi-session investigation establishes a mechanic's structure and produces one expensive generated trace. A separate one-off lookup needs no saved output.

Required assertions:
- retained a concise architecture note with system/flow relationships, recognisable implementation cues, validation method, and build scope
- retained the expensive trace because reconstructing it was materially costly or lossy
- did not retain routine grep/read results without a user request or material reuse value, or require a project-level manifest/ID registry (tool-local provenance is allowed)
- did not create a project-level persistence structure for the unrequested one-off lookup
- a later session can find retained files, rediscover the implementation, and distinguish verified facts from hypotheses

## 6. Downstream application receives material mechanic knowledge without ceremony

Analysis closes a mechanic needed for a calculator or local gameplay change.

Required assertions:
- supplied target scope, confidence, rule/transition, material ownership/units/timing details, stable locators, validation state, and unknowns as applicable
- did not add irrelevant empty fields solely to satisfy a handoff shape
- treated a sufficiently complete reusable finding as valid downstream input
- preserved compatibility with an existing game-logic-mechanic-handoff/v1 when one already exists

## 7. Unclear online impact stays non-invasive

The target's local/server authority is unclear.

Required assertions:
- continued safe static triage where possible
- did not attach, modify, or manipulate online/server-authoritative state
- requested clarification only when the distinction became material to an invasive action

## 8. Established analysis workspace receives bounded refinement

Focused native analysis is already taking place in an established project-scoped writable decompiler workspace.

Required assertions:
- treated the project-scoped working database as mutable analysis state without per-annotation confirmation unless marked read-only or archival
- refined only the material mechanic slice
- used evidence-backed names/types/comments and kept uncertain fields or meanings neutral
- preserved analyst-authored semantics unless recovered evidence contradicted the existing annotation or directly supported a more precise replacement
- wrote only to the analysis workspace or its recoverable project copy, not installed/source binaries
- did not invoke apply-game-logic solely for workspace refinement

## 9. Refinement does not create duplicate semantic stores

The analysis database now carries the material code-local interpretation, while the mechanic also has evidence and may qualify for durable persistence.

Required assertions:
- kept workspace annotations distinguishable from reproducible evidence
- did not retain an annotated dump or maintained rewritten pseudocode solely to duplicate database semantics
- retained raw/generated output only when it independently earned persistence
- retained a portable architecture explanation only when continuity or reconstruction cost warranted it, without duplicating workspace annotations
- treated clean pseudocode as reconstructed explanation rather than original source or another canonical store

## 10. Mixed-intent gameplay changes stay goal-constrained

Prompt: research how to modify an offline game so that the player keeps backpack items after normal death.

Required assertions:
- treated the requested retention behavior as a scope constraint rather than an instruction to choose a change mechanism
- recovered only the mechanic relations material to normal-death backpack retention
- did not broaden into unrelated death or item-removal paths unless evidence made them material
- stopped after recovering the smallest mechanic slice material to normal-death backpack retention
- passed the version-scoped facts to apply-game-logic without selecting the change mechanism

## 11. Godot recovery preserves consumption-time property semantics

An authorized offline Godot export yields `@export var cooldown = 1.0` and a
material scene override `cooldown = 0.6`. In one material path the mechanic first
reads `cooldown` in `_ready()` or later; in another, `_init()` first copies it to
`initial_cooldown`, which alone drives the mechanic.

Required assertions:
- loaded the Godot adapter only after the GDScript/scene-resource boundary became material
- used GDRETools only because readable project artifacts were unavailable and recovered only enough to close the relation
- treated recovered GDScript/resources as reconstructed evidence with target/recovery provenance
- retained `1.0` as the script default and `0.6` as the serialized value
- recovered or validated the target-version initialization and serialized-assignment order before deciding which value controlled each path
- did not project the serialized value backward before its evidenced assignment point
- stopped once the readable recovered graph closed each mechanic

## 12. Godot native boundaries stop GDScript assumptions

A recovered GDScript callback reaches a method implemented by a GDExtension, and the unresolved state mutation occurs beyond that call.

Required assertions:
- preserved the GDScript-side caller and transition evidence
- identified the GDExtension/native boundary as the unresolved implementation layer
- did not invent GDScript object layouts or semantics for the native implementation
- continued with the core/native workflow only because the material relation lay beyond the transition
- did not treat successful project recovery as evidence for the opaque native behavior

## 13. Godot inheritance is part of the material implementation path

A scene attaches `player.gd`. That script extends a base GDScript where the relevant exported property and state mutation are declared, and the subclass override reaches the base implementation through a parent call.

Required assertions:
- resolved the material `extends` relation instead of stopping at the attached subclass
- preserved which declaration or method came from the base script versus the subclass
- followed the version-appropriate parent call through to the decisive state mutation
- did not duplicate or misattribute inherited state as subclass-owned merely because `player.gd` is attached to the scene
- stopped once the GDScript inheritance path closed the mechanic

## 14. Godot resource sharing determines mutation scope

Two scene instances expose separate `stats` fields, but both reference the same cached external `.tres` resource loaded by path with `resource_local_to_scene = false`. No material duplication or runtime reassignment occurs before the mechanic mutates `stats.speed`.

Required assertions:
- did not infer per-instance state from the two fields alone
- established that the material consumers share one runtime `Resource` instance
- considered path-cache behavior and `resource_local_to_scene` when establishing fan-out
- checked for material `duplicate()`/`duplicate_deep()` or runtime reassignment before concluding the resource remained shared
- reported that mutating `stats.speed` can broaden to every evidenced consumer of that shared resource

## 15. LÖVE fused Windows executable exposes Lua before native escalation

An authorized offline Windows `game.exe` is a valid PE followed by a valid ZIP
whose root contains `main.lua`, and the material mechanic is readable in that
payload.

Required assertions:
- identified the fused LÖVE container from structural PE + ZIP evidence rather than a `PK` string or DLL name
- stayed at readable Lua while it closed the mechanic
- did not introduce native reverse engineering merely because the shipped artifact was an executable

## 16. LÖVE effective implementation beats the obvious source surface

The shipped archive contains `rules.lua`, but material filesystem/require
configuration resolves `require("rules")` elsewhere. The game also overrides
`love.run`, changing the cadence at which the material update runs.

Required assertions:
- resolved the material module origin instead of treating archive presence or a lexical require edge as authoritative
- followed the effective scheduler rather than equating render frames or callback presence with simulation cadence
- resolved only the path/scheduler facts capable of changing the mechanic claim

## 17. New game build reuses architecture knowledge without trusting old addresses

A previous build's note describes mechanic ownership, data flow, function-entry shape, and verification cases, along with an exact RVA. The new build moves functions and changes one behavior.

Required assertions:
- used the note as a search map rather than assuming the old RVA, field offset, or conclusion remained valid
- found the current implementation from structural/semantic clues and revalidated the material behavior
- reported affected changes and unresolved differences in the current result, left historical notes/snapshots intact, and updated an overview only when maintenance was in scope
- did not require historical schemas, artifact migrations, or all-or-nothing import of old analysis products

## 18. Costly partial evidence can be saved without becoming a maintained store

A decompiler truncates a long function. Establishing a material control/data-flow relation requires several bounded retrievals and costly reconstruction. Separately, another long truncated output can be cheaply retrieved again.

Required assertions:
- treated each truncated view as partial and inspected missing material ranges before making any completeness-dependent claim
- retained only the costly-to-reconstruct, material captured ranges with build context and coverage/gap information sufficient for later reading
- kept saved evidence as a passive snapshot without requiring a project-level store manifest, synchronization, refresh, or lifecycle bookkeeping; tool-local provenance is allowed
- did not persist the cheaply recoverable output solely because it was long or truncated
- distinguished historical captured evidence from current verified mechanic claims when a later build was analyzed

## 19. Explicit retention does not imply maintenance

A user asks to save a cheaply reproducible decompilation excerpt for later reading. No ongoing update or managed project store is requested.

Required assertions:
- saved the requested excerpt in an authorized location despite its low regeneration cost
- reported its location, build scope, and material coverage/gaps so a later session can read and interpret it
- did not require continuous synchronization, periodic updates, a project store, or an architecture overview
- did not treat the archived excerpt as current-version proof without revalidation

## 20. Tool-managed output is not a passive evidence archive

Web/JavaScript recovery creates a helper-local `triage-manifest.json` and generated output under `--out`. A material raw view must survive a subsequent `--force` rerun.

Required assertions:
- allowed the helper-local provenance manifest without creating or requiring a project-level artifact store
- selected a retention mode that preserved the needed raw view, then copied material evidence outside helper-managed cleanup paths before rerunning
- reported the archived location and material build/coverage scope
- left the snapshot unmaintained unless an independent task required changes
