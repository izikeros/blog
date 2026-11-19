# AGENTS.md — safjan.com blog

Pelican 4.12 static blog (https://safjan.com, apex domain; `www` redirects).
Theme: `pelican-themes/Flex` (git submodule → `izikeros/Flex`, has its own `AGENTS.md`).
More detail: `.github/copilot-instructions.md`.

## Audience and voice

Readers are AI technical leaders, enterprise practitioners, forward-deployed
engineers and senior+ AI/ML/LLM engineers. Write as a practitioner: concrete
trade-offs, decision criteria, failure modes, numbers with methodology. Avoid
hype, filler and generic "ultimate guide" phrasing.

**Before writing, rewriting or editing prose, read [`STYLE.md`](STYLE.md)**
(author voice, AI-tells to avoid, before/after examples, final checklist).

## Tech stack

- Python 3.12, **uv** (`pyproject.toml` + `uv.lock`) is the only dependency manager.
- Pelican >= 4.12; pelican-obsidian, pelican-jupyter and pelican-ai-analyzer-bar
  installed from izikeros' GitHub repos (pinned in `uv.lock`, refresh with
  `uv lock --upgrade-package <name>`); sitemap, series, neighbors, render-math,
  yaml-metadata, related-posts.
- Node via `npx`: pagefind (search), prettier, html-validate. Pre-commit: prettier, markdownlint-cli2.

## Setup

```bash
git submodule update --init
make venv   # uv lock --upgrade && uv sync + git installs of pelican-obsidian / pelican-jupyter
```

## Layout

```
content/posts/posts/<YYYY>/YYYY-MM-DD_slug.md   # articles (shown on index)
content/posts/notes/<slug>.md                   # short notes, Category: note (hidden from index, /til.html)
content/posts/notebooks/YYYY-MM-DD-name/*.ipynb # notebook articles (+ .nbdata metadata)
content/pages/                                  # static pages
content/images/, content/pdfs/                  # assets
pelican-plugins/                                # local plugins (llms_txt, seo_leo_enhancer, ...)
scripts/                                        # content maintenance scripts
helpers/                                        # notebooks/scripts for article figures
.agents/skills/                                 # agent skills (shared by Copilot CLI and Droid)
docs/                                           # GENERATED site (GitHub Pages) — never edit by hand
```

## Frontmatter (YAML, capitalized keys)

```yaml
---
Title: Clear, specific title
Slug: clear-specific-title
Date: 2026-01-31
Modified: 2026-01-31
Category: LLM Engineering # see "Categories" below
Tags:
  - rag
  - evaluation
Summary: One or two plain sentences stating what the reader learns (used in listings, meta description and llms.txt).
Status: published         # REQUIRED: missing Status defaults to draft (DEFAULT_METADATA)
---
```

Required: `Title`, `Date`, `Category`, `Summary`. Use capitalized keys only
(no `tags`/`Tags` mix).

**Rule: whenever you modify an article or note, set `Modified:` to today's date
(`YYYY-MM-DD`)** in the same commit. Add the key after `Date:` if missing.
Applies to body and frontmatter edits alike.

**Exempt: bulk mechanical changes never update `Modified:`.** These are
scripted or repetitive edits across many files that don't change what a reader
sees, e.g. frontmatter key normalization, lint/format fixes, removing anchor
IDs, link or path rewrites, repairing broken notebook JSON. Leave `Modified:`
untouched in such commits.

## Categories

One category per article, picked by topic (format such as "howto" is a tag).
The list is enforced by `KNOWN_CATEGORIES` in `scripts/validate_frontmatter.py`.

| Category | Use for |
|---|---|
| LLM Engineering | Building with LLMs: model choice/migration, prompting, frameworks, enterprise use |
| RAG & Retrieval | RAG pipelines, chunking, embeddings, vector DBs, knowledge graphs, index versioning |
| Evaluation & Observability | LLM/RAG/ML evaluation, metrics, monitoring, tracing |
| MLOps & LLMOps | Deployment, pipelines, platforms, policies, data validation, maturity |
| AI Engineering Leadership | Teams, roles, careers, process (Agile, Shape Up), AI-assisted engineering practice |
| Responsible AI | Explainability (SHAP, LIME), privacy, governance, regulation |
| Applied ML & Data Science | Classic ML, statistics, EDA, visualization, document AI, Kaggle, trading |
| Software Engineering & Tools | Python engineering, testing, coding assistants, CLI/shell, self-hosting, blogging |
| note | Short TIL notes in `content/posts/notes/` (hidden from index) |

Removed category URLs redirect via `CATEGORY_REDIRECTS` in `pelicanconf.py`
(plugin `pelican-plugins/category_redirects`). `LLMS_TXT_CATEGORY_ORDER` puts
the positioning categories first in `llms.txt`.

## Commands

Use the repo venv: `.venv/bin/python`, `.venv/bin/pelican` (or `source .venv/bin/activate`).

| Purpose | Command | Side effects |
|---|---|---|
| Validate post metadata | `make validate-frontmatter PY=.venv/bin/python` | none |
| Safe checks (metadata + tests) | `make check PY=.venv/bin/python` | none |
| Production build to temp dir | `.venv/bin/pelican content -o /tmp/blog-out -s publishconf.py` | none (~1 min) |
| Dev server | `make devserver` | writes `docs/` with dev URLs |
| Production build | `make publish` | rewrites `docs/` + pagefind |

`docs/` is huge: avoid broad searches/rewrites there.
`tests/test_fix_yaml_tags.py` is stale (its plugin no longer exists).

Do NOT run `make e2e` or `make push` — they `git commit` and `git push`.
Do NOT build into `docs/` unless asked; prefer `-o /tmp/...` for verification.
`scripts/fix_duplicate_ids.py`, `remove_anchor_ids.py`, `generate_summaries.py`
modify content in place — run with `--dry-run` first where supported.

## Skills (`.agents/skills/`)

Load the matching skill before doing these tasks:

| Task | Skill |
|------|-------|
| Write a new post, note or page; fill in frontmatter | `new-blog-content` |
| Check content before commit or publish; "post is missing" | `content-qa` |
| Publish or deploy; "why isn't it live" | `publish-and-verify` |
| Edit an existing article (TOC, tags, SEO/LEO, Modified/Edits) | `article-*` |

Add new skills to `.agents/skills/<name>/SKILL.md` (uppercase file name).

## Don'ts

- Don't commit secrets (`.env`, `.factory/mcp.json` tokens, API keys), `.venv/`, `node_modules/`, `cache/`.
- Don't modify the Flex submodule here — changes belong in the izikeros/Flex repo.
- Don't push to remotes or publish the site without explicit instruction.

## Git

- Remotes: `forgejo` (primary push target; Forgejo push-mirrors to GitHub on
  every push) and `origin` (GitHub, read-only from the work Mac).
  GitHub-side commits sync back to Forgejo every 5 min via
  `scripts/github-to-forgejo-sync.sh` (cron on the NAS, fast-forward only).
- Atomic, conventional commits (`feat:`, `fix:`, `docs:`, `content:`, `chore:`).
- Never add `Co-authored-by` trailers for AI tools.
- Don't commit `docs/` together with source changes.
