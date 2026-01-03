---
Title: Working Faster with Git Worktrees and AI-Based Multi-Workflow Development
Slug: git-worktrees-ai-multi-workflows
Date: 2025-11-28
Modified: 2025-11-28
Status: published
Tags: git, worktrees, ai-coding, refactoring, workflows, vscode, productivity
Category: note
summary: A practical, hands-on guide to turning a single codebase into a multi-workflow environment using Git worktrees, VS Code, and AI coding assistants. The tutorial shows how to isolate experiments, compare results, and speed up refactoring work with agents and Copilot.
---

_A practical step-by-step tutorial using Git worktrees, small and large refactorings, and GitHub Copilot._

## Prerequisites

Before starting, ensure you have:

- **Git 2.5+** (check with `git --version`)
- **Python 3.8+** and pip
- **VS Code** (optional but recommended)
- **pytest** (`pip install pytest`)
- **GitHub Copilot** or another AI coding assistant
- Basic familiarity with Git branching and command-line operations

## Introduction

There is a moment when a project grows from a single-track workflow into something more complex. The codebase stays small, but you want to try a few big ideas at once. Or you want GitHub Copilot (or any AI coding agent) to attempt two different solutions while you continue working normally. One branch is not enough. Stashes are too messy. Full clones eat time and attention.

[Git worktrees](https://git-scm.com/docs/git-worktree) solve this elegantly. They let one repository produce several working directories, each on its own branch, all sharing the same underlying store. One directory becomes the human-edited version. Another becomes the AI sandbox. A third holds an alternative AI proposal. You compare the results side by side without the mental reset of switching branches.

This tutorial shows you how to build a multi-workflow setup using a simple Python mini-project. You will run two AI-assisted refactoring tasks: one small and one heavy. You will then evaluate them, compare results, validate correctness, and merge only the parts worth keeping.

## Starting Point: A Tiny Codebase

### Initial Project Setup

First, create a fresh repository:

```bash
mkdir project
cd project
git init
git checkout -b develop
```

Create a file called `stats.py` with some simple statistics functions:

```python
# stats.py

def average(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    mid = len(sorted_values) // 2
    if len(sorted_values) % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]

def variance(values):
    # Wrong: variance uses mean, not sum of squared values directly
    return sum(v * v for v in values) / len(values)
```

Commit this baseline:

```bash
git add stats.py
git commit -m "Initial commit with stats module"
```

There is an obvious bug in `variance`. The right definition uses squared deviations from the mean.

```python
# Correct version of variance (population variance)
def variance(values):
    m = average(values)
    return sum((v - m) ** 2 for v in values) / len(values)
```

Note: This calculates population variance (dividing by N). Sample variance would use N-1.

This is our baseline. A candidate for small refactoring is the variance fix. A candidate for heavy refactoring is reorganising everything into a class-based structure or splitting the module into multiple files.

## Step 1: Create a Clean Main Worktree

You start in the main repository folder, checked out on `develop`. This is your everyday environment.

```bash
cd project
git status
```

Everything looks normal.

## Step 2: Prepare Worktrees for AI Workflows

Now create worktrees with new branches for experimentation. The `git worktree add` command creates both the branch and the working directory in one step:

```bash
git worktree add -b ai/refactor-small ../refactor-small
git worktree add -b ai/refactor-heavy ../refactor-heavy
```

Your directory structure now looks like:

```
parent-directory/
├── project/           # main worktree (develop branch)
│   └── stats.py
├── refactor-small/    # worktree (ai/refactor-small branch)
│   └── stats.py
└── refactor-heavy/    # worktree (ai/refactor-heavy branch)
    └── stats.py
```

You now have three directories:

- `project/` for your normal coding
- `refactor-small/` for the AI to attempt precise, localised edits
- `refactor-heavy/` for a broad exploration of reorganising the project

You can verify existing workflows with:

```bash
git worktree list
```

Each is a full working directory with its own branch and commit history, but the `.git` data is shared. Switching happens simply by changing directories, not by resetting state.

## Step 3: Run the First Workflow – A Small AI Refactor

Go into the `refactor-small` directory and open your IDE.

```bash
cd ../refactor-small
code .
```

Open `stats.py` and use **GitHub Copilot Chat** to fix the variance implementation. Exemplary prompt:

> Clean up this file. Fix the variance bug, add type hints, and make error handling more robust. Keep changes minimal.

Review the AI's suggestions carefully. Accept changes that look correct. The result should be something like:

```python
# stats.py after small refactor

from typing import Iterable

def average(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Cannot compute average of empty list")
    return sum(values) / len(values)

def median(values: Iterable[float]) -> float:
    values = sorted(values)
    if not values:
        raise ValueError("Cannot compute median of empty list")
    mid = len(values) // 2
    if len(values) % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]

def variance(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Cannot compute variance of empty list")
    m = average(values)
    return sum((v - m) ** 2 for v in values) / len(values)
```

Commit the result.

```bash
git add stats.py
git commit -m "Small refactor: fix variance, add type hints, add basic validation"
```

Nothing touches the `project/` folder. No stashes. No switching.

## Step 4: Run the Heavy Workflow – A Large-Scale AI Refactor

Open the second worktree in a **separate VS Code window**.

```bash
cd ../refactor-heavy
code .
```

This time, ask your AI assistant:

> Rewrite this module using an object-oriented structure. Split statistics operations into separate classes if needed. Add validation. Keep the public API clear and ergonomic. Keep the code in the same file do not split into multiple files.

Expect a much bigger rewrite. Verify changes and commit again:

```bash
git add stats.py
git commit -m "Major rewrite: object-oriented Stats class with reorganized structure"
```

Now you have two valid, complete refactor attempts captured in versioned form, side by side, without any switching friction.

## Step 5: Validate and Compare the Results

Here is where multi-workflows shine. You can run tests, linters, or performance checks in each directory independently and in parallel.

Back in the main project directory, create a test script:

```python
# test_stats.py (in project/ and refactor-small/)

from stats import average, median, variance

def test_all():
    values = [1, 2, 3, 4, 5]
    assert average(values) == 3
    assert median(values) == 3
    assert round(variance(values), 5) == 2.0

if __name__ == "__main__":
    test_all()
    print("✓ All tests passed")
```

Copy this file to both worktrees. For the heavy version, create a different test:

```python
# test_stats.py (in refactor-heavy/)

from stats import Stats

def test_stats_class():
    s = Stats([1, 2, 3, 4, 5])
    assert s.average() == 3
    assert s.median() == 3
    assert round(s.variance(), 5) == 2.0

if __name__ == "__main__":
    test_stats_class()
    print("All tests passed")
```

Run tests separately in each worktree:

```bash
cd project
python test_stats.py
# Output: All tests passed

cd ../refactor-small
python test_stats.py
# Output: All tests passed

cd ../refactor-heavy
python test_stats.py
# Output: All tests passed
```

You get independent validation. If the heavy refactor has bugs, you know immediately without polluting the main line of work.

## Step 6: Decide What to Merge

You now have three evolving branches:

- `develop` with your original code
- `ai/refactor-small` with a careful, stable refactor
- `ai/refactor-heavy` with a more ambitious rewrite

Decision time usually involves:

- Code clarity
- Compatibility with existing imports
- Test coverage
- Future extensibility
- Performance

For many teams, the small refactor becomes a straightforward merge:

```bash
cd ../project  # Return to main worktree
git switch develop
git merge ai/refactor-small
# Output: Fast-forward or Merge made by the 'recursive' strategy.
```


After merging, run tests again to ensure everything works:

```bash
python test_stats.py
```

The heavy refactor might need additional time, iteration, or might stay as a long-running branch until more confidence is built. You can keep that worktree around for continued experimentation.

## Step 7: Cleaning Up

After merging what you want, remove worktrees you no longer need.

```bash
git worktree remove ../refactor-small
```

For branches you want to keep but not actively work on:

```bash
# Archive the heavy refactor branch for future reference
git branch --move ai/refactor-heavy archive/refactor-heavy-2025-12
git worktree remove ../refactor-heavy
```

Or delete the branch entirely if you don't need it:

```bash
git worktree remove ../refactor-heavy
git branch -D ai/refactor-heavy
```

If Git complains the directory still exists, delete it manually and run:

```bash
rm -rf ../refactor-heavy
git worktree prune
```

List remaining worktrees:

```bash
git worktree list
```

## Why This Workflow Works So Well

This approach removes the friction of experimental coding. AI tools prefer entire files or folders as context, and they sometimes rewrite aggressively rather than patch small areas. Worktrees give them dedicated sandboxes, and they give you mental clarity: each branch corresponds to a purpose. You can compare outputs by simply opening two folders side by side instead of juggling switching commands that reset your IDE state.

Worktrees also encourage discipline. You evaluate AI-generated changes deliberately, not impulsively. You treat each branch as a self-contained proposal. This makes working with powerful automated tools safer, faster, and easier to reason about.

The biggest advantage is velocity without chaos: several workflows move forward independently, but none interfere with your main development branch. You keep the codebase clean, and you can run experiments all day without ever fearing that an agent will overwrite something you care about.

If you use AI in your everyday coding, this structure should become second nature. It transforms the way you evaluate ideas, especially when dealing with both small fixes and large rewrites.

## Troubleshooting Common Issues

**Problem**: "fatal: 'ai/refactor-small' is already checked out at..."  
**Solution**: You can't check out the same branch in multiple worktrees. Use different branch names.

**Problem**: Changes appear in the wrong worktree  
**Solution**: Check which directory you're in with `pwd`. Verify the branch with `git branch --show-current`.

**Problem**: VS Code commits to wrong branch  
**Solution**: Always open the worktree directory as the workspace root, not a parent folder. Check the branch indicator in the bottom-left corner.

**Problem**: Tests fail after AI refactor  
**Solution**: Review AI changes line-by-line. AI tools sometimes introduce subtle bugs. Use `git diff` to see exactly what changed.

**Problem**: Can't delete worktree  
**Solution**: Close all editors and terminals in that worktree, then use `git worktree remove --force` if needed.

## Extras

```

### Using VS Code with Multiple Worktrees Without Losing Your Mind

Now comes the tricky part. Developers get confused in multi-worktree setups not because Git is hard, but because the editor happily opens whatever folder you point at and then people forget which workflow they’re editing. One tiny commit into the wrong branch and your careful separation collapses.

The easiest way to stay sane is to open each worktree as a separate VS Code window.

If you open the root project folder and start navigating into `.worktrees/...`, you’re setting yourself up for mistakes. Instead, open the worktree directory itself:

```bash
code ../project
code ../refactor-small
```

This gives each workflow its own VS Code instance, with its own branch badge in the bottom-left status bar. You never want both instances to point at the same folder tree.

The moment you enter a file in the wrong window, you’ll see the branch indicator complaining. Git worktree integration in VS Code is surprisingly stable as long as each window corresponds to just one worktree.
