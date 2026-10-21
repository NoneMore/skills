# Mathematical framing and representation

Use when a local construction may be a special case of a more canonical mathematical object.

- Separate the intended mathematics from its Lean encoding; trace wrappers, stabilization predicates, or transports toward generic owners (e.g. fixed points, closures, universal properties).
- Compare canonical notions, equivalent characterizations, and natural duals when they would change what should be proved.
- Ask whether a lower-level law removes repeated local machinery. If the proposal crosses an abstraction boundary, test **one representative composition path**, not just an isolated declaration.
- Use focused library searches, scratch equivalences, assumptions, or a boundary case to discriminate candidates. A blocked composition path may expose a missing generic law.
- Revisit a previously rejected approach only if a relevant prerequisite or library API has changed.
