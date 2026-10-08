# Tracer-bullet decomposition

A tracer-bullet slice is a narrow but complete path through the parts of the system required to make one meaningful behavior work. Prefer it when the slice can be demonstrated or verified independently.

Good slices tend to:

- end in observable behavior or a concrete verifiable capability;
- cross whatever layers are necessary instead of assigning one ticket per layer;
- be small enough to reason about while still leaving the system in a valid state;
- expose integration assumptions early rather than postponing them to a final catch-all ticket.

Dependencies are constraints, not ordering preferences. Add an edge only when the blocked item cannot responsibly start or complete before the blocker. Keep independent work independent.

When a prerequisite refactor genuinely enables several later slices and can itself leave the system valid, model it explicitly. When a migration or mechanical change cannot be safely split into independently valid vertical slices, represent the real sequencing instead of pretending it is end-to-end feature work.
