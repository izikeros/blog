---
Category: note
Date: 2023-11-13
Modified: 2023-11-13
Slug: the-importance-of-adding-py-typed-file-to-your-typed-package
Status: published
Summary: Learn why and how to add a `py.typed` file to your Python package for proper type checking with tools like `mypy`. Discover the steps to integrate this file using `poetry` or `setup.py` and understand its importance for accurate package distribution.
ai_summary: true
Title: The Importance of Adding a `py.typed` File to Your Typed Package
tags:
  - python
  - package
  - mypy
  - poetry
  - typink
  - type-hints
  - pep
---
X::[[python_package]]
X::[[python_packaging_tools]]
X::[[python_manifest_in_file]]

For the Python programming, type checking might be an important aspect aspect that ensures the correctness of your code. The `mypy` type checker is a powerful tool that uses type annotations to verify your code. However, it might not recognize the type hints provided by your package unless you include a `py.typed` file. This is a common oversight that can lead to incorrect package publishing.

## Understanding `py.typed`

**The `py.typed` file is a marker file that indicates to type checkers like `mypy` that your package comes with type annotations.** Without this file, the type checker won't use the type hints provided by your package, leading to potential type errors. This requirement is outlined in [PEP-561](https://www.python.org/dev/peps/pep-0561/#packaging-type-information) and the [mypy documentation](https://mypy.readthedocs.io/en/stable/installed_packages.html#making-pep-561-compatible-packages).

## Adding `py.typed` to Your Package

Adding a `py.typed` file to your package is straightforward. Simply create a `py.typed` file in your package directory and include it in your distribution.

If you're using [poetry](https://python-poetry.org/), you can add the following lines under the `[tool.poetry]` section of `pyproject.toml`:

```toml
packages = [
  {include = "mypackage"},
  {include = "mypackage/py.typed"},
]
```

For those using `setup.py`, you can add `package_data` to the `setup` call:

```python
setup(
    package_data={"mypackage": ["py.typed"]},
)
```

After adding the `py.typed` file, release [a new version for your package](https://github.com/whtsky/pixelmatch-py/commit/9c6297cedd10232ffbe23cc54a4e46e76d1fa13a). This will ensure that the type information from your packages works as expected.

## Conclusion

If you're a Python package maintainer, don't forget to include a `py.typed` file in your typed package. This simple step can make a significant difference in ensuring the correctness of your code and the usability of your package. It's a small effort that goes a long way in maintaining the quality and reliability of your Python package.

**Credits** to [Wu Haotian](https://dev.to/whtsky) for the article [Don't forget `py.typed` for your typed Python package - DEV Community](https://dev.to/whtsky/don-t-forget-py-typed-for-your-typed-python-package-2aa3) - I have learned about this mechanism from that post.
