---
title: Change black line length
date: 2021-11-29
modified: 2022-09-01
status: published
tags: black, python, pyqa, quality
summary: notes on using black formatter
slug: change-black-line-length
category: note
citation_needed: false
---
X:[[black_formatter]]
X::[[black_change_max_line_length]]

![black logo](https://black.readthedocs.io/en/stable/_static/logo2-readme.png)
## Project settings
To change the character limit for the Black Python formatter, you can add the following section to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) file:
```ini
[tool.black]
line-length = 119
```

- PEP8 recommends a line length of [79 characters](https://www.python.org/dev/peps/pep-0008/#maximum-line-length) (72 for docstrings)
- Black sets line lengths to [88 characters by default](https://black.readthedocs.io/en/stable/the_black_code_style.html?highlight=length#line-length)
- The Django docs recommend a maximum line length of [119 characters](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) (79 for docstrings)

## vscode black formatter line length
You can configure the black formatter in VSCode via `Code -> Preferences -> Settings` and then search for "python formatting black args" phrase.

in two separate lines provide the line length argument and it's value: 
```
--line-length`
100
```
In the second line, `100` is the desired limit for the maximum line length.

You can add the information to the formatting section of  `settings.json` which can be found in the project's `.vscode` directory

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "120"],
    "python.linting.enabled": true
}
```
(credits to user mrx for this [hint](https://dev.to/adamlombard/vscode-setting-line-lengths-in-the-black-python-code-formatter-1g62#comment-1iei2))