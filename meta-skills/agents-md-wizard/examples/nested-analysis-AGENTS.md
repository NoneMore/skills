# AGENTS.md

## Scope

These instructions add to the workspace-level `AGENTS.md` for analysis work under this directory.

## Data lifecycle

Treat `raw/` as immutable captured input. Write cleaned and transformed data to `processed/`, preserving enough metadata to reproduce the transformation.

`metrics.md` is the source of truth for metric definitions. When a notebook or report disagrees with it, reconcile the definition before reporting a result.

## Claims

Separate descriptive results from causal claims. Record assumptions when an interpretation depends on data quality, exclusions, or modeling choices.

## Completion

Analysis work is complete when reported metrics trace to `metrics.md`, transformations are reproducible from preserved inputs, and material limitations are stated.
