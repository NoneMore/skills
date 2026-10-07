---
name: implement
description: Turn a requested production change into working, verified production behavior. Use when the user explicitly wants code or other production artifacts changed, including features, bug fixes, refactors, migrations, or performance work.
disable-model-invocation: true
---

# Implement

## Purpose

Turn a requested production change into working production behavior.

## Accepts

A direct request, issue, specification, ticket, conversation decision, or other sufficiently clear implementation contract.

## Owns

- the requested production behavior, not merely the textual edit;
- preservation of relevant behavior outside the intended change unless changing it is justified;
- production artifacts that are fit to remain in the real system;
- evidence that the changed behavior works at the boundary where it is expected to matter.

Do not leave exploratory shortcuts, fake dependencies, temporary instrumentation, or throwaway scaffolding in the production result unless they intentionally belong to the design.

Choose verification that is proportionate to the behavior and risk. Testing before, during, or after implementation is a method choice, not a lifecycle requirement.

## Specialized guidance

- [debugging.md](references/debugging.md) when the failure mechanism is unclear or a tight feedback loop would materially reduce uncertainty;
- [testing.md](references/testing.md) when test placement or behavioral coverage needs explicit guidance;
- [mocking.md](references/mocking.md) when boundary substitution is necessary.

Research, experiments, prototypes, refactoring techniques, migrations, benchmarks, and self-review may be used directly when they help complete the requested production outcome.

## Done when

The requested production behavior works, relevant preservation expectations hold, temporary exploratory artifacts are cleaned up, and there is proportionate evidence at the meaningful system boundary that the result is acceptable to keep.

## Does not require

TDD, a separate review skill, a tracker claim, a canonical implementation-result record, a commit, a pull request, reconciliation, or any prescribed successor capability unless the user or project explicitly requires that artifact or action.
