# Writing for Agents

This reference is for wording **instructions written specifically for agent consumption**. It helps express an already-settled behavioral contract; it does not decide whether a Skill, workspace instruction, reference, or workflow should exist. [Skill Design Principles](SKILL-DESIGN-PRINCIPLES.md) remains the authority for those design decisions.

## Scope

Apply to agent-only text such as `SKILL.md`, `AGENTS.md` / `CLAUDE.md`, agent-facing reference files, and runtime instructions. A document being readable or retrievable by an agent does not make it agent-only. Do not optimize human-facing or shared documents (including READMEs, governance, architecture notes, ADRs, and specifications) for agent context at the expense of human readers.

For workspace instruction files, `agents-md-wizard` owns target selection, loader semantics, and preservation of existing human policy; this reference only informs the wording of content whose authority and scope are already established. Do not treat these writing suggestions as permission to alter policy.

## Instruction Precision

- Name the condition under which an instruction applies when the distinction changes behavior. Use conditions an agent can determine from the task and available evidence.
- State the consequential action, constraint, or result. Resolve ambiguity that changes a decision or outcome, but leave room for judgment when a rigid procedure would be worse.
- For a pointer to another resource, say **what it contains** and **when to consult it**. Check for both missed relevant reads (trigger too narrow) and unnecessary reads (trigger too broad).
- Do not force every sentence into a condition/action template. Add precision where it changes what the agent does.

**Pointer example (illustrative):**

Before:

> Read `docs/testing.md` when needed.

After:

> When changing snapshot generation or test fixtures, read `docs/testing.md` for the repository's test-data conventions before editing.

The revised pointer describes a recognizable trigger and why the material matters, without requiring that reference for unrelated edits.

## Behavioral Leverage

- Prefer task-specific information the agent cannot safely infer: meaningful constraints, exceptions, dependencies, observable checks, and decisions.
- Replace generic exhortations with a concrete requirement only when the task actually has one. Instructions such as *be careful*, *think harder*, or *follow instructions correctly* do not themselves supply missing behavior.
- Preserve justified prohibitions and safeguards; writing style must not erase a real policy constraint or pretend prose can enforce runtime permissions.

**Requirement example (illustrative):**

Before:

> Be thorough when updating database migrations.

After:

> For a migration that renames a field, verify that readers and writers handle the old and new names across the supported compatibility window.

The second instruction names work that can be checked; it does not ask the model to become generally more diligent.

## Instruction Economy

- Remove stale details, repeated policy, and copies of repository state that tools or maintained files can recover cheaply. Keep non-obvious conventions, rationale, and constraints that a lookup would not reveal.
- Keep each durable rule in its authoritative location; link to it at the point of need rather than paraphrasing it throughout the instruction set.
- Treat a suspected no-op as a model-, runtime-, and task-dependent hypothesis. Prune it when removing it does not introduce a meaningful execution or verification regression; do not infer uselessness from terse wording alone.
- Prefer deleting a behaviorally inert instruction to replacing it with a different motivational slogan.

**Pruning example (illustrative):** instead of maintaining a stale list of currently available check commands, point to the project manifest or build configuration where those commands are defined, while retaining any non-obvious rule about which check a particular change requires.
