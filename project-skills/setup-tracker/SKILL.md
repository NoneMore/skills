---
name: setup-tracker
description: "Configure the project tracker with the intended GitHub Issues or Local Markdown backend."
disable-model-invocation: true
---

# Setup Tracker

Configure tracker storage only. Do not run downstream workflows or modify existing issues.

Read [ISSUE-MODEL.md](ISSUE-MODEL.md), then read only the selected backend document. Publish a self-contained copy to `docs/agents/issues.md` so downstream workflows do not depend on this Skill's installation path.

## 1. Choose backend

- Explicit Local Markdown choice → Local Markdown.
- Exactly one canonical GitHub repository → GitHub.
- Several plausible GitHub repositories → ask which is canonical.
- No intended GitHub repository → Local Markdown.

## 2. Inspect configuration

Read `docs/agents/issues.md` if present.

- If it already configures the same backend, treat this as an idempotent rerun: make only missing setup changes and refresh the generated contract. Do not modify tracked issues.
- If it configures another tracker/backend, stop unless the user explicitly requested replacement. Replacement changes setup artifacts only; it does not migrate or rewrite existing issues.

For GitHub, confirm repository identity, Issues availability, label read/write access, and existing tracker labels. For Local Markdown, inspect `.tracker/issues/`.

Do not classify, repair, close, relabel, or otherwise adopt existing issues.

## 3. Configure

For GitHub, ensure these labels exist while preserving unrelated labels:

- `tracker:kind:intake`, `tracker:kind:managed`
- `tracker:type:investigation`, `tracker:type:change`
- `tracker:status:needs-triage`, `tracker:status:ready`, `tracker:status:waiting`, `tracker:status:done`

Do not modify issue templates. Native relation capabilities are checked only by workflows that use those relations.

For Local Markdown, ensure `.tracker/issues/` exists. Do not rewrite existing issue files.

## 4. Publish and verify

Write `docs/agents/issues.md` with:

```markdown
# Issue tracker
Backend: <github|local-markdown>
Repository: <owner/repo>        # GitHub only
Issue root: .tracker/issues/    # Local Markdown only
```

Then append the complete issue model and selected backend document. The generated contract must contain the rules directly, not rely on Skill-relative links.

Only when the user explicitly asks to wire the tracker into project instructions, add or update one short pointer to `docs/agents/issues.md`.

Re-read only what setup changed. Verify the GitHub labels or local issue root and confirm the generated contract names the intended backend and contains no execution-claim/orchestration protocol.

Report the configured backend and stop.
