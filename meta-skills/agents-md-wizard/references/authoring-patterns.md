# Authoring patterns

Use this reference only when the core authoring rules leave a concrete drafting or migration problem unresolved. It is a pattern library, not a second policy specification.

## Prefer behavior over description

Weak:

```md
Be careful with data and write high-quality analysis.
```

Stronger:

```md
Treat `raw/` as captured evidence. Write transformations to `processed/`; do not overwrite inputs.
Before reporting a metric, use the definition in `metrics.md` and make the transformation reproducible.
```

A rule earns space when removing it would make a downstream agent meaningfully more likely to make an expensive mistake.

## Use task-triggered pointers

When another maintained document owns detailed truth, point to it at the moment it matters:

```md
For publication edits, follow `docs/editorial-style.md`; keep detailed terminology and formatting rules there.
```

Avoid copying whole style guides, schemas, metric definitions, command catalogs, or directory trees into the instruction artifact.

## Make completion observable

Prefer concrete completion conditions over generic “test your work” language:

```md
After changing the parser, run `./scripts/check-parser` and report the result.
Do not claim clean completion while that check is failing.
```

Useful completion rules name an observable file update, validation command, synchronization step, traceability condition, or required report.

## Write local deltas compactly

When the active topology establishes overlay composition, omit inherited policy:

```md
# Local instructions

`published/` is generated from `source/`. Make corrections in the source/generation path rather than hand-editing published output.
```

Do not add inheritance disclaimers or copy root policy for convenience.

## Migrate existing policy minimally

Classify existing lines before editing:

- **retain** — still valid and behaviorally useful;
- **sharpen** — valid intent, vague expression;
- **remove** — verified stale, duplicated, or no longer behaviorally useful;
- **conflict** — cannot be resolved from evidence and needs a human decision.

Show semantic-preserving edits in the ordinary pre-write review along with material removals, rewrites, target choices, or overrides. Ask separate policy questions only when the underlying decision is unresolved; otherwise one reviewable proposal and one approval gate are enough.

## Keep instruction weight low

Common candidates for deletion:

- generic quality slogans;
- obvious facts already visible in manifests/config;
- exhaustive workspace maps;
- transient inventories or versions;
- duplicated maintained documentation;
- branch-only rules placed globally;
- repeated warnings that do not add a distinct behavior.

Prefer short sections with direct imperatives and exact paths. Hard guardrails should be unmistakable, but not repeated in multiple forms.
