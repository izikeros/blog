---
Category: note
Date: '2023-03-09'
Modified: '2023-07-12'
Prompt: How to store data in python class. Discuss property/attribute and class variable. Explain the difference
Slug: the-difference-between-class-attribute-or-property-and-the-class-variable
Status: published
Tags: python, class, class-variable, object-oriented-programming, class-property, property, attribute, class-attribute
Title: The Difference Between Class Attribute or Property and the Class Variable
todo: verify the code
---

In Python, you can store data within a class using properties/attributes or class variables.

## Properties/Attributes

Properties, also called attributes, are variables that store data within a class instance. They are defined within the class, but outside of any methods. Here's an example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

In the example above, `name` and `age` are attributes of the `Person` class. They are created and assigned values within the `__init__` method using the `self` keyword. You can access and modify these attributes using dot notation, like so:

```python
person = Person("John", 30)
print(person.name)  # Output: John
person.age = 31
print(person.age)   # Output: 31
```

## Class Variables

Class variables are variables that are shared among all instances of a class. They are defined within the class, but outside of any methods and are prefixed with the class name. Here's an example:

```python
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

```

In the example above, `count` is a class variable that is used to keep track of the number of `Person` instances that have been created. It is incremented every time a new instance is created within the `__init__` method. You can access class variables using the class name, like so:

```python
person1 = Person("John", 30)
person2 = Person("Jane", 28)
print(Person.count)  # Output: 2

```

### Difference
>
> The main difference between attributes/properties and class variables is that **attributes are specific to each instance** of a class, while **class variables are shared among all instances**.

Attributes are defined within the `__init__` method and can be different for each instance. Class variables are defined outside of any methods and are shared by all instances.

Another difference is that attributes/properties can be accessed and modified using dot notation on an instance of a class, while class variables are accessed using the class name.

In general, if you need to store data that is specific to each instance of a class, use attributes/properties. If you need to store data that is shared among all instances of a class, use class variables.

## References

[python - difference between class variable and class attribute - Stack Overflow](https://stackoverflow.com/questions/22822710/difference-between-class-variable-and-class-attribute)
