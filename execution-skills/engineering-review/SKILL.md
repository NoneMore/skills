---
name: engineering-review
description: "Read-only engineering review and acceptance discipline. Use when judging an existing implementation, diff, design, or artifact against requirements and governing constraints, with independent positive and negative evidence including regressions, design violations, scope creep, and unnecessary complexity."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Review

Judge whether an engineering artifact or change deserves acceptance. Review is not satisfied by proving only that requested behaviour exists.

The core acceptance rule is:

> **Completion requires positive evidence and negative evidence.**

A change can implement the requested feature correctly and still fail review because it violates architecture, contracts, invariants, scope, maintainability constraints, or introduces unjustified complexity.

## Invocation boundary

Invoke when the primary task is to review, audit, verify, or accept an existing implementation, diff, design, specification, or engineering artifact against requirements or governing standards.

When available, prefer `engineering-investigation` for open-ended fact finding or diagnosis and `engineering-implementation` for unconditional implementation or a conditional fix whose condition is established and is now being pursued. A conditional fix request still begins with review until its condition is established.

Review is read-only unless the underlying task separately and explicitly authorizes fixes. Finding a defect does not itself grant mutation authority.

## Establish the review contract

Identify the smallest set of sources that legitimately govern the artifact:

- explicit current user acceptance intent;
- originating requirements/specification and accepted design;
- canonical architecture decisions, contracts, schemas, or compatibility promises;
- repository instructions and maintained coding/engineering standards;
- relevant tests and current behaviour;
- explicit scope/non-goals and risk boundaries.

Do not treat stale plans, incidental implementation patterns, or historical commentary as equal authority to maintained governing sources.

If the originating requirement is unavailable, say what basis the review can and cannot establish rather than inventing a specification.

## Two independent evidence axes

Review the artifact on at least two independent axes when both are relevant.

### A. Positive / intent evidence

Ask whether the requested or specified outcome is actually present:

- requirements and acceptance behaviour are implemented;
- important error/edge behaviour matches the contract;
- necessary compatibility or migration behaviour exists;
- direct and affected-system evidence supports the claim;
- no requirement is satisfied only superficially while the real observable behaviour remains wrong.

### B. Negative / constraint evidence

Actively look for important states that must **not** have become true:

- violation of accepted architecture or module boundaries;
- broken public/internal contracts or compatibility promises;
- weakened invariants, security, data, concurrency, performance, or operational guarantees;
- regressions outside the direct happy path;
- accidental scope expansion or unrelated changes;
- unnecessary coupling, abstraction, indirection, configuration, state, or dependency surface;
- duplicated sources of truth;
- stale or contradictory maintained engineering knowledge;
- new maintenance burden not justified by the requested outcome.

Passing the positive axis does not cancel failure on the negative axis, and vice versa.

## Review the diff and the resulting system

When a diff exists, inspect both:

- **what changed** — unexpected files, scope, generated content, dependency updates, broad refactors, hidden contract changes;
- **what the system now is** — resulting ownership, dependency direction, API/data model, failure semantics, operational behaviour, and maintainability.

A locally tidy diff can still create a poor system seam. A broad diff can still be appropriate if the governing change genuinely requires it. Judge against the accepted outcome and constraints, not aesthetic size alone.

## Evidence discipline

Use the closest safe evidence available:

- focused tests or reproductions for requested behaviour;
- relevant repository-native checks;
- targeted inspection of boundaries/contracts;
- runtime probes where appropriate;
- broader regression checks proportional to blast radius and consequence.

Seek disconfirming evidence deliberately. Challenge tests that merely mirror the implementation or encode the same unverified assumption.

Repository test commands may have side effects; read-only review does not authorize consequential mutation or external effects merely because a command is called a test.

## Complexity review

"Unnecessary complexity" is not a stylistic veto. Identify concrete maintenance cost relative to the problem being solved.

Strong findings include:

- a new abstraction duplicates an existing seam;
- a generalized framework solves hypothetical future cases while making the current path harder to understand or verify;
- state/coupling/dependency surface grows without an accepted requirement;
- local implementation freedom has been turned into a new permanent architecture decision without justification;
- the change creates multiple places that must now stay synchronized.

Do not reject unfamiliar code simply because a simpler-looking alternative exists. Explain the concrete cost and the governing principle it conflicts with.

## Findings severity and independence

Report findings by material impact, not by how easy they are to notice.

For each material finding state:

- the violated requirement/constraint or unjustified state;
- evidence/location;
- consequence;
- whether it blocks acceptance;
- whether the issue is definitely introduced by the reviewed change or may be pre-existing.

Do not bury a blocking architecture violation under a list of minor style comments.

## Read-only authority and fixes

If the task is review-only, stop at findings and acceptance judgment.

If the user explicitly authorized fixing discovered defects, preserve the review boundary until the defect is established, then use `engineering-implementation` when available. Without it, make only the qualifying fix, preserve unrelated work and governing constraints, and verify the changed behaviour. Re-evaluate the fix against both evidence axes; a false or unresolved condition leaves the task read-only.

## Knowledge impact

Perform a lightweight knowledge-impact check. If review reveals that a maintained canonical source is stale, contradictory, misplaced, or newly incomplete, use `engineering-knowledge-governance` when available, or apply repository conventions to reconcile the canonical source within task authority. In a read-only task, report the reconciliation need rather than editing it.

## Capacity feedback

If observed review progress or remaining verification materially undermines a supplied capacity assumption or threatens a known limit, report evidence, completed/remaining coverage, uncertain capacity impact, and a recommendation to the user or authorized upstream owner. Preserve the workload label and report unknown limits/telemetry honestly. Pending a decision, continue only independent bounded checks within existing authority/limits. Preserve permitted findings and resume state before a known limit and stop affected work safely; do not begin a check that cannot reasonably fit including recovery. Silence grants no extension. Report insufficient evidence rather than lowering the acceptance bar to fit the estimate; apply an explicit owner decision without repeating still-valid checks.

## Acceptance outcome

Do not collapse the result to "tests pass".

A concise result may distinguish:

- **Intent / requirements:** PASS / FAIL / INCOMPLETE
- **Governing constraints / design:** PASS / FAIL / INCOMPLETE
- **Regression / unintended effects:** PASS / FAIL / INCOMPLETE
- **Complexity / maintenance burden:** ACCEPTABLE / MATERIAL CONCERN / INCOMPLETE
- **Overall acceptance:** ACCEPT / REJECT / INSUFFICIENT EVIDENCE

Use only dimensions that matter for the artifact. Overall acceptance requires no unresolved blocking failure on an applicable dimension.
