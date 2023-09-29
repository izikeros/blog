---
Category: note
Date: '2022-04-14'
Modified: '2023-07-12'
Slug: python-configuration-management
Status: published
Summary: None
Tags: python, configuration, hydra, decouple
Title: Python - Configuration Management
citation_needed: true
---
Python is a powerful programming language that is widely used in a variety of applications, from web development and data science to machine learning and AI. One of the key aspects of any Python project is managing configurations, which can become complex and difficult to manage as the project grows. In this blog post, we will take a look at three popular packages for managing configurations in Python: hydra, decouple, omegaconf and others. We will explore the features and capabilities of each package, and provide examples of how to use them in a Python project. By the end of this post, you will have a better understanding of how to manage configurations in Python and be able to choose the package that best fits your needs.

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [hydra](#hydra)
- [decouple](#decouple)
- [omegaconf](#omegaconf)
- [Upsilonconf](#upsilonconf)
- [ml_collections](#ml_collections)
  - [Features](#features)
  - [Basic Usage of ml_collections](#basic-usage-of-ml_collections)

<!-- /MarkdownTOC -->

<a id="hydra"></a>
## hydra
[Hydra](https://hydra.cc/) is a Python library that allows you to access parameters from a configuration file inside a Python script.

Features:
- composite configs
- various options for launching:
	- easy config modifications from cli
	- multiruns

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

From: https://towardsdatascience.com/how-to-structure-a-data-science-project-for-readability-and-transparency-360c6716800


<a id="decouple"></a>
## decouple
> Python Decouple: Strict separation of settings from code

Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.

It also makes it easy for you to:

- store parameters in ini or .env files;
define comprehensive default values;
- properly convert values to the correct data type;
- have only one configuration module to rule all your instances.
- It was originally designed for Django, but became an independent generic tool for separating settings from code.

Envvars works, but since `os.environ` only returns strings, it’s tricky.

Let’s say you have an envvar `DEBUG=False`. If you run:
```
if os.environ['DEBUG']:
    print True
else:
    print False
```
It will print `True`, because `os.environ['DEBUG']` returns the string "False". Since it’s a non-empty string, it will be evaluated as True.

Decouple provides a solution that doesn’t look like a workaround: `config('DEBUG', cast=bool)`.

From: package description on pypi

<a id="omegaconf"></a>
## omegaconf
[OmegaConf](https://github.com/omry/omegaconf) is a hierarchical configuration system, with support for merging configurations from multiple sources (YAML config files, dataclasses/objects and CLI arguments) providing a consistent API regardless of how the configuration was created.

 > OmegaConf is also the backbone for the more advanced [Hydra](https://hydra.cc/) framework.
 
 
Documentation v2.2: [Installation — OmegaConf 2.2.4.dev0 documentation](https://omegaconf.readthedocs.io/en/2.2_branch/usage.html)

<a id="upsilonconf"></a>
## Upsilonconf
Concretely, the idea of this library is to provide an alternative to OmegaConf without the overhead of the variable interpolation (especially the `antlr` dependency). It is also very similar to the (discontinued) [AttrDict](https://github.com/bcj/AttrDict) library. In the meantime, there is also the [ml_collections](https://github.com/google/ml_collections) library, which seems to build on similar ideas as this project.

<a id="ml_collections"></a>
## ml_collections
[google/ml_collections](https://github.com/google/ml_collections)
ML Collections is a library of Python Collections designed for ML use cases.
The two classes called `ConfigDict` and `FrozenConfigDict` are "dict-like" data structures with dot access to nested elements. Together, they are supposed to be used as a main way of expressing configurations of experiments and models.
<a id="features"></a>
### Features

-   Dot-based access to fields.
-   Locking mechanism to prevent spelling mistakes.
-   Lazy computation.
-   FrozenConfigDict() class which is immutable and hashable.
-   Type safety.
-   "Did you mean" functionality.
-   Human readable printing (with valid references and cycles), using valid YAML format.
-   Fields can be passed as keyword arguments using the `**` operator.
-   There is one exception to the strong type-safety of the ConfigDict: `int` values can be passed in to fields of type `float`. In such a case, the value is type-converted to a `float` before being stored. (Back in the day of Python 2, there was a similar exception to allow both `str` and `unicode` values in string fields.)

<a id="basic-usage-of-ml_collections"></a>
### [Basic Usage of ml_collections](https://github.com/google/ml_collections#basic-usage)

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
