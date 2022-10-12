---
category: note
date: '2021-09-28'
modified: '2021-09-28'
slug: python-documentation-with-pdoc3
status: published
suggested_tags: documentation, pdoc3, python
summary: summary
tags: documentation, pdoc3, python, documentation-generator, sphinx
title: Python - project documentation from the code with pdoc3
---

Despite Sphinx seems to be the most common tool for generating documentation pdoc3 is an interesting option.


Generate html documentation:
```sh
pdoc --force --html --output-dir ./doc_myproject myproject
```
where `--force` will overwrite any existing generated (`--output-dir`) files.


Generate html documentation and open in browser:
```sh
pdoc --force --html --output-dir ./doc_myproject myproject && xdg-open ./doc_myproject/myproject/index.html
```

I used to add these two documentation-related targets to the project's Makefile:
```makefile
## Generate pdoc HTML documentation for prolog package
doc:
	pdoc --force --html --output-dir ./doc_myproject myproject

## Generate pdoc HTML documentation for prolog package and open in browser
doc_view:
	pdoc --force --html --output-dir ./doc_myproject myproject && xdg-open ./doc_myproject/myproject/index.html
```
X:: [[sphinx_for_documentation]] [[mkdocs]]