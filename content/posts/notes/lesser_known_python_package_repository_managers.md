---
Title: Lesser-known Python Package Repository Managers
Slug: lesser-known-python-package-repository-managers
Date: 2023-08-12
Modified: 2023-08-12
Status: published
Tags: pypi, python, python-package, package-repository, artifactory, devpi
Category: note
---
X::[[self_hosted_python_package_repository]]
X::[[python_packages_on_local_NAS]]
up::[[MOC_Python]]

The [Artifactory](https://jfrog.com/artifactory/) (paid) and [Devpi](https://devpi.net/docs/devpi/devpi/stable/%2Bd/index.html) (free, open source) are most widely used python package repository managers, but there are some other interesting projects. Here are a few lesser-known Python package repository managers along with links to their source code or home websites.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Warehouse](#warehouse)
- [pypiserver](#pypiserver)
- [Bandersnatch](#bandersnatch)
- [EggBasket](#eggbasket)

<!-- /MarkdownTOC -->

<a id="warehouse"></a>
## Warehouse

![github stars shield](https://img.shields.io/github/stars/pypa/warehouse.svg?logo=github)

The current codebase behind the Python Package Index (PyPI). While not lesser-known, it's worth mentioning as an alternative to the official PyPI implementation.

- Source Code: [https://github.com/pypa/warehouse](https://github.com/pypa/warehouse)

<a id="pypiserver"></a>
## pypiserver

  ![github stars shield](https://img.shields.io/github/stars/pypiserver/pypiserver.svg?logo=github)

PyHockey is a minimal Python package server that's easy to set up and use for hosting private packages.

- Source Code: [https://github.com/pypiserver/pypiserver](https://github.com/pypiserver/pypiserver)

<a id="bandersnatch"></a>
## Bandersnatch

![github stars shield](https://img.shields.io/github/stars/pypa/bandersnatch.svg?logo=github)

A PyPI mirror client that can be used to create a complete copy of the Python Package Index (PyPI) locally or in a private network.

- Home: [https://pypi.org/project/bandersnatch/](https://pypi.org/project/bandersnatch/)
- Source Code: [https://github.com/pypa/bandersnatch](https://github.com/pypa/bandersnatch)


<a id="eggbasket"></a>
## EggBasket

EggBasket is a lightweight, easily-configurable Python package server designed for simplicity and ease of use.

- Home: [https://pypi.org/project/eggbasket/](https://pypi.org/project/eggbasket/)

Please note that the popularity and maintenance status of these repositories may vary, so it's a good idea to review the documentation and GitHub repositories to ensure they meet your requirements before setting up a self-hosted package repository.