---
name: content-qa
description: Read-only quality gate for blog content before committing or publishing. Validates frontmatter, lints Markdown, checks notebooks are valid JSON, runs a production build into /tmp, and spot-checks rendered HTML. Use after adding or editing posts, notes, pages or notebooks, before publishing, or when a post is missing from the site.
---

# Content QA

Nothing here modifies the repository. Report the findings, then fix only what the user asked for. When you do fix an article or note, set its `Modified:` to today's date (`YYYY-MM-DD`).

## 1. Static checks

```bash
make check                                                  # frontmatter errors + unit tests
.venv/bin/python scripts/validate_frontmatter.py --warnings # include warnings
npx --no-install markdownlint-cli2 <changed .md files>      # MD013 (line length) is tolerated in prose
```

## 2. Notebooks are valid JSON

Pelican skips a broken notebook with only one log line, so the post just disappears.

```bash
find content -name '*.ipynb' -not -path '*/.venv/*' -not -path '*checkpoints*' -print0 \
  | xargs -0 -n1 python3 -c "import json,sys;json.load(open(sys.argv[1]))"
```

If one fails, find the last valid version in git history (`git log --follow -- <nb>`, then `git show <sha>:<nb> | python3 -c 'import json,sys;json.load(sys.stdin)'`) and repair it with a minimal change. Never edit notebooks as text.

## 3. Production build into /tmp (about 1 minute)

```bash
rm -rf /tmp/qa && .venv/bin/pelican content -o /tmp/qa -s publishconf.py 2>&1 | grep -E -A4 "ERROR|WARNING|Done"
```

- Compare the `Processed N articles, M drafts` counts with what you expect. A missing post is usually `Status` missing (it defaults to draft) or a skipped file.
- `Skipping ... could not find information about 'title'` means a `.md` file has no frontmatter. Add frontmatter, or move the file out of `content/`.
- Never build into `docs/` for QA. A dev build there contains `127.0.0.1` URLs.

## 4. Spot-check the rendered output

```bash
P=/tmp/qa/<slug>/index.html
grep -o '<h[23][^>]*>.*</h[23]>' $P | head      # headings rendered (a tab before ## breaks them)
grep -c '<meta name="description"' $P
grep -n '<slug>' /tmp/qa/sitemap.xml /tmp/qa/llms.txt
```

## Report

Give a short table: check, result, and file:line for each problem.
