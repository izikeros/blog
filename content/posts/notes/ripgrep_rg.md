---
Category: note
Date: 2024-09-13
Modified: 2024-09-13
Slug: notes-on-using-ripgrep-for-projects-with-python-jupyter-ipynb-notebooks-and
Status: published
Summary: Learn how to effectively use ripgrep (rg) for searching Python, Jupyter notebook (.ipynb), and Markdown (.md) files with various options like file type specificity, context display, and pattern matching.
ai_summary: true
Title: Notes on using ripgrep for projects with python, jupyter (ipynb) notebooks and markdown files
tags:
  - ripgrep
  - grep
  - search
  - code-search
  - python-project
  - developer-tools
---
Notes on using ripgrep (rg) mainly for use cases as a Python developer working with .py, .ipynb, and .md files:

## Basic search

```sh
   rg "pattern" path/to/search
```

## Search only Python files

```sh
   rg --type py "pattern"
```

## Search Jupyter notebooks

```sh
   rg --type-add 'ipynb:*.ipynb' --type ipynb "pattern"
```

## Search Markdown files

```sh
   rg --type md "pattern"
```

## Case-insensitive search

```sh
   rg -i "pattern"
```

## Search for whole words

```sh
   rg -w "word"
```

Show context around matches
```sh
   rg -C 3 "pattern"  # 3 lines before and after
```

## Search for multiple patterns

```sh
   rg "pattern1|pattern2|pattern3"
```

Exclude specific directories:
```sh
   rg "pattern" --glob '!{venv,__pycache__}'
```

## Search for Python functions

```sh
    rg "def \w+\("
 ```

## Search for Markdown headers

```sh
    rg "^#{1,6} .+"
 ```

## Count matches

```sh
    rg -c "pattern"
 ```

## Display only the filenames where a pattern appears

To display only the filenames where a pattern appears, you can use the `-l` or `--files-with-matches` option in ripgrep. Here's how to do it:

```sh
rg -l "pattern"
```

## Search for files with a specific name pattern

`rg --files -g "*.py"`

## Use AND logic for multiple patterns

`rg "pattern1" | rg "pattern2"`
