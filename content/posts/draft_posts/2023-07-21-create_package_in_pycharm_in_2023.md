---
Title: Create Python Package in PyCharm
Slug: create-python-package-in-pycharm
Date: 2023-07-21
Modified: 2023-07-21
Start: 2023-07-21
Tags: machine-learning, python
Category: Machine Learning
Image: /images/head/abstract_1.jpg
banner: "/images/head/abstract_1.jpg"
Summary: 
Status: draft
prompt:
---

# Creating a Python Package Using PyCharm and Poetry

Welcome, fellow Python enthusiasts! Today, we'll walk you through the process of creating a Python package using the PyCharm IDE and the Poetry dependency management tool. By the end of this tutorial, you'll have a fully functional Python package that can convert lowercase text to uppercase. So, let's get started!
![[Pasted image 20230724200030.png]]
![[Pasted image 20230724200250.png]]
![PyCharm and Poetry logos](images/pycharm_poetry_logos.jpg)

## Prerequisites

Before we begin, make sure you have the following installed on your system:

1. **Python**: Download and install the latest version of Python from [the official website](https://www.python.org/downloads/).
2. **PyCharm**: Download and install the latest version of the PyCharm Community Edition from [JetBrains' official website](https://www.jetbrains.com/pycharm/download/).
3. **Poetry**: Install Poetry by following the [official installation instructions](https://python-poetry.org/docs/#installation).

With everything set up, we're ready to dive into creating our Python package.

## Creating a New Project in PyCharm

First, let's create a new Python project in PyCharm:

1. Launch PyCharm and click on "Create New Project".

![Create new project in PyCharm](images/create_new_project.jpg)

2. Choose a location for your project and give it a name. For this tutorial, we'll name our project `text_converter`.

3. Make sure the "Project Interpreter" is set to "New environment using" and select "Virtualenv" as the environment. Choose the Python interpreter you installed earlier.

![Select project interpreter](images/project_interpreter.jpg)

4. Click on "Create" to start your new Python project.

## Initializing a Poetry Project

Now that we have our project set up in PyCharm, let's initialize it as a Poetry project:

1. Open the terminal in PyCharm by clicking on the "Terminal" tab at the bottom of the screen.

![Open terminal in PyCharm](images/open_terminal.jpg)

2. In the terminal, navigate to your project's root directory and run the following command to initialize a new Poetry project:

```bash
poetry init
```

3. Follow the prompts to configure your project. For this tutorial, you can use the default settings.

![Initialize Poetry project](images/poetry_init.jpg)

4. After the initialization is complete, you'll see a new `pyproject.toml` file in your project directory. This file contains the project's metadata and dependencies.

## Creating the Package Directory Structure

Let's create the directory structure for our `text_converter` package:

1. In PyCharm, right-click on the project name in the "Project" panel and select "New" > "Directory". Name the new directory `text_converter`.

![Create package directory](images/create_package_directory.jpg)

2. Inside the `text_converter` directory, create a new file called `__init__.py`. This file is required for Python to treat the directory as a package.

3. Create another file inside the `text_converter` directory and name it `converter.py`. This file will contain the code for our text conversion functionality.

## Writing the Text Conversion Code

Open the `converter.py` file and write the following code:

```python
def lowercase_to_uppercase(text: str) -> str:
    return text.upper()
```

This simple function takes a string as input and returns the same string converted to uppercase using the `str.upper()` method.

## Creating the Package's Entry Point

To make our package easily accessible from the command line, we'll create an entry point script. In the project root directory, create a new file called `main.py` and add the following code:

```python
from text_converter.converter import lowercase_to_uppercase

def main():
    text = input("Enter text to convert to uppercase: ")
    uppercase_text = lowercase_to_uppercase(text)
    print(f"Uppercase text: {uppercase_text}")

if __name__ == "__main__":
    main()
```

This script imports the `lowercase_to_uppercase` function from our `text_converter.converter` module and defines a `main` function that takes user input, converts the text to uppercase, and prints the result. The `if __name__ == "__main__":` block ensures that the `main` function is executed when the script is run directly.

## Adding the Entry Point to `pyproject.toml`

To make our package installable and executable, we need to add the entry point to the `pyproject.toml` file. Open the file and add the following lines under the `[tool.poetry]` section:

```toml
[tool.poetry.scripts]
text_converter = "main:main"
```

This configuration tells Poetry to create a command called `text_converter` that will execute the `main` function from our `main.py` script when called.

## Building and Installing the Package

With everything in place, let's build and install our package using Poetry:

1. In the terminal, run the following command to build the package:

```bash
poetry build
```

2. After the build is complete, you'll see a `dist` directory containing the package files.

![Poetry build output](images/poetry_build.jpg)

3. Install the package locally by running:

```bash
poetry install
```

4. Test the package by running the `text_converter` command in the terminal:

```bash
text_converter
```

You should see the following output:

```
Enter text to convert to uppercase: hello world
Uppercase text: HELLO WORLD
```

Congratulations! You've successfully created a Python package using PyCharm and Poetry. You can now distribute your package, share it with others, or use it in your own projects. Happy coding!

![Python package success](images/python_package_success.jpg)