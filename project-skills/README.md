# Project tracker prototype

An isolated prototype for a small project-tracking contract.

It defines:

- two tracked issue kinds: `intake` and `managed`;
- two managed-work types: `investigation` and `change`;
- explicit lifecycle status and a checkable completion condition for managed work;
- direct sources, optional parent/child decomposition, and blocking dependencies;
- GitHub Issues and Local Markdown representations;
- a setup skill that configures the backend without adopting existing work.

Only explicitly classified issues participate in the tracker. Existing unclassified repository issues remain ordinary repository issues unless a later workflow explicitly chooses to classify one.

The tracker contract describes work and relationships. It deliberately does not define execution claiming, agent concurrency, orchestration, migration/versioning, or repository delivery policy. Those concerns belong to the workflows that need them.

GitHub uses namespaced tracker labels and native relations when the relevant GitHub capability is available. Local Markdown stores the same model in `.tracker/issues/`.

See [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) for semantics and the backend references for representation.

## Non-goals

This prototype does not port downstream workflows, migrate or take over existing issues, install public issue forms, support other tracker vendors, or modify the current Matt skills.
