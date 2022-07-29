---
title: Python - configuration management
date: 2022-04-14
status: published
tags: python, configuration, hydra, decouple
summary: 
slug: python-configuration-management
category: note
citation_needed: true
todo: 
---
<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [hydra-core package](#hydra-core-package)
- [decouple package](#decouple-package)
- [omegaconf](#omegaconf)

<!-- /MarkdownTOC -->

<a id="hydra-core-package"></a>
## hydra-core package
[Hydra](https://hydra.cc/) is a Python library that allows you to access parameters from a configuration file inside a Python script.

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


<a id="decouple-package"></a>
## decouple package
> Python Decouple: Strict separation of settings from code

Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.

It also makes it easy for you to:

- store parameters in ini or .env files;
define comprehensive default values;
- properly convert values to the correct data type;
- have only one configuration module to rule all your instances.
-It was originally designed for Django, but became an independent generic tool for separating settings from code.

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
OmegaConf is a hierarchical configuration system, with support for merging configurations from multiple sources (YAML config files, dataclasses/objects and CLI arguments) providing a consistent API regardless of how the configuration was created.