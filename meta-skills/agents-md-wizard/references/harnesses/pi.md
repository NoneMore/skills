# Pi Coding Agent harness profile

**Verified:** 2026-09-10 against current upstream `earendil-works/pi` source at commit `400d6905ce46ec46e79da8a7701b1b48850192df` and current upstream usage documentation. Treat governing runtime instructions as newer authority if they disagree.

## Artifact names

Pi context-file discovery uses one candidate per directory in this order:

1. `AGENTS.override.md`
2. `AGENTS.md`
3. `AGENTS.MD`
4. `CLAUDE.md`
5. `CLAUDE.MD`

The same candidate resolver is used for Pi's global agent directory (`PI_CODING_AGENT_DIR`, default `~/.pi/agent`) and filesystem ancestor directories.

Pi also has `.pi/SYSTEM.md` / global `SYSTEM.md` and `APPEND_SYSTEM.md` mechanisms, but those alter or append the system prompt and are not interchangeable with ordinary project context files. Keep them outside this profile's default write target unless the user explicitly asks for system-prompt customization.

## Discovery boundary

Pi first loads one context candidate from its global agent directory when present. For project/local context, current source walks from the cwd up through filesystem ancestors to the filesystem root, then orders discovered files ancestor-first through cwd. It does **not** use a Git/project-root cutoff for this context-file chain.

Context-file discovery can be disabled with `--no-context-files` / `-nc`; when governing runtime context indicates it is disabled, an otherwise valid `AGENTS.md`/`CLAUDE.md` target is inert for that run.

## Candidate precedence

Within one directory, the first existing regular file in the candidate list wins. `AGENTS.override.md` therefore replaces a sibling `AGENTS.md` or `CLAUDE.md` for that directory, while context selected from other directories remains layered normally.

## Scope and composition

The selected global context is followed by selected filesystem context files ordered from broad ancestor to cwd. Pi appends these context files to the model's project context; cwd-near files therefore compose with broader ancestor files rather than standing alone.

Pi's automatic context applicability is **cwd-ancestry based**, not "every file touched below the workspace" based. A context file in `subdir/` is automatically loaded when Pi starts with cwd at `subdir/` or below it; starting Pi at the repository root does not automatically load deeper `subdir/AGENTS.md` merely because the agent later edits a file there. Author nested/local instructions as deltas only when that cwd-based loading pattern matches the intended use.

Because Pi walks filesystem ancestors rather than stopping at a repository root, inspect only the actually applicable chain needed to determine effective behavior; do not broaden ordinary workspace discovery merely because Pi's loader can see higher ancestors.

## Write target guidance

- Generic project setup: prefer `AGENTS.md` in the user's intended project/workspace root.
- Preserve an existing `CLAUDE.md` when it is the active local project context unless the user wants migration; do not create a duplicate `AGENTS.md` just to mirror it.
- For durable narrower behavior used by sessions launched from that directory or below, place an `AGENTS.md` there and encode only the local delta against applicable ancestors. If sessions normally start higher up, do not assume this nested file will load automatically; keep the needed behavior in an actually loaded scope or make the invocation/cwd convention explicit.
- Use `AGENTS.override.md` only when intentional same-directory replacement is desired.
- After changing context files in an active interactive Pi session, `/reload` (or restart) is needed for the session to pick up the change.

## Verification sources

- Pi source, context candidate order and ancestor discovery: https://github.com/earendil-works/pi/blob/400d6905ce46ec46e79da8a7701b1b48850192df/packages/coding-agent/src/core/resource-loader.ts
- Pi usage documentation, context files and reload behavior: https://github.com/earendil-works/pi/blob/400d6905ce46ec46e79da8a7701b1b48850192df/packages/coding-agent/docs/usage.md
- Pi README, current context-file behavior: https://github.com/earendil-works/pi/blob/400d6905ce46ec46e79da8a7701b1b48850192df/packages/coding-agent/README.md
