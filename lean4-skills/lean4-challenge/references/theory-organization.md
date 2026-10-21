# Theory organization and theorem placement

Use when a theorem's module placement may contradict its mathematical prerequisites or burden consumers.

- Identify the generic layer that can state the result, independently of current file names; inspect relevant import directions and actual consumers.
- Compare keeping the result, moving it, introducing a lower-level generic theorem, or exposing a local facade.
- Check a **minimal import path and one real consumer**. A scratch theorem that compiles in isolation does not establish dependency or integration fitness.
- Weigh avoided duplication and import coupling against possible cycles, new abstraction cost, and migration impact.
