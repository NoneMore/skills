# Engineering Knowledge Model and Lifecycle

Use this reference for the detailed canonicality, placement, naming, status, provenance, persistence, and lifecycle rules behind the `engineering-knowledge-governance` skill.

The goal is not a standardized document tree. The goal is a repository whose important engineering claims remain **authoritative, discoverable, and maintainable**, with status, provenance, and freshness explicit where they materially affect trust. Transient plans belong here only when cross-context or cross-agent continuity requires them.

## Contents

1. [Discover the repository's documentation system first](#1-discover-the-repositorys-documentation-system-first)
2. [Choose the canonical home before choosing the filename](#2-choose-the-canonical-home-before-choosing-the-filename)
3. [Keep knowledge roles separate from file taxonomy](#3-keep-knowledge-roles-separate-from-file-taxonomy)
4. [Naming policy](#4-naming-policy)
5. [Placement policy](#5-placement-policy)
6. [Status and lifecycle](#6-status-and-lifecycle)
7. [Provenance, freshness, and trust](#7-provenance-freshness-and-trust)
8. [Minimal document contract](#8-minimal-document-contract)
9. [Split, merge, rename, and retire deliberately](#9-split-merge-rename-and-retire-deliberately)
10. [Persistence test before writing or persisting coordination state](#10-persistence-test-before-writing-or-persisting-coordination-state)
11. [Reconcile after consequential work](#11-reconcile-after-consequential-work)

## 1. Discover the repository's documentation system first

Before creating or reorganizing documents, inspect the repository for existing conventions and authoritative homes. Relevant evidence may include:

- `README`, `CONTRIBUTING`, `AGENTS`, or repository instructions;
- existing `docs/`, architecture, RFC, ADR, design, runbook, or planning areas;
- naming patterns used by maintained documents;
- links from code, tests, issue templates, release processes, or developer tooling;
- explicit statements that a document or directory is canonical.

Treat repository conventions as constraints when they are current and intentional. Do not introduce a competing taxonomy merely because another structure is theoretically cleaner.

## 2. Choose the canonical home before choosing the filename

For each durable claim, determine where a future engineer would reasonably expect the authoritative version to live.

Prefer, in order:

1. update an existing canonical artifact;
2. extend an existing maintained document whose scope already owns the claim;
3. create a new artifact only when the knowledge has a distinct scope, audience, lifecycle, or maintenance owner that would make embedding it misleading or unwieldy.

Do not duplicate the same authoritative claim across a design doc, plan, README, and handoff. Secondary summaries may exist, but they should point to the canonical source or be mechanically checked for consistency when feasible.

A document is not canonical merely because it is newer, longer, or more detailed. Canonicality comes from repository convention, explicit ownership, active references, or a deliberate decision made during the task.

## 3. Keep knowledge roles separate from file taxonomy

Use these reasoning roles when deciding what deserves durable representation:

- **Fact** — an observed, verifiable truth whose source, scope, or freshness may matter.
- **Constraint** — a binding boundary whose violation would materially change the solution.
- **Specification** — an accepted contract for desired behaviour, scope, constraints, and governing approach. It may be durable when future work must continue to obey it, or change-local when its durable truths are later absorbed into canonical contracts/design.
- **Design** — a durable structural choice or model with relevant invariants, trade-offs, and rationale.
- **Plan** — transient coordination of sequence, dependencies, progress, and open work.

Specification, Design, and Plan are distinct roles even when one file temporarily contains more than one. A specification defines what should become true and the accepted engineering direction; design explains how the system should hold together; a plan coordinates how work proceeds. Plans are persisted only when continuity requires them and should not become permanent truth merely because they were written.

These are reasoning roles, not required directories or filename prefixes. A single design document may contain observed facts, binding constraints, and a proposed design. A project README may be the canonical home for a compatibility constraint. A plan may reference several design decisions without owning them.

Do not create `facts.md`, `constraints.md`, `design.md`, and `plan.md` solely to mirror the knowledge model.

Split artifacts when their lifecycle or authority diverges, not merely because their categories differ.

## 4. Naming policy

### Follow local convention first

Match the repository's established conventions for casing, separators, numbering, prefixes, dates, and directory placement when those conventions are maintained and unambiguous.

### Conservative fallback when no convention exists

If the repository has no usable convention:

- prefer a maintained documentation area such as `docs/` over adding several new top-level files;
- use topic-oriented subdirectories only when multiple artifacts justify the category;
- use lowercase kebab-case filenames for Markdown;
- choose stable, noun-oriented topic names that describe the subject rather than the current activity;
- use role suffixes such as `-plan`, `-runbook`, or `-migration` only when the role materially affects lifecycle or interpretation;
- avoid agent names, session identifiers, temporary ticket wording, and vague names such as `notes.md`, `misc.md`, `new-design.md`, or `final.md`;
- avoid version suffixes such as `v2`, `latest`, or `final-final`; represent lifecycle through document status and version control instead;
- avoid dates unless chronology is part of the document class, such as decision records, incident reports, migration logs, or time-bounded plans.

Good fallback names are specific enough to remain meaningful after the current task, for example `authentication-flow.md`, `api-compatibility.md`, or `cache-migration-plan.md`.

## 5. Placement policy

Place knowledge near the system that owns it when that improves discoverability and maintenance, while respecting repository conventions.

Prefer a shared documentation area when the knowledge crosses several components or represents a repository-wide contract. Prefer component-local documentation when ownership and validity are component-specific.

Do not create a new directory for a single document unless the repository already uses that taxonomy or the directory represents a durable category expected to contain more material.

Plans and handoffs should not become permanent top-level clutter. Keep them in the repository's existing planning area, colocate them with the project they coordinate, or retire them when their coordination value ends.

## 6. Status and lifecycle

When a reader could mistake target state for current state, make status explicit.

Use the repository's existing status vocabulary when one exists. Otherwise use concise terms appropriate to the artifact, such as:

- specification/design: `proposed`, `accepted`, `implemented`, `superseded` where those distinctions matter;
- plan: `active`, `blocked`, `completed`, `abandoned`;
- constraint or compatibility promise: `active`, `deprecated`, `superseded`;
- fact whose freshness matters: record when or how it was verified rather than inventing a workflow status.

These labels are not a mandatory schema. Use them only where ambiguity would materially affect trust.

An accepted specification or target design that is not implemented must not be presented as current behaviour. A completed plan does not become specification or design. A superseded artifact should point to its replacement when it remains in the repository for operational reasons.

Prefer updating, superseding, or deleting stale artifacts over leaving contradictory documents for future agents to reconcile. Version control is normally the archive for obsolete content.

## 7. Provenance, freshness, and trust

A durable claim should carry enough context for a future reader to judge whether it is still trustworthy.

Record provenance when the source is not obvious from the artifact itself. Link to primary specifications, code, tests, external contracts, decisions, or observed runtime evidence instead of restating them unnecessarily.

Record freshness when truth can decay with environment, deployment, dependency, or external-system changes. Prefer statements such as "verified against X" or "current as of Y" only when that information materially changes trust.

Make uncertainty visible. An explicit unknown or unresolved question is safer than a confident statement whose basis is weak or stale.

## 8. Minimal document contract

Do not impose a universal template, but a durable document should let its intended reader determine, where relevant:

- what subject and scope the artifact owns;
- whether it describes current state, target state, or coordination state;
- which claims are authoritative here and which are references to another source;
- what important constraints, invariants, or trade-offs shape the content;
- what provenance or evidence supports claims whose basis is not obvious;
- what status or freshness information is necessary to interpret it safely.

If an artifact cannot answer the relevant questions without reconstructing the original conversation, it is not yet durable.

## 9. Split, merge, rename, and retire deliberately

### Split when

- one artifact contains sections with different owners or lifecycles;
- one part is canonical while another is transient coordination;
- the document has become difficult to navigate and the resulting boundaries are stable;
- independent consumers need a smaller authoritative unit.

### Merge when

- multiple artifacts make overlapping authoritative claims;
- readers must compare documents to reconstruct one coherent decision or contract;
- separate files have no meaningful lifecycle or ownership distinction.

### Rename or move when

- the current name or location materially harms discoverability or misstates scope;
- repository conventions have an established canonical pattern;
- a structural change has made the old ownership boundary misleading.

Update inbound links and references when renaming or moving documents. Do not create aliases or duplicate copies unless compatibility requires them.

### Retire when

- the knowledge is obsolete and version control is sufficient history;
- a canonical replacement exists;
- a completed transient artifact has no continuing coordination or explanatory value.

Keep obsolete material only when its historical or operational role remains important, and mark that role clearly.

## 10. Persistence test before writing or persisting coordination state

Before creating or expanding durable documentation, ask whether at least one is true:

- another capable agent would likely make a materially worse decision without this knowledge;
- reconstructing it later would be expensive, ambiguous, or risky;
- an existing trusted source would otherwise remain incomplete, stale, or misleading;
- cross-context or cross-agent continuity requires explicit coordination state.

If none apply, prefer leaving the knowledge in code, tests, version history, or the current task report rather than creating another durable artifact.

## 11. Reconcile after consequential work

After consequential work changes, invalidates, or newly establishes durable engineering knowledge:

1. identify durable claims that the change invalidated or made incomplete;
2. update the canonical source rather than adding a competing explanation;
3. update references affected by renames or moves;
4. mark target/current-state distinctions accurately;
5. remove or supersede stale coordination artifacts whose ongoing presence would mislead future work.

Documentation is complete only when the repository no longer presents materially contradictory current truths about the changed system.
