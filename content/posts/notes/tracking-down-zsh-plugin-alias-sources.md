---
Title: Tracking Down zsh Alias Plugin Sources
Slug: tracking-down-zsh-alias-plugin-sources
Date: 2025-02-28
Modified: 2025-02-28
Status: published
Tags:
  - til
  - zsh
  - zsh-alias
  - alias
Category: note
---

When hunting for the origin of mysteriously defined by unknown plugin zsh aliases:

```bash
zsh -xv 2>&1 | grep "alias_name"
```

This works by:

1. Starting zsh with `-x` (trace) and `-v` (verbose) flags
2. Redirecting both stdout and stderr (`2>&1`) to capture all output
3. Filtering with `grep` to find when your alias is defined

For a more targeted approach with less output:

```bash
zsh -xv 2>&1 | grep -A 3 "source.*plugin" | grep "alias_name"
```

This helps identify which plugin file is sourcing your alias.
