---
title: Git hooks
date: 2021-10-20
status: published
tags: git, hooks, pre-commit hooks, software project, project
summary: Example how to setup git hooks manually or with pre-commit tool
slug: git-hooks
category: note
citation_needed: false
---
Git hook makes easier to keep order in the software project:
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
There is tool [pre-commit](https://pre-commit.com/) that ease installation and configuration of git hooks. Read my note on that: [Pre-commit hooks](./pre-commit-hooks/)

References:
- [Git Hooks](https://githooks.com/) - user friendly description, tons of examples, reference links
- [Git Book on hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) - 

See also:
