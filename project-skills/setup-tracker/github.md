# GitHub Issues backend

Representation and operations for the tracker. The issue model owns semantics.

## Capability requirement

Use this backend only when GitHub Issues are enabled and the available tooling/API can read and write issues, labels, assignees, native sub-issues, and native issue dependencies.

If native sub-issues or dependencies cannot be read and written, use Local Markdown. Do not encode those relations in issue text.

<!-- repository-contract:start -->

## Representation

- **Type:** managed work has exactly one of `tracker:type:investigation` or `tracker:type:change`; intake has neither.
- **Status:** managed work has exactly one explicit status label allowed by the semantic contract. Intake has at most one explicit intake status label. Untyped intake with no tracker status label derives `needs-triage` while open and `done` while closed. Any other intake status is explicit.
- **Sources:** managed work has exactly one reserved body line, for example `Sources: #101, #117`; use `Sources: None` when empty. Intake may omit the line; an omitted intake line means `Sources: None`. If present, the reserved line is unique.
- **Hierarchy:** native sub-issues.
- **Dependencies:** native issue dependencies.
- **Claim:** the sole GitHub assignee of managed work. Intake assignees are not tracker claims.

The tracker status labels are `tracker:status:needs-triage`, `tracker:status:needs-info`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`, and `tracker:status:cancelled`, subject to the semantic contract.

Terminal statuses use GitHub closed state. Other statuses use open state. For derived intake status, an unlabeled open intake is `needs-triage` and an unlabeled closed intake is `done`.

Repository labels such as `bug`, `enhancement`, or `documentation` remain independent.

## Managed-work body

Managed issues must contain:

```markdown
Sources: <#101, #117|None>

## Completion condition

<issue-specific, checkable completion condition>
```

When managed work is `waiting`, it must also contain exactly one active waiting section:

```markdown
## Waiting

Waiting for: <external event or human decision>

Resume when: <checkable condition>
```

Remove the active `## Waiting` section before moving managed work out of `waiting`; preserve relevant historical information in a Skill-owned notes or result section when needed.

Add `## Context` only when context beyond the title, sources, and linked relations is needed to define or execute the work.

Skills that create or execute managed work may append structured sections they own, for example `## Execution notes`, `## Implementation result`, `## Conclusion`, or `## Evidence`. Preserve all unrelated sections when updating an owned section.

Do not copy type, status, sources, hierarchy, dependencies, or assignee into ordinary body sections. `Sources:` is the reserved provenance line and remains the canonical GitHub body representation for direct sources.

## Intake templates

Public GitHub issue templates are intake aids only. They must not ask reporters to choose managed-work type, completion condition, hierarchy, dependencies, claim, or internal lifecycle state.

Keep existing useful intake forms. When a common intake surface is missing, setup may install the corresponding default issue form shipped with this skill. Shipped forms apply `tracker:status:needs-triage` when possible. Existing forms do not need to be rewritten merely to add that label because unlabeled open intake derives the same status.

Keep blank issues enabled so valid external intake is not rejected merely because it does not fit a form. A blank issue with no tracker labels is valid intake and derives `needs-triage` while open.

Issues created through any form or as a blank issue remain untyped external intake. Repository taxonomy labels applied by forms remain independent from tracker type and status.

## Operations

When creating managed work, set exactly one managed-work type and one explicit status allowed by the semantic contract, write the required `Sources:` line and completion condition, and preserve any Skill-owned extension sections supplied by the creating workflow. Intake has no managed-work type.

When changing status, replace any explicit canonical tracker status label with the intended status label and keep GitHub open/closed state consistent with terminal status. Derived status is only the representation default for intake without a tracker status label; mutations may materialize it explicitly. Before moving managed work out of `ready`, release its execution claim. Entering `waiting` also requires the active `## Waiting` section; leaving `waiting` requires removing that active section.

When changing Sources, preserve the rest of the issue body.

Before adding a native parent or dependency relation, verify that both endpoints satisfy the semantic endpoint rules and that the new edge would not create a cycle. Respect GitHub's native relationship limits; if the intended graph cannot be represented natively, stop rather than encoding a textual fallback.

Use native operations for hierarchy and dependencies.

To acquire a managed-work claim, first verify that the issue is on the executable frontier, then add the current actor as assignee without intentionally retaining any other managed-work assignee. Re-read the issue immediately. Execution may proceed only while the current actor is the sole assignee and the issue remains `ready` with no live blocker. Because GitHub assignees are coordination rather than a strict distributed lock, re-check the sole claim before consequential external effects or tracker mutations. If multiple managed-work assignees are observed, treat the claim as conflicted: do not continue execution and remove only the current actor's assignment when possible.

When releasing a claim, remove the current actor as assignee. Do not use managed-work assignees for long-lived ownership metadata.

When a skill updates an extension section, change only the section it owns and preserve the completion condition and all unrelated content.

After a mutation, re-read the fields and body sections that were changed and verify the intended values persisted.

<!-- repository-contract:end -->

## Setup-only checks and mutations

Before modifying tracker configuration, inspect existing tracker-shaped state.

- Inspect existing labels and existing issues that carry any canonical tracker type or status label.
- Stop without modifying the tracker if an issue has multiple managed-work type labels, multiple tracker status labels, a managed-work type with no explicit valid managed-work status, or an intake-only status/type combination forbidden by the semantic contract.
- Stop if managed work has multiple assignees.
- For existing managed work, also stop if the `Sources:` line or `## Completion condition` is missing, duplicated, or malformed.
- For existing managed work in `waiting`, also stop if the active `## Waiting` section or either required line is missing, duplicated, or malformed; stop if non-waiting managed work retains an active `## Waiting` section.
- Stop if a source self-references, if hierarchy or dependency endpoints violate the managed-work-only rule, or if hierarchy or dependencies contain a self-edge or cycle.
- Stop if an explicit terminal status is open or an explicit non-terminal status is closed.
- Untyped issues with no tracker status label are valid historical intake: open derives `needs-triage`; closed derives `done`.
- If `docs/agents/issues.md` already declares a different tracker model, backend, or contract version, stop. Replacing or upgrading a different tracker contract is migration and is out of scope.

Create missing canonical tracker type and status labels. Preserve unrelated labels.

Preserve repository-owned issue templates. Add a shipped intake form only when the repository lacks a suitable form for that entry point, and never overwrite a different existing template. Ensure `.github/ISSUE_TEMPLATE/config.yml` has `blank_issues_enabled: true`; preserve all other existing chooser configuration.
