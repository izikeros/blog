---
title: Use python TypedDict to type hint dictionaries
date: 2022-04-22
status: published
tags: 
summary: 
slug: use-python-typeddict-to-type-hint-dictionaries
category: note
citation_needed: false
todo: 
---

Define types for the fields in dictionary using TypedDict as base class to inherit from and then use this class in hints.

```python
from typing import TypedDict


class NameInfo(TypedDict):
    name: str
    first_letter: str


def get_info(name: str) -> NameInfo:
    return {'name': name, 'first_letter': name[0]}
```

from: https://stackoverflow.com/a/54198204/3247880