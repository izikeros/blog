---
Title: Replacing Makefile with Invoke for Cross-Platform Python Tasks
Slug: replacing-makefile-with-invoke-for-crossplatform-python-tasks
Date: 2025-08-14
Modified: 2025-08-14
Status: published
Tags: makefile, cross-platform-build, python, invoke, task-automation, developer-experience, windows, macos, linux, team-collaboration, build-tools, portable-scripts
Category: note
---
I’ve always liked Make. It’s quick to type, powerful, and honestly kind of fun once you know the quirks. On macOS and Linux, it just works.

Then my teammate on Windows ran `make test-unit`. Boom. Red text. Paths broke. Shell flags disappeared. Instead of testing code, we were testing our patience.

After a couple of these moments, I realized I had two choices:

1. Keep duct-taping Windows support into the Makefile.
2. Switch to a tool that doesn’t care which OS you’re on.

I chose option 2.

## From my old Makefile

It looked like this — perfectly fine for macOS/Linux, but brittle on Windows:

```make
SRC_FILES = src
SRC_AND_TEST_FILES = src tests
R_PYPROJECT = requirements-pyproject.txt

test-unit: ## Run the unit tests with pytest.
	@echo -e "$(COLOR_CYAN)Running unit tests...$(COLOR_RESET)"
	pytest --log-cli-level=INFO -rA tests/unit/

format: ## Running code formatter: black and isort
	@echo "(isort) Ordering imports..."
	@isort $(SRC_AND_TEST_FILES)
	@echo "(black) Formatting codebase..."
	@black --config pyproject.toml $(SRC_AND_TEST_FILES)
	@echo "(ruff) Running fix only..."
	@ruff check $(SRC_AND_TEST_FILES) --fix-only

lint: ## Run the linter (ruff) to check the code style.
	@echo -e "$(COLOR_CYAN)Checking code style with ruff...$(COLOR_RESET)"
	ruff check $(SRC_AND_TEST_FILES)

changelog: ## Generate a changelog using git-cliff
	git-cliff -o CHANGELOG.md
```

It’s not bad code. It’s just not friendly to every shell.  
`echo -e` works in Bash, not in cmd.exe. Color codes are ignored in PowerShell. Paths and quoting rules differ. Small stuff, but it adds up.

## How I rewrote it to work everywhere

I moved the build logic into Python with [Invoke](https://www.pyinvoke.org/). The syntax is simple, it runs anywhere Python runs, and I can call the exact same commands on macOS, Linux, and Windows.

```python
# tasks.py — Invoke version
from invoke import task

SRC_FILES = "src"
SRC_AND_TEST_FILES = "src tests"

@task
def test_unit(c):
    print("Running unit tests...")
    c.run("python -m pytest --log-cli-level=INFO -rA tests/unit/")

@task
def format(c):
    print("(isort) Ordering imports...")
    c.run(f"python -m isort {SRC_AND_TEST_FILES}")
    print("(black) Formatting codebase...")
    c.run(f"python -m black --config pyproject.toml {SRC_AND_TEST_FILES}")
    print("(ruff) Running fix only...")
    c.run(f"python -m ruff check {SRC_AND_TEST_FILES} --fix-only")

@task
def lint(c):
    print("Checking code style with ruff...")
    c.run(f"python -m ruff check {SRC_AND_TEST_FILES}")

@task
def changelog(c):
    c.run("git-cliff -o CHANGELOG.md")
```

Now my teammate runs:

```bash
invoke test-unit
invoke format
invoke lint
invoke changelog
```

No “works on my machine” syndrome. No branching logic for OS detection. It just works.

## Why this change paid off

- I write a command once — it runs everywhere.
- No one needs to know shell quirks to contribute.
- Commands are short and consistent across the team.

Make is still a great tool. But for a Python project with a mixed-OS team, moving the build brain into Python was a quiet productivity win.