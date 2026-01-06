---
Summary: Learn how to use Python's `warnings` module to ignore or suppress warnings either globally or locally within a code block. Discover methods for disabling and re-enabling warnings to fine-tune your debugging process.
ai_summary: true
category: note
date: 2022-05-12
slug: python-ignore-warnings
tags:
  - python/warning/ignore
  - python
title: How to ignore warnings in Python
status: published
---
## use warnings module directly

```python
# disable
import warnings
warnings.filterwarnings('ignore')

# enable warnigs
warnings.filterwarnings('default') # or 'once' to show warnings only once
```

## use context manager

You can use the `warnings.catch_warnings()` context manager to temporarily suppress warnings within a block of code. Here's an example:

```python
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    # code that generates warnings here
    # ...
# warnings are enabled again outside of the context manager

```

In this code, the `catch_warnings()` context manager is used to temporarily catch any warnings that are generated within the indented block of code. The `filterwarnings()` function is called within the context manager to disable warnings. Once the block of code exits, warnings are re-enabled automatically outside of the context manager.

You can modify the `filterwarnings()` call within the context manager to fine-tune which warnings are suppressed or shown, depending on your needs.

up::[[MOC_Python]]
X::[[python_warnings]]
