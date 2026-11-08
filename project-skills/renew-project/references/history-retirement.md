# History retirement

Consult this reference only when an authorized renewal includes moving archived Changes, old reports, one-off tools, or other historical process material out of the current working tree. This is not routine Change completion or an instruction to delete every historical artifact.

## Decide what can leave the tree

- Start from the specified history-retirement scope. Check current documentation, code comments, tests, scripts, and tooling for dependencies on the affected historical paths. If important current facts or constraints exist only there, move the minimum needed knowledge into the appropriate current authority before removal; do not republish the whole Change narrative.
- Distinguish historical process residue from required audit/approval records, useful positive or negative findings, proof or reproducibility evidence, incident rollback material, and legal or contractual records. Keep necessary current artifacts current; preserve required historical evidence in an accessible location rather than deleting it.
- A completed Change should already have undergone local artifact disposition. At renewal, revisit only material gaps or retention questions; do not automatically re-distill every archived Change. When the current baseline is self-contained, retirement may be mostly removal.

## Preserve, remove, verify

1. Identify a committed pre-retirement state that includes the material to be removed. Record its commit SHA and verify the relevant files are present. Do not treat uncommitted or externally stored files as captured by a Git snapshot.
2. For retirement of a historical Change set, establish a project-approved, stable, remotely accessible Git ref to that state (for example, a protected archive branch or tag). Verify the remote ref resolves to the intended commit and that its contents can be retrieved. Check protection and deletion/retention controls rather than assuming a ref name makes it durable. Leave a discoverable retrieval pointer in an existing PR or project entry, not a new obligatory Phase registry.
3. Account separately for external samples, environments, binaries, licenses, and other material needed to substantiate retention or reproduction claims. When required, preserve location, provenance, integrity, access, and retention terms; Git alone does not capture these dependencies.
4. Remove only authorized historical paths. Repair current-tree links and references, including source comments and development commands, that would otherwise point to removed paths. Historical citations may instead use stable, retrievable revision links where appropriate.
5. Check affected navigation, setup/build/test flows, relevant contracts, and a representative follow-on task without requiring archived Changes. Record the preserved ref, actual checks, and any limitations in existing review evidence. If preservation or recovery cannot be verified, leave the affected material in place and report why.

Removing files from `main` cleans the current tree; it does not shrink existing Git object/history storage. Rewriting shared history or migrating to an independent-history repository is a separate, explicitly authorized operation, not an implicit retirement step.
