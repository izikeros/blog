---
category: note
date: '2021-09-29'
slug: python-convert-docstring-styles
status: published
suggested_tags: convert, docstring, python, style
summary: Description of tools for converting docstring style in python code
tags: convert, docstring, python, style
title: Python - convert docstring styles
---

When refactoring the project one might want to change docstring style e.g. from numpy-style to google-style. At this point tool like Pyment comes in handy.

# [Pyment](https://github.com/dadadel/pyment/)

Currently, the managed styles in input/output are 
- javadoc,
- one variant of reST (re-Structured Text, used by Sphinx),
- numpydoc,
- google docstrings,
- groups (other grouped style).
- 
## Usage:
you can either apply changes immediately or generate patch (review the path and then apply)

run from the command line:
```sh
pyment  myfile.py    # will generate a patch
pyment -w myfile.py  # will overwrite the file
```

to apply specific style (here - google style):
```sh
pyment -w -o google myfile.py
```


Input/output docstring style parameters: "javadoc", "reST", "numpydoc", "google" (default is "reST"). The input can be also `auto` for style auto-detection.

You might want to limit operation to only conversion by using option `-t, --convert`. With this option, existing docstrings will be converted but Pyment won't create missing ones.


# References:
[Reference documentation](https://github.com/dadadel/pyment/blob/master/doc/sphinx/source/pyment.rst)
