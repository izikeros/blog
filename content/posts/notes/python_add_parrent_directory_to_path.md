---
title: Python Add Parent Directory To Path
date: 2022-02-22
status: published
tags: python, gist, snippet, jupyter, notebook
summary: 
slug: python-add-parent-directory-to-path
category: note
citation_needed: false
todo: 
---
Adding parent path with the modules to import is sometimes useful in jupyter notebooks.

```python
# Add parent directory to path
import sys; sys.path.insert(0, '..')
```

See also my GitHub [gist]().