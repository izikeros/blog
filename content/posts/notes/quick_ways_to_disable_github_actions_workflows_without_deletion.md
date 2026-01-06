---
Category: note
Date: 2024-10-03
Modified: 2024-10-03
Slug: quick-ways-to-disable-github-actions-workflows-without-deletion
Status: published
Summary: Learn three quick methods to temporarily disable GitHub Actions workflows without deleting them, including commenting out code, using manual triggers, and adding conditional logic.
ai_summary: true
Title: Quick Ways to Disable GitHub Actions Workflows Without Deletion
tags:
  - github
  - github-actions
  - workflow
  - ci
  - yaml
---
GitHub Actions workflows are powerful automation tools, but sometimes you need to temporarily disable them. Here are three simple methods to pause a workflow without deleting its YAML file:

1. Comment out the file: Add '#' at the start of each line in the workflow file.
2. Use manual triggers: Replace existing triggers with `on: workflow_dispatch`.
3. Add a false condition: Insert `if: false` under the `jobs` key.

## Example of method 3

```yaml
name: My Workflow

on:
  push:
    branches: [main]

jobs:
  if: false  # This disables the entire workflow
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      # ... rest of the job steps
```
