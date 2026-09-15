---
on:
  workflow_dispatch:
    inputs:
      query:
        description: Exact synthetic code-search marker
        required: true
        type: string

permissions:
  contents: read
  copilot-requests: write

engine: copilot
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

Call the GitHub `search_code` tool exactly once with query `${{ inputs.query }}` and `perPage` set to `1`. Do not add a `repo:`, `org:`, `user:`, path, filename, language, or visibility qualifier.

Then create exactly one issue in the current repository. Use title `search result for ${{ inputs.query }}`. In the body, reproduce only the returned repository full name, path, and matched text fragment. Do not inspect or output any other repository or data. If the search returns no item or access is denied, create the issue with body `NO_RESULT_OR_BLOCKED`.
