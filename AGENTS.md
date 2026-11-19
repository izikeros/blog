# AGENTS.md — safjan.com blog

Pelican 4.11 static blog (https://safjan.com, apex domain; `www` redirects).
Theme: `pelican-themes/Flex` (git submodule → `izikeros/Flex`, has its own `AGENTS.md`).
More detail: `.github/copilot-instructions.md`.

## Audience and voice

Readers are AI technical leaders, enterprise practitioners, forward-deployed
engineers and senior+ AI/ML/LLM engineers. Write as a practitioner: concrete
trade-offs, decision criteria, failure modes, numbers with methodology. Avoid
hype, filler and generic "ultimate guide" phrasing.

## Tech stack

- Python 3.12, **uv** (`uv.lock`); PDM files (`pdm.lock`) are legacy.
- Pelican >= 4.11; pelican-obsidian / pelican-jupyter from izikeros' git forks
  (installed by `make venv`); sitemap, series, neighbors, render-math, yaml-metadata, related-posts.
- `pyproject.toml` references `../pelican-ai-analyzer-bar` as an editable path
  dependency — it must exist as a sibling directory for `uv sync` to succeed.
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
Category: Generative AI   # note | Machine Learning | Generative AI | MLOps | Responsible AI | Howto | Linux | Software Development | Data Science
Tags:
  - rag
  - evaluation
Summary: One or two plain sentences stating what the reader learns (used in listings, meta description and llms.txt).
Status: published         # REQUIRED: missing Status defaults to draft (DEFAULT_METADATA)
---
```

Required: `Title`, `Date`, `Category`, `Summary`. Use capitalized keys only
(no `tags`/`Tags` mix). Bump `Modified` only for substantive updates.

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
