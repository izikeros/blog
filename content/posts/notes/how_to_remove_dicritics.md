---
Title: How to Remove Diacritics and Sanitize Strings in Python
Slug: how-to-remove-diacritics-and-sanitize-strings-in-python
Date: 2024-08-30
Modified: 2024-08-30
Status: published
tags: python, nlp, sanitize, sanitization, diacritics, accent, umlaut, unidecode, 
Category: note
---

When working with international text data, you often need to convert characters with diacritical marks (like accents, umlauts, or other language-specific symbols) to their basic Latin equivalents. This process, known as diacritic removal or string sanitization, can be crucial for tasks such as:

- Improving search functionality
- Normalizing data for analysis
- Ensuring compatibility with systems that only support ASCII characters

In this guide, we'll show you how to easily sanitize strings in Python using the `unidecode` library.

## Step 1: Install the unidecode Library

First, you need to install the `unidecode` library. Open your terminal or command prompt and run:

```
pip install unidecode
```

## Step 2: Import the Library

In your Python script, import the `unidecode` module:

```python
import unidecode
```

## Step 3: Create a Sanitization Function

Define a function that will sanitize your strings:

```python
def sanitize_string(text):
    return unidecode.unidecode(text)
```

This function takes a string as input and returns the sanitized version.

## Step 4: Use the Function

Now you can use this function to sanitize any string. Here's an example with various languages:

```python
# Example usage
examples = [
    "Łódź",  # Polish
    "España",  # Spanish
    "München",  # German
    "François",  # French
    "Νίκος",  # Greek
    "Россия"  # Russian
]

for example in examples:
    sanitized = sanitize_string(example)
    print(f"Original: {example}")
    print(f"Sanitized: {sanitized}")
    print()
```

## Step 5: Run the Script

When you run this script, you'll see output like this:

```
Original: Łódź
Sanitized: Lodz

Original: España
Sanitized: Espana

Original: München
Sanitized: Munchen

Original: François
Sanitized: Francois

Original: Νίκος
Sanitized: Nikos

Original: Россия
Sanitized: Rossiia
```


## Alternative Libraries
While `unidecode` is comprehensive, you might also explore alternatives like `unicodedata` from the Python standard library for more control over the process.

