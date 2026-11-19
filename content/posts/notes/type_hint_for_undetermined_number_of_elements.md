---
Category: note
Date: 2023-04-03
Modified: 2026-11-19
Slug: type-hint-for-undetermined-number-of-elements
Status: published
Summary: How to type hint a tuple that holds any number of strings in Python, using typing.Tuple with the ellipsis (...) syntax.
ai_summary: true
Tags:
  - python
  - type-hints
  - mypy
  - elypsis
  - tuple
  - union
  - python/typing
Title: Python - How to Make Type Hint for the Tuple With Undetermined Number of Strings?
Prompt: in python how to make type hint for the tuple with undetermined number of strings
---
To type hint a tuple with any number of strings, put an ellipsis (`...`) after the element type:

```python
def process_strings(strings: tuple[str, ...]) -> str:
    return ", ".join(strings)

strings1 = ("hello", "world")
strings2 = ("foo", "bar", "baz")

print(process_strings(strings1))  # Output: "hello, world"
print(process_strings(strings2))  # Output: "foo, bar, baz"
```

`tuple[str, ...]` means "a tuple of any length where every element is a `str`", including the empty tuple. The ellipsis is only valid as the second and last argument, so `tuple[str, int, ...]` is an error.

The built-in `tuple[...]` works from Python 3.9. On older versions use `typing.Tuple`:

```python
from typing import Tuple

def process_strings(strings: Tuple[str, ...]) -> str:
    return ", ".join(strings)
```

You don't need `Union` here. If the elements can have different types, put the `Union` inside: `tuple[Union[str, int], ...]` (or `tuple[str | int, ...]` on Python 3.10+). An earlier version of this note used `Tuple[Union[str, ...], ...]`, which is not a valid type hint - `...` is not a type and cannot be a member of a `Union`.

**Edits:**

- 2026-11-19: Fixed the type hint (was `Tuple[Union[str, ...], ...]`), added the Python 3.9+ `tuple[str, ...]` form

up::[[python_type_hints]]
X::[[elypsis_in_python_type_hints]]
