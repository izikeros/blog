---
name: article-toc-generator
description: Add or update Table of Contents in markdown articles with proper anchor links. Removes legacy SublimeText MarkdownTOC plugin markers and generates clean, genuine TOC. Automatically invokes article-post-edit-actions skill after completion.
---

# Article TOC Generator

Generate and maintain Table of Contents for markdown blog articles with proper anchor navigation. Handles migration from legacy SublimeText MarkdownTOC plugin format to clean markdown TOC.

## When to Use

- User asks to add a table of contents to an article
- User wants to update/refresh TOC after adding new sections
- Article needs navigation structure for better readability
- Preparing an article for publication
- Migrating old articles from MarkdownTOC plugin format

## Inputs

- **file_path**: Path to the markdown article file
- **levels** (optional): Heading levels to include (default: "2,3" for ## and ###)

## Process

### Step 1: Read and Parse Article

1. Read the markdown file
2. Identify front matter (content between `---` markers)
3. Find all headings at specified levels (## and ### by default)
4. Check for existing TOC - detect legacy MarkdownTOC plugin markers:
   - `<!-- MarkdownTOC ... -->` (various attribute combinations)
   - ``

### Step 2: Generate Anchor Names

For each heading, create a kebab-case anchor:

1. Convert to lowercase
2. Replace spaces with hyphens
3. Remove special characters (keep alphanumeric and hyphens)
4. Handle duplicates by appending numbers if needed

**Examples:**
| Heading | Anchor |
|---------|--------|
| `## Leveraging Hybrid Search` | `leveraging-hybrid-search` |
| `### Query Compression` | `query-compression` |
| `## What's New in 2024?` | `whats-new-in-2024` |
| `## References` | `references` |

### Step 3: Remove Legacy MarkdownTOC Markers

If legacy SublimeText MarkdownTOC plugin markers are found, remove them completely:

**Patterns to detect and remove:**
```markdown
<!-- MarkdownTOC -->
<!-- MarkdownTOC autolink="true" -->
<!-- MarkdownTOC autolink="true" autoanchor="true" -->
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

```

**Regex pattern for detection:**
```
<!-- MarkdownTOC[^>]*-->

```

**Action:**
1. Find opening marker: `<!-- MarkdownTOC` ... `-->`
2. Find closing marker: ``
3. Extract TOC content between markers (the actual list items)
4. Remove both markers, keep only the TOC list temporarily
5. The TOC list will be regenerated fresh in Step 5

### Step 4: Add Anchor Tags to Headings

Insert HTML anchor tag above each heading:

```markdown
<a id="section-name"></a>

## Section Name
```

**Important:** 
- Add blank line before anchor for proper rendering
- Anchor tag goes on its own line, directly above heading
- Don't add anchors if they already exist

### Step 5: Generate Clean TOC Block

Create a clean TOC **without** legacy MarkdownTOC plugin markers:

```markdown
## Table of Contents

- [First Section](#first-section)
- [Second Section](#second-section)
  - [Subsection A](#subsection-a)
  - [Subsection B](#subsection-b)
- [Third Section](#third-section)
```

**TOC Structure:**
- Optional `## Table of Contents` heading (include if article uses headings for structure)
- Level 2 headings (##) at root level
- Level 3 headings (###) indented with 2 spaces
- Each entry: `- [Heading Text](#anchor-name)`
- **No HTML comment markers** - pure markdown

### Step 6: Insert TOC in Article

**Location:** After front matter, before first content paragraph

1. Find end of front matter (second `---`)
2. Remove any existing TOC block (including legacy MarkdownTOC markers)
3. Insert new clean TOC after a blank line
4. Ensure blank line after TOC before content

**If legacy TOC exists:**
- Remove entire block including `<!-- MarkdownTOC ... -->` and `` markers
- Replace with clean markdown TOC at same position

### Step 7: Invoke Post-Edit Actions

After completing TOC changes, invoke the `article-post-edit-actions` skill with:
- **file_path**: Same article file
- **edit_descriptions**: 
  - "Added table of contents" (if new TOC)
  - "Updated table of contents" (if refreshed existing TOC)
  - "Migrated from legacy MarkdownTOC format" (if old markers were removed)
  - "Added anchor links to headings" (if anchors were added)

## Example Transformations

### Example 1: New Article (no existing TOC)

**Before:**
```markdown
---
Title: My Article
Date: 2024-01-15
---
Introduction paragraph here.

## First Section

Content...

### Subsection

More content...

## Second Section

Final content...
```

**After:**
```markdown
---
Title: My Article
Date: 2024-01-15
Modified: 2026-02-07
---
Introduction paragraph here.

## Table of Contents

- [First Section](#first-section)
  - [Subsection](#subsection)
- [Second Section](#second-section)

<a id="first-section"></a>

## First Section

Content...

<a id="subsection"></a>

### Subsection

More content...

<a id="second-section"></a>

## Second Section

Final content...

**Edits:**

- 2026-02-07: Added table of contents
- 2026-02-07: Added anchor links to headings
```

### Example 2: Migrating from Legacy MarkdownTOC Plugin

**Before (with SublimeText MarkdownTOC markers):**
```markdown
---
Title: Old Article
Date: 2020-05-10
---
Introduction paragraph here.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [First Section](#first-section)
- [Second Section](#second-section)



<a id="first-section"></a>

## First Section

Content...

<a id="second-section"></a>

## Second Section

Final content...
```

**After (clean markdown TOC):**
```markdown
---
Title: Old Article
Date: 2020-05-10
Modified: 2026-02-07
---
Introduction paragraph here.

## Table of Contents

- [First Section](#first-section)
- [Second Section](#second-section)

<a id="first-section"></a>

## First Section

Content...

<a id="second-section"></a>

## Second Section

Final content...

**Edits:**

- 2026-02-07: Migrated from legacy MarkdownTOC format
```

## Output

- Modified article with:
  - TOC block after front matter
  - Anchor tags above all headings
  - Updated metadata (via post-edit actions skill)

## Success Criteria

- [ ] TOC placed after front matter, before content
- [ ] All ## and ### headings included in TOC
- [ ] Anchor IDs use kebab-case naming
- [ ] Each heading has corresponding `<a id="">` tag above it
- [ ] TOC links match anchor IDs exactly
- [ ] Indentation correct (### indented under ##)
- [ ] Post-edit actions skill invoked with appropriate descriptions
- [ ] Modified date updated
- [ ] Edits section updated with change description

## Edge Cases

### Legacy MarkdownTOC Markers
Various formats to handle:
```markdown
<!-- MarkdownTOC -->
<!-- MarkdownTOC autolink="true" -->
<!-- MarkdownTOC autolink="true" autoanchor="true" -->
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->
<!-- MarkdownTOC levels="1,2,3" -->
```
- All variations should be detected and removed
- Closing marker is always ``
- Replace with clean markdown TOC

### Existing Clean TOC
- If TOC exists without MarkdownTOC markers, regenerate it
- Keep same position in document

### Existing Anchors
- Skip headings that already have `<a id="">` directly above
- Or update anchor if ID doesn't match expected format

### Special Characters in Headings
- Remove: `!@#$%^&*()+=[]{}|;:'",.<>?/\``
- Keep: alphanumeric, spaces (convert to hyphens)
- Apostrophes in contractions: remove (`What's` → `whats`)

### Duplicate Headings
If same heading text appears multiple times:
- First occurrence: `#section-name`
- Second occurrence: `#section-name-1`
- Third occurrence: `#section-name-2`

## Notes

- This skill always chains to `article-post-edit-actions` on completion
- Preserve any content between front matter and first heading (intro paragraphs)
- **No HTML comment markers** - generate pure markdown TOC
- Legacy MarkdownTOC markers from SublimeText plugin should be removed
- Clean markdown TOC is more portable and readable
