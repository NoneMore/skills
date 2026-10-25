---
name: bootstrap-project
description: Bootstrap or adapt a project's code-first governance conventions for architecture knowledge, ADR history, and change-centered work. Use when the user explicitly asks to set up or revise this project practice.
disable-model-invocation: true
---

# Bootstrap Project Governance

## Purpose

Establish or adapt a human-readable project governance practice for organizing implementation knowledge, architectural decisions, and change-centered work.

## Accepts

A repository or project and a request to bootstrap, adopt, or revise its project-governance conventions. A request for advice or a preview is read-only; an explicit setup or update request authorizes changes within the requested project scope.

## Owns

- expressing the code-first authority model and the distinct purposes of architecture, ADRs, and change work;
- selecting the smallest project-local conventions and file organization that fit the request and existing project practice;
- establishing or adapting those conventions within the authorized project scope;
- making the resulting conventions discoverable and usable by human contributors as well as agents.

## Recommended practice

Use these defaults when the project has not established its own conventions.

### Human-first governance entry

- **Project governance is for people first.** Write shared project-governance conventions in a discoverable, human-readable project document, such as an established contributor guide or `docs/governance.md`. Make it reachable from the project's README or existing contributor entry point. This document is the canonical home for the shared rules.
- **Agent instructions are an adapter.** When useful, keep `AGENTS.md` or an established equivalent as a brief pointer to the human-facing conventions, with any genuinely agent-specific instructions kept separate from the shared rules.

### Authority and knowledge

- **Code first.** Code is the primary evidence of behavior implemented in the repository. Actual runtime behavior may also depend on deployment configuration and operational evidence. Documentation, including comments, supports interpretation but cannot override implementation evidence. A proposed design or specification may describe a *future* target, not current implemented behavior.
- **Comments are code-adjacent documentation.** Use them to preserve non-obvious, durable local knowledge, such as rationale, invariants, constraints, and intended interface semantics that the code does not make sufficiently clear. Keep comments close to relevant code; avoid restating obvious behavior or duplicating implementation details. High-level architectural understanding belongs in architecture documentation, and consequential architectural decision history belongs in ADRs. When code and comments materially disagree during a task, distinguish actual behavior from intended behavior rather than assuming either establishes correctness. Address or report the discrepancy within the task's scope.
- **Development documentation can provide a practical entry point.** When setup, build, run, or test guidance is useful, prefer an existing developer or contributor guide, or a focused `docs/development.md` when a separate entry point is warranted. Keep such guidance concise and actionable, pointing to relevant scripts and configuration rather than documenting their internals. Keep existing guidance accurate as documented workflows change; unrelated implementation work does not require documentation updates.
- **Architecture summarizes the implemented system.** Describe current high-level structure, responsibilities, boundaries, useful pointers to code, and the architectural outcomes of implemented decisions in `docs/architecture/`. It may also express directional, non-prescriptive design goals, distinguished from implemented facts. Avoid duplicating fine-grained code behavior or ADR rationale; consult code for implementation details.
- **ADRs preserve architectural decision history, not the current design registry.** Keep consequential architectural decisions, their context, alternatives, and rationale in `docs/adr/` when the reasoning would be costly to reconstruct. Once a decision is implemented, reflect its architectural outcome in architecture documentation without copying its historical reasoning. Ordinary project work need not read ADRs unless historical rationale matters.
- **Supersession points backward.** A new ADR names any older ADRs it fully or partially supersedes and describes the affected decision. Do not add status fields or edit an old ADR to point forward. An older ADR can move to `docs/adr/archive/` even after partial supersession; applicable implemented architectural outcomes remain visible through architecture docs, and archived ADRs remain available for history.
- **Read according to the question.** Start with existing development guidance, when available, for setup, build, run, and test instructions, architecture documentation for high-level understanding and code navigation, code for repository implementation, applicable Change materials for proposed work, and relevant ADRs for decision rationale or history. Reading order does not establish authority precedence. Do not require reading every artifact type for every task.
- **Avoid duplicate authorities.** Keep change-scoped specifications tied to their change instead of maintaining a permanent fine-grained catalog of implemented behavior or requirements.

### Change-centered work

- **A Change is a bounded, cohesive change intent**, not a task, PR, forced lifecycle phase, or child of another Change. It may span tasks or PRs; related work can share a Change, independent intentions can have separate Changes. Do not require a Change for every trivial edit.
- Use `specs/active/<change>/` for the current work context, and `specs/archive/<change>/` for changes no longer being advanced (including completed, cancelled, or superseded work). `active` does not mean implementation-ready; `archive` does not prove implementation, validity, or ongoing applicability.
- A Change directory has **no mandatory files**. It may hold `design.md`, `spec.md`, `tasks.md`, or other useful materials. A task-scoped spec is for the change, not a permanent project-level behavior authority. Archived work is historical context, not a maintained specification.
- When revising an active change-scoped specification, update it in place to reflect the settled requirements. Archived specifications remain historical and are not synchronized with later implementation changes.
- Keep execution state such as owners, priorities, and progress in the existing tracker when one is used. Put work breakdown or dependencies in `tasks.md` only if it adds value; do not maintain the same volatile state in two places. Git, tests, and PRs retain implementation and verification evidence.
- Change materials may inform an ADR for consequential architectural decisions or an architecture update after implementation. These remain separate activities, guided by their respective purposes.

A default layout (adapt names and locations to project conventions) is:

```text
project/
├── README.md                 # links to the project's governance entry
├── AGENTS.md                 # optional, concise agent-facing pointer
├── src/                      # existing code layout; do not restructure
├── tests/                    # existing test layout; do not restructure
├── specs/
│   ├── active/
│   │   └── <change>/
│   │       ├── design.md     # optional
│   │       ├── spec.md       # optional
│   │       └── tasks.md      # optional
│   └── archive/
│       └── <change>/
└── docs/
    ├── governance.md         # human-readable, canonical shared conventions
    ├── development.md        # optional developer setup, build, run, and test entry
    ├── architecture/
    └── adr/
        └── archive/
```

The layout illustrates possible locations; use existing project conventions and create directories as needed.

## Approach

1. **Scope the request.** Identify the target project and whether the user wants a proposed convention, initial setup, or adaptation of existing conventions.
2. **Inspect locally relevant evidence.** Read the contributor documentation, project instructions, and relevant code/document/change structure needed to place the conventions and preserve existing project practice.
3. **Adapt rather than replace.** Prefer an established human-facing contributor document for shared governance, or create a focused human-readable document and link it from the existing README/contributor entry. Keep `AGENTS.md` (or the project's established equivalent) as a short pointer when useful.
4. **Create only useful artifacts.** Establish the requested conventions through useful content rather than empty placeholders.
5. **Verify the result.** Check the changed files and local links, including a human-facing path to the governance conventions and any agent-facing pointer. Preserve existing policy outside the authorized scope, and report what was created or adapted, what remains a recommendation, and any material limitation.

## Stop conditions and completion

- If a requested edit would overwrite relevant existing human policy without clear authorization to change it, or its destination is materially ambiguous, keep the unaffected work intact and surface only the blocking choice. If writing is not authorized or possible, provide a concrete suggested layout or edit instead of claiming setup succeeded.

Done when the requested project practice is concretely established or adapted in a human-discoverable project location (with only necessary agent-facing navigation), or a read-only recommendation is delivered, with the actual changed paths and any material limits stated.
