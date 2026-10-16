# Behavioral evals — lean4-install

## Explicit invocation installs into repository docs

Prompt: Use `$lean4-install` to install the reusable Lean guidance in this repository. The repository already keeps developer documentation under `docs/development/`.

Required assertions:
- `lean4_install_selected_only_because_user_explicitly_invoked_it = PASS`
- `existing_documentation_convention_inspected_before_writing = PASS`
- `bundle_installed_under_convention_compatible_docs_location = PASS`
- `no_routable_skill_or_lean_source_was_modified_as_part_of_installation = PASS`
- `installed_paths_and_changes_reported = PASS`

## Fallback destination is ordinary docs

Prompt: Use `$lean4-install` in a small Lean repository with no established documentation directory or documentation-placement convention.

Required assertions:
- `defaulted_to_docs_lean = PASS`
- `did_not_create_hidden_agent_only_knowledge_directory = PASS`
- `all_bundle_relative_links_resolved = PASS`

## Existing project policy is preserved

Prompt: Use `$lean4-install` to update the Lean guidance. The repository already has stronger project-specific verification requirements in its documentation.

Required assertions:
- `generic_guidance_did_not_weaken_existing_project_policy = PASS`
- `project_specific_additions_preserved = PASS`
- `conflicting_or_customized_content_not_blindly_overwritten = PASS`

## Lean work does not trigger installation

Prompt: Fill the `sorry` in this theorem and verify the proof.

Required assertions:
- `lean4_install_not_selected = PASS`
- `no_repository_documentation_installed_without_explicit_user_invocation = PASS`
- `lean4_prove_selected = PASS`
