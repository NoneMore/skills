# Runtime Fallbacks

Use the strongest available feedback loop without making host-specific adapter details part of the common skill context.

## Profiles

1. **Live Lean/LSP:** inspect goals and diagnostics, search mathlib, and test candidate snippets against the active file. This is the preferred profile.
2. **Lean + deterministic helpers:** use scripts for tasks such as sorry discovery, axiom audits, parsing, or structured search; use Lean/Lake for semantic verification.
3. **Lean/Lake only:** use source search plus direct compilation. Keep edits smaller because feedback is slower and less local.
4. **Read-only:** explain/review based on available source and clearly mark anything that could not be Lean-verified.

## Fallback rules

- Missing LSP is a capability reduction, not permission to skip verification.
- Prefer deterministic helpers for deterministic parsing/transformation when they are available and trusted.
- Resolve helper locations through the host/runtime adapter. Do not hard-code native plugin installation paths into portable workflow instructions.
- If neither live tooling nor Lean/Lake can verify a semantic claim, report the limitation explicitly.

For LSP capabilities, consult `../lean-lsp-server.md` or `../lean-lsp-tools-api.md` only when the task depends on their details.