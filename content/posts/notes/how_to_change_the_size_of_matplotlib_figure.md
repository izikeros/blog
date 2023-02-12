---
Title: How to change the size of matplotlib figure?
Slug: how-to-change-the-size-of-matplotlib-figure
Date: 2023-02-12
Modified: 2023-02-12
Status: published
Tags: matplotlib, python/visualization, styling 
Category: note
---

To change the size of a matplotlib figure, there are several ways you can do it. Here are some examples:

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [1.  Using the `figure` function](#1-using-the-figure-function)
- [2.  Using the `rcParams` dictionary](#2-using-the-rcparams-dictionary)
- [3.  Using the `subplots` function](#3-using-the-subplots-function)
- [4.  Using the `set_size_inches` method](#4-using-the-set_size_inches-method)
- [5.  Using the `rc` function](#5-using-the-rc-function)

<!-- /MarkdownTOC -->

<a id="1-using-the-figure-function"></a>
## 1.  Using the `figure` function

You can use the `figure` function to create a new figure with a specific size. Here's an example:

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))

```

This will create a new figure with a width of 8 inches and a height of 6 inches.

<a id="2-using-the-rcparams-dictionary"></a>
## 2.  Using the `rcParams` dictionary

You can also use the `rcParams` dictionary to set the default figure size for all figures. Here's an example:

```python
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (8, 6)

```
This will set the default figure size to a width of 8 inches and a height of 6 inches.

<a id="3-using-the-subplots-function"></a>
## 3.  Using the `subplots` function

You can use the `subplots` function to create a new figure and one or more subplots with a specific size. Here's an example:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

```

This will create a new figure with a single subplot with a width of 8 inches and a height of 6 inches.

<a id="4-using-the-set_size_inches-method"></a>
## 4.  Using the `set_size_inches` method

You can also use the `set_size_inches` method to change the size of an existing figure. Here's an example:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(8, 6)

```

This will change the size of the existing figure to a width of 8 inches and a height of 6 inches.

<a id="5-using-the-rc-function"></a>
## 5.  Using the `rc` function

You can use the `rc` function to set the figure size for a specific figure only. Here's an example:

```python
import matplotlib.pyplot as plt

with plt.rc_context({"figure.figsize": (8, 6)}):
    fig = plt.figure()
```

This will create a new figure with a width of 8 inches and a height of 6 inches, but only for that specific figure.

Overall, there are multiple ways to change the size of a matplotlib figure. You can either set a default size for all figures using the `rcParams` dictionary, create a new figure with a specific size using the `figure` or `subplots` function, change the size of an existing figure using the `set_size_inches` method, or set the size of a specific figure using the `rc` function. Choose the method that best fits your needs depending on your specific use case.

For more ideas and use-cases you might want to look at stackoverflow question and answers:
https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib