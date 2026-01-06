---
Category: note
Date: 2023-04-03
Modified: 2023-07-12
Slug: type-hint-for-undetermined-number-of-elements
Status: published
Summary: Learn how to use Python's `typing.Tuple` and `Union` with ellipsis (`...`) to create type hints for tuples containing an undetermined number of strings.
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
To make a type hint for a tuple with an undetermined number of strings in Python, you can use the `Tuple` and `Union` types from the `typing` module. Here's an example:

```python
from typing import Tuple, Union

def process_strings(strings: Tuple[Union[str, ...], ...]) -> str:
    return ", ".join(strings)

strings1 = ("hello", "world")
strings2 = ("foo", "bar", "baz")

print(process_strings(strings1))  # Output: "hello, world"
print(process_strings(strings2))  # Output: "foo, bar, baz"

```

In the type hint above, `Tuple` is used to indicate that we are working with a tuple, and `Union` is used to indicate that each element of the tuple can be either a `str` or an ellipsis (`...`), which represents an infinite number of `str` elements. The second `...` indicates that the tuple can contain an undetermined number of elements.

up::[[python_type_hints]]
X::[[elypsis_in_python_type_hints]]
