---
Category: note
Date: 2022-04-14
Modified: 2023-07-12
Slug: python-configuration-management
Status: published
Summary: None
tags:
  - python
  - configuration
  - hydra
  - decouple
  - omegaconf
  - yaml
  - config
  - experiment
  - experiment-management
Title: Python - Configuration Management
citation_needed: true
---
One of the key aspects of any Python project is managing configurations, which can become complex and difficult to manage as the project grows. In this blog post, we will take a look at three popular packages for managing configurations in Python: hydra, decouple, omegaconf and others. We will explore the features and capabilities of each package, and provide examples of how to use them in a Python project. By the end of this post, you will have a better understanding of how to manage configurations in Python and be able to choose the package that best fits your needs.



- [hydra](#hydra)
- [decouple](#decouple)
- [omegaconf](#omegaconf)
- [Upsilonconf](#upsilonconf)
- [ml\_collections](#ml_collections)
  - [Features](#features)
  - [Basic Usage of ml\_collections](#basic-usage-of-ml_collections)
- [Pydantic](#pydantic)
- [Honorable mentions](#honorable-mentions)
  - [Dynaconf](#dynaconf)
  - [ConfigParser](#configparser)
  - [Cerberus](#cerberus)



## hydra

[Hydra](https://hydra.cc/) is a Python library that allows you to access parameters from a configuration file inside a Python script.

Features:

- composite configs
- various options for launching:
 	- easy config modifications from cli
 	- multiruns
- CLI: completion for model parameters

Create exemplary `main.yaml` in directory `config`

```yaml
raw: 
  path: data/raw/sample.csv

processed:
  path: data/processed/processed.csv

final:
  path: data/final/final.csv
```

then we can access the value inside the configuration file by adding the decorator `@hydra.main` on a specific function. Inside this function, we can access the value under `processed` and `path` by using a dot notation: `config.processed.path` .

```python
"""
This is the demo code that uses hydra to access the parameters in under the directory config.
Author: Khuyen Tran
"""

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

@hydra.main(config_path="../config", config_name='main')
def process_data(config: DictConfig):
    """Function to process the data"""

    raw_path = abspath(config.raw.path)
    print(f"Process data using {raw_path}")
    print(f"Columns used: {config.process.use_columns}")

if __name__ == '__main__':
    process_data()
```

From: <https://towardsdatascience.com/how-to-structure-a-data-science-project-for-readability-and-transparency-360c6716800>

EuroPython 2022 conference talk about Hydra and integration with MLFlow:
```vid
https://www.youtube.com/watch?v=bNGu8A6F3-8
```

Hands-on tutorial how to introduce hydra to the exemplary data science project:
```vid
https://www.youtube.com/watch?v=tEsPyYnzt8s
```

## decouple
>
> Python Decouple: Strict separation of settings from code

[Decouple](https://pypi.org/project/python-decouple/) helps you to organize your settings so that you can change parameters without having to redeploy your app.

It also makes it easy for you to:

- store **parameters in** **ini** or **.env** files;
- define comprehensive **default values**;
- properly **convert values to the correct data type**;
- have only **one configuration module** to rule **all your instances**.

Envvars works, but since `os.environ` only returns strings, it’s tricky.

Let’s say you have an envvar `DEBUG=False`. If you run:

```python
if os.environ['DEBUG']:
    print True
else:
    print False
```

It will print `True`, because `os.environ['DEBUG']` returns the string "False". Since it’s a non-empty string, it will be evaluated as True.

Decouple provides a solution that doesn’t look like a workaround: `config('DEBUG', cast=bool)`.

From: package description on pypi

> **NOTE:** Since `config` can read parameters from .env (and .ini) - decouple can replace using dotenv.

## omegaconf

[OmegaConf](https://github.com/omry/omegaconf) is a hierarchical configuration system, with support for merging configurations from multiple sources (YAML config files, dataclasses/objects and CLI arguments) providing a consistent API regardless of how the configuration was created.

 > OmegaConf is also the backbone for the more advanced [Hydra](https://hydra.cc/) framework.

Documentation v2.2: [Installation - OmegaConf 2.2.4.dev0 documentation](https://omegaconf.readthedocs.io/en/2.2_branch/usage.html)

## Upsilonconf

![github stars shield](https://img.shields.io/github/stars/hoedt/upsilonconf.svg?logo=github)
Concretely, the idea of [upsilonconf](https://github.com/hoedt/upsilonconf) library is to provide an alternative to OmegaConf without the overhead of the variable interpolation (especially the `antlr` dependency). It is also very similar to the (discontinued) [AttrDict](https://github.com/bcj/AttrDict) library. In the meantime, there is also the [ml_collections](https://github.com/google/ml_collections) library, which seems to build on similar ideas as this project.

## ml_collections

[google/ml_collections](https://github.com/google/ml_collections)
ML Collections is a library of Python Collections designed for ML use cases.
The two classes called `ConfigDict` and `FrozenConfigDict` are "dict-like" data structures with dot access to nested elements. Together, they are supposed to be used as a main way of expressing configurations of experiments and models.

### Features

- Dot-based access to fields.
- Locking mechanism to prevent spelling mistakes.
- Lazy computation.
- FrozenConfigDict() class which is immutable and hashable.
- Type safety.
- "Did you mean" functionality.
- Human readable printing (with valid references and cycles), using valid YAML format.
- Fields can be passed as keyword arguments using the `**` operator.
- There is one exception to the strong type-safety of the ConfigDict: `int` values can be passed in to fields of type `float`. In such a case, the value is type-converted to a `float` before being stored. (Back in the day of Python 2, there was a similar exception to allow both `str` and `unicode` values in string fields.)

### Basic Usage of ml_collections

(from  documentation)
```python
from ml_collections import config_dict

cfg = config_dict.ConfigDict()
cfg.float_field = 12.6
cfg.integer_field = 123
cfg.another_integer_field = 234
cfg.nested = config_dict.ConfigDict()
cfg.nested.string_field = 'tom'

print(cfg.integer_field)  # Prints 123.
print(cfg['integer_field'])  # Prints 123 as well.

try:
  cfg.integer_field = 'tom'  # Raises TypeError as this field is an integer.
except TypeError as e:
  print(e)

cfg.float_field = 12  # Works: `Int` types can be assigned to `Float`.
cfg.nested.string_field = u'bob'  # `String` fields can store Unicode strings.

print(cfg)
```

## Pydantic

The core is based on *pydantic*, a data validation library for Python.  
  
More precisely, on their *BaseSettings* class.  
  
𝗪𝗵𝘆 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗽𝘆𝗱𝗮𝗻𝘁𝗶𝗰 𝗕𝗮𝘀𝗲𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 𝗰𝗹𝗮𝘀𝘀?  
  
- you can quickly load values from .𝘦𝘯𝘷 files (or even 𝘑𝘚𝘖𝘕 or 𝘠𝘈𝘔𝘓)  
- add default values for the configuration of your application  
- the MOST IMPORTANT one → It validates the type of the loaded variables. Thus, you will always be ensured you use the correct variables to configure your system.  
  
𝗛𝗼𝘄 𝗱𝗼 𝘆𝗼𝘂 𝗶𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁 𝗶𝘁?  
  
It is pretty straightforward.  
  
You subclass the 𝘉𝘢𝘴𝘦𝘚𝘦𝘵𝘵𝘪𝘯𝘨𝘴 class and define all your settings at the class level.  
  
It is similar to a Python 𝘥𝘢𝘵𝘢𝘤𝘭𝘢𝘴𝘴 but with an extra layer of data validation and factory methods.  
  
If you assign a value to the variable, it makes it optional.  
  
If you leave it empty, providing it in your .𝙚𝙣𝙫 file is mandatory.  
  
𝗛𝗼𝘄 𝗱𝗼 𝘆𝗼𝘂 𝗶𝗻𝘁𝗲𝗴𝗿𝗮𝘁𝗲 𝗶𝘁 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗠𝗟 𝗰𝗼𝗱𝗲?  
  
You often have a training configuration file (or inference) into a JSON or YAML file (I prefer YAML files as they are easier to read).  
  
You shouldn't pollute your 𝘱𝘺𝘥𝘢𝘯𝘵𝘪𝘤 settings class with all the hyperparameters related to the module (as they are a lot, A LOT).  
  
Also, to isolate the application & ML settings, the easiest way is to add the 𝘵𝘳𝘢𝘪𝘯𝘪𝘯𝘨_𝘤𝘰𝘯𝘧𝘪𝘨_𝘱𝘢𝘵𝘩 in your settings and use a 𝘛𝘳𝘢𝘪𝘯𝘪𝘯𝘨𝘊𝘰𝘯𝘧𝘪𝘨 class to load it independently.  
  
Doing so lets you leverage your favorite way (probably the one you already have in your ML code) of loading a config file for the ML configuration: plain YAML or JSON files, hydra, or other fancier methods.  
  
Another plus is that you can't hardcode the path anywhere on your system. That is a nightmare when you start using git with multiple people.  
  
```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
	model_config = SettingsConfigDict(env_file=(".env", ".env.prod"))
	
	QDRANT_URL: str = “localhost:6333"
	QDRANT_API_KEY: Optional[str] = None
	VECTOR_DB_COLLECTION: str # Mandatory
	
	training_config_path: Path # Mandatory
	
	class Config:
        env_file = ".env"

settings = AppSettings( )

training_config = TrainingConfig.from_yaml(settings.training_config_path)

```

## Honorable mentions

Modern Python solutions for managing configurations include:  

### Dynaconf

Dynaconf is a powerful settings management library that supports multiple file formats (JSON, YAML, TOML, INI) and environment variables.
It allows hierarchical settings and dynamic loading of configurations.

### ConfigParser  

Part of the Python standard library, ConfigParser is used for handling configuration files in INI format.
It is simple and lightweight, suitable for basic configuration needs.

### Cerberus

Cerberus is a lightweight and extensible data validation library for Python.
It can be used to validate configuration data against a schema.
