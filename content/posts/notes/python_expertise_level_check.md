---
Title: Python Expertise Level - Self-Assessment
Slug: python-expertise-level-self-assessment
Date: 2023-10-17
Modified: 2023-10-17
Status: published
tags: python, programming, interview, job-interview, skills 
Category: note
todo: add links that one can learn the techniques
prompt: I would like to create a simple classification of Python programmers into 3 categories beginners, advanced, and experts. Use simple claims to describe programmers in each category and that makes this category distinct from other categories. Exemplary statements uses generators, knows how to use decorators, etc. Give me at least 10 statements for each level of advancement.
params: gpt-4, temp 0.4, topp=0.05
---

X::[[MOC_Software_Development]]
up::[[MOC_Python]]

Sometimes you need to assess your own or candidate's level of expertise in Python programming. I have created some statements that roughly corresponds to the various level of expertise. Note that knowing programming language techniques contributes to expertise but does not make a great programmer automatically. Knowledge of algorithms and data structures, programming patterns, and software architectures are some other important factors - to mention a few.

Having that said, I still find useful this simple classification of Python programmers into three categories: beginners, advanced, and experts.

## Beginners

1. Familiar with basic Python syntax and data types (strings, integers, lists, dictionaries).
2. Can write simple functions and use control flow statements (if, for, while).
3. Understands the concept of variables and variable scope.
4. Can use basic Python libraries like `math` and `random`.
5. Knows how to handle errors and exceptions using try/except blocks.
6. Can read from and write to files.
7. Understands the basics of object-oriented programming: classes, objects, methods.
8. Can use basic string and list methods for manipulation.
9. Knows how to use basic Python data structures like lists, tuples, and dictionaries.
10. Can write simple Python scripts to automate tasks.

## Advanced

1. Understands and uses generators and decorators.
2. Can write complex functions and classes with multiple methods and attributes.
3. Understands and uses list comprehensions and lambda functions.
4. Can use regular expressions for pattern matching in strings (note: more regex skill that python)
5. Understands and uses context managers for resource management.
6. Can use advanced Python data structures like sets and frozensets.
7. Understands and uses Python's memory management and optimization techniques.
8. Can use Python's built-in functions like `map()`, `filter()`, `reduce()`.
9. Understands and uses Python's module and package system.

## Experts

1. Understands and uses metaclasses and descriptors.
2. Can write and understand asynchronous code using `asyncio`.
3. Understands and uses Python's concurrency and parallelism features.
4. Can use Python's C API to extend Python with C/C++ code.
5. Understands and uses Python's dynamic typing system to its full extent.
6. Can write and understand complex decorators and context managers.
7. Proficient in Python's debugging and profiling, using tools like `pdb` for debugging and `cProfile` for profiling to optimize their code.
8. Have a deep understanding of Python's Global Interpreter Lock (GIL) and how it affects multithreaded programs.

There is [HN](https://news.ycombinator.com/item?id=38032092) discussion on this note.

**Edits:**

- 2023-10-30: remove from Experts: 7. Understands and uses Python's garbage collection system.
- 2023-10-30: remove from Experts: Have a good understanding of Python's internals, such as bytecode, the Python interpreter's execution model, and how Python's data types are implemented at the C level.
- 2023-10-30: remove from Advanced: Can use advanced Python libraries like `numpy`, `pandas`, `matplotlib` not a python std lib.
- added note:
