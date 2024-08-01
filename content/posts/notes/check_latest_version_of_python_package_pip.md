---
Title: How to Check Latest Version of Python Package?
Slug: how-to-check-latest-version-of-python-package
Date: 2024-07-03
Modified: 2024-07-03
Status: published
tags: pip, package-version, pypi, pypi-api, jq, curl, yolk, json, python
Category: note
---

Recently, for pip >= 21.2 the syntax `pip install pandas==` does not work anymore. There are several methods to get this information in a different way.

## Use pip

There is a new experimental command:

```sh
pip index versions <package_name>
```

This command shows all available versions, with the latest at the top.

## Use PyPI API and jq
Alternatively you can use PyPI API with curl and [jq](https://github.com/jqlang/jq):

```sh
curl -s https://pypi.org/pypi/<package_name>/json | jq -r '.info.version'
```

This retrieves the latest version directly from PyPI.

```sh
curl -s https://pypi.org/pypi/<package_name>/json | jq -r 'releases | keys'
```

For convenience, you can use a shell function. Here's how you can do it:

1. Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`) in a text editor.
2. Add the following function(s):
```bash
# display the latests version
pyversion() {
    curl -s "https://pypi.org/pypi/$1/json" | jq -r '.info.version'
}

# display all versions
py-all-versions() {
    curl -s "https://pypi.org/pypi/$1/json" | jq -r 'releases | keys'
}
```

> **NOTE**: using PyPI API + jq is significantly faster than using `pip index versions`. using pypi API took ~0.4 s while pip index version took ~2 s.


## Using the `yolk` package:

First, install yolk3k:
```sh
pip install yolk3k
```

Then run:
```sh
yolk -V <package_name>
```
