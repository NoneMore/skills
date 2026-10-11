# Runtime Validation

Load this reference whenever the core dynamic-validation gate marks runtime
validation as material. This file provides the branch-specific validation
procedure; it does not redefine the core gate or make runtime validation a
mandatory second phase for every analysis.

## Authorization and validation boundary

Do not launch or attach to a target merely because runtime observation would
strengthen a conclusion. Read-only static inspection may proceed within the
requested scope. Launching, attaching, instrumentation, hooks, and memory writes
must be within the user's requested/authorized offline analysis scope.

If runtime tooling is unavailable, unsafe, outside scope, or would require a
prohibited DRM/anti-cheat bypass, provide the validation procedure instead and
leave dynamically material claims unconfirmed.

Before running instrumentation, state what it will observe or change. Scope it to
the intended offline process, exact module/content version, and the smallest
runtime surface needed for the claim.

## Choose the smallest validation boundary

For source-available logic, prefer in order:

1. static/exhaustive proof when it fully decides the claim;
2. an extracted pure-function or minimal state-transition harness;
3. subsystem simulation;
4. full runtime integration only when the smaller boundaries cannot exercise the
   material behavior.

Do not emulate unrelated UI/runtime subsystems merely to exercise isolated game
logic. If a harness repeatedly fails because of incidental environment
dependencies, reduce or redesign the harness rather than expanding unrelated
stubs.

For compiled/runtime-only logic, prefer logging reads, calls, arguments, returns,
and state transitions before writing memory or changing control flow.

## Keep controlled interventions material

Use a write or hook only when it is materially needed to distinguish the live
behavior under test. Guard only the preconditions required for a safe, semantically
correct intervention.

For code or instruction replacement, verify the expected original bytes before
mutation. For mutable runtime data, require an exact prior value only when equality
is itself a material precondition; a snapshot retained for restoration does not
become a compare-and-swap guard merely because it exists. Validate pointer,
object/container identity, lifetime, or comparable runtime assumptions when they
are material to a safe dereference or write.

If a material precondition fails, stop that intervention rather than weakening the
guard, substituting a nearby site, or broadening compatibility. Capture the state
needed to restore temporary code/data changes and release instrumentation-owned
resources where applicable. State explicitly when behavior already produced by
the experiment cannot be undone by detaching or restoring the mechanism.

## Controlled observation protocol

Use a fixed save/checkpoint and reproduction path when practical. Record relevant
RNG/seed conditions when randomness can affect the result.

- Establish a control run.
- Add observation with the smallest possible instrumentation surface.
- When validating a modification, compare control, observation, and modified runs
  as applicable.
- Change one material variable at a time.
- Record observed values, timestamps or step counts, reproduction steps, and
  limitations.
- Exercise pause, death, loading, cutscenes, difficulty changes, save/reload,
  scene/room transitions, or other lifecycle edges only when they can change the
  claim.

The runtime observation must test the claimed behavior rather than merely reread
the same static value through another tool.

## Claims that usually need runtime closure

### Time and scheduling

Establish clock/scheduler, update rate, units, pause/time-scale behavior, loading
behavior, and any conversion to seconds. Do not infer seconds from a plausible
constant alone.

### Causal control

Show that the candidate value, field, call, or branch changes or governs the
observed mechanic rather than merely correlating with it. Where practical, use a
controlled intervention or an independently varying runtime condition.

### Caller, actor, or event-source discrimination

When multiple callers or shared paths exist, identify which runtime source
actually reaches the mechanic in the controlled scenario. Do not generalize one
observed caller to every actor/context without evidence.

### State lifetime

Test creation/init, activation, pooling/reuse, pause, death/despawn, loading,
scene/room changes, save/reload, and reset only as material to the claim. Record
what survives each relevant boundary.

### Intervention scope

Before relying on a runtime write, hook, or patch point, verify the candidate
address mapping and determine whether the touched state or call path is shared.
Observe side effects that could invalidate the intended narrow scope.

### Random/probabilistic behavior

When the static formula does not determine the effective distribution, establish
the runtime RNG source/stream, skipped/repeated-roll conditions, relevant seed
conditions, range mapping/comparison, and enough controlled observations to
distinguish the competing hypotheses.

## Evidence state after validation

Promote a **Working hypothesis** to **Confirmed** only when the runtime result
closes the material semantic unknown and is consistent with the version-scoped
static evidence. A failed or ambiguous runtime test does not confirm the opposite
claim automatically; update the hypothesis set and record the limitation.
