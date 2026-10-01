# Writing Agent Briefs

Use this reference only when a triaged item is moving to `ready-for-agent` or `ready-for-human`.

An agent brief is the durable execution contract attached to the tracker item. The original report and discussion remain context; the brief states the behavior that still has to become true.

Use the triage disclaimer required by `SKILL.md` at the start of every published brief.

## Contract rules

A good brief is:

- **Durable:** prefer behavior, interfaces, invariants, and stable symbols over file paths or line numbers.
- **Behavioral:** state what must be true, not a step-by-step implementation recipe.
- **Complete:** include independently checkable acceptance criteria and explicit non-goals.
- **Evidence-grounded:** distinguish behavior established during verification from reporter claims that remain unverified.
- **Tracker-agnostic:** use the configured tracker's identity/reference format rather than hard-coding GitHub mechanics.

A PR/MR brief differs only in its starting point: **Current behavior** describes what the existing diff already accomplishes and what remains incomplete.

## Template

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** one-line statement of the required outcome

**Current behavior:**
Behavior established during triage. Mark any material reporter claim that remains
unverified. For a PR/MR, include what the existing diff establishes and what remains.

**Desired behavior:**
The observable behavior or contract that should hold when the work is complete,
including edge cases and error conditions that are part of the established scope.

**Key interfaces:**
- Stable interface, type, protocol, or invariant that constrains the change
- Another interface only when independently relevant

**Acceptance criteria:**
- [ ] Independently verifiable criterion 1
- [ ] Independently verifiable criterion 2
- [ ] Independently verifiable criterion 3

**Out of scope:**
- Adjacent behavior explicitly excluded during triage, or "None established"
```

## Completion check

Before publishing, verify all of the following:

- category and summary agree with the maintainer-approved triage outcome;
- current behavior matches the verification outcome, and unverified claims are not presented as facts;
- desired behavior does not require the implementing agent to make an unresolved product or architecture decision;
- every acceptance criterion can be checked independently;
- out-of-scope entries reflect established exclusions rather than newly invented scope;
- no line number or brittle file location is carrying the meaning of the contract.

If any of these fail, the item is not ready for an agent brief yet. Return to clarification or `needs-info` rather than papering over the gap.
