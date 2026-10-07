# Intake assessment

Use this reference when an incoming issue or pull request needs more than a superficial classification.

## Establish the request and current state

Read the full item and relevant discussion. For a pull request, inspect the actual diff or resulting behavior. Check existing code, documentation, tracker history, or prior decisions only where they can materially change the disposition.

Useful questions include:

- Is the requested behavior already present?
- Is this a duplicate of active or previously decided work?
- Does the report describe a reproducible defect, an unverified claim, or a missing capability?
- Is there enough information to state the desired observable outcome?
- Is a product, scope, or architecture decision still required before another actor could proceed responsibly?

## Verify claims proportionately

Verification should match the claim that matters to triage:

- **Bug report:** attempt the supplied reproduction or another check that exercises the reported symptom when practical.
- **Pull request:** base claims about the contribution on its diff or resulting code, not the base branch alone.
- **Enhancement:** establish current behavior when the disposition depends on whether the requested capability already exists.

Keep the result explicit: established by evidence, not established by the check performed, or not verifiable with the available information/access. Do not upgrade the latter two into facts.

## Reach a semantic disposition, not a new taxonomy

Typical conclusions include actionable work, reporter information needed, a maintainer/project decision needed, duplicate/already satisfied, defer, or decline. These are reasoning outcomes, not required tracker states. Map them to whatever representation the project already uses.

If the work is actionable, capture only the durable information that the next actor genuinely needs: desired behavior, important constraints or interfaces, independently checkable success conditions, and known exclusions when they matter. Preserve useful original context instead of rewriting the entire report into a mandatory template.

If information is missing, ask only for information that can change the disposition or make the work actionable; do not restart questions already answered in the item history.

## Persist only through real project conventions

When the user asks for mutation, use the tracker's existing labels, status fields, comments, closure semantics, templates, and relationships. Do not create a parallel readiness vocabulary merely for this skill.

After consequential mutations, re-read the item when practical to confirm the intended state actually persisted.
