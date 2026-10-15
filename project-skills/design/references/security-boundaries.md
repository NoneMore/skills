# Security boundaries

Use this guidance when trust, identity, authority, isolation, or data exposure can materially change the design.

## Model authority explicitly

Identify the principals, protected resources, trust boundaries, and which component may act on whose behalf. Separate authentication from authorization, and place enforcement where the information needed to decide is authoritative and bypass can be controlled.

Treat network location or an "internal" service label as a deployment fact, not a sufficient trust model. Cross-tenant, cross-privilege, or delegated operations deserve explicit isolation and authority semantics when their failure would be material.

## Minimize and contain trust

Give components only the authority their responsibilities require, and avoid propagating secrets or ambient credentials beyond the boundary that uses them. Validate untrusted input before it can influence privileged or durable state. Preserve an audit trail where accountability for a material action or decision matters.

Security mechanisms earn their complexity by containing a plausible threat with material consequences; do not stack defensive layers solely because an attack is imaginable. When agents or automation are involved, instructions and prompt text are not authorization boundaries: enforce permissions at the runtime, tool, or resource boundary that controls the action.
