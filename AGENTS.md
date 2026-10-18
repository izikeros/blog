# AGENTS.md

Guidance for AI coding agents working in this repository.

## Overview

Source and generated output of the blog [safjan.com](https://www.safjan.com), built with the Pelican
static site generator. Markdown (and some notebook) articles live in `content/`; the rendered site is
written to `docs/` and committed (GitHub Pages compatible). See `README.md` for detailed maintenance notes.

## Tech stack

- Python 3.12 (`requires-python = "==3.12.*"`), uv (`uv.lock`) – PDM files (`pdm.lock`, `.pdm-python`) are legacy
- Pelican >= 4.11 with many plugins (pelican-obsidian and pelican-jupyter from izikeros' git forks,
  sitemap, series, neighbors, render-math, yaml-metadata, related-posts, ...)
- Theme: `pelican-themes/Flex` (git submodule, izikeros/Flex fork)
- Node tooling via `npx`: pagefind (search index), prettier, html-validate; `package.json` holds theme asset scripts
- Dev: pytest, djlint; pre-commit hooks: prettier, markdownlint-cli2

## Repo layout

- `content/posts/` – articles (`posts/<year>/...`), plus `notes/`, `notebooks/`; `content/pages/`, `images/`, `pdfs/`
- `docs/` – generated site (`OUTPUT_PATH`), thousands of files – never edit by hand
- `pelicanconf.py` (dev), `publishconf.py` (production, `SITEURL = https://www.safjan.com`)
- `pelican-themes/` – Flex submodule and other themes
- `pelican-plugins/` – local plugins directory referenced by `PLUGIN_PATHS` (not tracked in git)
- `scripts/` – content maintenance: `fix_duplicate_ids.py`, `remove_anchor_ids.py`, `generate_summaries.py` (local Ollama)
- `tests/test_fix_yaml_tags.py` – tests for the `fix_yaml_tags` plugin from `pelican-plugins/`
- `helpers/` – notebooks/scripts used to create article figures
- `.factory/skills/` – article editing skills (SEO, tags, TOC, post-edit)

## Setup

```bash
git submodule update --init
make venv            # uv lock --upgrade && uv sync + git installs of pelican-obsidian / pelican-jupyter
```

`pyproject.toml` also references `../pelican-ai-analyzer-bar` as an editable path dependency – it must exist
as a sibling directory for `uv sync` to succeed.

## Build / run (Makefile)

```bash
make devserver       # pelican -lr, serve + regenerate
make html            # build with pelicanconf.py into docs/
make publish         # build with publishconf.py + npx pagefind
make validate-html   # / validate-html-strict, format-html
make fix-duplicate-ids | remove-anchor-ids | generate-summaries
make clean
```

## Test

```bash
pytest tests         # needs the local pelican-plugins/ directory
```

## Conventions

- Articles are Markdown with YAML front matter; keep existing metadata keys (title, date, tags, category,
  summary, ...) consistent with neighbouring posts. Front Matter CMS data lives in `.frontmatter/`.
- Markdown is checked by markdownlint-cli2 and prettier via pre-commit.
- Content changes go in `content/`; regenerate `docs/` with `make publish` instead of editing HTML.

## Gotchas

- `make e2e` and `make push` run `git add`/`commit`/`push` automatically – do not run them as part of agent work.
- `docs/` is huge; avoid broad searches/rewrites there and keep diffs to generated output out of unrelated commits.
- `generate-summaries` calls an Ollama server on localhost.

## Don'ts

- Don't commit secrets (e.g. `.factory/mcp.json` tokens, API keys) or `.venv/`, `node_modules/`, `cache/`.
- Don't modify the Flex submodule here – changes belong in the izikeros/Flex repo.
- Don't push to remotes or publish the site without explicit instruction.
