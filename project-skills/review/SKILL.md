---
name: review
description: Independently evaluate an existing result and produce evidence-backed findings against the expectations relevant to the requested review. Use for code or PR review, implementation-vs-spec verification, design review, spec review, plan or decomposition review, or other concrete existing results.
disable-model-invocation: true
---

# Review

## Purpose

Determine where an existing result does or does not meet the expectations relevant to the requested review.

## Accepts

Code, diffs, pull requests, current implementations, designs, specifications, plans, decompositions, prototypes, and other sufficiently concrete results.

## Owns

- criteria appropriate to the reviewed object and the user's review intent rather than a universal checklist;
- evidence-backed findings that distinguish violated expectations and material risks from preferences or speculation;
- independent verification of material claims instead of treating the producer's explanation as proof;
- a review result that does not require producing the replacement artifact in order to be complete.

When the intent or expected behavior is available, checking whether the existing result satisfies it is ordinary review. No separate reconciliation phase is required.

## Specialized guidance

Load object-specific guidance only when relevant:

- [code.md](references/code.md) for diffs, PRs, or current implementations;
- [design.md](references/design.md) for architecture and design directions;
- [spec.md](references/spec.md) for specifications or requirements artifacts;
- [decomposition.md](references/decomposition.md) for ticket or work breakdowns.

## Done when

Material findings relevant to the requested review are substantiated with enough evidence to explain what expectation is met or violated, where the evidence comes from, and why the issue matters. If no material findings remain, say so and state any meaningful coverage limits.

## Does not require

A tracker lifecycle, a fresh diff, two fixed review axes, a replacement implementation, or a follow-up capability.
