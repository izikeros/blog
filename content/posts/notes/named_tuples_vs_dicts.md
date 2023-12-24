---
Category: note
Date: '2023-04-03'
Modified: '2023-07-12'
Slug: named-tuples-vs-dictionaries
Status: published
Tags: python, named-tuple, dict, dictionary, data-structure
Title: Python - Named Tuples or Dictionaries to Store Structured Data?
---
up::[[MOC_Python]]
Let's assume that in python, we have long list of pairs to store. In this note we will discuss what are the pros and cons of using named tuple vs. dict to store single pair?

Both named tuples and dictionaries are useful data structures for storing key-value pairs in Python, but they have different pros and cons depending on the situation.

## Named tuples

Here are some pros and cons of using named tuples:

### Pros

- Named tuples are immutable, so they are safer to **use in multithreaded** environments where multiple threads might try to modify the same data at the same time.
- Named tuples can be **more memory-efficient** than dictionaries, especially if you have a large number of instances with the same fields.
- Named tuples are more readable than dictionaries when you have a fixed set of fields and you want to give them meaningful names.

### Cons

- Named tuples are less flexible than dictionaries because you can't add or remove fields once they are defined.
- Named tuples can be less convenient to use than dictionaries if you need to access fields by key rather than by attribute name.

### Dictionaries

Here are some pros and cons of using dictionaries:

### Pros

- Dictionaries are more flexible than named tuples because you can add or remove fields at any time.
- Dictionaries are more convenient to use than named tuples if you need to access fields by key rather than by attribute name.

### Cons

- Dictionaries are mutable, so you need to be careful when using them in multithreaded environments.
- Dictionaries can be less memory-efficient than named tuples, especially if you have a large number of instances with the same fields.
- Dictionaries are less readable than named tuples when you have a fixed set of fields and you want to give them meaningful names.

## Conclusion

if you have a fixed set of fields with meaningful names, and you don't need to add or remove fields at runtime, a named tuple is a good choice. If you need more flexibility or you need to access fields by key rather than by attribute name, a dictionary is a better choice.
