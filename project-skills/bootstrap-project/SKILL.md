---
name: bootstrap-project
description: Bootstrap or adapt a project's code-first governance conventions for architecture knowledge, ADR history, and change-centered work. Use when the user explicitly asks to set up or revise this project practice.
disable-model-invocation: true
---

# Bootstrap Project Governance

## Purpose

Establish or adapt a lightweight, complete **recommended project practice** for people working on the project, including agents. The governance convention belongs to the project, not to the invoking agent or this skill. This is a user-invoked setup capability, not a coordinator or prerequisite for `design`, `specify`, or `decompose`.

## Accepts

A repository or project and a request to bootstrap, adopt, or revise its project-governance conventions. A request for advice or a preview is read-only; an explicit setup or update request authorizes changes within the requested project scope.

## Owns

- expressing the code-first authority model and the distinct purposes of architecture, ADRs, and change work;
- selecting the smallest project-local conventions and file organization that fit the request and existing project practice;
- setting up or adapting those conventions without overwriting unrelated project policy;
- making the resulting conventions discoverable and usable by human contributors as well as agents.

## Recommended practice

Use these defaults when the project has not chosen another practice. They are recommendations, **not** runtime rules or obligations imposed on other skills.

### Human-first governance entry

- **Project governance is for people first.** Write shared project-governance conventions in a discoverable, human-readable project document, such as an established contributor guide or `docs/governance.md`. Make it reachable from the project's README or existing contributor entry point. This document is the canonical home for the shared rules; do not rely on `AGENTS.md` as the sole or primary governance document.
- **Agent instructions are an adapter, not a second authority.** When useful, keep `AGENTS.md` or an established equivalent as a brief pointer to the human-facing conventions, plus only truly agent-specific instructions. Do not duplicate the governance rules there or assume a particular filename is loaded without evidence of the runtime's behavior.

### Authority and knowledge

- **Code first.** Where code exists, it is the first authority on implemented behavior and system reality. Documentation, including comments, is supporting information; it cannot override the code. A proposed design or specification may describe a *future* target, not current implemented behavior.
- **Architecture summarizes the implemented system.** Describe current high-level structure, responsibilities, boundaries, useful pointers to code, and the architectural outcomes of implemented decisions in `docs/architecture/`. It may also express directional, non-prescriptive design goals, distinguished from implemented facts. Avoid duplicating fine-grained code behavior or ADR rationale; consult code for implementation details.
- **ADRs preserve architectural decision history, not the current design registry.** Keep consequential architectural decisions, their context, alternatives, and rationale in `docs/adr/` when the reasoning would be costly to reconstruct. Once a decision is implemented, reflect its architectural outcome in architecture documentation without copying its historical reasoning. Ordinary project work need not read ADRs unless historical rationale matters.
- **Supersession points backward.** A new ADR names any older ADRs it fully or partially supersedes and describes the affected decision. Do not add status fields or edit an old ADR to point forward. An older ADR can move to `docs/adr/archive/` even after partial supersession; applicable implemented architectural outcomes remain visible through architecture docs, and archived ADRs remain available for history.
- **Read according to the question.** Start with architecture documentation for high-level understanding and code navigation, code for actual implemented behavior, applicable Change materials for proposed work, and relevant ADRs for decision rationale or history. Reading order is not authority precedence: code remains authoritative about what is implemented. Do not require reading every artifact type for every task.
- **Avoid duplicate authorities.** Do not maintain a long-lived fine-grained specification catalog for current implemented behavior or permanent requirements. Small-grained as-is facts belong in code (comments only where helpful); high-level understanding belongs in architecture docs. Preserve historical work without treating it as current authority.

### Change-centered work

- **A Change is a bounded, cohesive change intent**, not a task, PR, forced lifecycle phase, or child of another Change. It may span tasks or PRs; related work can share a Change, independent intentions can have separate Changes. Do not require a Change for every trivial edit.
- Use `specs/active/<change>/` for the current work context, and `specs/archive/<change>/` for changes no longer being advanced (including completed, cancelled, or superseded work). `active` does not mean implementation-ready; `archive` does not prove implementation, validity, or ongoing applicability.
- A Change directory has **no mandatory files**. It may hold `design.md`, `spec.md`, `tasks.md`, or other useful materials. A task-scoped spec is for the change, not a permanent project-level behavior authority. Archived work is historical context, not a maintained specification.
- Keep execution state such as owners, priorities, and progress in the existing tracker when one is used. Put work breakdown or dependencies in `tasks.md` only if it adds value; do not maintain the same volatile state in two places. Git, tests, and PRs retain implementation and verification evidence.
- Change materials may inform architecture updates or an ADR when a lasting high-level decision merits it, but this is not an automatic conversion, synchronization, or review workflow.

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
    ├── architecture/
    └── adr/
        └── archive/
```

The layout is illustrative, not a demand to create empty directories or placeholder documents.

## Approach

1. **Scope the request.** Identify the target project and whether the user wants a proposed convention, initial setup, or adaptation of existing conventions. Do not treat skill invocation alone as permission to edit.
2. **Inspect locally relevant evidence.** Read the existing contributor documentation, project instructions, and relevant code/document/change directory structure only as needed to avoid misplacing or overwriting content. Do not conduct a project-wide completeness or conflict audit, or try to resolve unrelated inconsistencies.
3. **Adapt rather than replace.** Prefer an established human-facing contributor document for shared governance, or create the smallest useful human-readable document and link it from the existing README/contributor entry. Keep `AGENTS.md` (or the project's established equivalent) as a short pointer when useful; do not copy the governance document, the whole skill, or easily rediscovered repo facts. Do not assert a runtime loads a filename without evidence of its loader semantics.
4. **Create only useful artifacts.** Establish locations through real content as requested; do not require stub specs, ADRs, tasks, indexes, schemas, approval gates, status machines, or a hierarchy of Changes. Do not rewrite production code merely to bootstrap governance.
5. **Verify the result.** Check the changed files and local links, including a human-facing path to the governance conventions and any agent-facing pointer. Preserve existing policy outside the authorized scope, and report what was created or adapted, what remains a recommendation, and any material limitation.

## Boundaries and completion

- Projects may adopt, modify, ignore, or contradict these defaults. Do not secretly enforce them through `design`, `specify`, `decompose`, or other skills; all remain independently user-invoked.
- Do not require an agent to search for conflicting documents, audit completeness, reconcile design/spec/work artifacts, or propagate changes across them. Follow applicable existing project instructions for the task at hand without inventing additional obligations.
- If a requested edit would overwrite relevant existing human policy without clear authorization to change it, or its destination is materially ambiguous, keep the unaffected work intact and surface only the blocking choice. If writing is not authorized or possible, provide a concrete suggested layout or edit instead of claiming setup succeeded.

Done when the requested project practice is concretely established or adapted in a human-discoverable project location (with only necessary agent-facing navigation), or a read-only recommendation is delivered, with the actual changed paths and any material limits stated.
