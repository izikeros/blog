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

## Introduction

There is a moment when a project grows from a single-track workflow into something more complex. The codebase stays small, but you want to try a few big ideas at once. Or you want GitHub Copilot (or any AI coding agent) to attempt two different solutions while you continue working normally. One branch is not enough. Stashes are too messy. Full clones eat time and attention.

[Git worktrees](https://git-scm.com/docs/git-worktree) solve this elegantly. They let one repository produce several working directories, each on its own branch, all sharing the same underlying store. One directory becomes the human-edited version. Another becomes the AI sandbox. A third holds an alternative AI proposal. You compare the results side by side without the mental reset of switching branches.

This tutorial shows you how to build a multi-workflow setup using a simple Python mini-project. You will run two AI-assisted refactoring tasks: one small and one heavy. You will then evaluate them, compare results, validate correctness, and merge only the parts worth keeping.

## Starting Point: A Tiny Codebase

Assume we begin with a very small project containing one module called `stats.py`. It calculates a few simple statistics.

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

There is an obvious bug in `variance`. The right definition uses squared deviations from the mean.

```python
# Correct version of variance
def variance(values):
    m = average(values)
    return sum((v - m) ** 2 for v in values) / len(values)
```

This is our baseline. A candidate for small refactoring is the variance fix. A candidate for heavy refactoring is reorganising everything into a class-based structure or splitting the module into multiple files.

## Step 1: Create a Clean Main Worktree

You start in the main repository folder, checked out on `develop`. This is your everyday environment.

```bash
cd project
git status
```

Everything looks normal.

## Step 2: Prepare Worktrees for AI Workflows

Now create a branch exclusively for the small refactoring, and another branch to explore a heavy rewrite.

```bash
git worktree add ../refactor-small ai/refactor-small
git worktree add ../refactor-heavy ai/refactor-heavy
```

You now have three directories:

- `project/` for your normal coding
- `refactor-small/` for the AI to attempt precise, localised edits
- `refactor-heavy/` for a broad exploration of reorganising the project

Each is a full working directory with its own branch and commit history, but the `.git` data is shared. Switching happens simply by changing directories, not by resetting state.

## Step 3: Run the First Workflow – A Small AI Refactor

Go into the `refactor-small` directory and open your IDE.

Ask Copilot (or another model) to fix the variance implementation and streamline the small functions. Something like:

> Clean up this file. Fix the variance bug, add type hints, and make error handling more robust. Keep changes minimal.

Copilot should produce something along these lines:

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

Open the second worktree.

```bash
cd ../refactor-heavy
```

This time, ask your AI assistant:

> Rewrite this module using an object-oriented structure. Split statistics operations into separate classes if needed. Add validation. Keep the public API clear and ergonomic.

Expect a much bigger rewrite. Copilot might produce something like this:

```python
# stats/metrics.py after heavy refactor

class Stats:
    def __init__(self, values):
        if not values:
            raise ValueError("Values cannot be empty")
        self.values = list(values)

    def average(self):
        return sum(self.values) / len(self.values)

    def median(self):
        sorted_values = sorted(self.values)
        mid = len(sorted_values) // 2
        if len(sorted_values) % 2 == 0:
            return (sorted_values[mid - 1] + sorted_values[mid]) / 2
        return sorted_values[mid]

    def variance(self):
        m = self.average()
        return sum((v - m) ** 2 for v in self.values) / len(self.values)
```

This version creates a directory layout like:

```
stats/
    __init__.py
    metrics.py
```

Commit again:

```bash
git add .
git commit -m "Major rewrite: object-oriented Stats class with reorganized structure"
```

Now you have two valid, complete refactor attempts captured in versioned form, side by side, without any switching friction.

## Step 5: Validate and Compare the Results

Here is where multi-workflows shine. You can run tests, linters, or performance checks in each directory independently and in parallel.

Back in the main project, create a quick test script:

```python
# test_stats.py

from stats import average, median, variance

def test_all():
    values = [1, 2, 3, 4, 5]
    assert average(values) == 3
    assert median(values) == 3
    assert round(variance(values), 5) == 2.0
```

For the heavy version, you might need a different import:

```python
# test_stats_heavy.py

from stats.metrics import Stats

def test_stats_class():
    s = Stats([1, 2, 3, 4, 5])
    assert s.average() == 3
    assert s.median() == 3
    assert round(s.variance(), 5) == 2.0
```

Run tests separately in each worktree:

```bash
cd project
pytest -q

cd ../refactor-small
pytest -q

cd ../refactor-heavy
pytest -q
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
git switch develop
git merge ai/refactor-small
```

The heavy refactor might need additional time, iteration, or might stay as a long-running branch until more confidence is built.

## Step 7: Cleaning Up

After merging what you want, remove worktrees you no longer need.

```bash
git worktree remove ../refactor-small
git worktree remove ../refactor-heavy
```

If Git complains the directory still exists, delete it manually and run:

```bash
git worktree prune
```

## Why This Workflow Works So Well

This approach removes the friction of experimental coding. AI tools prefer entire files or folders as context, and they sometimes rewrite aggressively rather than patch small areas. Worktrees give them dedicated sandboxes, and they give you mental clarity: each branch corresponds to a purpose. You can compare outputs by simply opening two folders side by side instead of juggling switching commands that reset your IDE state.

Worktrees also encourage discipline. You evaluate AI-generated changes deliberately, not impulsively. You treat each branch as a self-contained proposal. This makes working with powerful automated tools safer, faster, and easier to reason about.

The biggest advantage is velocity without chaos: several workflows move forward independently, but none interfere with your main development branch. You keep the codebase clean, and you can run experiments all day without ever fearing that an agent will overwrite something you care about.

If you use AI in your everyday coding, this structure should become second nature. It transforms the way you evaluate ideas, especially when dealing with both small fixes and large rewrites.

## Extras


### Comparing Workflows with `git diff --no-index` and Practical Multi-Workflow Tips

At some point you want to know which variant actually performed better. Maybe the baseline is cleaner. Maybe the Copilot heavy-refactor got overly creative. A simple trick is to compare two worktrees without committing anything. This is where `git diff --no-index` feels almost unfair because it ignores Git’s object database and simply diffs two directories. Perfect for AI-driven experimentation.

You run this from anywhere, and Git treats both directories like normal folders.

```bash
git diff --no-index ../baseline ../agent-refactor
```

If you are inside `agent-refactor`, the paths look like this:

```bash
git diff --no-index . ../baseline
```

This gives you a raw diff across files regardless of whether they’re tracked in the same repo. The output is blunt, noisy, and brutally honest, which is exactly what you want when checking what an AI agent really did. When the diff is unreadable, that’s often a hint that the refactor mutated too much at once. In those cases, I sometimes do a narrower diff:

```bash
git diff --no-index ../baseline/path/to/module.py path/to/module.py
```

or even a directory-level diff to check how wide the blast radius went:

```bash
git diff --no-index ../baseline/src ../agent-refactor/src
```

### Using VS Code with Multiple Worktrees Without Losing Your Mind

Now comes the tricky part. Developers get confused in multi-worktree setups not because Git is hard, but because the editor happily opens whatever folder you point at and then people forget which workflow they’re editing. One tiny commit into the wrong branch and your careful separation collapses.

The easiest way to stay sane is to open each worktree as a separate VS Code window.

If you open the root project folder and start navigating into `.worktrees/...`, you’re setting yourself up for mistakes. Instead, open the worktree directory itself:

```bash
code ../baseline
code ../agent-refactor
```

This gives each workflow its own VS Code instance, with its own branch badge in the bottom-left status bar. You never want both instances to point at the same folder tree.

The moment you enter a file in the wrong window, you’ll see the branch indicator complaining. Git worktree integration in VS Code is surprisingly stable as long as each window corresponds to just one worktree.

### Committing From the VS Code UI to the Correct Branch

Another easy place to make mistakes is committing. VS Code’s SCM panel will happily stage and commit changes, but only if the workspace folder is the actual worktree root.

If the root folder in your VS Code window is `../agent-refactor`, then the SCM panel will commit to the branch connected to that worktree. This is the safe path.

If, however, you open a parent directory and the worktree folder is nested inside, VS Code gets confused because it sees multiple `.git` locations. In that setup committing is dangerous. That’s the exact scenario where you accidentally commit to the wrong branch.

So the rule of thumb is very blunt: always open the worktree root as your workspace root, never a parent folder.

One more subtle point. When you use the VS Code "Source Control" view, it shows untracked files, staged files, everything. But the "branch" name in the status bar is the ultimate truth. If your window says "main" and you think you're inside an experimental worktree, stop immediately and re-open the correct folder.

### How to Inspect Which Workflow You Are In

There are several quick signals you can build into your workflow.

You can add a small file at the root of each worktree:

```bash
echo "WORKFLOW=baseline" > workflow.tag
echo "WORKFLOW=agent-refactor" > workflow.tag
```

This is not tracked by Git if you put it in `.git/info/exclude`. When this file is present, VS Code’s quick search reveals it instantly. The visible presence of the tag helps when you jump between windows.

You can also put a different color theme per workflow window. For example, baseline = light theme, refactor = dark theme. It sounds silly, but it prevents accidental edits.

Another simple method is to customize the terminal prompt inside each window:

```bash
# In baseline worktree
export PS1="[baseline] $PS1"
# In agent-refactor
export PS1="[refactor] $PS1"
```

Now your integrated terminal reminds you where you are every time you run a command.

### A Section for Power Users

AI-assisted multi-workflows shine even more when you enable some advanced tricks.

- Run benchmark scripts separately in each worktree. A fast benchmark runner in `baseline` and then the same in `agent-refactor` will give you meaningful signals about performance regressions.
    
- Automate comparison with a one-liner script:
    

```bash
#!/bin/bash
git diff --no-index ../baseline ../agent-refactor | code -
```

This opens a diff buffer in VS Code directly. It feels like magic.

- You can use the GitLens extension. It understands worktrees and shows you exactly which branch belongs to which folder.
    
- Test AI agents in parallel by launching each agent process pointing at a different worktree. This isolates their writes and makes their behaviors easier to compare. When the AI agent misbehaves, simply drop that worktree.
