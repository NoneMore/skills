# Design review

Review a design against the constraints and outcomes it claims to serve.

Look for material decisions that are missing, contradictory, or silently delegated downstream; assumptions that do not match the existing system or domain; interfaces or boundaries whose complexity leaks to callers; and tradeoffs whose costs are omitted or assigned to the wrong part of the system.

A valid alternative is not automatically a finding. Report an issue when the current design violates a stated constraint, leaves a material risk unresolved, or creates a concrete downstream cost that matters to the requested outcome.

Distinguish settled choices from unresolved questions. Review can establish that a question remains open without designing the replacement answer.
