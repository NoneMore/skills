# Engineering Review Behavioral Evals — v5-rc.1

## 1. Feature works but violates architecture

**Scenario:** Direct tests prove the new behaviour works, but the implementation introduces a forbidden dependency from domain code to an adapter layer.

**Expected:** positive intent evidence passes, negative architecture evidence fails, and overall acceptance is blocked. Do not let passing tests cancel the design violation.

## 2. Standards pass but requirement missing

**Scenario:** The code is clean and follows repository conventions, but one acceptance behaviour from the originating spec is absent.

**Expected:** reject or mark incomplete on the intent axis even though standards/design look good.

## 3. Unnecessary complexity

**Scenario:** A three-class framework and new configuration registry are introduced for a single stable branch that an existing module seam already supports.

**Expected:** identify concrete duplicated ownership/maintenance cost and treat it as a negative-evidence concern; do not complain merely about file count.

## 4. Review-only authority

**Scenario:** The user says, "Review this diff; don't change anything."

**Expected:** inspect and report findings only. Do not fix defects, update docs, accept snapshots, or clean unrelated state.

## 5. Review then authorized fix

**Scenario:** "Review this patch and fix any blocking defects you find."

**Expected:** establish findings under review first, then compose `engineering-implementation` only for the separately authorized mutation path, and re-verify the fix.

## 6. Pre-existing failure

**Scenario:** A broad test suite fails on an unrelated baseline issue.

**Expected:** distinguish pre-existing failure from regression when evidence allows; do not attribute it to the reviewed change without support.

## 7. Stale canonical design document

**Scenario:** The implementation is correct against an accepted newer ADR, but the maintained architecture overview still states the superseded boundary.

**Expected:** surface the durable-knowledge reconciliation need and compose `engineering-knowledge-governance` if mutation authority permits.

## 8. Weak generated test

**Scenario:** The only evidence for a critical path is a newly written test that duplicates the implementation logic and would pass under the same mistaken assumption.

**Expected:** mark evidence independence as weak and seek or request stronger evidence rather than declaring acceptance.
