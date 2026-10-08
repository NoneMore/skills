# Testing

Use this guidance when test placement, behavioral coverage, or dependency substitution is not obvious.

Prefer tests that verify observable behavior through a meaningful stable boundary. Use lower-level tests when they provide cheaper diagnosis or isolate logic with a clear contract; no test level is universally preferred.

Avoid assertions about incidental internal collaboration when the behavior can be checked directly. Expected outcomes should be independent enough that the test does not merely reproduce the implementation by construction.

Use fakes, mocks, or other substitutes when the real dependency would make a useful test impractical, unsafe, slow, or nondeterministic. Prefer narrow stable boundaries and avoid substitutions that force tests to mirror incidental call structure.

Choose coverage proportionate to the changed behavior and risk rather than following a fixed test taxonomy.
