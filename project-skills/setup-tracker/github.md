# GitHub Issues backend

Representation and operations for the tracker. The issue model owns semantics.

## Capability requirement

Use this backend only when GitHub Issues are enabled and the available tooling/API can read and write issues, labels, assignees, native sub-issues, and native issue dependencies.

Use whichever available GitHub API or tool surface can satisfy those operations. Lack of one convenience command is not a reason to change backends. If the intended GitHub backend cannot satisfy every required operation with the available tooling, stop and report the missing capability. Do not fall back to Local Markdown and do not encode native relations in issue text.

<!-- repository-contract:start -->

## Representation

- **Kind:** every tracked issue has exactly one of `tracker:kind:intake` or `tracker:kind:managed`. An issue with neither kind label is outside the tracker. An issue with both is invalid.
- **Type:** managed work has exactly one of `tracker:type:investigation` or `tracker:type:change`; intake has neither. Type labels without `tracker:kind:managed` are invalid tracker state.
- **Status:** every tracked issue has exactly one explicit status label allowed by the semantic contract for its kind. Status is never derived from GitHub open/closed state or from missing labels.
- **Sources:** managed work has exactly one reserved body line, for example `Sources: #101, #117`; use `Sources: None` when empty. Intake may omit the line; an omitted intake line means `Sources: None`. If present, the reserved line is unique.
- **Hierarchy:** native sub-issues.
- **Dependencies:** native issue dependencies.
- **Claim:** the sole GitHub assignee of managed work. Intake assignees are not tracker claims.

The tracker kind labels are `tracker:kind:intake` and `tracker:kind:managed`.

The tracker status labels are `tracker:status:needs-triage`, `tracker:status:needs-info`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`, and `tracker:status:cancelled`, subject to the semantic contract.

Terminal statuses use GitHub closed state. Non-terminal statuses use open state. Closing an issue never determines whether its semantic status is `done` or `cancelled`; set the explicit status first.

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

Do not copy kind, type, status, sources, hierarchy, dependencies, or assignee into ordinary body sections. `Sources:` is the reserved provenance line and remains the canonical GitHub body representation for direct sources.

## Intake templates

Public GitHub issue templates are intake aids only. They must not ask reporters to choose managed-work type, completion condition, hierarchy, dependencies, claim, or internal lifecycle state.

Keep existing useful intake forms. When a common intake surface is missing, setup may install the corresponding default issue form shipped with this skill. Shipped forms apply both `tracker:kind:intake` and `tracker:status:needs-triage`.

Keep blank issues enabled so reporters are not rejected merely because their input does not fit a form. A blank issue without a tracker kind label is unclassified and outside the tracker until a triage or intake workflow explicitly classifies it. Setup never classifies or adopts such issues.

Issues created through shipped forms are tracked intake. Existing repository forms remain repository-owned; setup does not silently reinterpret issues created through them. Repository taxonomy labels applied by forms remain independent from tracker kind, type, and status.

## Operations

When creating intake, set `tracker:kind:intake`, set exactly one explicit intake status, and do not set a managed-work type.

When explicitly adopting an unclassified issue as intake, preserve its reporter, wording, evidence, discussion, and unrelated repository metadata; add `tracker:kind:intake` and exactly one explicit intake status. Adoption is a downstream intake/triage operation, never a setup operation.

When creating managed work, set `tracker:kind:managed`, exactly one managed-work type, and exactly one explicit managed-work status allowed by the semantic contract; write the required `Sources:` line and completion condition; preserve any Skill-owned extension sections supplied by the creating workflow.

When changing status, replace any explicit canonical tracker status label with the intended status label and keep GitHub open/closed state consistent with terminal status. Before moving managed work out of `ready`, release its execution claim. Entering `waiting` also requires the active `## Waiting` section; leaving `waiting` requires removing that active section.

When changing Sources, preserve the rest of the issue body.

Before adding a native parent or dependency relation, verify that both endpoints satisfy the semantic endpoint rules and that the new edge would not create a cycle. Respect GitHub's native relationship limits; if the intended graph cannot be represented natively, stop rather than encoding a textual fallback.

Use native operations for hierarchy and dependencies.

To acquire a managed-work claim, first verify that the issue is on the executable frontier, then add the current actor as assignee without intentionally retaining any other managed-work assignee. The runtime must already guarantee that the same managed issue is not being executed concurrently by another top-level executor; subagents are part of the claiming execution and do not claim the issue independently. Re-read the issue immediately. Execution may proceed only while the current actor is the sole assignee and the issue remains `ready` with no live blocker. If multiple managed-work assignees are observed, treat the claim as conflicted: do not continue execution and remove only the current actor's assignment when possible.

When releasing a claim, remove the current actor as assignee. Do not use managed-work assignees for long-lived ownership metadata.

When a skill updates an extension section, change only the section it owns and preserve the completion condition and all unrelated content.

After a mutation, re-read the fields and body sections that were changed and verify the intended values persisted.

<!-- repository-contract:end -->

## Setup-only checks and mutations

Before modifying tracker configuration, inspect existing canonical tracker labels, `docs/agents/issues.md`, and issues carrying any canonical tracker kind, type, or status label.

If no compatible `docs/agents/issues.md` contract exists but any existing issue already carries canonical tracker kind, type, or status labels, stop without modifying tracker state. Adopting, repairing, or migrating pre-existing tracker-shaped issues belongs to a separate migration/takeover workflow.

Ordinary existing GitHub issues with no canonical tracker kind, type, or status labels are outside this tracker. Setup must preserve them and must not classify, validate, close, relabel, or otherwise adopt them.

When a compatible current contract already exists, validate every tracked issue before mutation:

- every tracked issue has exactly one tracker kind and exactly one status allowed for that kind;
- intake has no managed-work type; managed work has exactly one managed-work type;
- type or status labels without a tracker kind are invalid;
- managed work has at most one assignee;
- managed work has exactly one valid `Sources:` line and exactly one `## Completion condition` section;
- managed work in `waiting` has exactly one active `## Waiting` section containing both required lines, while non-waiting managed work has none;
- sources reference existing tracked issues and do not self-reference;
- hierarchy and dependency endpoints obey the managed-work-only rule and contain no self-edge or cycle;
- terminal status is closed and non-terminal status is open.

Any failed check stops setup before tracker mutation. Setup never repairs issue data.

If `docs/agents/issues.md` already declares a different tracker model, backend, or contract version, stop. If it declares the same contract version but its normative contract text differs from the current version-1 contract, also stop. Replacing, upgrading, repairing, or taking over tracker contracts is migration and is out of scope.

Create missing canonical tracker kind, type, and status labels. Preserve unrelated labels.

Preserve repository-owned issue templates. Add a shipped intake form only when the repository lacks a suitable form for that entry point, and never overwrite a different existing template. Ensure `.github/ISSUE_TEMPLATE/config.yml` has `blank_issues_enabled: true`; preserve all other existing chooser configuration.
