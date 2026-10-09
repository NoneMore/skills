# Modifying and organizing existing specifications

Use this guidance when the requested outcome changes or reorganizes an existing durable project specification.

## Choose the target safely

Use the source the user designates. Otherwise, modify an existing specification only when the relevant source can be identified unambiguously from the project context.

If multiple plausible specifications overlap, disagree, or leave it materially unclear which one should be changed, do not guess. Surface the ambiguity instead of modifying a possibly wrong source.

Other artifacts such as code, tests, issues, ADRs, examples, or documentation may reveal useful evidence or conflicts. They do not justify silently switching to a different specification source.

## Modify without collateral change

Apply the requested semantic change and preserve settled semantics outside its scope.

When useful, distinguish:

- added semantics;
- modified semantics;
- removed semantics;
- explicitly unchanged semantics when needed to prevent likely ambiguity.

Preserve the existing specification's useful structure unless restructuring is part of the request. If other project evidence conflicts with the specification, report or reconcile the discrepancy only within the requested scope rather than silently rewriting unrelated requirements.

## Organize without changing meaning

When organizing existing specifications:

- improve headings, ordering, references, and local clarity;
- consolidate duplicated material when the meaning is equivalent;
- keep distinct requirements distinct when merging them would lose meaning;
- surface conflicts or ambiguous overlaps instead of silently choosing a winner;
- preserve settled semantics unless the user explicitly asks to change them.

Do not invent a new repository hierarchy, versioning scheme, lifecycle, manifest, or governance mechanism merely to make the specifications look more organized.

## Done when

The intended specification source was changed rather than a plausible but wrong alternative, requested semantic changes are represented without unrelated semantic drift, and organizational cleanup preserves meaning while making unresolved conflicts explicit.
