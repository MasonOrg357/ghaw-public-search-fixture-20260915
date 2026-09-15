---
on:
  workflow_dispatch:
    inputs:
      query:
        description: Fixed owned-org qualifier plus exact synthetic marker
        required: true
        type: string

permissions:
  contents: read
  copilot-requests: none

engine:
  id: copilot
  version: "1.0.82"
max-turns: 6
timeout-minutes: 10

tools:
  bash: false
  cli-proxy: false
  github:
    toolsets: [repos]
    allowed:
      - name: search_code
        max-calls: 1
    allowed-repos: public
    min-integrity: none
    github-token: ${{ secrets.GHAW_FIXTURE_READ_TOKEN }}

safe-outputs:
  create-issue:
    max: 1
    title-prefix: "[GHAW fixture] "
---

# Owned code-search confidentiality differential

This is an authorized bug-bounty test using only synthetic data in researcher-owned repositories.

Call the GitHub `search_code` tool exactly once with query `${{ inputs.query }}` unchanged and `perPage` set to `1`. The supplied query contains the fixed `org:MasonOrg357` qualifier plus one synthetic marker. Do not add, remove, or alter any qualifier or search term.

Then create exactly one issue in the current repository. Use title `search result for ${{ inputs.query }}`. In the body, reproduce only the returned repository full name, path, and matched text fragment. Do not inspect or output any other repository or data. If the search returns no item or access is denied, create the issue with body `NO_RESULT_OR_BLOCKED`.
