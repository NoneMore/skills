# Durable Application Artifacts

Use this reference when an application must survive the current session: a deployed mod/patch/hook/instrumentation file, retained simulator/tool, or any change whose provenance and rollback matter later.

Do not create durable records for throwaway calculations or explanations.

## Minimum durable record

Keep the following together:

- target game/content version, build, and material hashes;
- the finding/mechanic record actually consumed;
- authoritative implementation source/configuration;
- mechanism and stable locator/version guard;
- original/control state needed to restore or compare;
- applied/derived state;
- validation performed and limitations;
- rollback/cleanup procedure;
- remaining assumptions or unknowns.

A compact record.md plus the authoritative implementation and any required backup/validation files is sufficient. Preserve the consumed mechanic input verbatim when practical so a later session can tell exactly what the application relied on.

## Storage

If an existing game-logic project store is already available and useful, register the retained files there using its current tooling. Otherwise keep a simple application directory in the user's working project. Durable provenance must not depend on another Skill being installed solely for bookkeeping.

Do not treat an application artifact as new evidence that the underlying mechanic is correct merely because it was derived from that mechanic.

For destructive changes that satisfy the rollback precondition in [SKILL.md](../SKILL.md), retain the captured original bytes/content or integrity-verifiable backup with the durable record.

## Recovery check

A later session should be able to answer four questions without chat history:

1. What exact target and mechanic knowledge did this application depend on?
2. What authoritative file/config/code produced the deployed result?
3. What validation showed the intended behavior and scope?
4. How can the target be disabled, restored, or rolled back?

If any answer depends only on conversational memory, the retained record is incomplete.
