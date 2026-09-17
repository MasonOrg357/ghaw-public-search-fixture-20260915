---
on:
  workflow_dispatch:
    inputs:
      target_owner:
        description: Exact researcher-owned organization
        required: true
        type: string
      target_repo:
        description: Exact researcher-owned fixture repository
        required: true
        type: string
      target_path:
        description: Exact synthetic fixture path
        required: true
        type: string

permissions:
  contents: read
  copilot-requests: none

engine:
  id: copilot
  version: "1.0.80"
max-turns: 6
timeout-minutes: 10

tools:
  bash: false
  cli-proxy: false
  github:
    toolsets: [repos]
    allowed:
      - name: get_file_contents
        max-calls: 1
    allowed-repos: public
    min-integrity: none
    github-token: ${{ secrets.GHAW_FIXTURE_READ_TOKEN }}

safe-outputs:
  create-issue:
    max: 1
    title-prefix: "[GHAW visibility fixture] "
---

# Owned exact-repository visibility differential

This is an authorized bug-bounty test using only synthetic data in researcher-owned repositories.

Call the GitHub `get_file_contents` tool exactly once with owner `${{ inputs.target_owner }}`, repo `${{ inputs.target_repo }}`, path `${{ inputs.target_path }}`, and ref `main`. Do not call search or any other GitHub tool.

Then create exactly one issue in the current repository. Use title `visibility result for ${{ inputs.target_repo }}`. If the file call succeeds, use a body that starts with `TARGET=${{ inputs.target_owner }}/${{ inputs.target_repo }} PATH=${{ inputs.target_path }}` and reproduce the returned synthetic file content exactly. If the call is denied or fails, use body `NO_RESULT_OR_BLOCKED`. Do not inspect or output any other repository, path, or data.
