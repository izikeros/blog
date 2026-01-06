---
Category: note
Date: 2022-05-12
Modified: 2023-07-12
Slug: pytest-check-lists-equal
Status: published
Summary: Learn how to write a function using pytest to check if two lists are equal by comparing their lengths and sorted contents.
ai_summary: true
Tags:
  - pytest
  - python
  - assert
Title: Pytest Check if Lists Are Equal
---
In the assertions this can be useful to check if two lists are equal:

```python
def check_lists_equal(list_1: list, list_2: list) -> bool:
    """Check if two lists are equal."""
    return len(list_1) == len(list_2) and sorted(list_1) == sorted(list_2)
```
