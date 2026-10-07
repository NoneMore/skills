# Deepening module clusters

Use this method when architectural friction comes from several shallow modules whose complexity would be better concentrated behind a smaller interface. Use the vocabulary in [deep-modules.md](deep-modules.md).

## Classify dependencies before choosing a seam

Different dependencies justify different designs:

- **In-process computation or memory** can often remain fully inside the deepened module with no adapter.
- **Local substitutable infrastructure** such as a test database or in-memory filesystem may stay behind an internal seam when a realistic local stand-in already exists.
- **Owned remote services** can justify a port when transport genuinely varies or isolation at that boundary materially improves the design.
- **True external services** often need a narrow injected boundary so production and test behavior can be controlled without leaking vendor details through the module's public interface.

Do not introduce a port merely because a dependency exists. The seam should pay for itself through real variation, isolation, or locality.

## Keep internal seams internal

A module may have internal seams used by its implementation or tests without exposing those seams to callers. Do not enlarge the public interface simply to make internal testing convenient.

## Replace shallow verification when the deeper interface supersedes it

When a new deep interface becomes the meaningful behavioral boundary, prefer tests through that interface. Remove lower-level tests only when the higher-level tests genuinely preserve the behavior they protected; do not delete useful diagnostics or coverage mechanically.

A successful deepening should reduce caller knowledge and concentrate related change, not merely add another abstraction layer around the same scattered complexity.
