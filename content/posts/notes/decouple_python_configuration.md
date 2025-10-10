---
Title: Use Decouple With Pydantic or Python Dataclass to Manage Configuration in Python App
Slug: use-decouple-with-pydantic-or-python-dataclass-to-manage-configuration-in-py
Date: 2024-04-19
Modified: 2024-04-19
Status: published
tags:
  - python
  - config
  - configuration
  - pydantic
  - decouple
  - python-app-config
  - immutable
  - casting
  - env-vars
  - environmental-variables
Category: note
---
X::[[python_configuration_management]]

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Basic Usage](#usage)
- [Add pydantic or dataclass](#add-pydantic-or-dataclass)
   - [Using `pydantic`:](#using-pydantic)
   - [Using `dataclass`:](#using-dataclass)
   - [Advantages of using `pydantic` or `dataclass`:](#advantages-of-using-pydantic-or-dataclass)
   - [Should the config be immutable?](#should-the-config-be-immutable)
- [dataclass + decouple example](#dataclass--decouple-example)

<!-- /MarkdownTOC -->

<a id="usage"></a>

## Basic Usage

`python-decouple` is a viable alternative to `python-dotenv` for managing environment variables in Python projects. It allows you to define environment variables in a `.env` file and access them in your Python code easily. Here's how you can migrate from `python-dotenv` to `python-decouple`:

1. **Installation**:

   First, you need to install `python-decouple` if you haven't already:

   ```bash
   pip install python-decouple
   ```

2. **Create a `.env` file**:

   If you haven't already, create a `.env` file in your project directory and add your environment variables in the format `KEY=VALUE`, one per line. For example:

   ```plaintext
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

3. **Modify your Python code**:

   Update your Python code to use `python-decouple` instead of `python-dotenv`. Here's a basic example:

   ```python
   # Old code using python-dotenv
   from dotenv import load_dotenv
   import os

   load_dotenv()

   secret_key = os.getenv('SECRET_KEY')
   debug = os.getenv('DEBUG')

   print(f"Secret Key: {secret_key}")
   print(f"Debug Mode: {debug}")
   ```

   Migrate to `python-decouple`:

   ```python
   # New code using python-decouple
   from decouple import config

   secret_key = config('SECRET_KEY')
   debug = config('DEBUG', default=False, cast=bool)

   print(f"Secret Key: {secret_key}")
   print(f"Debug Mode: {debug}")
   ```

   In the above example:
   - `config('SECRET_KEY')` reads the value of `SECRET_KEY` from the `.env` file.
   - `config('DEBUG', default=False, cast=bool)` reads the value of `DEBUG` from the `.env` file, with a default value of `False` if `DEBUG` is not set, and converts it to a boolean.

<a id="add-pydantic-or-dataclass"></a>

## Add pydantic or dataclass

Using `pydantic` or `dataclass` to define a configuration class in your Python project can  lead to more reliable and pythonic code. Both `pydantic` and `dataclass` provide ways to define data structures with type validation and optional default values. Whether your config should be immutable depends on your specific use case and preferences, but immutability can often lead to safer and more predictable behavior, especially in multi-threaded or concurrent environments.

Here's how you can use `pydantic` and `dataclass` to define a configuration class for your project:

<a id="using-pydantic"></a>

### Using `pydantic`

```python
from pydantic import BaseModel

class AppConfig(BaseModel):
    secret_key: str
    debug: bool = False

# Usage
config = AppConfig(secret_key="your_secret_key")
print(config)
```

<a id="using-dataclass"></a>

### Using `dataclass`

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    secret_key: str
    debug: bool = False

# Usage
config = AppConfig(secret_key="your_secret_key")
print(config)
```

<a id="advantages-of-using-pydantic-or-dataclass"></a>

### Advantages of using `pydantic` or `dataclass`

1. **Type validation**: Both `pydantic` and `dataclass` allow you to specify the types of your configuration attributes, providing type safety and reducing the risk of runtime errors.

2. **Default values**: You can specify default values for configuration attributes, making it easier to define a set of common configurations while still allowing customization when needed.

3. **Immutability** (with `frozen=True` in `dataclass`): Making the configuration class immutable can prevent accidental modification of configuration values, leading to more predictable behavior, especially in multi-threaded or concurrent environments.

4. **Pythonic syntax**: Both `pydantic` and `dataclass` provide a concise and pythonic syntax for defining data structures, making your code more readable and maintainable.

<a id="should-the-config-be-immutable"></a>

### Should the config be immutable?

Whether your config should be immutable depends on your specific use case and requirements. Here are some considerations:

- **Predictability**: Immutability can make your code more predictable by preventing accidental changes to configuration values.
- **Concurrency**: In multi-threaded or concurrent environments, immutability can help prevent race conditions and synchronization issues.
- **Testing**: Immutable objects are often easier to test since you don't need to worry about side effects from modifications.

However, if you anticipate needing to modify configuration values dynamically at runtime, immutability may not be suitable for your use case. Ultimately, consider your project's requirements and design your configuration class accordingly.

<a id="dataclass--decouple-example"></a>

## dataclass + decouple example

Here is an example demonstrating how to combine `dataclass` with `python-decouple` to manage configuration in a Python project:

1. **Install `python-decouple`**:

   If you haven't already, install `python-decouple`:

   ```bash
   pip install python-decouple
   ```

2. **Create a `.env` file**:

   Create a `.env` file in your project directory and add your environment variables:

   ```plaintext
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

3. **Define a `dataclass` for configuration**:

   Create a Python file (e.g., `config.py`) and define a `dataclass` for your configuration:

   ```python
   from dataclasses import dataclass

   @dataclass
   class AppConfig:
       secret_key: str
       debug: bool
   ```

4. **Read configuration from `.env` using `decouple`**:

   Modify your `config.py` file to read the configuration from the `.env` file using `decouple`:

   ```python
   from dataclasses import dataclass
   from decouple import config

   @dataclass
   class AppConfig:
       secret_key: str = config('SECRET_KEY')
       debug: bool = config('DEBUG', default=False, cast=bool)

   # Create an instance of AppConfig
   config = AppConfig()
   ```

5. **Usage**:

   Now you can use the `AppConfig` class instance in your project to access configuration values:

   ```python
   from config import config

   # Access configuration values
   print(f"Secret Key: {config.secret_key}")
   print(f"Debug Mode: {config.debug}")
   ```

With this setup, you're using `dataclass` to define a structured configuration class, and `decouple` to read configuration values from the `.env` file. This combination allows you to manage your project's configuration in a more organized and pythonic way.
