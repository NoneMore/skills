# Governing decisions during implementation

Read when sources conflict or execution falsifies a consequential assumption.

## Resolve a contract conflict

Identify what each source can establish: current user intent defines the requested change within applicable instructions; maintained specifications and decisions describe governing contracts; tests/runtime establish observed behaviour; historical notes and plans need freshness and provenance checks.

An explicit request to change a contract may include reconciling its tests and documentation. Establish the compatibility, migration, data, and scope consequences before treating the old contract as either immutable or irrelevant. Ask the decision owner only when a material choice remains unresolved by the request and available evidence.

For example, an explicit change from `404` to `204` can authorize updating the maintained response contract. A request to simplify a serializer does not authorize changing its public format merely because that shortens the implementation.

## Recover from a falsified plan

Distinguish local mechanics from a governing change. If a helper layout is unsuitable but contracts and outcome stay intact, choose another layout. If a planned synchronous integration only supports asynchronous behaviour and the difference affects compatibility, stop the dependent work and surface that consequence.

Preserve completed valid work, record the contradictory evidence and affected assumptions, and propose the smallest revision that restores a feasible path. Do not continue substantial work on a known-invalid assumption or silently make a new architecture decision inside implementation.

## Transfer the revised state

When another executor owns the next step, carry the accepted revision, preserved fixed decisions, current implementation state, remaining work, and evidence gaps. Use canonical sources rather than creating another competing specification. Reconcile maintained knowledge within the task's authority when the governing contract changes.
