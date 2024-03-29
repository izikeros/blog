---
Category: note
Date: '2021-10-08'
Modified: '2023-07-12'
Slug: git-pre-commit-hooks
Status: published
Summary: Pre-commit is a convenient framework to manage git hooks. Uses configuration in the yaml file, handle the installation of required hooks and tools.
Tags: best-practices, commit, git, GitHub, hooks, management, project
Title: Pre-Commit Hooks
---
up:: [[MOC_Git]]

Pre-commit is a convenient framework to manage git hooks. Uses configuration in YAML file, handles the installation of required hooks and tools.

# Pre-commit

repo with [hooks](https://github.com/pre-commit/pre-commit-hooks) to be used with [pre-commit](https://pre-commit.com/)

## Install pre-commit

```sh
pip install pre-commit
```

## Create config file e.g

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    sha: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    sha: 21.12b0
    hooks:
    -   id: black
```

## Install hooks

run `pre-commit install` to set up the git hook scripts. Now pre-commit will run automatically on git commit

## Run against all files before committing (optional)

It's usually a good idea to run the hooks against all the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)

```sh
pre-commit run --all-files
```

upgrade pre-commit hooks to the most recent version:

```sh
pre-commit autoupdate
```

see also: <https://github.com/sds/overcommit>

An exemplary set of hooks

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
# Use: `pre-commit autoupdate` to update the hooks

# Hooks:
# - JupyText - for syncing notebooks with python scripts
# - black - for formatting
# - pyupgrade - A tool to automatically upgrade syntax for newer versions of the language.
# - flake8 - various checks
# - trailing-whitespace
# - end-of-file-fixer
# - mixed-line-ending

repos:
# synchronize notebooks staged for commit with corresponding python scripts
-   repo: https://github.com/mwouts/jupytext
    rev: v1.13.4
    hooks:
    - id: jupytext
      args: [--sync, --pipe, black]
      additional_dependencies:
        - black==21.12b0 # Matches black hook version
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: mixed-line-ending
-   repo: https://github.com/psf/black
    rev: 21.12b0
    hooks:
    -   id: black
-   repo: https://github.com/asottile/pyupgrade
    rev: v2.29.1
    hooks:
    -   id: pyupgrade
        args: [--py36-plus]
-   repo: https://github.com/pycqa/flake8
    rev: '4.0.1'  
    hooks:
    -   id: flake8
        exclude: (__pycache__|.venv|tmp|notebooks)
        #additional_dependencies: [flake8-docstrings]
```

## Selection of hooks for organizing imports

Perhaps the most used import organizer is [isort](https://github.com/PyCQA/isort) (4.5k stars).
The others are:

- [reorder_python_imports](https://github.com/asottile/reorder_python_imports) (423 stars)
- [zimports](https://github.com/sqlalchemyorg/zimports) (64 stars)
- [importantize](https://github.com/miki725/importanize) (57 stars)

```yaml
  # ------------ Sort imports ------------
   - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)

   - repo: https://github.com/sqlalchemyorg/zimports/
    rev: v0.4.0
    hooks:
      - id: zimports

  - repo: https://github.com/asottile/reorder_python_imports
    rev: v2.7.1
    hooks:
      - id: reorder-python-imports

  - repo: https://github.com/miki725/importanize/
    rev: 'master'
    hooks:
      - id: importanize
        args: [ --verbose ]
```

## Excluding

If you don't want some directories to be subject to pre-commit exclude them as in the example:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: '4.0.1'  
    hooks:
    -   id: flake8
        exclude: (__pycache__|.venv|tmp|notebooks)
        #additional_dependencies: [flake8-docstrings]
```

use `files` to define pattern which files to include. E.g. `files: \.x$` - files ending with `.x` (?)

for more advanced filtering see section "Filtering files with types" on: <https://pre-commit.com/#advanced>

example:

```
    files: ^foo/
    types_or: [javascript, jsx, ts, tsx]
```

will match any of `foo/bar.js` / `foo/bar.jsx` / `foo/bar.ts` / `foo/bar.tsx` but not `baz.js`.

up:: [[MOC_Git]]]
