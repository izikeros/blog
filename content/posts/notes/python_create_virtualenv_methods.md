---
category: note
date: 2022-05-12
status: published
slug: python-create-virtualenv-methods
tags: python, virtual-environment, venv, virtualenv, pyenv, conda, pipenv, poetry, docker, pdm, hatch, pipx, python-environment-setup, python-dependency-management, python-packaging
title: Creating Virtual Environments in Python
---

Python virtual environments are an essential tool for isolating project dependencies and avoiding conflicts between different projects. This article will guide you through methods of creating virtual environments in Python.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Using `venv`](#using-venv)
- [Using `virtualenv`](#using-virtualenv)
- [Using `pyenv`](#using-pyenv)
- [Using `conda`](#using-conda)
- [Using `pipenv`](#using-pipenv)
- [Using `Poetry`](#using-poetry)
- [Using `Docker`](#using-docker)
- [Using `PDM`](#using-pdm)
- [Using `Hatch`](#using-hatch)
- [Using `Pipx`](#using-pipx)

<!-- /MarkdownTOC -->

<a id="using-venv"></a>
## Using `venv`

`venv` is a module that comes pre-installed with Python 3.3 and later versions. It allows you to create lightweight virtual environments with their own site directories.

To create a virtual environment using `venv`, use the following commands:

```sh
# Linux and macOS
python3 -m venv virtual_environment_name

# Windows
py -m venv virtual_environment_name
```

If you want to create a virtual environment with a specific Python version, e.g., 3.9, you can do so by specifying the Python version as follows:

```sh
python3.9 -m venv virtual_environment_name
```

To activate this environment and install any packages, use the following commands:

```sh
# Linux and macOS
source virtual_environment_name/bin/activate

# Windows
.\virtual_environment_name\Scripts\activate
```

<a id="using-virtualenv"></a>
## Using `virtualenv`

`virtualenv` is a third-party Python package that you can install using pip. It allows you to create multiple side-by-side environments.

First, install `virtualenv` using the following command:

```sh
brew install virtualenv
```

Then, create a virtual environment with a specific Python version, e.g., 3.9, as follows:

```sh
virtualenv -p 3.9 $HOME/.virtualenvs/safeeyes
```

<a id="using-pyenv"></a>
## Using `pyenv`

`pyenv` is a powerful tool for managing multiple Python versions. It doesn't come pre-installed with Python, so you'll need to install it separately. Once installed, you can use it to create virtual environments.

Detailed instructions on how to use `pyenv` for creating virtual environments will be covered in a separate article.


## Alternatives
While `venv`, `virtualenv`, and `pyenv` are the most commonly used tools for creating virtual environments in Python, there are alternative methods available. Here are a few:

<a id="using-conda"></a>
### Using `conda`

`conda` is a package, dependency, and environment management tool for any language, but it is particularly popular in the Python community. It comes pre-installed with the Anaconda Python distribution.

To create a virtual environment with `conda`, use the following command:

```sh
conda create --name virtual_environment_name python=3.9
```

To activate the environment, use:

```sh
conda activate virtual_environment_name
```

<a id="using-pipenv"></a>
### Using `pipenv`

`pipenv` is a tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command.

Install `pipenv` using pip:

```sh
pip install pipenv
```

Then, to create a new virtual environment for your project, navigate to your project directory and run:

```sh
pipenv install
```

This command will create a new virtual environment (if one doesn't already exist) and install the packages specified in the Pipfile.

To activate the environment, use:

```sh
pipenv shell
```

<a id="using-poetry"></a>
### Using `Poetry`

`Poetry` is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

Install `Poetry`:

```sh
curl -sSL https://install.python-poetry.org | python -
```

To create a new virtual environment and install dependencies, navigate to your project directory and run:

```sh
poetry install
```

This command will create a new virtual environment (if one doesn't already exist) and install the packages specified in the pyproject.toml file.

To activate the environment, use:

```sh
poetry shell
```

<a id="using-docker"></a>
### Using `Docker`

While not a Python-specific tool, Docker can be used to create isolated environments for Python applications. A Docker container can be thought of as a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the system tools, libraries, and settings.

To use Docker, you need to create a `Dockerfile` that specifies the Python version and the dependencies your application needs. Then, you can build a Docker image from this `Dockerfile` and run your application inside a Docker container based on this image.

<a id="using-pdm"></a>
### Using `PDM`

PDM is a modern Python package manager with PEP 582 support. It uses the pyproject.toml file to manage dependencies and environments, which makes it compatible with other tools that use this standard.

To create a new project with a dedicated environment, use:

```sh
pdm new my_project
```

To activate the environment, use:

```sh
pdm shell
```

<a id="using-hatch"></a>
### Using `Hatch`

Hatch is a productivity tool designed to make your workflow easier and more efficient, while also reducing the number of other tools you need to know. It is heavily inspired by npm.

To create a new project with a dedicated environment, use:

```sh
hatch new my_project
```

The command above will create a new directory named `my_project`, set up a new virtual environment, and initialize a new Git repository.

<a id="using-pipx"></a>
### Using `Pipx`

Pipx is a tool to help you install and run end-user applications written in Python. It's like `pip`, but for whole Python applications rather than for Python libraries.

To install a Python application in its own isolated environment, use:

```sh
pipx install my_project
```
