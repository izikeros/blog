---
Title: Understanding Python's `copy` vs `deepcopy` - When to Use Each
Slug: understanding-pythons-copy-vs-deepcopy-when-to-use-each
Date: 2025-03-20
Modified: 2025-03-20
Status: published
Tags:
  - python
  - python-copy
  - deepcopy
  - mutable
  - immutable
  - nested-objects
Category: note
---

When working with Python objects, understanding how to properly copy them is crucial for avoiding unexpected behaviors in your code. Python provides two main approaches for copying objects: `copy` and `deepcopy`. Let's explore the differences, use cases, and potential pitfalls of each.

## The Basics: Shallow vs. Deep Copying

Python's `copy` module provides two primary functions:

1. `copy.copy()` - Creates a shallow copy
2. `copy.deepcopy()` - Creates a deep copy

The difference lies in how they handle nested objects.

### Shallow Copy (`copy.copy()`)

A shallow copy creates a new object, but doesn't create copies of nested objects - it just copies references to them. This means changes to nested objects in the copy will affect the original, and vice versa.

### Deep Copy (`copy.deepcopy()`)

A deep copy creates a completely independent clone - it recursively copies all nested objects, creating a fully separate hierarchy of objects.

## Let's See It In Action

Here's a practical example showing the difference:

```python
import copy

# Let's create a nested list
original = [1, 2, [3, 4]]

# Create a shallow copy
shallow_copied = copy.copy(original)

# Create a deep copy
deep_copied = copy.deepcopy(original)

# Let's modify the nested list in the original
original[2][0] = 'changed!'

print("Original:", original)
print("Shallow copy:", shallow_copied)
print("Deep copy:", deep_copied)
```

Output:

```
Original: [1, 2, ['changed!', 4]]
Shallow copy: [1, 2, ['changed!', 4]]
Deep copy: [1, 2, [3, 4]]
```

Notice how changing the nested list in the original affected the shallow copy but not the deep copy!

## Typical Use Cases

### When to Use Shallow Copy (`copy`)

1. **Performance Matters**: When dealing with large objects where a deep copy would be expensive, and you're confident you won't modify nested objects.
    
2. **Simple Data Structures**: When your object contains only immutable values like numbers, strings, or tuples.
    

```python
import copy

# Dictionary with simple values
user_settings = {
    "theme": "dark",
    "notifications": True,
    "volume": 75
}

# Safe to use shallow copy here
backup_settings = copy.copy(user_settings)
```

### When to Use Deep Copy (`deepcopy`)

1. **Complex Nested Objects**: When working with objects that contain mutable objects like lists, dictionaries, or custom classes.
    
2. **When Independence is Critical**: When you need to ensure modifications to the copy don't affect the original at all.
    

```python
import copy

# Complex nested structure representing a user profile
user_profile = {
    "name": "Alex",
    "preferences": {
        "theme": "dark",
        "notifications": ["email", "push"]
    },
    "friends": [
        {"name": "Taylor", "status": "online"},
        {"name": "Jordan", "status": "offline"}
    ]
}

# We need a true independent copy to modify
new_profile = copy.deepcopy(user_profile)
# Now we can safely modify nested lists and dictionaries
new_profile["friends"][0]["status"] = "away"
new_profile["preferences"]["notifications"].append("sms")

print("Original friend status:", user_profile["friends"][0]["status"])  # Still "online"
print("Copy friend status:", new_profile["friends"][0]["status"])  # "away"
```

## Common Gotchas and Pitfalls

### 1. Forgetting the import

Remember to `import copy` before using these functions!

### 2. Assignment Is Not Copying

```python
# This is NOT a copy - it's just another reference to the same object
list2 = list1
```

### 3. List Slicing Creates Shallow Copies

```python
original = [1, 2, [3, 4]]
sliced_copy = original[:]  # Equivalent to copy.copy()

original[2][0] = "changed!"
print(sliced_copy)  # Will show [1, 2, ['changed!', 4]]
```

### 4. Performance Considerations

Deep copying can be resource-intensive for large nested structures:

```python
import copy
import time

# Create a large nested structure
large_structure = [list(range(1000)) for _ in range(1000)]

# Time shallow copy
start = time.time()
shallow = copy.copy(large_structure)
print(f"Shallow copy took: {time.time() - start:.6f} seconds")

# Time deep copy
start = time.time()
deep = copy.deepcopy(large_structure)
print(f"Deep copy took: {time.time() - start:.6f} seconds")
```

### 5. Circular References

Be careful with circular references when using `deepcopy`:

```python
import copy

# Create a circular reference
circular = [1, 2, 3]
circular.append(circular)  # The list contains itself!

# This works fine, handling the circular reference properly
deep_circular = copy.deepcopy(circular)
```

## Custom Copying Behavior

You can customize how your objects are copied by implementing `__copy__` and `__deepcopy__` methods:

```python
import copy

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __copy__(self):
        # Create a new instance and copy attributes
        return Person(self.name, self.address)
    
    def __deepcopy__(self, memo):
        # Create a new instance with deeply copied attributes
        return Person(self.name, copy.deepcopy(self.address, memo))
    
    def __repr__(self):
        return f"Person(name={self.name}, address={self.address})"

# Example usage
person = Person("Alice", {"city": "New York", "zip": "10001"})
person_copy = copy.copy(person)
person_deepcopy = copy.deepcopy(person)

# Modify the address in the original
person.address["city"] = "Boston"

print(person)  # Shows updated city
print(person_copy)  # Also shows updated city (shallow copy)
print(person_deepcopy)  # Still shows "New York" (deep copy)
```

## Related Topics to Explore

1. **Immutable vs. Mutable Objects**: Understanding this fundamental Python concept helps clarify when copying is necessary.
    
2. **Object References in Python**: Diving deeper into how Python handles object references.
    
3. **Memory Management**: Learning how Python allocates and deallocates memory can help you make better choices about copying.
    
4. **The `pickle` Module**: For serializing and deserializing Python objects, another approach to object copying.
    
5. **Performance Optimization**: Strategies for efficient copying when working with large data structures.
    

## References

- [Python's Official Documentation on the copy module](https://docs.python.org/3/library/copy.html)
- [Python Data Model - Object Customization](https://docs.python.org/3/reference/datamodel.html#object.__copy__)
- [Real Python's Guide to Shallow vs Deep Copying](https://realpython.com/copying-python-objects/)

---
## Key takeaways
Understanding the distinction between shallow and deep copying is essential for writing robust Python code that behaves as expected. Choose `copy()` when you need a quick, lightweight duplication of simple structures, and `deepcopy()` when you need complete independence between the original and copied objects.
