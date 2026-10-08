# Debugging feedback loops

Use this method when the cause of a bug, regression, or performance problem is uncertain enough that implementation would otherwise be guesswork.

## Build a discriminating signal

Prefer a fast, repeatable check that exercises the user's actual symptom and can distinguish broken from fixed. Useful forms include a focused failing test, CLI or HTTP repro, headless-browser check, replayed trace, minimal harness, differential comparison, benchmark, or bisection command.

Tighten the loop when practical: make it faster, more deterministic, and more specific to the reported failure. For intermittent problems, improving the reproduction rate can be more useful than waiting for a perfectly deterministic repro.

## Reduce the hypothesis space

Once the symptom is observable, minimize inputs, steps, configuration, or environment while preserving the failure. Use falsifiable hypotheses whose predicted observations differ. Instrument only where the observation can distinguish those hypotheses; avoid broad logging that produces volume without discrimination.

For performance work, establish a measurement baseline before changing the system and use profiling, query plans, or benchmarks rather than treating log volume as evidence.

## Verify the repair

After the change, re-run the original symptom-level loop, not only a newly added unit test. Add a regression test when there is a meaningful behavioral seam for it. If no suitable seam exists, treat that as architectural evidence rather than writing a shallow test that cannot catch the real bug.

Remove temporary instrumentation, captured secrets, throwaway harnesses, and debug-only scaffolding before the production result is complete.
