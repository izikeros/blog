---
Category: note
Date: 2025-10-24
Modified: 2025-10-24
Slug: evolution-of-type-hints-in-python
Status: published
Summary: Learn about the evolution of type hints in Python, from initial comments to modern inline typing and key features introduced in each major version, enabling powerful static type checking with tools like mypy and pyright.
ai_summary: true
Tags: python, typing, pep484, static-typing, mypy
Title: Evolution of Type Hints in Python — From Comments to Inline Typing and Beyond
---
## The Mental Model

Python typing wasn’t born overnight. It crept into the language slowly, first as a loose suggestion and later as a core part of modern codebases.  
Originally, you could only hint types using comments (`# type: int`), but as Python matured, its typing syntax grew more expressive, more compact, and more powerful.

The journey started with **PEP 484** in **Python 3.5**, introducing the `typing` module and annotations as first-class citizens. Since then, nearly every minor version brought a refinement or simplification, allowing developers to express richer constraints without resorting to verbose generics.

```python
# Python 3.5 (PEP 484)
from typing import List

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")
````

This basic form of static typing opened the door for tools like **mypy**, **pyright**, **pylance** and most recently **ty**, **pyrefly** to provide editor-level correctness checks.

This basic form of static typing opened the door for tools like [**mypy**](https://mypy-lang.org/), [**pyright**](https://github.com/microsoft/pyright), [**pylance**](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), and most recently [**ty**](https://docs.astral.sh/ty/), [**pyrefly**](https://pyrefly.org/) to provide editor-level correctness checks.

## Key Features Through Versions

### Python 3.5 (PEP 484) — The Birth of Typing

Introduced the `typing` module:

- `List`, `Dict`, `Tuple`, `Optional`, `Union`
- `Callable`, `Any`, `TypeVar`, `Generic`
- Function annotations became official.

### Python 3.6 — Variable Annotations

You could finally type variables directly without using comments:

```python
name: str = "Alice"
scores: list[int] = [10, 20, 30]  # still needed `List[int]` before 3.9
```

Also introduced `typing.NamedTuple` and `typing.NewType`.

### Python 3.7 — Postponed Evaluation (PEP 563)

Type hints were treated as **strings** by default (via `from __future__ import annotations`), delaying their evaluation until runtime.  
This solved circular import issues and reduced overhead in function definitions.

### Python 3.8 — TypedDict and Literal Types

Added:

- `TypedDict` for describing dicts with specific key/value types.
- `Final` and `Literal` for immutability and constant values.
- `Protocol` (PEP 544) for structural subtyping.

```python
from typing import TypedDict, Literal

class Movie(TypedDict):
    title: str
    year: int

def rate_movie(rating: Literal["good", "bad"]) -> None:
    ...
```

### Python 3.9 — Built-in Generics (PEP 585)

This was a huge quality-of-life upgrade:  
`list[int]` replaced `List[int]`, `dict[str, int]` replaced `Dict[str, int]`.

```python
# Before
from typing import Dict
users: Dict[str, int]

# After
users: dict[str, int]
```

### Python 3.10 — Union Operator (PEP 604)

Simplified `Union` syntax using the `|` operator.

```python
# Before
def parse(data: Union[str, bytes]) -> None: ...

# After
def parse(data: str | bytes) -> None: ...
```

Also improved type narrowing in `match` statements (structural pattern matching).

### Python 3.11 — Self Type, Variadic Generics, TypedDict Enhancements

- `Self` for methods returning their own type (PEP 673).
- `TypeVarTuple` and `Unpack` for variadic generics (PEP 646).
- `NotRequired` and `Required` for `TypedDict` fields.

```python
from typing import Self

class Shape:
    def set_size(self, x: int) -> Self:
        self.x = x
        return self
```

### Python 3.12 — The `typing` Cleanup

Deprecated old-style generics (`List`, `Dict`, etc.).  
Introduced `TypeAliasType` (PEP 695) and made `type` annotations simpler:

```python
type Vector = list[float]  # clean, explicit alias
```

### Python 3.13 — No More `from __future__ import annotations`

Postponed evaluation of annotations is now **default**, removing one of the last confusing steps in typing setup.

## Useful Patterns

### Simplified Union Types

Readable and concise unions are now idiomatic:

```python
def load_data(source: str | Path) -> str: ...
```

### Structural Subtyping with Protocols

Protocol-based typing (instead of inheritance) allows flexible contracts:

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def cleanup(obj: SupportsClose) -> None:
    obj.close()
```

### TypedDict for JSON-like Data

Great for static checking of structured but dict-based data:

```python
class Config(TypedDict, total=False):
    host: str
    port: int
```

### Self Type for Fluent Interfaces

Commonly used in builder-style classes:

```python
class Query:
    def where(self, condition: str) -> Self:
        ...
    def execute(self) -> None:
        ...
```

### A Quick Summary of Typing Evolution

```mermaid
graph LR
A[3.5: typing module (PEP 484)] --> B[3.6: variable annotations]
B --> C[3.7: postponed evaluation]
C --> D[3.8: TypedDict, Literal, Protocol]
D --> E[3.9: built-in generics]
E --> F[3.10: union | operator]
F --> G[3.11: Self, variadic generics]
G --> H[3.12: TypeAliasType, PEP 695]
H --> I[3.13: annotations postponed by default]
```

Typing has moved from verbose and experimental to elegant and essential.  
Modern Python encourages typing as part of its design philosophy — readable, predictable, and expressive.
