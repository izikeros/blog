---
date: '2021-10-08'
status: published
suggested_tags: commit, github, hook, pre, sh, yaml, git
summary: Pre-commit is convenient framework to manage git hooks. Uses configuration in yaml file, handle installation of required hooks and tools.
tags: best practices, commit, git, github, hooks, management, project
title: Git pre-commit hooks
slug: git-pre-commit-hooks
category: note
---

Pre-commit is convenient framework to manage git hooks. Uses configuration in yaml file, handle installation of required hooks and tools.

# Pre-commit
repo with [hooks](https://github.com/pre-commit/pre-commit-hooks) to be used with [pre-commit](https://pre-commit.com/)

## Install pre-commit
```sh
pip install pre-commit
```

## Create config file e.g.:
```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    sha: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    sha: 19.3b0
    hooks:
    -   id: black
```

## Install hooks
run `pre-commit install` to set up the git hook scripts. Now pre-commit will run automatically on git commit

## Run against all files before commit (optional)
It's usually a good idea to run the hooks against all of the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)
```sh
pre-commit run --all-files
```

see also: https://github.com/sds/overcommit

