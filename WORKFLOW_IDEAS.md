# Blog Workflow Improvement Ideas

Ideas for improving the Obsidian + LLM + Jupyter blog writing workflow.

## Current Setup Analysis

Already installed and working:
- **pelican-obsidian** (custom fork) - handles wikilinks, callouts
- **pelican-jupyter** - renders Jupyter notebooks
- **yaml_metadata** - YAML frontmatter support
- **Pagefind** - full-text search
- **exclude_category** - filtered index pagination
- YAML frontmatter format compatible with Obsidian

## 1. Enable More Installed Plugins

These are installed but not enabled in `pelicanconf.py`:

```python
PLUGINS = [
    "exclude_category",
    "yaml_metadata",
    "pelican_obsidian",      # ADD: Obsidian wikilinks, callouts, embeds
    "pelican_jupyter",       # ADD: Jupyter notebook rendering
    "neighbors",             # ADD: Previous/Next article links
    "related_posts",         # ADD: Show related articles
    "sitemap",               # ADD: SEO sitemap generation
]
```

## 2. Cross-Posting / Syndication Tools

### Option A: CLI Tool (Recommended)

**[cross-post](https://github.com/shahednasser/cross-post)** - CLI to publish to Dev.to, Medium, Hashnode

```bash
pip install cross-post
cross-post https://safjan.com/my-article/ -p dev hashnode medium
```

Add Makefile target:
```makefile
syndicate:
	@read -p "Article URL: " url; \
	cross-post $$url -p dev hashnode medium
```

### Option B: Browser Extension

**[OnePublish](https://onepubli.sh)** - Cross-post from Notion/web to Dev.to, Hashnode, Medium, LinkedIn

### Option C: RSS-based Auto-Syndication

- Dev.to can import from RSS feed automatically (Settings -> Extensions)
- Configure canonical URLs to point back to your blog for SEO

### Option D: Platform-Specific APIs

Create a script that uses:
- Dev.to API: `POST https://dev.to/api/articles`
- Hashnode GraphQL API
- Medium API (limited)

## 3. New Custom Plugin Ideas

### A. `llm-metadata` Plugin

Auto-generate missing metadata using LLM API:

```python
# Features:
# - Generate summary if missing
# - Suggest tags based on content
# - Generate meta description for SEO
# - Estimate reading level

# Usage in frontmatter:
# LLM-Generate: summary, tags
```

### B. `canonical-syndication` Plugin

Track where articles are syndicated:

```yaml
---
Title: My Article
Syndicated-To:
  - platform: dev.to
    url: https://dev.to/username/article
    date: 2024-01-15
  - platform: medium
    url: https://medium.com/@user/article
    date: 2024-01-16
---
```

Display "Also published on" links in article footer with platform icons.

### C. `obsidian-publish-status` Plugin

Sync publish status between Obsidian and Pelican:

```python
# Maps Obsidian properties to Pelican metadata:
# - publish: true  -> Status: published
# - publish: false -> Status: draft
# - Reads from Obsidian's YAML frontmatter
```

### D. `git-article-stats` Plugin

Track article history from git:

```python
# Adds to article context:
# - article.git_created_date
# - article.git_modified_date  
# - article.git_revision_count
# - article.git_contributors
```

### E. `social-cards` Plugin

Auto-generate Open Graph images:

```python
# Creates OG images with:
# - Article title
# - Author name/avatar
# - Blog branding
# - Category/tags
# Saves to /images/og/{slug}.png
```

## 4. Makefile Workflow Enhancements

```makefile
# Validate frontmatter before publish
validate:
	@echo "Validating frontmatter..."
	@python scripts/validate_frontmatter.py content/posts/

# Create new article from template
new-article:
	@read -p "Article title: " title; \
	slug=$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-'); \
	date=$$(date +%Y-%m-%d); \
	cp templates/article.md "content/posts/$$date-$$slug.md"; \
	sed -i '' "s/{{title}}/$$title/g; s/{{date}}/$$date/g; s/{{slug}}/$$slug/g" \
		"content/posts/$$date-$$slug.md"; \
	echo "Created: content/posts/$$date-$$slug.md"

# Create new note
new-note:
	@read -p "Note title: " title; \
	slug=$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-'); \
	date=$$(date +%Y-%m-%d); \
	cp templates/note.md "content/posts/notes/$$slug.md"; \
	sed -i '' "s/{{title}}/$$title/g; s/{{date}}/$$date/g; s/{{slug}}/$$slug/g" \
		"content/posts/notes/$$slug.md"; \
	echo "Created: content/posts/notes/$$slug.md"

# Syndicate latest article
syndicate-latest:
	@latest=$$(git log --diff-filter=A --name-only --pretty=format: -1 -- 'content/posts/*.md' | head -1); \
	if [ -n "$$latest" ]; then \
		slug=$$(basename "$$latest" .md | sed 's/^[0-9-]*//'); \
		echo "Syndicating: $(SITEURL)/$$slug/"; \
		cross-post "$(SITEURL)/$$slug/" -p dev hashnode; \
	else \
		echo "No new article found"; \
	fi

# Generate social media images for all articles
social-images:
	python scripts/generate_og_images.py

# Check for draft articles
drafts:
	@echo "Draft articles:"
	@grep -l "Status: draft" content/posts/**/*.md 2>/dev/null || echo "No drafts found"

# List articles without images
missing-images:
	@echo "Articles without featured images:"
	@for f in content/posts/**/*.md; do \
		if ! grep -q "^Image:" "$$f" 2>/dev/null; then \
			echo "  $$f"; \
		fi; \
	done
```

## 5. Obsidian Integration Improvements

### Article Template

Create `_templates/blog-article.md` in Obsidian:

```yaml
---
Title: {{title}}
Date: {{date:YYYY-MM-DD}}
Modified: {{date:YYYY-MM-DD}}
Category: 
Status: draft
Tags:
  - 
Summary: 
Image: /images/head/
Slug: {{title | lower | replace(" ", "-")}}
---

## Introduction

## Main Content

## Conclusion

## References
```

### Note Template

Create `_templates/blog-note.md`:

```yaml
---
Title: {{title}}
Date: {{date:YYYY-MM-DD}}
Modified: {{date:YYYY-MM-DD}}
Category: note
Status: published
Tags:
  - 
Slug: {{title | lower | replace(" ", "-")}}
---

{{content}}
```

### Recommended Obsidian Plugins

| Plugin | Purpose |
|--------|---------|
| **Templater** | Dynamic templates with dates, auto-slugs |
| **Linter** | Enforce YAML frontmatter format |
| **Dataview** | Query draft/published status, create dashboards |
| **Obsidian Git** | Auto-commit and sync with blog repo |
| **Natural Language Dates** | Quick date entry |
| **Tag Wrangler** | Manage and rename tags across files |

### Obsidian Dataview Queries

Dashboard for blog management:

```dataview
TABLE Status, Category, Date
FROM "content/posts"
WHERE Status = "draft"
SORT Date DESC
```

```dataview
TABLE length(file.tags) as "Tag Count", Date
FROM "content/posts"  
WHERE !contains(Category, "note")
SORT Date DESC
LIMIT 10
```

## 6. LLM-Assisted Writing Workflow

### Pre-writing
1. Use Claude/ChatGPT to outline article structure
2. Generate initial draft or expand bullet points
3. Ask for code examples and explanations

### Post-writing
1. Generate summary/meta description
2. Suggest relevant tags
3. Create social media posts for syndication
4. Generate alt-text for images

### Prompt Templates

**Summary Generation:**
```
Given this article content, write a 2-3 sentence summary suitable for 
RSS feeds and social media. Focus on the key takeaway for readers.

[article content]
```

**Tag Suggestion:**
```
Based on this article about [topic], suggest 5-8 relevant tags from 
this existing tag list: [existing tags]. Also suggest 2-3 new tags 
if appropriate.

[article content]
```

## 7. Priority Recommendations

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Enable pelican_obsidian, pelican_jupyter, sitemap | 5 min | High |
| 2 | Add Makefile targets (new-article, validate) | 30 min | High |
| 3 | Set up cross-post CLI + syndicate target | 30 min | Medium |
| 4 | Create Obsidian templates | 15 min | Medium |
| 5 | Build canonical-syndication plugin | 2 hrs | Medium |
| 6 | Add frontmatter validation script | 1 hr | Medium |
| 7 | Build llm-metadata plugin | 4 hrs | High |
| 8 | Build social-cards plugin | 3 hrs | Medium |

## Resources

- [cross-post CLI](https://github.com/shahednasser/cross-post)
- [OnePublish Extension](https://onepubli.sh)
- [pelican-obsidian](https://github.com/jonathan-s/pelican-obsidian)
- [Dev.to API Docs](https://developers.forem.com/api)
- [Hashnode API Docs](https://api.hashnode.com/)
