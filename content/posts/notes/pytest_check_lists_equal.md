---
title: Pytest check if lists are equal
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: pytest-check-lists-equal
tags: pytest, python, assert
---
In the assertions this can be useful to check if two lists are equal:
```python
def check_lists_equal(list_1: list, list_2: list) -> bool:
    """Check if two lists are equal."""
    return len(list_1) == len(list_2) and sorted(list_1) == sorted(list_2)
```