---
Category: note
Date: 2023-01-05
Modified: 2023-07-12
Slug: difference-between-numba-jit-and-njit-decorators
Status: published
Summary: "The difference between the Numba jit and njit decorators: njit is stricter about input and output types, and in return can compile faster, more memory-efficient code."
Tags:
  - python
  - numba
Title: Difference Between Numba Jit and Njit Decorators
citation_needed: false
---

`numba.jit` is a function decorator that tells Numba to compile a Python function into native machine code using just-in-time (JIT) compilation. It can be used to speed up the execution of the function by compiling it to machine code, which can be faster than interpreting the Python code.

`numba.njit` is a function decorator that is similar to `numba.jit`, but it has stricter requirements for the types of input and output that the function can accept and return. This means that `numba.njit` may be more restrictive in the types of functions it can compile, but it may also be faster and more memory-efficient than `numba.jit`.

In general, you should use `numba.njit` if you know that the function you are trying to compile has a simple and well-defined input and output, and you are willing to make any necessary changes to the function's signature to meet the requirements of `numba.njit`. Otherwise, you can use `numba.jit`, which is more flexible but may be slower and less memory-efficient.

up::[[MOC_Python]]
