---
name: handoff
description: Package the current work into a compact continuation brief for another agent or session. Use when the user explicitly wants a handoff, continuation note, or resumable context artifact.
disable-model-invocation: true
---

# Handoff

## Purpose

Produce a portable continuation brief that lets a fresh agent resume the requested work without reconstructing material state from scratch.

## Owns

- the current objective and requested outcome;
- settled material decisions and constraints;
- the current state of work and evidence that matters to continuation;
- unresolved blockers, risks, and residual uncertainty that can change the next action;
- concrete references to durable artifacts that already hold detail;
- the smallest useful next-action context for the receiving agent.

Do not duplicate specs, issues, ADRs, commits, diffs, logs, or other durable artifacts when a path or URL is sufficient. Redact secrets, credentials, private tokens, and unnecessary personal data.

If the user names the next session's purpose, optimize the brief for that purpose rather than preserving unrelated conversation history.

## Persistence

The handoff itself is the requested artifact. Use the destination the user specifies. If no destination is specified, return the brief in conversation unless the runtime or task clearly requires a file.

## Done when

A fresh agent can identify what is being continued, what is already settled or completed, what remains material, where authoritative detail lives, and what can be done next without relying on suite-specific lifecycle state.
