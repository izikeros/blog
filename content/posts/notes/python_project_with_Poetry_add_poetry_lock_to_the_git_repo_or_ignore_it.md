---
Category: note
Date: 2023-11-12
Modified: 2023-11-12
Slug: python-project-with-Poetry-add-poetry-lock-to-the-git-repo-or-ignore-it
Status: published
Summary: In a Python project using Poetry, adding `poetry.lock` to your Git repository ensures consistent dependency versions across all environments. Also include `pyproject.toml` for project metadata and clarity on dependencies.
ai_summary: true
Title: In the Python project made with Poetry shall I add poetry.lock to the git repo or ignore it?
tags:
  - python
  - python-project
  - poetry
  - gitignore
  - git
  - repo
---
up:[[MOC_Python_Project]]

In a Python project managed with Poetry, you should definitely add the `poetry.lock` file to your Git repository. The `poetry.lock` file ensures that all project dependencies are specified with fixed versions, providing deterministic builds across different environments.

By including the `poetry.lock` file in your repository, you ensure that anyone cloning or checking out your project will have the exact same versions of the dependencies installed. This guarantees that they will have a consistent development environment and can reproduce the same build and execution results.

Including the `poetry.lock` file also serves as documentation for the specific versions of the dependencies used in your project. This information can be helpful for troubleshooting and debugging purposes.

When working with Poetry, you can also add the `pyproject.toml` file to your Git repository. This file contains the project metadata and the dependencies specified in a readable format, giving a high-level overview of your project's requirements.

Including both the `poetry.lock` and `pyproject.toml` files ensures that others can easily set up and work with your project while maintaining consistency across different development environments.

X::[[poetry]]
