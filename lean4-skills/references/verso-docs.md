# Verso Documentation Roles

Use when Lean doc comments use Verso roles or when documentation diagnostics indicate an inline code element is ambiguous or unresolved.

Prefer semantic roles that preserve links and hover information:

- `{name}` for declared names;
- `{lean}` for Lean expressions/snippets;
- `{lit}` for literal pseudo-code that should not be resolved;
- `{given}` when introducing a variable for later Lean snippets, where supported by the current documentation setup.

Use `{lit}` as an intentional escape hatch, not the default way to silence a resolution problem.

## Debugging

When a doc diagnostic fires:

1. decide whether the inline text is a declaration name, Lean expression, or literal notation;
2. use the corresponding role;
3. qualify ambiguous names enough to resolve in the documentation environment;
4. verify with the project's actual documentation/lint gate.

For broader upstream mathlib documentation and file conventions, load [mathlib-style.md](mathlib-style.md).
