---
Category: note
Date: '2023-04-03'
Modified: '2023-07-12'
Slug: type-hints-elypsis-for-arbitrary-number-of-elements
Status: published
Tags: python, type-hints, mypy, elypsis, python-typing
Title: How to Use Elypsis in Type Hints to Indicate Arbitrary Number of Elements
---
In type hints, `...` (ellipsis) is used to indicate that a function parameter or return value can have an arbitrary number of arguments or elements.

For example, if you have a function that takes an arbitrary number of integers as arguments, you can use `...` in the function signature to indicate that:

```python
def foo(*args: int) -> List[int]:
    return [x * 2 for x in args]
```

Here, `*args` is used to indicate that the function can take any number of arguments, and the `int` type hint indicates that each argument must be an integer. The return type is a list of integers.

Similarly, you can use `...` in a type hint for a tuple to indicate that the tuple can have an arbitrary number of elements of a given type. For example:

```python
from typing import Tuple

def bar(t: Tuple[str, ...]) -> str:
    return " ".join(t)

t1 = ("hello", "world")
t2 = ("foo", "bar", "baz")

print(bar(t1))  # Output: "hello world"
print(bar(t2))  # Output: "foo bar baz"
```

Here, `Tuple[str, ...]` is used to indicate that `t` is a tuple of strings, and the `...` indicates that the tuple can have an arbitrary number of elements.

up::[[python_type_hints]]
X::[[type_hint_for_undetermined_number_of_elements]]
X::[[python_type_hints_NoReturn_None_NoType]]
X::[[type_hints_dictionary]]