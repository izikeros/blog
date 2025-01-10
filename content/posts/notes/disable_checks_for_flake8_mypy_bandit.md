---
category: note
date: 2022-05-12
modified: 2024-07-17
status: published
slug: disable-checks-for-flake8-mypy-bandit-and-black
tags: bandit, black, check, disable, flake8, mypy, linting, code-formatting , formatting, black-formatter, static-type-checking, typing, type-hints
title: Disable checks for flake8, mypy, bandit and black
---

<!-- MarkdownTOC levels="2" autolink="true" autoanchor="true" -->

- [Introduction](#introduction)
- [Flake8: Flexible Python Code Linter](#flake8-flexible-python-code-linter)
- [Mypy: Static Type Checker](#mypy-static-type-checker)
- [Bandit: Security Linter](#bandit-security-linter)
- [Black: The Uncompromising Code Formatter](#black-the-uncompromising-code-formatter)
- [Best Practices](#best-practices)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="introduction"></a>

## Introduction

In Python development, code quality tools like Flake8, Mypy, Bandit, and Black are invaluable for maintaining clean, consistent, and secure code. However, there are situations where you might need to disable certain checks. This guide provides detailed instructions on how to selectively disable checks for each tool, ensuring you can maintain code quality while accommodating specific project needs.

<a id="flake8-flexible-python-code-linter"></a>

## Flake8: Flexible Python Code Linter

Flake8 is a popular linting tool that combines PyFlakes, pycodestyle, and Ned Batchelder's McCabe script. Here are multiple ways to disable its checks:

<a id="1-inline-disabling"></a>

### 1. Inline Disabling

- Use the comment `# noqa` at the end of a line to disable all checks for that line.
- For specific error codes, use `# noqa: <error_code>`, e.g., `# noqa: E501` to ignore line length.

<a id="2-configuration-file-flake8"></a>

### 2. Configuration File (.flake8)

Create a `.flake8` file in your project root:
```ini
[flake8]
ignore = E226,E302,E41
max-line-length = 160
exclude = tests/*
max-complexity = 10
```

<a id="3-per-file-disabling"></a>

### 3. Per-File Disabling

Add this at the top of a file to disable specific checks:
```python
# flake8: noqa: E226,E302,E41
```

<a id="note-on-pyprojecttoml"></a>

### Note on pyproject.toml

As of my last update, Flake8 does not natively support `pyproject.toml`. However, you can use plugins like `flake8-pyproject` to enable this functionality.

<a id="mypy-static-type-checker"></a>

## Mypy: Static Type Checker

Mypy helps catch type-related errors before runtime. Here's how to disable its checks:

<a id="1-inline-disabling-1"></a>

### 1. Inline Disabling

- Use `# type: ignore` to ignore all type checks on a line.
- For specific error codes: `# type: ignore[error-code]`

<a id="2-configuration-file-mypyini-or-setupcfg"></a>

### 2. Configuration File (mypy.ini or setup.cfg)

```ini
[mypy]
ignore_missing_imports = True
disallow_untyped_defs = False
```

<a id="3-per-file-disabling-1"></a>

### 3. Per-File Disabling

Add this at the top of a file:
```python
# mypy: ignore-errors
```

<a id="bandit-security-linter"></a>

## Bandit: Security Linter

Bandit is a tool designed to find common security issues in Python code. To disable its checks:

<a id="1-inline-disabling-2"></a>

### 1. Inline Disabling

- Use `# nosec` to skip security checks for a line.
- For specific checks: `# nosec B101,B102`

<a id="2-configuration-file-bandityaml"></a>

### 2. Configuration File (bandit.yaml)

```yaml
skips: ['B311', 'B315']
```

<a id="3-command-line-exclusion"></a>

### 3. Command-Line Exclusion

```bash
bandit -r your_project_directory -x tests,docs
```

<a id="black-the-uncompromising-code-formatter"></a>

## Black: The Uncompromising Code Formatter

Black automatically formats Python code to adhere to a consistent style. Here's how to disable its formatting:

<a id="1-inline-disabling-3"></a>

### 1. Inline Disabling

Use comment blocks to prevent formatting of specific code sections:
```python
# fmt: off
<lines of code>
# fmt: on 
```

<a id="2-configuration-file-pyprojecttoml"></a>

### 2. Configuration File (pyproject.toml)

```toml
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | build
  | dist
)/
'''
```

<a id="3-handling-formatting-conflicts"></a>

### 3. Handling Formatting Conflicts

When there's a discrepancy between Black and Flake8, especially for slice formatting, you have two options:

a. Disable Black formatting for the problematic code:
```python
# fmt: off
chunks.append([doc[i : i + this_chunk_size]])
# fmt: on
```

b. Use Black formatting and disable Flake8 complaints:
```python
chunks.append(doc[i : i + this_chunk_size])  # noqa E203
```

<a id="best-practices"></a>

## Best Practices

1. **Selective Disabling**: Only disable checks when absolutely necessary. Overuse can lead to decreased code quality.
2. **Documentation**: Always comment why a check is being disabled to inform other developers.
3. **Regular Reviews**: Periodically review disabled checks to see if they can be re-enabled.
4. **Team Consensus**: Establish team guidelines for when and how to disable checks.

> **NOTE:** While these tools are crucial for maintaining high code quality, there are valid reasons to occasionally disable their checks. By understanding how to do so effectively, you can balance code quality with project-specific needs and developer productivity.
