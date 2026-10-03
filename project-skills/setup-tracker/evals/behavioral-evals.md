# Setup Tracker Behavioral Evals

These scenarios exercise protocol boundaries that must hold across prompt-driven implementations of `setup-tracker` and downstream consumers of its generated repository contract.

## 1. Terminal managed work cannot reopen

**Scenario:** A managed issue is `done`. A downstream workflow wants to set it back to `ready` because new follow-up work was discovered.

**Expected:** reject the status transition. Preserve the terminal issue and create separate managed work when appropriate. The same rule applies to `cancelled`, and ordinary operations must not change `done` to `cancelled` or vice versa. An idempotent write of the existing terminal status is allowed.

**Failure signs:** reopening the issue, changing one terminal status into the other, or treating GitHub reopen/close state as permission to change semantic lifecycle status.

## 2. GitHub blank intake respects the persisted cutover

**Scenario:** Before first setup publication, the repository already contains unclassified issues through `#120`. Setup publishes `Intake-Cutover-Number: 120`. Later, unclassified blank issue `#123` arrives. A fresh session scans the repository and sees both `#119` and `#123`.

**Expected:** leave `#119` outside the tracker. `#123` is eligible for downstream intake classification because its number is above the persisted cutover. The decision must be recoverable from `docs/agents/issues.md` without session memory or issue-age heuristics.

**Failure signs:** adopting `#119`, refusing `#123` only because the creating event was not observed live, or deriving the boundary from timestamps.

## 3. Compatible rerun never advances the GitHub cutover

**Scenario:** A repository already has a compatible contract with `Intake-Cutover-Number: 120`, and issues now extend through `#180`. Setup is run again without migration intent.

**Expected:** preserve `120` exactly. Do not recompute the cutover from current repository state and do not rewrite the compatible contract.

**Failure signs:** changing the cutover to `180`, causing newly received but still-unclassified issues to become historical by rerunning setup.

## 4. Archived canonical label stops before mutation

**Scenario:** `tracker:status:ready` already exists but is archived or otherwise cannot be applied. Other canonical labels are missing and issue templates are absent.

**Expected:** stop during preflight before creating labels, editing templates, or publishing the repository contract. Report the unusable canonical label as a setup conflict; do not silently unarchive or replace it.

**Failure signs:** performing partial setup mutations before discovering the conflict, creating a similarly named replacement, or treating the archived label as a usable existing label.

## 5. Global GitHub validation exhausts pagination

**Scenario:** Tracked issues or native relation edges span multiple API pages, and a dependency cycle exists only on a later page.

**Expected:** consume every page required for complete issue/relation enumeration, detect the cycle, and stop before mutation. If the active tooling cannot continue pagination or otherwise prove complete enumeration, treat the required capability as unavailable.

**Failure signs:** validating only the first page, declaring the graph acyclic from partial data, or silently degrading to textual relations.

## 6. Claim requires a concrete assignable GitHub principal

**Scenario:** Managed issue `#210` is on the executable frontier, but the runtime cannot resolve the current actor to one GitHub login, or the resolved login is not assignable to the repository.

**Expected:** do not claim and do not begin consequential execution. Report the claim capability/identity problem. If a concrete assignable login exists, assign it, re-read the issue, and proceed only while it is the sole assignee and the issue remains executable.

**Failure signs:** using an arbitrary account, proceeding unassigned, treating a display name as a GitHub login, or skipping the post-claim re-read.

## 7. Local Markdown crosses 9999 without ambiguity

**Scenario:** `.tracker/issues/9999.md` is the greatest existing local issue. A creator needs the next issue.

**Expected:** create `.tracker/issues/10000.md`. References use `10000`. Do not stop at four digits, wrap to `0000`, or create `00001.md`.

**Failure signs:** fixed-width overflow, reuse of a lower numeric gap, or accepting more than one filename representation for the same numeric value.

## 8. Local concurrent creation retries monotonically

**Scenario:** Two creators both observe `0042` as the greatest ID and race to create `0043.md`.

**Expected:** one create-only operation succeeds. The other detects the collision, rescans, and attempts `0044.md` (or later if another creator won first). No existing file is overwritten and lower gaps are not reused.

**Failure signs:** last-writer-wins overwrite, choosing a lower unused number after collision, or claiming create-only safety when the runtime cannot provide it and callers are not serialized.

## 9. Contract publication remains gated by backend verification

**Scenario:** GitHub label/template mutations succeed, but post-mutation verification cannot prove complete relation enumeration or finds a canonical label unusable.

**Expected:** do not publish `docs/agents/issues.md`. A later run must see the partial backend state, rerun preflight, and either complete safely or stop without adopting unrelated issues.

**Failure signs:** publishing the contract despite failed backend verification or using the contract marker to conceal an incomplete backend setup.
