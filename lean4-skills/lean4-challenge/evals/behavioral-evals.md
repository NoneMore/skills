# Real-task evaluation — lean4-challenge

Open-ended mathematical design judgment is difficult to measure with synthetic fixtures whose expected answers are already built into the task. Prefer observation on real Lean/mathlib work over maintaining an exhaustive prompt/fixture matrix.

When a real task is available, preserve the original request, relevant project context, observed Lean/tool evidence, and outcome. Look for:

- A consequential design choice or hidden mathematical abstraction that materially affects the result, including cases where retaining the existing design is best.
- Credible alternatives tested at a decisive boundary or consumer, rather than plausible-sounding suggestions alone.
- The outcome the user actually requested (directions or a supported judgment), honest verification limits, and no production mutations.
- Investigation cost proportionate to its value, including tool use or subagents when relevant.

Promote a concrete, repeatable failure to a targeted regression only when doing so would change a design decision. Do not report unrun observations as PASS. Check frontmatter, reference links, and invocation policy statically.
