# OpenAI Codex harness profile

**Verified:** 2026-09-10 against current OpenAI Codex source at commit `ddea03ad049142943bdbf13e937b1d67e8c1ba0c` plus OpenAI's published agent-loop documentation. Treat governing runtime instructions as newer authority if they disagree.

## Artifact names

- Global user guidance: `$CODEX_HOME/AGENTS.override.md` first, otherwise `$CODEX_HOME/AGENTS.md`; the default Codex home is typically `~/.codex`.
- Project guidance in each applicable directory: `AGENTS.override.md`, then `AGENTS.md`, then configured `project_doc_fallback_filenames`.
- At most one project instruction file is selected per directory.

## Discovery boundary

For project instructions, Codex determines a project root from `project_root_markers` (default behavior uses `.git`). It searches from that project root down to the current working directory, inclusive, and does not walk above the project root. If no project root marker is found, only the cwd is considered.

Project-level instruction loading can also be gated by the active Codex project/trust state supplied by the runtime; do not assume a filesystem file is effective when governing context says project instructions are disabled.

## Candidate precedence

Within one searched directory:

1. `AGENTS.override.md`
2. `AGENTS.md`
3. configured fallback filenames, in configured order

`AGENTS.override.md` replaces the same-directory normal/fallback candidate; it does not erase applicable files from broader directories. Candidate selection is based on the first existing filename in precedence order. A selected empty file can contribute no instruction text while still shadowing lower-precedence same-directory candidates; do not assume content-level fallback to `AGENTS.md` or a configured fallback filename.

## Scope and composition

An `AGENTS.md`-family file scopes to the directory tree rooted at the directory containing it. For files touched in a deeper subtree, applicable deeper instruction files take precedence on conflicts. Codex startup discovery preloads the applicable chain from project root to cwd; when work moves into a deeper subdirectory, the agent's governing Codex instructions require checking for additional applicable `AGENTS.md` files there.

Selected startup project files are concatenated from project root to cwd. Broader instructions appear earlier; more specific cwd-near instructions appear later. Model a narrower Codex instruction file as a scoped overlay on the broader effective contract, with direct system/developer/user instructions remaining higher authority than repository guidance.

Codex applies a combined project-document byte budget (`project_doc_max_bytes`, 32 KiB by default in current implementation). Keep high-value instructions compact and prefer pointers to maintained detail.

## Write target guidance

- Generic project setup: prefer `AGENTS.md` at the project root unless the user explicitly wants a narrower scope or an existing Codex convention indicates otherwise.
- Scoped durable behavior: place `AGENTS.md` in the narrowest directory whose subtree needs the delta.
- Use `AGENTS.override.md` only when replacement of the same-directory candidate is intentional; do not use it merely as a stronger-looking nested file.
- A custom fallback filename is effective only when it is actually configured; do not create one from filename preference alone.

## Verification sources

- OpenAI Codex source, project discovery/composition: https://github.com/openai/codex/blob/ddea03ad049142943bdbf13e937b1d67e8c1ba0c/codex-rs/core/src/agents_md.rs
- OpenAI Codex source, global instruction candidate order: https://github.com/openai/codex/blob/ddea03ad049142943bdbf13e937b1d67e8c1ba0c/codex-rs/codex-home/src/instructions/mod.rs
- OpenAI Codex base instructions, subtree scope and conflict precedence: https://github.com/openai/codex/blob/ddea03ad049142943bdbf13e937b1d67e8c1ba0c/codex-rs/protocol/src/prompts/base_instructions/default.md
- OpenAI, “Unrolling the Codex agent loop”: https://openai.com/index/unrolling-the-codex-agent-loop/
