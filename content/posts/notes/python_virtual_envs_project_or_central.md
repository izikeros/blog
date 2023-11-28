---
Title: Location of Python Virtual Environments - Choosing Between Project-Folder and Centralized Folder
Slug: location-of-python-virtual-environments-choosing-between-project-folder-and-central-folder
Date: 2023-07-27
Modified: 2023-07-27
Status: published
tags: python, virtualenv, location, venv-dir
Category: note
---

## Project-folder Virtual Environments
> In this approach, you create a virtual environment **within the project directory** itself. This means that each project has its isolated Python environment, and you manage dependencies specific to that project. 

With this approach you have clarity where the associated venv resides - helpful when doing cleanup or backup.

## Centralized Location for Virtual Environments
> In this approach, you create a **centralized directory** where **all virtual environments reside**. This directory can be outside your projects, e.g., `~/.virtualenvs` or any other location you prefer.

With this approach you keep project directory containing mainly code - the other, replicable content - virtual environment files - are located somewhere outside the project. This helps to e.g. backup whole directory without worrying about excluding virtualenv which is typically not worth backing-up.

X: [[python_create_virtualenv_methods]]