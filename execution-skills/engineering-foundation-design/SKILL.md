---
name: engineering-foundation-design
description: "Explicit-only orchestration for establishing or materially resetting a project's foundational engineering architecture, boundaries, contracts, invariants, and conventions. Orthogonal to Small/Medium/Large workload capacity."
disable-model-invocation: true
metadata:
  version: "v5-rc.1"
  invocation: "user"
---

# Engineering Foundation Design

Turn high-ambiguity foundational work into a small, trustworthy engineering contract that later agents can execute without repeatedly reopening architecture.

## Invocation contract

This is a **user-invoked orchestration skill**. Relevance is not permission to invoke it. A greenfield repository, broad architecture question, project-initialization request, or Small/Medium/Large workload label does **not** implicitly enter bootstrap mode unless the user or an upstream Meta-Agent acting under user-selected policy deliberately invokes this skill (or an equivalent runtime command). Without that explicit mode choice, handle the task with the ordinary applicable skills and authority boundaries.

Once invoked, this skill may compose with model-invoked disciplines such as `engineering-implementation` and `engineering-knowledge-governance`; manual invocation does not itself grant repository mutation, VCS, deployment, publication, or other external-effect authority.

Before beginning foundational design, remind the user to verify the execution environment:

- Use a strong-capability model with sufficient reasoning effort for consequential architecture decisions. If model or reasoning configuration is available, check that it is set appropriately rather than assuming the runtime default is sufficient.
- Ensure the environment has network access or web-search capability so current external evidence can inform brainstorming and challenge assumptions.
- Ensure the project has no accepted existing foundational constraints or design, or confirm that the user deliberately intends to replace or supersede the relevant content and accepts the potentially destructive consequences. This design confirmation does not itself authorize repository mutation, deletion, migration, or other external effects.

If any prerequisite is unavailable or cannot be verified, state that limitation before proceeding so the user can decide whether to adjust the environment, explicitly authorize a foundational reset, or continue with reduced evidence. Never treat an uninspected existing project as a blank slate.

Bootstrap is **orthogonal to workload capacity**. A Small explicit task may bootstrap a tiny subsystem; a Large initiative may leave mature foundations untouched. Never map Large to bootstrap automatically.

This is a **bootstrap capability**, not a permanent project-management framework. Once explicitly invoked, it is appropriate when a repository is being created, its architecture is being established, or existing foundations are being materially reset. It is not a default route for routine features, fixes, or local refactors merely because they benefit from planning.

**The goal is not more documents. The goal is fewer unresolved consequential decisions for downstream execution.**

## Capability routing

Foundational design has a high decision burden. When the runtime can choose or delegate models, prefer a stronger-capability model for work involving several of the following:

- project or subsystem initialization;
- architecture and module boundaries;
- public contracts or compatibility strategy;
- persistence, concurrency, security, deployment, or failure-model choices;
- cross-cutting conventions that many later changes must follow;
- irreversible or expensive-to-reverse structure;
- material trade-offs with incomplete evidence.

Do not assume a weaker executor should infer these decisions from implementation details. The bootstrap should make consequential choices explicit enough that later bounded work can be delegated safely.

Model capability does not expand authority. Repository mutation, VCS changes, deployment, publication, credential changes, and other external effects still require authority from the underlying task and applicable execution skills.

## Discover before defining

Before creating foundational artifacts or structure:

- inspect existing repository instructions, documentation, code, tests, build configuration, and history when present;
- identify canonical sources already owning architecture, contracts, conventions, or operational constraints;
- distinguish current state from proposed target state;
- preserve unrelated user work and existing authoritative decisions unless the requested bootstrap explicitly changes them;
- resolve what repository evidence can answer before inventing new policy.

For a greenfield repository, discover the requested product outcome, deployment/runtime environment, compatibility needs, risk profile, and non-goals before committing to structure.

## Minimum engineering contract

A successful bootstrap establishes only the foundational knowledge that materially reduces future ambiguity. Depending on the project, that may include:

1. **Outcome and non-goals** — what the system or subsystem is for and what is intentionally outside scope.
2. **Architecture boundaries** — major components, ownership, dependency direction, and forbidden coupling where it matters.
3. **Critical invariants and constraints** — compatibility, data, safety, security, performance, operational, or environmental requirements that later work must preserve.
4. **External and internal contracts** — APIs, schemas, events, protocols, or interfaces whose stability matters.
5. **Engineering conventions** — only conventions consequential enough that inconsistent choices would materially harm maintainability or correctness.
6. **Verification strategy** — the important evidence classes later implementation should use to prove changes.
7. **Known unresolved decisions** — material questions that remain open, with enough context to prevent accidental assumptions.
8. **Canonical locations** — where future agents should look for the authoritative version of the above.

These are information roles, not required files or headings. Prefer the repository's existing canonical homes. A small project may need only a README plus code and tests; a larger system may justify architecture or decision records.

## Keep the bootstrap thin

Do not create a `.trellis`-like control tree, mandatory `prd/design/implement` files, per-task status records, or duplicated specifications merely to satisfy this skill.

Persist information only when future work would be materially worse without it. Apply `engineering-knowledge-governance` when available for canonicality, placement, lifecycle, provenance, and reconciliation decisions.

Prefer:

- one canonical architecture source over parallel summaries;
- accepted decisions over exhaustive rationale transcripts;
- executable contracts and tests where they are the best source of truth;
- links to canonical sources over copied context;
- explicit unknowns over invented completeness.

## Bootstrap and implementation

When bootstrap work also includes authorized repository mutation, use `engineering-implementation` when available. Otherwise preserve unrelated work, make only scoped changes, verify intended behaviour and critical constraints, and report evidence gaps. This skill defines foundational direction; it does not replace coding execution rules.

Do not let implementation convenience silently redefine the architecture being established. If evidence falsifies a foundational assumption, revise the design deliberately and reconcile affected canonical knowledge before delegating further work.

## Exit condition

Bootstrap is complete when the next meaningful implementation tasks can be planned and executed **without requiring their executors to make new consequential architecture or product decisions by accident**.

Before handing off, ensure another capable agent can determine:

- the target outcome and important non-goals;
- the accepted architecture and critical constraints relevant to future work;
- which decisions are fixed versus still open;
- where canonical specifications and design decisions live;
- what evidence future changes should use;
- which work should still return to a stronger planning/design capability rather than being decided locally.

Do not continue polishing architecture documents after this condition is met unless the user requested deeper design work.
