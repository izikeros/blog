---
Title: Quick Ways to Disable GitHub Actions Workflows Without Deletion
Slug: quick-ways-to-disable-github-actions-workflows-without-deletion
Date: 2024-10-03
Modified: 2024-10-03
Status: published
tags:
  - github
  - github-actions
  - workflow
  - ci
  - yaml
Category: note
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
