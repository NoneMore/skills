# Durable Application Outputs

Use this reference for deployed or retained implementations whose provenance, validation, or rollback must survive the current session. One-off calculations and explanations need no durable records.

## Keep the output self-contained

A concise `record.md` alongside the actual implementation/configuration and any necessary validation results or backups is sufficient. It should let a later session identify:

- the exact target build and material version/hash guard;
- the mechanic knowledge consumed, its evidence/validation state, and any version-sensitive assumptions;
- the authoritative implementation and how it is applied;
- observed validation results, coverage, and unresolved limitations;
- original/control state and an executable rollback or cleanup procedure when relevant.

Use the user's existing working project or another authorized location outside the installed game. No mandated directory structure, project store, manifest, ID registration, or schema is needed. Link to existing architecture notes when helpful rather than copying a large knowledge base; preserve the specific mechanic input if the later reader would otherwise lose its meaning.

For destructive modifications, keep the captured original content or integrity-verifiable backup with enough information to restore it, and verify the rollback precondition in [SKILL.md](../SKILL.md) **before** modifying the target. A deployed copy inside the game directory is not the authoritative source artifact. Successful implementation does not independently prove the underlying mechanic.

## Recovery check

A later session should be able to determine what build and knowledge the output used, which file produced the result, what was tested, and how to disable or restore it without chat history. Retain only the material needed to answer those questions.
