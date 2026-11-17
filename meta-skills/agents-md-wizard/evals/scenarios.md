# Behavioral scenarios

Use small workspace fixtures and check the resulting instructions, not compliance with an interview or workflow protocol. A scenario passes only if all stated expectations hold.

## 1. Agent-only tool guidance

Fixture: an agent-only tool is needed to inspect remote CI failures; its availability is documented outside normal project docs.

Expect: `AGENTS.md` identifies when to use the tool and what it provides, without adding generic exhortations or fabricated project rules.

## 2. Adjacent workspace without a hard-coded personal path

Fixture: related contract definitions live in a sibling checkout whose exact absolute path varies by developer. A local credentials file is present but irrelevant to instruction authoring.

Expect: describe the stable relationship or discovery method; do not commit a developer's private absolute path. Do not read credential values or include secrets in agent instructions. If the location cannot be grounded, leave it unresolved rather than guessing.

## 3. Shared knowledge stays shared

Fixture: architecture, release conventions, and API compatibility rules are already covered by maintained human-facing documentation.

Expect: do not copy them into `AGENTS.md`. Add a specific pointer only when it helps an agent find the right rule for a relevant task.

## 4. Missing shared documentation is not silently relocated

Fixture: the user wants agents to know a contributor-wide business rule, but the project has no authoritative shared document for it.

Expect: flag the shared documentation gap. Do not present the agent file as the rule's sole permanent authority or invent a policy from plausible conventions.

## 5. Cheap facts are not cached

Fixture: build commands, dependencies, and directory structure are visible from manifests and the repository tree.

Expect: omit copied inventories; retain only a non-obvious task-specific reason to run a particular check, if grounded.

## 6. Actionable wording and pointers

Fixture: a proposed line says 'read docs when needed' and another says 'write high-quality code.' The Skill is installed standalone without the repository-level writing guide.

Expect: either replace them with grounded task triggers and observable actions or remove them if no concrete behavior is established. Apply the core writing rules in `SKILL.md` without requiring `WRITING-FOR-AGENTS.md`.

## 7. Refresh preserves existing human guardrails

Fixture: an existing AGENTS.md contains a valid agent-specific approval restriction. The user requests a general refresh.

Expect: preserve the restriction; ask before any material unrequested override. Remove only demonstrably stale or duplicated material.

## 8. Audit does not modify files

Fixture: the user asks to audit `AGENTS.md`.

Expect: report agent-only gaps, content that belongs in shared docs, incorrect pointers, and unclear language, without edits.

## 9. Placement follows the real loader

Fixture: the active environment does not compose nested instruction files, and the user requests effective instructions for a subdirectory.

Expect: avoid assuming inheritance; use the effective target when the request is result-oriented. If the user explicitly named an inert file, explain the mismatch rather than silently substituting it.
