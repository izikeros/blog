---
Title: Bare Asterisk in Python Function Signatures - Keyword Only Arguments
Slug: bare-asterisk-in-python-function-signatures
Date: 2025-10-10
Modified: 2025-10-10
Status: published
Tags: python, api, pep, keyword-arguments, future-proofing
Category: note
---

## Core Principle

The `*` by itself in a function signature forces everything after it to be keyword-only arguments. It's a syntax barrier - arguments before the asterisk can be positional, arguments after it must be named.

```python
def foo(a, b, *, c, d):
    pass

foo(1, 2, c=3, d=4)  # works
foo(1, 2, 3, 4)      # breaks
```

**History:** Introduced in Python 3.0 via PEP 3102. This was part of the Python 3 overhaul, so it's never been available in Python 2.

## Useful Extensions

You can mix this with other parameter types in ways that make sense for your API:

**With default values:**

```python
def __init__(self, required_arg, *, optional=None, debug=False):
    pass
```

*_Combined with _args:__

```python
def process(*items, separator=", ", prefix=""):
    # items catches unlimited positional args
    # separator and prefix must be keyword-only
    pass
```

**All keyword-only (rare but valid):**

```python
def configure(*, host, port, timeout=30):
    # Everything must be named, nothing positional
    pass
```

## Specific Use Cases

**Library APIs where clarity matters** - When you have optional parameters that could be confused if passed positionally. The httpx example I saw does this: `def __init__(self, message: str, request: httpx.Request, *, body: object | None)` - the body parameter is important enough to deserve an explicit name.

**Future-proofing** - If you might add more required positional parameters later, putting optional ones after `*` means you won't break existing calls. Old code keeps working even as your signature evolves.

**Preventing argument order bugs** - When you have multiple parameters of the same type, forcing keywords prevents `foo(timeout, retries)` vs `foo(retries, timeout)` mixups.

## Nuances

**The bare asterisk doesn't capture anything** - it's purely a delimiter that says "keyword-only from here on." This is different from `*args`, which actually captures excess positional arguments into a tuple.

```python
# Bare asterisk - just marks the boundary
def func(a, *, b):
    pass

func(1, b=2)        # works
func(1, 2)          # TypeError: too many positional arguments
func(1, 2, b=3)     # TypeError: too many positional arguments
```

The function above only accepts one positional argument (`a`). The `*` doesn't "consume" anything - it just blocks additional positional arguments from being accepted.

*_When you use _args with keyword-only parameters__ - you put a name on the asterisk, and now it captures all the excess positional arguments, but you can still have keyword-only parameters after it:

```python
def func(a, *args, b):
    print(f"a={a}, args={args}, b={b}")

func(1, b=2)              # a=1, args=(), b=2
func(1, 2, 3, b=4)        # a=1, args=(2, 3), b=4
func(1, 2, 3, 4)          # TypeError: missing keyword-only argument 'b'
```

Here `*args` is greedy - it captures all positional arguments after `a`. But `b` still must be passed by keyword because it comes after the `*args`.

**The key distinction:**

- `def func(a, *, b):` - accepts exactly one positional arg, `b` must be keyword
- `def func(a, *args, b):` - accepts unlimited positional args into `args`, `b` must be keyword
- `def func(a, *args)` - accepts unlimited positional args, no keyword-only parameters

This matters when designing APIs. Use bare `*` when you want to restrict positional arguments. Use `*args` when you want to accept a variable number of them but still have some parameters that must be named.


## References
- [PEP 3102 – Keyword-Only Arguments \| peps.python.org](https://peps.python.org/pep-3102/)