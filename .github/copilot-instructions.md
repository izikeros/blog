# Copilot Instructions for Safjan Blog

This is a Pelican-based static blog generator for [safjan.com](https://safjan.com). The site converts Markdown and Jupyter notebooks into a complete blog with custom Flex theme and numerous content-enriching plugins.

> Start with `AGENTS.md` (canonical agent guidance: layout, frontmatter, safe commands).

## Build & Development Commands

### Quick Start
```bash
source .venv/bin/activate    # Activate the repo virtual environment
make devserver               # Serve locally with auto-reload on http://localhost:8000
```

### Common Commands
- `make html` — Generate site in development mode
- `make publish` — Generate production build with pagefind search (no git push)
- `make check` — Non-mutating checks: frontmatter validation + unit tests
- `make clean` — Remove generated output directory
- `make serve [PORT=8000]` — Serve without regeneration
- `make e2e` — Full publish pipeline: build, pagefind indexing, git commit/push

### Content Management
- `make fix-duplicate-ids` — Fix duplicate HTML IDs in markdown files
- `make remove-anchor-ids` — Remove `<a id>` anchor elements from markdown
- `make generate-summaries` — Generate missing article summaries using Ollama
- `make format-html` — Format HTML output with Prettier
- `make validate-html` — Validate HTML (errors only)
- `make validate-html-strict` — Validate HTML including warnings

### Environment
- `make venv` — Set up virtual environment using uv
- Dependency management: Uses `uv` with `pyproject.toml` (Python 3.12)
- Uses `uv pip install` for git-based plugin installation (pelican-obsidian, pelican-jupyter)

## Architecture Overview

### Key Structure
```
content/
  posts/           # Blog articles (.md, .ipynb)
  pages/           # Static pages (about, contact, etc.)
  images/          # Article assets and figures
  pdfs/            # Downloadable files (resumes, etc.)
  styles/          # Custom CSS
docs/              # Generated site (GitHub Pages, DO NOT EDIT)
pelicanconf.py     # Development configuration (IS_DEVELOPMENT = True)
publishconf.py     # Production configuration override
pyproject.toml     # Python dependencies (uv-based)
pelican-themes/    # Theme customization (Flex fork)
pelican-plugins/   # Plugin directory
scripts/           # Python helper scripts
```

### Pelican Plugins
The blog uses numerous plugins installed in `pyproject.toml`:
- **pelican-jupyter** — Convert Jupyter notebooks (.ipynb) to articles
- **pelican-obsidian** — Process Obsidian vault references
- **pelican-yaml-metadata** — Parse YAML frontmatter
- **pelican-render-math** — LaTeX math rendering
- **pelican-series** — Group related posts into series
- **pelican-related-posts** — Show related article suggestions
- **pelican-neighbors** — Add previous/next article links
- **pelican-simple-footnotes** — Markdown footnote support
- **pelican-sitemap** — Generate sitemap.xml
- **pelican-featured-image** — Extract featured image from content
- **pelican-ai-analyzer-bar** — buttons to summarize the article in ChatGPT/Perplexity/Claude/Gemini/Grok (izikeros' GitHub repo)
- **pelican-share-post** — Social sharing buttons
- **pelican-more-categories** — Enhanced category support

### Content Metadata
Articles use YAML frontmatter (or Python-style metadata) with:
- `Title`, `Date`, `Modified`, `Category`, `Tags`, `Summary`
- When modifying an article or note, set `Modified:` to today's date (`YYYY-MM-DD`); bulk mechanical changes (key normalization, lint/format fixes, link rewrites) are exempt and must not touch it
- `Image` / featured image support
- `Series` for grouping related posts
- Obsidian/wikilink integration

### Theme
Custom fork of **Flex** theme with modifications:
- Modified Font Awesome styling and version handling
- Custom `custom.css` for social icon styling
- Sidebar branding and social links
- Dark mode support (JS-based theme toggle)

## Key Conventions

### Writing style
When writing, rewriting or editing article/note prose, follow `STYLE.md` (author voice, AI-tells to avoid, checklist).

### Content File Format
- **Markdown articles**: `content/posts/posts/<YYYY>/YYYY-MM-DD_article-slug.md`
- **Notes** (Category `note`, hidden from index): `content/posts/notes/<slug>.md`
- **Jupyter notebooks**: `content/posts/notebooks/YYYY-MM-DD-name/<name>.ipynb`
  - Requires YAML frontmatter in first cell or standard Pelican metadata
  - Use `remove_input` tag on styling/cleanup cells (last cell)
  - Format code with `black --ipynb`
  - Keep code lines short (ruler ~80) to avoid horizontal scroll
  - Hide trivial imports with `remove_input` tag
  - Provide Colab/Binder badges and table of contents

### Pelican Configuration
- **Development mode**: `IS_DEVELOPMENT = True` in `pelicanconf.py` (disables feeds, analytics)
- **Production mode**: `IS_DEVELOPMENT = False` in `pelicanconf.py`
- Categories to exclude from index: Set `INDEX_EXCLUDE_CATEGORIES` in config
- Special category: `note` — Hidden from homepage (filtered in index template)
- Output directory: `docs/` (GitHub Pages compatible)

### Pre-commit Hooks
- **HTML files** (`docs/**/*.html`): Formatted with Prettier (2-space indent, HTML parser)
- **Markdown files** (`content/posts/**/*.md`): Linted with markdownlint-cli2
- Run with `pre-commit run` or `pre-commit autoupdate`

### Styling & Assets
- Favicons: Generated via [RealFaviconGenerator](https://realfavicongenerator.net/), placed in `content/`
- CSS minification: `npm run minify-pygments` for code highlighting
- Font Awesome: `npm run copy-fontawesome` from node_modules
- JavaScript minification: `npm run minify-js` for dark mode theme script

### RSS/Atom Feeds
- Production: `FEED_ALL_ATOM`, `FEED_ALL_RSS`, `CATEGORY_FEED_ATOM` enabled
- Development: Feeds disabled by default
- Use `FEED_UTM_PARAMS` to customize tracking parameters

### Publishing Pipeline
`make publish` runs steps 1–2; `make e2e` runs all four (agents: never run `e2e`):
1. Build with `publishconf.py` settings
2. Run pagefind to generate full-text search index
3. Commit generated `docs/` directory to git
4. Push to remote

## Common Tasks

### Adding a New Blog Post
1. Create `content/posts/posts/<YYYY>/YYYY-MM-DD_article-slug.md` with YAML frontmatter:
   ```yaml
   ---
   Title: Article Title
   Date: YYYY-MM-DD
   Category: CategoryName
   Tags:
     - tag1
     - tag2
   Summary: Brief summary for listings
   Image: featured-image.png
   ---
   ```
2. Verify locally with `make devserver`
3. When ready: commit and `make publish` (or `make e2e`)

### Converting Jupyter Notebook to Blog Post
1. Place notebook in `content/posts/notebooks/YYYY-MM-DD-name/`
2. Add YAML frontmatter in first markdown cell
3. Remove/hide styling and utility cells with `remove_input` tag
4. Run `black --ipynb content/posts/notebook.ipynb`
5. Test with `make devserver`

### Fixing Generated Content Issues
- Duplicate HTML IDs: `make fix-duplicate-ids` (runs script, modifies .md files)
- Broken anchor links: `make remove-anchor-ids` (removes problematic `<a id>` tags)
- Missing summaries: `make generate-summaries` (uses Ollama, requires setup)

### Customizing Theme
- Theme files: `pelican-themes/Flex/` (custom fork)
- Changes are diverged from upstream; apply patches carefully
- Social icon styling: `static/dark-theme/` and custom.css
- Sidebar: Headline hardcoded in `SITESUBTITLE` variable

## Debugging

### Enable Debug Output
```bash
make DEBUG=1 html           # Run with verbose pelican output
pelican -lr --debug         # Debug live reload
```

### Common Issues
- **Plugin loading fails**: Ensure plugins installed via `uv` are listed in `pyproject.toml` and `pelicanconf.py`
- **Notebook not rendering**: Check frontmatter in first cell; ensure nbconvert/jupyter versions match config
- **Theme not applying**: Clear cache with `make clean`; check static file copying in `STATIC_PATHS`

## NPM Scripts

```bash
npm run build              # Run all minification/copy tasks
npm run minify-js          # Minify dark theme JS
npm run copy-fontawesome   # Copy Font Awesome icons to static/
npm run minify-pygments    # Minify Pygments CSS for code highlighting
npm run test               # Build and validate site
```

## Maintenance

### Upgrading Dependencies
```bash
uv lock --upgrade && uv sync  # Update Python packages
npm update                     # Update Node packages
```

### Git Workflow
- Content: Commit to branch, PR reviewed before merge
- `docs/` (generated): Committed automatically by `make publish`/`make e2e`
- Pre-commit hooks run on `.md` and `.html` files only
