# Lean Linter Authoring

Use for project-specific static checks expressed through Lean's linter/command infrastructure.

## Design the rule before the hook

A useful linter has:

- a precisely detectable condition;
- a clear reason the condition matters;
- a concrete remediation;
- a severity appropriate to whether the issue is style, maintainability, correctness, or safety;
- a way to test positive and negative cases.

Do not encode subjective preferences as mandatory failures merely because the linter API makes that easy.

## Keep detection narrow

Prefer syntax/environment facts that directly establish the issue. Avoid broad textual matching when syntax or declaration information is available. Attach messages to the smallest relevant source span.

Use warnings for advisory project policy and hard errors only when the project intentionally treats the rule as a build-stopping invariant.

## Configuration

Make project-wide enablement and local exceptions explicit. Exceptions should remain discoverable and, for important rules, explain why the local case is valid.

## Tests

Maintain small fixtures that demonstrate:

- the rule fires on the intended bad case;
- nearby valid syntax does not fire;
- disable/exception behavior works;
- the message points at the useful source location.

Verify current linter registration APIs against the active Lean toolchain before depending on internal command structures.
