# PR-gated specification lifecycle (optional)

This is an opt-in, stricter variant of the Change conventions in [bootstrap-project](../SKILL.md). It trades extra specification and PR maintenance for a reviewable record of a specification being introduced, implemented or terminated, and archived before merge. It is **not** the recommended default.

## Selection and authority

- Apply only when a user explicitly requests this variant or the target project already follows it. Do not infer adoption from the use of PRs, CI, specifications, or a desire for better documentation.
- Check that the project uses a PR-based contribution flow and accepts the cost of requiring a specification even for small or documentation-only PRs. Automated and external-contributor PRs also need a deliberate policy; do not invent silent exemptions.
- Put the adopted rules in the project's canonical human-readable governance document, linked from its contributor entry. An agent-facing file may point to those rules but must not become a competing authority.
- Keep code and runtime evidence authoritative for *implemented* behavior. Change specifications describe proposed work; archived specifications preserve historical intent and outcomes, not a permanent catalog of current behavior.

## Overrides to the default Change practice

| Default `bootstrap-project` convention | This optional variant |
| --- | --- |
| A Change may span multiple PRs. | A Change belongs to one PR; a PR may contain multiple Changes. |
| Trivial work need not have a Change. | Every PR introduces at least one new active Change with a non-empty `spec.md`. |
| A Change has no mandatory files. | Each Change has a `spec.md` covering intent, scope, and acceptance conditions. |
| `active/` and `archive/` are sufficient. | Add `planned/` for proposals not yet being implemented. |
| Archive when a Change stops advancing. | Archive all PR-active Changes before merge, including terminated work. |

These overrides are a coherent project-level policy **only when adopted**. Otherwise, follow the default Change practice. The architecture, ADR, code-first authority, and human-first documentation conventions remain unchanged.

## Change identity and lifecycle

```text
specs/
├── planned/<change>/       # proposed, not yet being implemented
├── active/<change>/        # being advanced in the current branch / PR
└── archive/<change>/       # no longer being advanced
```

- Use unique, descriptive `kebab-case` Change names, retaining the name when moving between directories. Do not reactivate a Change already active or archived on the target branch; subsequent work uses a new Change.
- A planned proposal may be activated in a PR by moving its directory into `active/`. A PR may leave unrelated proposals in `planned/`.
- Each Change contains a non-empty `spec.md` with the intended outcome, boundaries, and acceptance conditions. Add `design.md` or `tasks.md` only when helpful. Keep volatile execution state in the existing tracker.
- Revise an active specification in place as requirements settle. Archive the entire Change directory, preserving its history, when the PR completes or terminates it. Record the reason, acceptance outcome, verification evidence, and unresolved items in the archived specification.
- Neither `active` nor `archive` proves readiness, correctness, implementation, or current applicability. Git, tests, PR review, and deployed behavior remain distinct evidence.

## PR contract and working sequence

1. **Scope.** Identify the Change or Changes covered by this PR. Split larger proposals into independently closable Changes when necessary; one PR may complete several, but a Change must not be split across PRs.
2. **Specify first.** From the intended target branch, create or activate at least one `specs/active/<change>/spec.md` and commit it **before implementing** the work. Prefer a separate initial specification commit to make the order easy to review. Size the specification to the change.
3. **Implement and review.** Keep the active specification aligned with agreed scope during implementation and review. Record verification in the PR. Update architecture documentation for significant implemented outcomes and write an ADR for consequential decisions when warranted; neither substitutes for the Change.
4. **Close Changes.** Before merge, move every active Change in the PR to `specs/archive/<change>/` under the same name, annotate outcomes and any unfinished work, and commit the result. If further fixes follow archival, keep its outcome record accurate and repeat relevant verification.
5. **Merge.** Verify that the PR history contains a new active specification for each participating Change, that all are archived in the merge result, and that no tracked files remain under `specs/active/`. An unimplemented follow-up is a new planned Change rather than a still-active Change merged into the target branch.

The PR template should make the Change names, specification commits/links, verification, and archival outcome reviewable without duplicating the full specifications.

## Enforcement and limits

Where the repository supports it, a deterministic CI check can verify:

- PR history introduces at least one previously unactivated Change with a non-empty `specs/active/<change>/spec.md` (including activation from `planned/`);
- no participating Change reuses a name already active or archived on the base branch;
- each activated Change has a same-name, non-empty archived specification in the prospective merge result; and
- the prospective merge result has no tracked `specs/active/` files.

Test the check against both passing and failing synthetic Git histories, including activation from `planned/`, omitted or renamed archives, empty specifications, reused names, and changed merge results. A GitHub Actions check alone does **not** prevent merging: configure the target branch's required-status-check rules and verify they apply. Do not claim the gate is enforced until that is done.

History checks cannot establish that the written specification was substantively complete, that its commit truly preceded all implementation work, that one Change was never worked on in another PR, or that acceptance criteria were satisfied. Human review remains necessary. Checks also depend on preserving relevant PR commits until evaluation; a squash merge may be used *after* the PR check succeeds.

## Adoption

1. Inspect existing governance and in-flight Changes. Resolve conflicts and plan transitions explicitly; do not silently rewrite or retroactively treat old work as compliant.
2. Establish the variant in the human-facing governance document and contributor/PR entry points; preserve other project conventions.
3. Add only the enforcement scripts, tests, and CI hooks the project can operate. If enforcement is deferred, label the rules as conventions rather than verified merge gates.
4. Verify human and agent navigation, lifecycle paths, PR template, CI failure cases, and branch protection where applicable.

For one concrete implementation (not a universal template), see [wenku8-downloader's specification lifecycle commit](https://github.com/NoneMore/wenku8-downloader/commit/48f0dd187a394540394c7bb4792967934d23e1f2), including its governance policy, PR template, checker, tests, and workflow.
