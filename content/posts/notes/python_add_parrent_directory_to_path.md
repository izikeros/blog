---
title: Adding Parent Directory To Python Path
date: 2022-02-22
modified: 2022-02-22
status: published
tags: python, gist, snippet, jupyter, notebook
summary: 
slug: python-add-parent-directory-to-path
category: note
citation_needed: false
---


There may be times when you want to import modules from a parent directory in Python. This can be useful, for example, when working with Jupyter notebooks and you want to keep your code organized in a specific directory structure. In this article, we will explore different ways to add a parent directory to the Python path so that you can import modules from it.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Method 1: Using `sys.path.insert()`](#method-1-using-syspathinsert)
- [Method 2: Using `sys.path.append()`](#method-2-using-syspathappend)
- [Method 3: Using `PYTHONPATH` environment variable](#method-3-using-pythonpath-environment-variable)
- [Method 4: Using `.pth` file](#method-4-using-pth-file)
- [Using `Pathlib`](#using-pathlib)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="method-1-using-syspathinsert"></a>
## Method 1: Using `sys.path.insert()`

One way to add a parent directory to the Python path is to use the `sys.path.insert()` method. This method allows you to insert a new path at a specific index in the `sys.path` list. To add a parent directory to the Python path, you can use the following code:

```python
import sys
sys.path.insert(0, '..')
```
This code imports the `sys` module and then uses the `insert()` method to add the parent directory (indicated by `'..'`) to the beginning of the `sys.path` list. This means that the parent directory will be searched before any other paths in the list when importing modules.

<a id="method-2-using-syspathappend"></a>
## Method 2: Using `sys.path.append()`

Another way to add a parent directory to the python path is to use the `sys.path.append()` method, which will add the given path to the end of the sys.path list.
```python
import sys
sys.path.append('..')
```

This method would work in the same way as above method but the order of search of the path will be different.

<a id="method-3-using-pythonpath-environment-variable"></a>
## Method 3: Using `PYTHONPATH` environment variable

You can also add a parent directory to the Python path by setting the `PYTHONPATH` environment variable.

```sh
export PYTHONPATH="$PYTHONPATH:/path/to/parent/directory"
```
This way the parent directory will be added to the python path for the current terminal session. To make the change permanent, you can add the above line to your shell startup file, such as `~/.bashrc` or `~/.bash_profile`

<a id="method-4-using-pth-file"></a>
## Method 4: Using `.pth` file

Another way to add parent directory to the python path is to create a `.pth` file in python's site-packages directory.

```sh
echo '..' > /usr/local/lib/python3.8/site-packages/my_project.pth`
```
This will add the parent directory as a permanent path to python's sys.path list.

It's important to note that the above solutions will work for Python 2 and Python 3

<a id="using-pathlib"></a>
## Using `Pathlib`
There is a way to add a parent directory to the Python path using the `pathlib` module with method 1 or method 2 explained above.  `pathlib` is a built-in Python module that provides an object-oriented interface for working with file paths.

One way to add a parent directory to the Python path using `pathlib` is to use the `parent` attribute of a `Path` object. This attribute returns a new `Path` object representing the parent directory of the original `Path` object. For example, you can use the following code to add a parent directory to the Python path:

```python
from pathlib import Path import sys  sys.path.append(str(Path(__file__).resolve().parent.parent))
```

This code imports the `Path` class from the `pathlib` module, and then uses the `__file__` special variable to get the current file's path. It uses the `resolve()` method to get the absolute path of the current file and then uses the `parent` attribute to get the parent directory of the current file and again parent directory of the parent directory of current file. This new `Path` object is then passed to the `append()` method of the `sys.path` list to add the parent directory to the Python path.

Another way to use pathlib is to use `pathlib.Path().joinpath()` to add the parent directory to the python path.

```python
from pathlib import Path
import sys path = Path().joinpath().joinpath('..')
sys.path.append(str(path))
```
This way you can join multiple directories using the joinpath method.

It's important to note that this method uses the `str()` function to convert the `Path` object to a string, as the `sys.path` list only accepts strings.
<a id="conclusion"></a>
## Conclusion

In this article, we have covered different ways to add a parent directory to the Python path, which can be useful when working with Jupyter notebooks or other projects that require a specific directory structure. 

CAUTION: Keep in mind that adding the parent directory to the python path will make the modules inside it available for import, but it also makes the entire directory structure available for import, so it's important to have a clear and organized directory structure.