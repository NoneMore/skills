---
name: renew-project
description: Renew an established project's development baseline through justified documentation, code-structure, and historical-context improvements. Use when the user explicitly requests project renewal or a substantial project-level maintainability refresh.
disable-model-invocation: true
---

# Renew Project

## Purpose

Improve an established project's current development baseline so contributors can understand, verify, modify, and extend it without reconstructing past Changes or agent sessions. Reduce concrete accumulated maintenance and context costs; renewal is not a required lifecycle phase.

## Accepts

A project and an explicit request for project-wide or focused renewal. Assessment or advice is read-only; a request to carry out renewal authorizes changes within its scope, subject to project policy, actual permissions, and the safeguards for historical retirement.

## Owns

- identifying material friction in current knowledge, navigation, verification, code structure, or tooling;
- choosing and executing bounded improvements that address that friction;
- consolidating current documentation and restructuring implementation when justified;
- retiring historical artifacts from the current tree when explicitly in scope and safely recoverable;
- verifying the renewed baseline and making material results and limitations reviewable.

## Principles

- **Independence is an ongoing baseline requirement.** Ordinary development should leave the integration branch usable from current code, tests, and development/architecture guidance, without reading archived Changes or unfinished work context. Renewal addresses accumulated problems; it does not defer routine Change-completion responsibilities.
- **Scope follows the request.** For general renewal, inspect the project's knowledge and implementation surface for significant problems. For a focused request, inspect the named area and necessary dependencies. Finding an unrelated issue does not authorize changing it.
- **Preserve authority without duplication.** Respect the project's human-facing governance and established locations for implemented behavior, setup guidance, current architecture, consequential ADR rationale, and historical evidence. Do not introduce a renewal document as another maintained authority. Consult archived Changes only when specific historical rationale, provenance, or evidence is needed.
- **Require a reason to restructure.** Long files or numerous archived Changes are signals to inspect, not problems by count. Prefer a meaningful reduction in navigation, modification, or verification cost over uniform formatting or wholesale rewriting.
- **Preserve established contracts by default.** Internal modules and private interfaces may be reorganized where beneficial. Preserve observable behavior, public interfaces, data/error semantics, reproducibility, and relevant nonfunctional constraints unless the user explicitly authorizes a change. Tests are evidence of compatibility, not proof of complete equivalence.
- **Follow local contribution policy.** Use the project's adopted Change, PR, approval, and review practices. Renewal creates no Phase status, mandatory template, automatic cleanup schedule, or exception to existing merge rules.

## Approach

1. **Establish the boundary.** Identify the requested improvement, the current project baseline, applicable governance, and whether changes are authorized. Account for in-flight work and unrelated modifications before editing.
2. **Inspect relevant evidence.** Read the current entry points, implementation, tests, documents, and history pointers needed to identify real friction. Avoid a whole-repository or whole-archive review for a focused task.
3. **Select justified changes.** Make material trade-offs and compatibility constraints explicit. Choose the smallest effective improvements with proportionate verification, rather than requiring a separate plan for every renewal.
4. **Implement within scope.** Consolidate current knowledge at its existing authority, improve documentation navigation, and restructure code or tooling as warranted. Organize larger changes into independently reviewable units when useful; do not silently change product behavior or architectural direction.
5. **Retire history conditionally.** When the request explicitly includes removing archived Changes or historical process material, consult [History retirement](references/history-retirement.md) for preservation, safe removal, recovery, and verification. Do not infer permission to retire history from a documentation or code refactor request.
6. **Verify outcomes.** Run relevant build, test, lint, or contract checks where available; check affected references and developer navigation. Test independence from archived Changes using representative setup and follow-on development tasks when material. Evaluate the claimed improvement against the friction that motivated it, and report any unverified scope.

## Stop conditions and completion

If a proposed action exceeds the authorized scope, conflicts with adopted policy, requires an unresolved product/architecture decision, or cannot preserve material contracts or mandatory evidence, defer that action and surface the blocker. Continue independent, safe work when possible. A general renewal request does not authorize Git-history rewriting, remote-reference changes, or removal of protected evidence.

Done when the authorized improvements are delivered and relevant checks have been performed, the addressed maintenance burden is materially reduced (or a well-supported no-change conclusion is reached), the current baseline remains usable without historical Change context, and consequential limitations are stated. Reuse diffs, checks, PRs, and existing records rather than generating a mandatory renewal report.
