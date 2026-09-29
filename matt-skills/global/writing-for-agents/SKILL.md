---
name: writing-for-agents
description: Designing and writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Reference for writing documents an agent consumes: skills, `AGENTS.md` / `CLAUDE.md`, and docs reached through pointers. The packaging differs; the writing principles do not.

When the document is a skill, also read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation, and router mechanics.

## Core defaults

- Put information at the lowest level where it is reliably available when needed.
- Make important work end in a checkable completion condition.
- Keep each meaning in one authoritative place.
- Do not restate facts the environment can reveal cheaply.
- Keep model-dependent prompting tactics only when they improve observed behaviour.

## Context pointers

A **context pointer** is always-loaded text that names out-of-context material and says when to reach it. A skill description is one; a line in `AGENTS.md` pointing to another doc is another.

A good pointer does two jobs:

1. says what the target contains;
2. names the distinct cases that should trigger loading it.

Prefer discriminating capability, branch, or domain terms over generic prose. Avoid redundant trigger synonyms unless they materially improve routing. Do not spend pointer text repeating identity already obvious from the target.

If required material is routinely missed, sharpen the pointer before inlining the whole target.

### Two costs

Information placement trades two costs:

- **Context load**: material carried in the agent's context whether or not it is needed.
- **Cognitive load**: material the human must remember exists and know when to invoke.

Always-loaded pointers spend context load. Material with no pointer spends cognitive load. Neither cost should be minimized blindly; place information according to who must discover it and when.

## Put information at the right level

Think in three levels:

1. **In-file steps** — actions the agent should perform in order.
2. **In-file reference** — rules, definitions, or facts used while doing those steps.
3. **Disclosed reference** — material moved to another file and loaded only through a pointer.

Use progressive disclosure to keep the main path legible. A simple test is branching: inline what every path needs; move branch-specific material behind a pointer.

Within a file, keep a concept's definition, rules, and caveats together instead of scattering them across sections.

Split a document only when the cut earns its added indirection. Common reasons are:

- materially different branches need materially different context;
- a capability should be independently discoverable;
- a step still ends prematurely after its completion condition has been made as clear as possible, and separating later work is worth testing.

Prefer a sharper local instruction before adding another document or hand-off.

## Bound the work

Every important step should end on a **completion criterion**: a condition that lets the agent tell done from not-done.

Good criteria are:

- **checkable** — the agent can verify whether the condition holds;
- **appropriately exhaustive** — they state the scope that must be covered.

For example, "produce a change list" leaves scope open; "account for every modified model" sets an exhaustiveness bar.

When work ends too early, improve the completion condition first. Add workflow machinery only when the simpler bound does not produce reliable behaviour.

## Keep one source of truth

Put each meaning in one authoritative place. Duplicating the same rule across files increases maintenance cost, consumes context, and makes stale copies more likely.

The environment is also a source of truth. Files such as `package.json`, config, directory structure, generated schemas, and `--help` output often answer questions more reliably than prose.

Treat documentation that restates such facts as a cache. Keep the cache only when the lookup is expensive or the prose adds something the environment cannot reveal, such as:

- an unwritten convention;
- the reason behind a choice;
- a non-obvious constraint or gotcha.

Leave cheap one-file or one-command lookups to the environment.

## Prune aggressively

Review instructions for three failure modes:

- **irrelevant** — the line does not bear on the task or belongs only to a narrower branch;
- **stale** — the behaviour or environment it describes has changed;
- **no-op** — removing it does not materially change model behaviour.

Delete no-ops instead of polishing them. Shorter documents make important instructions easier to notice and easier to keep current.

For model-dependent wording choices, compare behaviour with and without the instruction when the distinction matters. Use representative evals when the cost or impact justifies a stable harness; otherwise rely on direct observation and keep claims tentative.

## Optional tuning

These techniques can help, but they are not architectural rules and their effects vary by model and context:

- **Shared vocabulary:** reuse compact, established domain terms when they genuinely compress repeated instructions or sharpen routing. Do not replace a precise contract with a clever label.
- **Positive phrasing:** state the target behaviour directly when possible. Use explicit negation for hard boundaries such as safety constraints, irreversible side effects, permission gates, and invariants.
- **Pointer ordering:** putting a discriminating term early may improve routing when pointer space is tight.

Keep these tactics only when they produce a useful observed effect.
