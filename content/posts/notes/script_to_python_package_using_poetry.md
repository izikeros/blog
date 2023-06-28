---
Title: Script to Python package using Poetry (and PyCharm)
Slug: script-to-python-package-using-poetry-and-pycharm
Date: 2023-06-28
Modified: 2023-06-28
Status: published
Tags: python, poetry, package, package-publish, pypi, git, tiktoken
Category: note
---
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [The task](#the-task)
- [Package creation](#package-creation)
    - [Create Project Directory](#create-project-directory)
    - [Open the Project in PyCharm](#open-the-project-in-pycharm)
    - [Install Dependencies](#install-dependencies)
    - [Configure PyCharm Interpreter](#configure-pycharm-interpreter)
    - [Initialize Git Repository](#initialize-git-repository)
    - [Create Package Structure](#create-package-structure)
    - [Move Script and Files](#move-script-and-files)
    - [Create `__init__.py`](#create-__init__py)
    - [Update `pyproject.toml`](#update-pyprojecttoml)
    - [Test the Script](#test-the-script)
    - [Package the Project](#package-the-project)
    - [Publish the Package](#publish-the-package)
    - [Versioning and Updates](#versioning-and-updates)

<!-- /MarkdownTOC -->

<a id="the-task"></a>
## The task
Let's assume that you have simple script that count tokens in provided text file. Below is the  script that accepts a positional input argument, which is the file name, and can be run from the command-line interface (CLI). See also the note on [How to count tokens?](https://safjan.com/how-to-count-tokens/)

```python
#!/usr/bin/env python3
import argparse
import tiktoken


def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


num_tokens_from_string(
    "tiktoken is great!",
)


def count_tokens(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return num_tokens_from_string(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count the number of tokens in a text file."
    )
    parser.add_argument("file", help="Path to the input text file")

    args = parser.parse_args()
    file_path = args.file

    num_tokens = count_tokens(file_path)
    print(f"Number of tokens: {num_tokens}")
```

In this script, the `argparse` module is used to handle command-line arguments. The script defines a single positional argument, `file`, which represents the file name of the input text file.

When the script is executed from the command line, it will parse the command-line arguments and retrieve the file path provided by the user. The `count_tokens` function will then be called with the file path, and the number of tokens will be printed.

To run the script from the CLI, use the following command:

```
python script_name.py file_path
```

Replace `script_name.py` with the actual name of your script file, and `file_path` with the path to the input text file you want to analyze. The script will then tokenize the text file and print the number of tokens.

> **NOTE:** you need `tiktoken` package installed before running the script. You can install it using pip:

```sh
pip install tiktoken
```

<a id="package-creation"></a>
## Package creation
To create and publish a Python package based on the provided script, you can follow the steps below:

<a id="create-project-directory"></a>
### Create Project Directory
Start by creating a new directory for your project. You can choose an appropriate name for the directory.

3. **Initialize the Project with Poetry**: Open your command-line interface and navigate to the project directory you created. Run the following command to initialize the project using Poetry:

   ```shell
   poetry init
   ```

   This command will prompt you to fill in information about your package, such as the package name, version, description, author details, and more. Fill in the required information as prompted.

<a id="open-the-project-in-pycharm"></a>
### Open the Project in PyCharm
Open PyCharm and select "Open" from the welcome screen or go to "File" > "Open" and choose the project directory you created.

 ### Configure Poetry Virtual Environment
 When opening the project in PyCharm for the first time, it will detect the presence of Poetry. You will be prompted to either allow PyCharm to create a Poetry virtual environment or create it manually. Select the option to create the virtual environment.

   If you already have a Poetry virtual environment set up manually, you can skip this step.

<a id="install-dependencies"></a>
### Install Dependencies
In your command-line interface, navigate to the project directory if you're not already there. Run the following command to install the necessary dependencies using Poetry:

   ```shell
   poetry install
   ```

   This command will create a virtual environment and install the required packages specified in your project's `pyproject.toml` file.

<a id="configure-pycharm-interpreter"></a>
### Configure PyCharm Interpreter
In PyCharm, go to "File" > "Settings" > "Project: <project_name>" > "Python Interpreter". Click on the gear icon and choose "Add...".

   Select "Poetry Environment" and choose the existing local Poetry interpreter associated with your project's virtual environment. Click "OK" to apply the changes.

<a id="initialize-git-repository"></a>
### Initialize Git Repository
In your command-line interface, navigate to the project directory if you're not already there. Run the following command to initialize a Git repository:

   ```shell
   git init
   ```

   This will set up a new Git repository for version control.

At this point, you have set up the project structure, initialized Poetry, configured the virtual environment in PyCharm, installed dependencies, and initialized a Git repository. Now, you can proceed with packaging and publishing your Python script.

<a id="create-package-structure"></a>
### Create Package Structure
Inside your project directory, create a package structure that follows Python's best practices. For example, you can create a directory named `my_package` that will contain your script and other necessary files.

<a id="move-script-and-files"></a>
### Move Script and Files
Move your script file and any other relevant files into the package directory (`my_package` in this example).

<a id="create-__init__py"></a>
### Create `__init__.py`
Inside the package directory (`my_package`), create an empty file named `__init__.py`. This file is required to make the directory a Python package.

<a id="update-pyprojecttoml"></a>
### Update `pyproject.toml`
Open your project's `pyproject.toml` file. Under the `[tool.poetry]` section, add the script file and any additional files that need to be included in the package. For example:

    ```toml
    [tool.poetry]
    ...
    [tool.poetry.scripts]
    my_script = 'my_package.my_script:main'
    ```

    Replace `my_script` with the desired command name for your script, and `my_package.my_script:main` with the correct import path to your script and its main function.

<a id="test-the-script"></a>
### Test the Script
Before publishing your package, it's essential to test your script to ensure it works as expected. You can execute the script locally to verify its functionality.

<a id="package-the-project"></a>
### Package the Project
In your command-line interface, navigate to the project directory. Run the following command to create a distributable package:

    ```shell
    poetry build
    ```

    This command will generate a distributable package (e.g., a `.tar.gz` file) in the `dist` directory within your project.

<a id="publish-the-package"></a>
### Publish the Package
To publish your package, you can use a package index such as PyPI (Python Package Index). First, you need to create an account on PyPI if you haven't already. Once you have an account, run the following command to publish your package:

    ```shell
    poetry publish
    ```

    This command will guide you through the process of publishing your package to PyPI. You'll be prompted to enter your PyPI credentials and confirm the publication.

    Note: Make sure your package has a unique name to avoid conflicts with existing packages on PyPI.

<a id="versioning-and-updates"></a>
### Versioning and Updates
When you make updates to your package, ensure to increment the version number in the `pyproject.toml` file under the `[tool.poetry.version]` section. This helps to track and manage different versions of your package.

That's it! You have now packaged and published your Python script using Poetry. Users can install your package using pip and use your script as a command-line tool.

Please note that publishing a package is a significant step, and it's essential to review and test your code thoroughly before sharing it with others.