---
title: Black code formatter
date: 2021-11-29
status: published
tags: black, python, pyqa
summary: notes on using black formatter
slug: black-code-formatter
category: note
citation_needed: false
todo: 
---

Black is non-configurable code formatter.

## Install black for jupyter notebook
```sh
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter nbextension enable jupyter-black-master/jupyter-black
```

## Change the line length character limit in Black
To change the character limit for the Black Python formatter, you can add following section to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) file:
```ini
[tool.black]
line-length = 119
```

- PEP8 recommends a line length of [79 characters](https://www.python.org/dev/peps/pep-0008/#maximum-line-length) (72 for docstrings)
- Black sets line lengths to [88 characters by default](https://black.readthedocs.io/en/stable/the_black_code_style.html?highlight=length#line-length)
- The Django docs recommend a maximum line length of [119 characters](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) (79 for docstrings)

## Usages of black
- with tox
- in pre-commit hooks
- as external tool in PyCharm