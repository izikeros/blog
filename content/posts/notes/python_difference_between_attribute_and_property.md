---
Category: note
Date: '2023-03-09'
Modified: '2023-07-12'
Slug: python-difference-betwee-attribute-and-property
Status: published
Tags: python,
Title: Python - Is There Any Difference Between Attribute and Property?
---
up::[[MOC_Python]]
X::[[property_attribute_vs_class_variable]]

In Python there is a difference between an attribute and a property, although they are often used interchangeably.

An attribute is a variable that belongs to an instance of a class. It is defined within the class, and its value can be accessed or modified using dot notation on the instance.

A property, on the other hand, is a special kind of attribute that is accessed or modified using getter and setter methods. The getter method is used to retrieve the value of the property, and the setter method is used to set the value of the property.

Here is an example that demonstrates the difference between an attribute and a property:

```python
class Person:
    def __init__(self, name):
        self.name = name   # This is an attribute
        
    @property
    def name(self):
        return self._name   # This is a property getter method
    
    @name.setter
    def name(self, value):
        self._name = value   # This is a property setter method

```

In the example above, the `Person` class has an attribute called `name`, which is set in the `__init__` method. However, the `name` attribute is also defined as a property using the `@property` and `@name.setter` decorators. The `name` property has a getter method that returns the value of the `_name` attribute, and a setter method that sets the value of the `_name` attribute.

With the `name` property defined in this way, you can get and set the `name` attribute using the property methods, like so:

```python
person = Person("John")
print(person.name)  # Output: John
person.name = "Jane"
print(person.name)  # Output: Jane
```

> An **attribute** is a **simple variable** that **belongs to an instance of a class**, while a **property** is a **special kind of attribute** that is accessed or modified using **getter and setter methods**.