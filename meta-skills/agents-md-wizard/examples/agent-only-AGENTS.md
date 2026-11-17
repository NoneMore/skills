# AGENTS.md (illustrative example)

- For changes involving the shared API contract, check for the sibling `../shared-contracts` checkout before editing. If it is absent, ask for the checkout location; do not assume the contract is stored in this repository.
- When diagnosing a remote CI failure, use the agent's CI log-reading tool if available to inspect the actual failure. If that tool is unavailable, explain the limitation rather than guessing from local source alone.
- When changing serialization behavior, read `docs/serialization.md` for contributor-wide compatibility requirements before editing. Those requirements belong in that shared document, not duplicated here.
