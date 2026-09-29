---
name: writing-for-agents
description: Designing and writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Reference for writing any document an agent consumes: a skill, an `AGENTS.md` / `CLAUDE.md`, a doc reached by a pointer. The packaging differs; the writing does not: the same levers make each one predictable, since the agent takes the same _process_ every run rather than producing the same output.

When the document you're writing is a skill, read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills.

## Principles and heuristics

Keep architectural rules separate from model-dependent prompting tactics. **Context pointers, the two loads, information hierarchy, completion criteria, single sources of truth, and environment-backed facts are design principles**: use them as defaults because they describe where information lives and how work is bounded. **Leading words, pointer-term ordering, positive-vs-negative phrasing, and hiding later steps are heuristics**: their effect can vary by model, task, and surrounding context.

Treat a heuristic as a hypothesis about an observable effect, not as a law about model internals. Validate it empirically when the distinction matters, the cost is material, or observed behaviour is ambiguous; otherwise keep the claim appropriately tentative and prune it when evidence shows no useful effect.

## Context pointers

A **context pointer** is a reference held in the agent's context that names some out-of-context material and encodes the condition for reaching it. A skill's description is one; a line in `AGENTS.md` naming a doc is the same object. The pointer's _wording_, not its target, decides when the agent reaches the material, and how reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

A pointer does two jobs: state what the material is, and list the **branches** that should trigger reaching it (a branch is a distinct case the document handles, so different runs take different paths through it). Every word of an always-loaded pointer costs on every turn, so it earns even harder pruning than the body:

- **Include a discriminating term**: name the capability, branch, or domain concept that should trigger the pointer, rather than relying on generic identity or prose.
- **One trigger per branch.** Synonyms that rename a single branch are one branch written twice; collapse them and keep only genuinely distinct branches.
- **Cut identity the body already carries.**

## The two loads

Every document and pointer you add spends one of two budgets:

- **Context load** is the cost of always-loaded material on the agent's window: an `AGENTS.md` line, a skill description, anything sitting in context every turn, spending tokens and attention whether or not it fires.
- **Cognitive load** is the cost on the human: which documents exist and when to reach for each. The human is the index. Not a cost to minimise: it is the price of human agency; spend it where human judgement matters, remove it where it does not.

Material reached only through a pointer escapes context load at the price of the pointer's own line; material with no pointer at all rides entirely on cognitive load.

## Information hierarchy

A document is built from two content types: **steps** (the ordered actions the agent performs) and **reference** (definitions, rules, facts consulted on demand). The two mix freely: all steps (a recipe), all reference (a review's rules, this skill), or both. The core decision is where each piece sits on the **information hierarchy**, a ladder ranked by how immediately the agent needs the material:

1. **In-file step** is the primary tier: what the agent does, in order.
2. **In-file reference** is consulted on demand. Often a legitimately flat peer-set (every rule of a review on one rung), which is a fine arrangement, not a smell.
3. **Disclosed reference** is pushed out into a separate file, reached by a context pointer, loaded only when the pointer fires. Spans a sibling file in the same folder through fully external reference that lives anywhere and any document can point at.

Push too little down and the top bloats; push too much and you hide material the agent actually needs. That tension is the whole decision.

**Progressive disclosure** is the move down the ladder (out of the main file and behind a pointer) so the top stays legible. Not primarily a token optimisation: it is how the hierarchy is protected. Branching is the cleanest disclosure test: inline what every branch needs, and push behind a pointer what only some branches reach. When a document has steps, in-file reference that should be disclosed buries them and turns attending to them into a coin-flip: a variance lever, not just a legibility one.

**Co-location** is the within-file companion: where the ladder decides _how far down_ a piece sits, co-location decides _what sits beside it_ once there. Keep a concept's definition, rules, and caveats under one heading rather than scattered, so reading one part brings its neighbours with it. The test: the document should read like documentation written for the agent. Grouped material reads that way; scattered material does not. (Distinct from duplication: that repeats one meaning in two places; scattering fragments one meaning across many.)

**Sprawl** is the failure mode here: a document simply too long, even when every line is live and unique. Attention thins across the excess, and every extra line is one more to keep relevant. The cure is the ladder: disclose reference behind pointers, and split by branch or sequence so each path carries only what it needs.

## Steps and completion criteria

Every step ends on a **completion criterion**, the condition that tells the agent the work is done. Two properties make it a lever:

- **Clarity**: can the agent tell done from not-done? A vague bound ("understanding reached") invites **premature completion**: ending the step before it is genuinely done, attention slipping to _being done_. Defend in order: **sharpen the bound first** (local and cheap). If the agent still rushes and visible later steps are a plausible contributor, test splitting the sequence across a real context boundary (a hand-off or subagent dispatch). Treat that split as a mitigation to validate when the added indirection or behavioural difference matters, not a default law of agent behaviour.
- **Demand**: how much it requires. "Every modified model accounted for" forces thorough work where "produce a change list" does not. Demand drives **legwork** (the digging the agent does within the work, latent in the wording rather than written as its own step), and it is not step-bound: "every rule applied" binds a body of flat reference just as "every step done" binds a sequence, which is how an all-reference document still carries an exhaustiveness bar.

The strongest criteria are both checkable and exhaustive.

## When to split

Splitting one document into two spends one of the two loads, so split only when the cut earns it:

- **By sequence**: split when a step has an irreducibly fuzzy completion bound and you observe premature completion for which visible later steps are a plausible contributor. Prefer a sharper criterion first; sequence splitting adds indirection, so validate the split empirically when that tradeoff matters.
- **By invocation**, skill-specific: see [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md).

## Heuristics to validate

The techniques in this section can improve behaviour, but their effect is model-relative. Treat each as a hypothesis about an observable effect. Use representative evals when the distinction matters enough to justify fixing the model, task, sampling, and grader; otherwise prefer direct observation and appropriately tentative wording.

### Pointer term ordering

Front-loading a discriminating term may improve routing by making the relevant capability, branch, or domain concept salient before explanatory detail. Token-order effects are model- and context-dependent, so use this as a tuning option when routing is weak or pointer space is tight, and validate it when the difference matters.

### Leading words

A **leading word** is a compact, shared concept the agent can use while running the document (_lesson_, _fog of war_, _tracer bullets_). Prefer established domain language that already lives in the model's pretraining and, ideally, in the humans, docs, and code around the task. A coined term can still work, but it needs enough definition to become useful.

A good leading word compresses a repeated concept without weakening its contract. It may help in two places:

- **Execution**: repeating the same compact term can focus attention on the same class of behaviour.
- **Invocation**: using the same domain term in prompts, docs, and code can give a context pointer a sharper trigger.

Examples of useful compression:

- "fast, deterministic, low-overhead" → _tight_ (a _tight_ loop).
- "a loop that demonstrably reproduces the bug" → _red_ (the loop goes _red_ on the bug, or it does not).

Do not replace a precise completion criterion or safety boundary with a clever label. The label is compression, not the contract. If the word adds no useful routing, execution, or concision in practice, prune it.

### Positive phrasing and hard boundaries

Prefer stating the **target behaviour** directly when a positive target exists. "Write one-line comments that explain why" gives the agent an action to perform; a prohibition that only names an unwanted behaviour may be less useful.

Explicit negation still earns its place for **hard boundaries**: safety constraints, irreversible side effects, permission gates, policy rules, and invariants where the forbidden action itself must be unambiguous. Pair the boundary with the desired action when both matter:

- "Create a migration that preserves existing data."
- "Never drop a production column without explicit approval."

Evaluate wording by observed behaviour, not by a universal claim about how every model processes negation.

## Pruning

- Keep each meaning in a **single source of truth**: one authoritative place, so changing the behaviour is a one-place edit. **Duplication** (the same meaning in more than one place) costs maintenance and tokens, and inflates a meaning's prominence on the ladder past its real rank. (The accidental inverse of a leading word, which repeats a token on purpose, never the meaning.)
- The **environment** is a source of truth too (`package.json` scripts, config files, the directory layout, `--help` output), and a document that restates it is a **cache**: a copy of a lookup, earning its load only when the lookup is expensive. Cache what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses. Leave the one-file, one-command lookups to the environment, where they cannot go stale.
- Check every line for **relevance**: does it still bear on what the document does? A line loses relevance by never bearing on the task (mere exposition, or a branch that should be disclosed) or by going stale as the behaviour or world it describes changes. Shorter documents are easier to keep relevant. Without a pruning discipline the default fate is **sediment**: stale layers that settle because adding feels safe and removing feels risky, until you must core down through them to find what is still live.
- Hunt **no-ops** sentence by sentence: an instruction the model already obeys by default pays load to say nothing. The test is model-relative: compare behaviour and outcomes with and without the instruction, using representative evals when the distinction is important enough to warrant a stable harness. If it creates no useful difference, delete it rather than polishing it. The same test applies to leading words and other heuristics; stronger wording is only useful when it produces a useful observed improvement.
