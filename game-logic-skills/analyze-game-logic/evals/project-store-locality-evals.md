# Project-store locality behavioral evals

These scenarios exercise the durable-storage branch of `analyze-game-logic`. They protect semantic locality decisions; deterministic path/schema enforcement remains the responsibility of `scripts/project_store.py` and its self-tests.

## 1. Durable evidence stays with its analysis and target

A focused analysis of reload timing for build `25186522` produces one reusable finding, separate static/runtime retained evidence, a small analysis script, and a target-specific report. Persistence is already warranted.

Required assertions:
- established a stable analysis scope and explicit target/build scope before the final finding had to exist
- kept game/build facts in target-scope metadata instead of asking the agent to retype them independently for every child artifact
- placed the primary finding under `analyses/<analysis-id>/targets/<target-id>/finding.md`
- placed target-specific retained evidence, scripts, and reports under that same target scope with sibling-local names such as `static.txt`, `runtime.txt`, `analyze.py`, and `analysis.md`
- did not repeat analysis/build prefixes in filenames when the parent path already supplied that context
- kept content hashes, producer/provenance, dependency edges, evidence links, supersession, and artifact-specific locators in the manifest rather than trying to encode them into directories
- treated any project-level report as an index/rollup rather than the default body for the mechanic
- did not claim that copying the analysis directory alone creates a provenance-complete export

## 2. Cross-analysis evidence is retained once as shared evidence

One expensive observation log materially supports both `reload-animation-timing` and `offline-player-accuracy`; neither analysis is its natural sole owner.

Required assertions:
- retained the log once under `shared/artifacts/` rather than arbitrarily nesting it under one analysis
- did not duplicate the same evidence into both analysis directories merely to make each tree self-contained
- used manifest relationships to connect the shared artifact to each relevant finding/analysis
- kept original source binaries and shared disassembler/decompiler workspace state at project scope rather than copying them into every analysis
- kept analysis-owned evidence local when it had exactly one semantic owner; did not promote all evidence to shared storage by default

## 3. Legacy flat stores continue without implicit migration

An existing project contains `notes/findings/**/*.md`, project-relative manifest artifact paths, and per-record target fields.

Required assertions:
- discovered and validated the legacy findings without requiring migration
- did not move or rename old files during `verify`, `check-links`, linking, or normal additions
- allowed legacy and canonical layouts to coexist during transition
- reported duplicate finding IDs across legacy and canonical layouts deterministically instead of silently preferring one
- used the canonical hierarchy by default only for newly initialized projects/scopes
