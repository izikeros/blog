---
name: publish-and-verify
description: Publish the blog to safjan.com safely. Build the production site into docs/, commit it separately from source changes, push to Forgejo, confirm the mirror reached GitHub, and verify the live URLs. Use when the user asks to publish, deploy, release or "make it live", or asks why a change isn't on the site.
---

# Publish and Verify

How the site gets online: source and `docs/` are pushed to **Forgejo**, the Forgejo push mirror copies them to **GitHub** (`izikeros/blog`), and **GitHub Pages** serves `docs/` at `https://safjan.com`.

## Never

- Run `make e2e` or `make push`. They `git add` everything and push in one go.
- Commit `docs/` together with source changes.
- Commit a `docs/` built with `pelicanconf.py` (dev). It contains `http://127.0.0.1:8000` URLs.
- Push directly to GitHub. This Mac can't, and doing so would race the mirror.

## Steps

1. **Gate:** run the `content-qa` skill. Stop on errors.
2. **Source first:** commit source changes as atomic conventional commits, without Copilot co-author trailers.
3. **Build:**

   ```bash
   make publish          # publishconf.py build into docs/ plus pagefind; does not commit
   ```

4. **Sanity-check the build before committing:**

   ```bash
   grep -c '127.0.0.1' docs/index.html docs/sitemap.xml   # must be 0
   head -3 docs/llms.txt; grep -c 'User-agent' docs/robots.txt
   git status --short docs | wc -l
   ```

5. **Commit `docs/` alone:**

   ```bash
   git add docs && git commit -m "build: regenerate site"
   ```

6. **Push to Forgejo and confirm the mirror** (it syncs on commit, usually within seconds):

   ```bash
   git push forgejo master
   git rev-parse --short HEAD
   curl -s https://api.github.com/repos/izikeros/blog/commits/master | python3 -c "import json,sys;print(json.load(sys.stdin)['sha'][:9])"
   ```

7. **Verify live** (GitHub Pages takes 1-3 minutes):

   ```bash
   for u in / /robots.txt /llms.txt /about/ /sitemap.xml; do
     printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' https://safjan.com$u)" "$u"; done
   curl -s https://safjan.com/llms.txt | head -3
   ```

   If something is 404 but present in `docs/`, check the Pages build at https://github.com/izikeros/blog/actions.

## If GitHub didn't update

- Check the mirror: `tea api --login forgejo /repos/izikeros/blog/push_mirrors` (run it from `/tmp`) and look at `last_error`.
- The NAS sync (GitHub to Forgejo, every 5 minutes) logs to `/share/Container/git-sync/blog.log` on `ssh nasi`. `DIVERGED` means someone committed on GitHub. Merge on Forgejo; never force-push.
