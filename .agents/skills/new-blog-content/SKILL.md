---
name: new-blog-content
description: Create a new blog post, TIL note or page for this Pelican blog with complete, valid frontmatter (Title, Slug, Date, Modified, Status, Tags, Category, Summary). Use when the user asks to write, draft, add or publish a new article, note or page, or to fill in missing frontmatter/summaries.
---

# New Blog Content

Create content that builds on the first try and is ready to be cited by search and answer engines.

Write the body in the author's voice: follow [`STYLE.md`](../../../STYLE.md) and run its checklist before finishing.

## Where files go

| Type | Path | Category |
|------|------|----------|
| Article | `content/posts/posts/YYYY/YYYY-MM-DD-slug.md` | an existing category (see `KNOWN_CATEGORIES` in `scripts/validate_frontmatter.py`) |
| TIL note | `content/posts/notes/snake_case_name.md` | `note` (hidden from the homepage, listed on `/til.html`) |
| Page | `content/pages/slug.md` | none |
| Notebook post | `content/posts/notebooks/YYYY-MM-DD-slug/*.ipynb` | see `.github/copilot-instructions.md` |

## Frontmatter template

```yaml
---
Title: Human readable title
Slug: kebab-case-slug
Date: YYYY-MM-DD
Modified: YYYY-MM-DD
Status: published
Tags: tag-one, tag-two
Category: note
Summary: One or two sentences, 150-300 characters, stating the answer or claim.
---
```

Templates in `~/vimwiki/Templates/blog_{post,note}_frontmatter.md` follow the same keys.

## Rules (each one has caused a real failure)

1. **Always set `Status`.** `pelicanconf.py` has `DEFAULT_METADATA = {"status": "draft"}`, so a file without `Status: published` is silently built as a draft. Pages also need it.
2. **Capitalized keys only** (`Tags`, not `tags`). Never put both casings in one file.
3. **`Summary` is required.** It feeds listings, meta description, Open Graph and `llms.txt`. Write it from the content: lead with the concrete answer, name the tools or concepts, and add no hype. For the target readers (AI technical leaders, enterprise practitioners, senior and staff engineers), give the takeaway, not the teaser.
4. **YAML safety:** a plain scalar must not contain `: ` (colon and space) or start with a backtick, `*`, `[`, `{`, `>`, `|`, `@`, `'`, `"` or `%`. Rephrase, or quote the whole value with single quotes.
5. **Dates:** `YYYY-MM-DD`, or ISO with a full offset (`+01:00`, not `+01:0`). Drafts may leave `Date` empty only while `Status: draft`.
6. **Body hygiene:** no leading tabs before headings (that turns them into code), no leftover citation markers like `【1-abc】`, unique heading texts, a language tag on code fences, and no blank line just before a closing fence.
7. Don't edit `docs/`; it is generated.

## Verify

```bash
.venv/bin/python scripts/validate_frontmatter.py --warnings <file>
npx --no-install markdownlint-cli2 <file>   # MD013 line length is tolerated in prose
```

Then run the `content-qa` skill for a production render check.
