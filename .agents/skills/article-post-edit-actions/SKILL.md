---
name: article-post-edit-actions
description: Standardize post-edit metadata updates for markdown articles. Updates the Modified date in front matter and maintains an Edits changelog section at the bottom of the article. Use after making any modifications to blog articles.
---

# Article Post-Edit Actions

Standardize metadata updates after editing a markdown article. This skill ensures consistent tracking of modifications across all blog posts.

## When to Use

- After any modification to a blog article
- Called automatically by the `article-toc-generator` skill
- When user requests to update article metadata
- After adding, removing, or modifying content in an article

## Inputs

- **file_path**: Path to the markdown article file
- **edit_descriptions**: List of brief, atomic descriptions of changes made (e.g., "Added table of contents", "Fixed typo in introduction")

## Process

### Step 1: Update Modified Date in Front Matter

1. Read the article file
2. Locate the front matter (between `---` markers)
3. Find the `Modified:` field
4. Update to current date in `YYYY-MM-DD` format
5. If `Modified:` doesn't exist, add it after `Date:` field

**Example:**
```yaml
---
Title: My Article
Date: 2024-01-15
Modified: 2026-02-07  # Updated to current date
---
```

### Step 2: Check for Edits Section

1. Search for `**Edits:**` at the bottom of the article
2. This section should be near the end, typically after References or before any metadata links (X::, up::)

### Step 3: Create or Update Edits Section

**If Edits section doesn't exist:**

1. Find the appropriate location (before any `X::` or `up::` links, or at the very end)
2. Add a blank line
3. Create the section:

```markdown
**Edits:**

- YYYY-MM-DD: Description of change
```

**If Edits section exists:**

1. Prepend new entries after `**Edits:**` line (newest first)
2. Each entry on its own line with format: `- YYYY-MM-DD: Description`

**Example of multiple entries:**
```markdown
**Edits:**

- 2026-02-07: Added table of contents
- 2026-02-07: Added anchor links to headings
- 2024-12-19: Added reference to observability tools
- 2024-06-26: Added summary
```

### Step 4: Save Changes

1. Write the updated content back to the file
2. Preserve all original formatting and content

## Entry Guidelines

### Atomic Descriptions
Each distinct type of change gets its own entry:
- Good: "Added table of contents", "Added anchor links"
- Bad: "Added TOC and anchors and fixed formatting"

### Description Style
- Start with action verb (Added, Updated, Fixed, Removed, Refactored)
- Be concise but informative
- Reference specific sections if relevant

### Examples of Good Entries
- `Added table of contents with anchor links`
- `Fixed broken link in References section`
- `Updated code examples for Python 3.11`
- `Added new section on performance optimization`
- `Removed outdated information about deprecated API`
- `Added RAG fusion paper reference`

## Output

- Modified article with:
  - Updated `Modified:` date in front matter
  - New entry/entries in `**Edits:**` section
- Confirmation of changes made

## Success Criteria

- [ ] `Modified:` date updated to current date (YYYY-MM-DD)
- [ ] `**Edits:**` section exists at article bottom
- [ ] New edit entry added with current date and description
- [ ] Entry format matches: `- YYYY-MM-DD: Description`
- [ ] Newest entries appear first (reverse chronological)
- [ ] Original article content preserved
- [ ] No duplicate entries for same change

## Notes

- Always use ISO date format: YYYY-MM-DD
- Preserve existing entries when adding new ones
- Place Edits section before any Obsidian-style links (X::, up::)
- Multiple changes in one edit session = multiple entries with same date
- This skill can be invoked standalone or chained from other skills
