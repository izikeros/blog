---
Category: note
Date: 2023-03-08
Modified: 2023-07-12
Slug: yapf-toml-package-is-needed-for-using-pyproject-toml-as-a-configuration -file
Status: published
Summary: "Learn how to resolve the \"yapf: toml package is needed\" error by adding `additional_dependencies: [toml]` when using pyproject.toml as a configuration file."
ai_summary: true
Tags:
  - yapf
  - pre-commit
  - code-quality
  - code-formatting
  - code-formatter
Title: Yapf Toml Package Is Needed for Using pyproject.toml as a Configuration File
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
<https://github.com/pre-commit/mirrors-yapf/issues/15#issuecomment-814037905>

X::[[black_yapf]]
X::[[black_formatter]]
