---
Title: Downgrade or Upgrade Your Python Version with uv
Slug: downgrade-or-upgrade-your-python-version-with-uv
Date: 2025-06-26
Modified: 2025-06-26
Status: published
Tags: uv, python-version, python-dependencies, python-upgrade, python-downgrade, python-version
Category: note
---

To downgrade your project’s virtual environment e.g. from Python 3.11 to 3.10 using **uv**, here’s a step‑by‑step process:

### 1. Install the desired Python version

Run:

```bash
uv python install 3.10
```

This downloads and manages Python 3.10 in `~/.local/share/uv/python/...` (or the equivalent on your OS) ([docs.astral.sh](https://docs.astral.sh/uv/guides/projects/?utm_source=chatgpt.com "Working on projects | uv - Astral Docs"), [docs.astral.sh](https://docs.astral.sh/uv/concepts/python-versions/?utm_source=chatgpt.com "Python versions | uv - Astral Docs")).

### 2. Pin your project to that version

Within your project directory:

```bash
uv python pin 3.10
```

This writes `3.10` to `.python-version`, ensuring that future commands use that interpreter ([docs.astral.sh](https://docs.astral.sh/uv/?utm_source=chatgpt.com "uv - Astral Docs")).

This might not work in case if your `pyproject.toml` file has a python requirement that prevents upgrade - edit this first, e.g. change:
```
requires-python = ">=3.11"
```
to
```
requires-python = ">=3.10"
```

You can also edit `.python-version` file to have it consistent with the rest of the project.

###  3. Recreate the virtual environment

The simplest and clean method:

```bash
rm -rf .venv
uv venv
```

This creates a fresh venv using Python 3.10, respecting the pin.

Alternatively, if you're managing dependencies via `pyproject.toml` + `uv.lock`:

```bash
uv sync
```

This will recreate the environment from locked specs using the pinned Python version ([news.ycombinator.com](https://news.ycombinator.com/item?id=43903914&utm_source=chatgpt.com "uv is the way. https://docs.astral.sh/uv/ Sadly it appears that people ..."), [docs.astral.sh](https://docs.astral.sh/uv/getting-started/features/?utm_source=chatgpt.com "Features | uv - Astral Docs")).

### Optional: Verify interpreter version

Run:

```bash
. .venv/bin/activate
python --version  # should show Python 3.10.x
```

