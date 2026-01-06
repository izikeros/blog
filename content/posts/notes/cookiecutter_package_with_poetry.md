---
Category: note
Date: 2023-07-26
Modified: 2023-07-26
Slug: cookiecutter-for-the-python-package-with-poetry
Status: published
Summary: Learn how to use Cookiecutter and Poetry to streamline Python project setup, leveraging pre-configured templates and efficient dependency management for a faster development cycle.
ai_summary: true
Tags:
  - cookiecutter
  - poetry
  - python-project
  - hypermodern
  - nox
  - shpinx
  - pypi
  - python-package
  - python/package
Title: Cookiecutters for the python package with poetry
---
X::[[python_package]]

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Introduction](#introduction)
  - [Cookiecutter and Poetry for Python Project Scaffolding](#cookiecutter-and-poetry-for-python-project-scaffolding)
  - [Benefits of Using Cookiecutter for Project Scaffolding](#benefits-of-using-cookiecutter-for-project-scaffolding)
  - [Advantages of Using Poetry for Dependency Management](#advantages-of-using-poetry-for-dependency-management)
- [Cookiecutters](#cookiecutters)
  - [cjolowicz/cookiecutter-hypermodern-python](#cjolowiczcookiecutter-hypermodern-python)
  - [fpgmaas/cookiecutter-poetry](#fpgmaascookiecutter-poetry)
  - [radix-ai/poetry-cookiecutter](#radix-aipoetry-cookiecutter)
  - [albertorios/cookiecutter-poetry-pypackage](#albertorioscookiecutter-poetry-pypackage)
  - [timhughes/cookiecutter-poetry](#timhughescookiecutter-poetry)
  - [johanvergeer/cookiecutter-poetry](#johanvergeercookiecutter-poetry)
  - [elbakramer/cookiecutter-poetry](#elbakramercookiecutter-poetry)
  - [wboxx1/cookiecutter-pypackage-poetry](#wboxx1cookiecutter-pypackage-poetry)
- [cookiecutter wrapper](#cookiecutter-wrapper)
- [Tools and services often used in python project cookiecutters](#tools-and-services-often-used-in-python-project-cookiecutters)

<!-- /MarkdownTOC -->

## Introduction

### Cookiecutter and Poetry for Python Project Scaffolding

In the world of Python development, efficient project setup and management are essential for streamlined and successful software development. Two powerful tools that aid in this process are **Cookiecutter** and **Poetry**.

**Cookiecutter** is a command-line utility that enables developers to create project templates, or "cookiecutters," which serve as scaffolds for new projects. These cookiecutters are pre-configured templates that include project structures, file layouts, and even code snippets to kickstart the development process. With its simplicity and flexibility, Cookiecutter allows developers to easily generate consistent and well-organized projects without reinventing the wheel each time.

On the other hand, **Poetry** is a modern package manager and build tool for Python projects. It simplifies dependency management, packaging, and publishing while ensuring reproducible builds and version control. Poetry provides a user-friendly interface for managing project dependencies and virtual environments, making it a valuable asset for Python developers looking for an efficient way to manage their project's requirements.

### Benefits of Using Cookiecutter for Project Scaffolding

Using Cookiecutter for project scaffolding offers several key advantages:

1. **Consistency**: Cookiecutter promotes consistency across projects by providing a standardized and repeatable starting point. This consistency ensures that developers adhere to best practices and maintain a clean project structure throughout the development process.

2. **Time Savings**: With Cookiecutter, developers can avoid the repetitive and time-consuming task of setting up a new project from scratch. By using pre-defined templates, the initial project setup becomes quick and hassle-free, allowing developers to focus on writing code and implementing features.

3. **Community-Driven Templates**: The open-source nature of Cookiecutter means that developers can access a vast repository of community-contributed templates. This diverse collection covers various project types and frameworks, making it easy to find a suitable starting point for almost any Python project.

4. **Flexibility and Customization**: While offering pre-configured templates, Cookiecutter also allows developers to customize their project scaffolds. This flexibility ensures that developers can tailor the project structure to fit their specific needs and project requirements.

### Advantages of Using Poetry for Dependency Management

Poetry's features complement the benefits of Cookiecutter, making it an ideal companion for Python project development:

1. **Dependency Management Made Easy**: Poetry simplifies the management of project dependencies, handling both direct dependencies and their dependencies, providing a single-source-of-truth for the project's requirements.

2. **Virtual Environments**: Poetry creates isolated virtual environments for projects, ensuring that each project has its own set of dependencies, avoiding version conflicts and promoting project stability.

3. **Publication and Distribution**: Poetry streamlines the process of publishing packages to the Python Package Index (PyPI), simplifying the distribution of Python packages and making them accessible to a wider audience.

4. **Version Control and Reproducibility**: Poetry's `pyproject.toml` file allows for clear specification of package versions, ensuring reproducible builds and making it easier to manage version updates.

## Cookiecutters

### cjolowicz/cookiecutter-hypermodern-python

<https://github.com/cjolowicz/cookiecutter-hypermodern-python>

![github stars shield](https://img.shields.io/github/stars/cjolowicz/cookiecutter-hypermodern-python.svg?logo=github)

[User Guide - Hypermodern Python Cookiecutter documentation](https://cookiecutter-hypermodern-python.readthedocs.io/en/2021.3.14/guide.html)

- Packaging and dependency management with [Poetry](https://python-poetry.org/)
- Test automation with [Nox](https://nox.thea.codes/)
- Linting with [pre-commit](https://pre-commit.com/) and [Flake8](http://flake8.pycqa.org/)
- Continuous integration with [GitHub Actions](https://github.com/features/actions)
- Documentation with [Sphinx](http://www.sphinx-doc.org/) and [Read the Docs](https://readthedocs.org/)
- Automated uploads to [PyPI](https://pypi.org/) and [TestPyPI](https://test.pypi.org/)
- Automated release notes with [Release Drafter](https://github.com/release-drafter/release-drafter)
- Automated dependency updates with [Dependabot](https://dependabot.com/)
- Code formatting with [Black](https://github.com/psf/black) and [Prettier](https://prettier.io/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Code coverage with [Coverage.py](https://coverage.readthedocs.io/)
- Coverage reporting with [Codecov](https://codecov.io/)
- Command-line interface with [Click](https://click.palletsprojects.com/)
- Static type-checking with [mypy](http://mypy-lang.org/)
- Runtime type-checking with [Typeguard](https://github.com/agronholm/typeguard)
- Security audit with [Bandit](https://github.com/PyCQA/bandit) and [Safety](https://github.com/pyupio/safety)
- Check documentation examples with [xdoctest](https://github.com/Erotemic/xdoctest)
- Generate API documentation with [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
- Generate command-line reference with [sphinx-click](https://sphinx-click.readthedocs.io/)
- Manage project labels with [GitHub Labeler](https://github.com/marketplace/actions/github-labeler)

### fpgmaas/cookiecutter-poetry

<https://github.com/fpgmaas/cookiecutter-poetry>

![github stars shield](https://img.shields.io/github/stars/fpgmaas/cookiecutter-poetry.svg?logo=github)

- [Poetry](https://python-poetry.org/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [black](https://pypi.org/project/black/), [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), and [deptry](https://github.com/fpgmaas/deptry/)
- Publishing to [Pypi](https://pypi.org/) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)

### radix-ai/poetry-cookiecutter

<https://github.com/radix-ai/poetry-cookiecutter>

![github stars shield](https://img.shields.io/github/stars/radix-ai/poetry-cookiecutter.svg?logo=github)

### albertorios/cookiecutter-poetry-pypackage

<https://github.com/albertorios/cookiecutter-poetry-pypackage>

![github stars shield](https://img.shields.io/github/stars/albertorios/cookiecutter-poetry-pypackage.svg?logo=github)

- Develop, build, and release Python packages using via [Poetry](https://python-poetry.org/)
- Test against multiple Python versions via [Tox](https://tox.readthedocs.io/en/latest/)
- Bump semantic version via [bump2version](https://github.com/c4urself/bump2version)
- Optional command-line interface via [Click](https://click.palletsprojects.com/)
- Repeatable build environments via [Docker](https://www.docker.com/)

### timhughes/cookiecutter-poetry

<https://github.com/timhughes/cookiecutter-poetry>

![github stars shield](https://img.shields.io/github/stars/timhughes/cookiecutter-poetry.svg?logo=github)

Cookiecutter template configured with the following:

- poetry
- pytest
- black
- bandit
- pyinstaller
- jupyterlab
- click

### johanvergeer/cookiecutter-poetry

<https://github.com/johanvergeer/cookiecutter-poetry>

![github stars shield](https://img.shields.io/github/stars/johanvergeer/cookiecutter-poetry.svg?logo=github)

- Testing setup with `pytest`
- [GitHub Actions](https://github.com/features/actions): Ready for GitHub actions
- [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.io/)
- Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a new tag to master (optional)
- Command-line interface using Click (optional)
- GitHub Issue templates for bug reports and feature requests

### elbakramer/cookiecutter-poetry

<https://github.com/elbakramer/cookiecutter-poetry>
(fork from johanvergeer/cookiecutter-poetry)

![github stars shield](https://img.shields.io/github/stars/elbakramer/cookiecutter-poetry.svg?logo=github)

- Package and dependency management using [Poetry](https://python-poetry.org/)
  - Has the option to stick with setuptools (setup.py)
- [GitHub Actions](https://github.com/features/actions): Ready for GitHub Actions
  - Build and test on push or pull request for continuous integration (CI) (+badge)
  - Build documentation on push, publish the built documentation to Github Pages (+badge)
  - Draft release on push, this draft can be published manually or even automatically when a new tag is pushed
  - Build and release Python package to [PyPI](https://pypi.org/) when a new release tag is published on GitHub
- Many [pre-commit](https://pre-commit.com/) hook-based formatting, linting, testing tools
  - Upgrade syntax for newer Python with [pyupgrade](https://github.com/asottile/pyupgrade)
  - Formatting with [black](https://github.com/psf/black)
  - Import sorting with [isort](https://github.com/PyCQA/isort)
  - Linting with [flake8](https://github.com/PyCQA/flake8) and [pylint](https://github.com/PyCQA/pylint/)
  - Static typing with [mypy](https://github.com/python/mypy)
  - Testing with [pytest](https://docs.pytest.org/en/stable/contents.html)
  - Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Other integrations with external sites/services
  - [Sphinx](http://sphinx-doc.org/) docs serving with [ReadTheDocs](https://readthedocs.io/) (+badge)
  - Coverage report with [Codecov](https://about.codecov.io/) (+badge)
  - Monitoring dependency version updates with [Requires.io](https://requires.io/) or [PyUp](https://pyup.io/) (+badge)
- Version bumping using [bump2version](https://github.com/c4urself/bump2version)
- Dynamic versioning using [dunamai](https://github.com/mtkennerly/dunamai)
- Command-line interface using [Click](https://click.palletsprojects.com/en/7.x/)

### wboxx1/cookiecutter-pypackage-poetry

<https://github.com/wboxx1/cookiecutter-pypackage-poetry>

![github stars shield](https://img.shields.io/github/stars/wboxx1/cookiecutter-pypackage-poetry.svg?logo=github)

- Testing setup with `unittest` and `python setup.py test` or `pytest`
- [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous Integration testing
- [Appveyor](http://appveyor.com/): Ready for Appveyor Continuous Integration testing
- [Tox](http://testrun.org/tox/) testing: Setup to easily test for Python 2.7, 3.4, 3.5, 3.6, 3.7
- [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.io/)
- [Bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
- Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a new tag to master (optional)
- Command-line interface using Click (optional)

## cookiecutter wrapper

<https://pypi.org/project/cookiecutter-poetry/>

Please note that the actual number of GitHub stars would be fetched dynamically when viewing the article in real-time. The badge URL with the GitHub stars includes a placeholder (`{shield}`) for the dynamic value, and the actual number will be displayed when the badge is rendered on the page.

## Tools and services often used in python project cookiecutters

- [Cookiecutter](https://cookiecutter.readthedocs.io/): Command-line utility for creating project templates.
- [Poetry](https://python-poetry.org/): Package manager and build tool for Python projects.
- [Pre-commit](https://pre-commit.com/): Framework for managing and maintaining multi-language pre-commit hooks.
- [Black](https://github.com/psf/black): Opinionated code formatter for Python.
- [Tox](https://tox.readthedocs.io/): Generic virtualenv management and test command line tool.
- [Nox](https://nox.thea.codes/): Flexible test automation tool.
- [Ruff](https://github.com/charliermarsh/ruff): Fast Linter, code quality tool for Python projects.
- [GitHub Actions](https://github.com/features/actions): Continuous integration and continuous deployment service by GitHub.
- [Codecov](https://about.codecov.io/): Code coverage reporting tool.
- [Bump2version](https://github.com/c4urself/bump2version): Version-bumping utility for software projects.
- [Docker](https://www.docker.com/): Platform for building, shipping, and running applications in containers.
- [Sphinx](http://www.sphinx-doc.org/): Documentation generator for Python projects.
- [Read the Docs](https://readthedocs.org/): Hosting service for software documentation.
- [Release Drafter](https://github.com/release-drafter/release-drafter): Automated release notes generation tool.
- [Dependabot](https://dependabot.com/): Automated dependency updates tool.
- [Prettier](https://prettier.io/): Opinionated code formatter for various languages, including Python.
- [pytest](https://docs.pytest.org/en/latest/): Framework for writing and running Python tests.
- [Coverage.py](https://coverage.readthedocs.io/): Code coverage measurement tool for Python.
- [Typeguard](https://github.com/agronholm/typeguard): Runtime type checking for Python functions.
- [Bandit](https://github.com/PyCQA/bandit): Security linter for Python code.
- [Safety](https://github.com/pyupio/safety): Security dependency checker for Python packages.
- [xdoctest](https://github.com/Erotemic/xdoctest): Tool for running code examples in docstrings.
- [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html): Sphinx extension for automatic documentation generation from docstrings.
- [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html): Sphinx extension for NumPy and Google style docstrings.
- [sphinx-click](https://sphinx-click.readthedocs.io/): Sphinx extension for Click-based command-line interfaces.
- [GitHub Labeler](https://github.com/marketplace/actions/github-labeler): GitHub Action for managing project labels.
