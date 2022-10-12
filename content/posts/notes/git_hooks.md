---
title: Git hooks
date: 2021-10-20
modified: 2021-10-20
status: published
tags: git, hooks, pre-commit_hooks, software/project, project
summary: Example of how to set up git hooks manually or with pre-commit tool
slug: git-hooks
category: note
citation_needed: false
---
Git hook makes it easier to keep order in the software project:
- can help following agreed conventions related with e.g.
	+ code format, code quality
	+ workflow
	+ commit practices and format

# Exemplary check before the commit
If not exists, create `hooks` directory in the `.git` folder of the demo and add these files.
```
.git/hooks
├── isort_hooks.py
└── pre-commit
```

isort_hooks.py
```python
#!/usr/bin/env python
import sys

from isort.hooks import git_hook

sys.exit(git_hook(strict=True, modify=True))
```

pre-commit
```sh
set -e	# stop script execution when error encoutered

# Run flake8 check
flake8 .

# Sort imports with isort
python ./.githooks/isort_hooks.py
```

# Alternatives
There is a tool [pre-commit](https://pre-commit.com/) that eases the installation and configuration of git hooks. Read my note on that: [Pre-commit hooks](./pre-commit-hooks/)

References:
- [Git Hooks](https://githooks.com/) - user-friendly description, tons of examples, reference links
- [Git Book on hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) - 

# Sharing git hooks with the team
Nowadays you can do the following to set a directory that is under version control to be your git hooks directory, e.g., `MY_REPO_DIR/.githooks` would be
```sh
git config --local core.hooksPath .githooks/
```
Still not directly enforceable but, if you add a note in your README (or whatever), this requires a minimum of effort on each developer's part.
Source: [Stackoverflow](https://stackoverflow.com/a/54281447/3247880)

See also:
- [Two Ways to Share Git Hooks with Your Team](https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/)

up:: [[MOC_git]]]