---
Title: yapf toml package is needed for using pyproject.toml as a configuration file
Slug: yapf-toml-package-is-needed-for-using-pyproject-toml-as-a-configuration -file
Date: 2023-03-08
Modified: 2023-03-08
Status: published
Tags: yapf, pre-commit 
Category: note
---

if you are getting error:

yapf: toml package is needed for using pyproject.toml as a configuration file

you can use:
```
-   repo: https://github.com/pre-commit/mirrors-yapf
    rev: v0.31.0
    hooks:
    -   id: yapf
        additional_dependencies: [toml]
```

solution from user **[asottile](https://github.com/asottile)**
https://github.com/pre-commit/mirrors-yapf/issues/15#issuecomment-814037905