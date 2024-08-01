---
title: Using Pyenv
slug: using-pyenv
category: note
date: 2022-05-12
modified: 2024-07-17
status: published
tags: macos, pyenv, python, pipx
---

# Pyenv

Python is a popular programming language used for a wide range of applications, from web development to data analysis and machine learning. As a Python developer, it is important to manage your Python installations properly to avoid conflicts and ensure consistent behavior across different projects. One tool that can help with this is pyenv, a simple and powerful Python version management tool.

Pyenv is particularly useful for macOS users, as it allows you to easily install and manage multiple versions of Python on your system without affecting the system Python that comes with macOS. This is important because some macOS applications and scripts rely on the system Python, and modifying or replacing it can cause unexpected issues.

To get started with pyenv on macOS, you can use Homebrew, a popular package manager for macOS. Open your terminal and run the following command:

```sh
brew install pyenv
```

This will install pyenv and its dependencies on your system. Once installed, you need to add some configuration to your shell startup script (.bashrc, .zshrc, etc.) to enable pyenv. Add the following lines to the end of your shell startup script:

```sh
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```
This tells your shell to initialize pyenv when you start a new shell session. You can then use pyenv to manage your Python installations.

## Usage
Here are some common pyenv commands:

```sh
# list python versions available for installation
$ pyenv install -l

# list python versions available for installation, filter results to given version of python
$ pyenv install -l | grep 3.11

# remove other versions of python than main (e.g. exclude pypy, conda,...)
# and filter results to given version of python
pyenv install -l | grep -E '^[[:space:]]*[0-9]' | grep 3.11

# install selected version
$ pyenv install 3.8.5

# display all currently installed Python versions
$ pyenv versions

# create virtualenv `myenv` with default pyenv python version (see )
$ pyenv virtualenv myenv

# set as global interpreter for the system
$ c

# uninstall selected version
$ pyenv uninstall 3.8.4

# check the path to where virtualenv is created
$ pyenv activate myenv
$ echo $VIRTUAL_ENV

# remove pyenv virtualenv
#   3.8.2/envs/greenhouse obtained with `pyenv versions`
$ pyenv uninstall 3.8.2/envs/greenhouse
#   or
$ pyenv virtualenv-delete greenhouse
```

### Using with PyCharm
You can also use pyenv with PyCharm, a popular Python IDE. To use pyenv with PyCharm, you need to create a virtual environment using pyenv first, and then add it to PyCharm as a local interpreter. Here are the steps:

1.  Create a new virtual environment using pyenv: `pyenv virtualenv <version> <name>`
2.  In PyCharm, go to `Settings > Project > Python Interpreter`.
3.  Click the "Add..." button and select "Local".
4.  Browse to the location of the Python executable in your pyenv virtual environment. It should be something like `/Users/username/.pyenv/versions/<version>/envs/<name>/bin/python`.
5.  Click "OK" to add the interpreter.

You can now use the virtual environment with PyCharm, and any packages you install will be installed in the virtual environment rather than globally on your system.

### Installing python with tkinter
There is stackoverflow question on that: [Unable to install tkinter with pyenv Pythons on MacOS - Stack Overflow](https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos)


See also:
X::[[mac_wiki_v2]]
X::[[install_global_packages_with_pipx]]
