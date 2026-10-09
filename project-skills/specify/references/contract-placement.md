# Choosing contract persistence

Use this guidance when the user wants a durable specification but the persistence target is not yet clear.

## Resolve an existing convention or require an explicit choice

Do not infer which existing artifact should become authoritative merely because it mentions the relevant behavior or appears to be the strongest candidate.

Use one of these paths:

1. update a contract source explicitly designated by the user as authoritative for the relevant scope, or unambiguously identified by the project's established contract-management convention; or
2. when the user chooses to establish or normalize specification persistence, designate a destination for a dedicated specification source using the unified specification shape described in [spec-shape.md](spec-shape.md).

A path or filename alone designates a destination, not an authoritative contract role. A user designation is sufficient when it explicitly assigns that role for the relevant scope. Treat a project convention as established only when maintained project authority or an enforced or maintained index/manifest explicitly assigns the relevant contract role or lifecycle; filenames, proximity, content similarity, implementation, tests, or history alone are not sufficient.

Repository evidence may identify the uniquely applicable managed source under an existing convention, but naming an arbitrary existing artifact does not promote it into a contract source. If multiple managed sources plausibly apply, or no established managed source applies and the user has not explicitly designated a source or chosen the dedicated specification path, return the complete specification in conversation and surface the missing persistence decision instead of inventing repository structure or authority.

## Follow the selected path

When using an existing or explicitly designated contract source, preserve its established shape and lifecycle unless the requested change explicitly includes restructuring that convention.

When the user chooses a dedicated specification source, use [spec-shape.md](spec-shape.md) for its semantic shape while preserving the user-designated destination. The specification shape does not itself define repository placement, naming, hierarchy, or lifecycle.

## Done when

The specification has either been persisted through an established managed contract convention or according to the user's explicit designation of an authoritative source or dedicated specification path, or the complete contract has been returned without inventing a persistence decision on the user's behalf.
