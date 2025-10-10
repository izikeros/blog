---
Category: note
Date: 2022-04-22
Modified: 2023-07-12
Slug: use-python-typeddict-to-type-hint-dictionaries
Status: published
Tags:
  - python
  - type-hints
  - TypedDict
  - mypy
Title: Use Python TypedDict to Type Hint Dictionaries
citation_needed: false
---

Define types for the fields in a dictionary using TypedDict as a base class to inherit from and then use this class in hints.

```python
from typing import TypedDict


class NameInfo(TypedDict):
    name: str
    first_letter: str


def get_info(name: str) -> NameInfo:
    return {'name': name, 'first_letter': name[0]}
```

from: <https://stackoverflow.com/a/54198204/3247880>

up::[[python_type_hints]]
