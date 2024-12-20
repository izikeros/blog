---
Title: Efficient Workflow for Reviewing Changes in Git before Pulling from Remote Branch
Slug: git-workflow-reviewing-changes-before-pulling-remote-branch
Date: 2023-06-20
Modified: 2024-10-31
Status: published
tags:
  - git
  - workflow
Category: note
todo: add links
---
## TLDR: Quick Git Command Reference

To quickly review changes before pulling, use this sequence of commands:

```bash
# 1. Fetch latest changes without merging
git fetch origin

# 2. See what's different
git log HEAD..origin/main    # Show commits you're missing
git diff HEAD..origin/main   # Show actual code changes
# or use Tig
tig HEAD..origin/main

# 3. If it looks good, pull changes
git pull origin main
```


## Introduction

When working with Git, it is essential to have a streamlined workflow that ensures you **review the changes made by others** before pulling them into your local branch. This practice helps **prevent conflicts** and ensures that your local repository remains in sync with the remote branch. In this blog post, we will outline a few simple steps to check the changes introduced by others in the remote branch before performing a `git pull`.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Introduction](#introduction)
  - [Step 1: Fetch Remote Changes](#step-1-fetch-remote-changes)
  - [Step 2: Inspect Remote Branch](#step-2-inspect-remote-branch)
  - [Step 3: Review Changes](#step-3-review-changes)
    - [Option 1: Using Git Diff](#option-1-using-git-diff)
    - [Option 2: Utilizing Visual Git Tools](#option-2-utilizing-visual-git-tools)
      - [tig](#tig)
    - [Option 3: Using PyCharm's Version Control Features](#option-3-using-pycharms-version-control-features)
      - [View Remote Changes](#view-remote-changes)
      - [Review Changes Using PyCharm's Diff Viewer](#review-changes-using-pycharms-diff-viewer)
      - [Interactive Review Features](#interactive-review-features)
      - [Resolve Conflicts in PyCharm](#resolve-conflicts-in-pycharm)
- [Step 4: Resolve Conflicts (if any)](#step-4-resolve-conflicts-if-any)
  - [Step 5: Pull Changes](#step-5-pull-changes)

<!-- /MarkdownTOC -->

<a id="step-1-fetch-remote-changes"></a>

### Step 1: Fetch Remote Changes

Before reviewing any changes, it is crucial to fetch the latest updates from the remote repository. This step ensures that your local repository has the most up-to-date information. To fetch changes, run the following command:

```sh
git fetch
```

This command retrieves all the latest changes from the remote repository without automatically merging them into your local branch.

<a id="step-2-inspect-remote-branch"></a>

### Step 2: Inspect Remote Branch

After fetching the remote changes, you can inspect the remote branch to see the modifications made by others. This step helps you understand the nature and scope of the changes before merging them into your branch. To view the remote branch, use the following command:

```sh
git log origin/branch-name
```

Replace `branch-name` with the name of the remote branch you want to review. This command displays a list of commits made to the remote branch, showing the commit hash, author, timestamp, and commit message.

<a id="step-3-review-changes"></a>

### Step 3: Review Changes

Now that you have a clear view of the commits in the remote branch, it's time to review the changes introduced. There are several ways to inspect the individual commits, depending on your preferred Git tooling. Here are a few common options:

#### Option 1: Using Git Diff

To review the changes introduced by a specific commit, you can use the `git diff` command. Run the following command, replacing `commit-hash` with the actual commit hash you want to inspect:

```sh
git diff commit-hash
```

This command displays a detailed diff of the changes made in that specific commit, allowing you to analyze the modifications line by line.

#### Option 2: Utilizing Visual Git Tools

If you prefer a more visual representation of changes, you can leverage Git GUI tools like [GitKraken](https://www.gitkraken.com/) (paid), [Sourcetree](https://www.sourcetreeapp.com/) (free, Atlassian Software License), [Git Cola](https://git-cola.github.io/) or [tig](https://jonas.github.io/tig/). These tools provide an intuitive interface that allows you to navigate through commits, inspect changes, and even visualize branching patterns.

##### tig

`tig test..master` - Show difference between two branches `test` and `master`

#### Option 3: Using PyCharm's Version Control Features

PyCharm provides robust Git integration that makes reviewing changes before pulling remarkably straightforward. Here's how to leverage PyCharm's GUI for this workflow:

##### View Remote Changes

1. Open the Git tool window by clicking `View → Tool Windows → Git` or pressing `Alt+9` (Windows/Linux) or `⌘9` (macOS)
2. Click the "Fetch" button in the Git tool window or press `Ctrl+T` (Windows/Linux) or `⌘T` (macOS) to fetch remote changes
3. In the Git tool window, expand the "Remote Branches" section to see incoming changes

##### Review Changes Using PyCharm's Diff Viewer

1. Right-click on the remote branch you want to review
2. Select `Compare with Current` to open PyCharm's diff viewer
3. The diff viewer will show:
   - Changed files in the left panel
   - Line-by-line differences in the main window
   - Color-coded modifications (green for additions, red for deletions)

##### Interactive Review Features

- Use the arrow keys or mouse wheel to scroll through changes
- Click the "Next Change" (↓) and "Previous Change" (↑) buttons to navigate between modifications
- Use the "Accept" (←) or "Reject" (→) arrows to selectively apply or discard changes
- Toggle between "Side-by-Side" and "Unified" diff views using the gear icon

##### Resolve Conflicts in PyCharm

If conflicts arise during the pull operation:

1. PyCharm will automatically detect conflicts and mark the files with a red exclamation mark
2. Double-click the conflicted file to open the merge tool
3. Use PyCharm's three-panel merge window to:
   - Accept changes from either side using the arrows
   - Manually edit the center panel for custom resolutions
   - Use the "Apply Non-Conflicting Changes" button for automatic resolution of non-conflicting parts

This visual approach using PyCharm's GUI tools can make the review process more intuitive, especially for developers who prefer IDE-integrated version control over command-line operations.

#### Option 4: Using VSCode's Git Integration

VSCode provides powerful built-in Git functionality that can be further enhanced with extensions. Here's how to effectively review changes using VSCode:

##### Built-in Git Features
1. Access the Source Control view by:
   - Clicking the Source Control icon in the Activity Bar (branches icon)
   - Using the shortcut `Ctrl+Shift+G` (Windows/Linux) or `⌘+Shift+G` (macOS)
2. Fetch changes using:
   - The refresh icon in the Source Control view
   - The Command Palette (`Ctrl+Shift+P` or `⌘+Shift+P`) and typing "Git: Fetch"

##### Review Changes Using VSCode's Built-in Diff Viewer
1. In the Source Control view:
   - Click on any modified file to see inline changes
   - Use the "Open Changes" icon (split window) to see side-by-side diff
2. Navigate changes using:
   - The change markers in the scroll bar
   - The "Next Change" (F7) and "Previous Change" (Shift+F7) commands
   - The arrows in the gutter to move between changes



<a id="step-4-resolve-conflicts-if-any"></a>

## Step 4: Resolve Conflicts (if any)

During your review, you may encounter conflicts between the changes made by others and your local modifications. Conflicts arise when Git cannot automatically merge two sets of changes. If conflicts occur, it is crucial to resolve them before pulling the changes into your branch.

To resolve conflicts, you can use Git's built-in merge tools or a visual Git tool like those mentioned earlier. These tools provide a side-by-side view of conflicting changes, enabling you to choose which modifications to keep and how to combine them effectively.

<a id="step-5-pull-changes"></a>

### Step 5: Pull Changes

After reviewing the changes, ensuring there are no conflicts or addressing any conflicts that arise, you can proceed with pulling the changes from the remote branch into your local branch. To pull the changes, use the following command:

```sh
git pull origin branch-name
```

Replace `branch-name` with the name of the remote branch from which you want to pull the changes. This command automatically merges the changes into your branch, keeping your local repository up to date.

### Extras 1: Enhanced Git Experience with VSCode Extensions

##### GitLens
GitLens is a powerful extension that supercharges VSCode's Git capabilities:

1. Install [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) from the Extensions Marketplace
2. Use key features:
   - **Current Line Blame**: See commit information inline
   - **File History**: Right-click a file and select "GitLens: View File History"
   - **Repository View**: Explore branches, tags, and commits in detail
   - **Revision Navigation**: Step through file history using the GitLens sidebar

```sh
code --install-extension eamodio.gitlens
```

##### Git Graph
[Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) provides a visual commit history:

1. Install [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) extension
2. Access features:
   - View the commit graph by clicking the "Git Graph" button in the Source Control view
   - Compare branches visually
   - Right-click commits for additional options
   - View detailed commit information

```sh
code --install-extension mhutchie.git-graph
```

##### Tips for Efficient Review in VSCode

1. **Keyboard Shortcuts**:
   - `Alt+←` / `Alt+→`: Navigate through edit history
   - `Ctrl+Shift+P`: Open Command Palette for Git commands
   - `Ctrl+K Ctrl+Alt+S`: Stage selected ranges

2. **Settings Customization**:
   ```json
   {
     "git.enableSmartCommit": true,
     "git.autofetch": true,
     "gitlens.hovers.currentLine.over": "line",
     "gitlens.codeLens.enabled": true
   }
   ```

- `"git.enableSmartCommit": true`
    - Enables "smart commit" functionality
    - When true, allows you to commit all changes when there are no staged changes
    - Saves time by skipping the staging step if you want to commit all modified files
    - Particularly useful for small, focused changes
- `"git.autofetch": true`
    - Automatically fetches changes from remote repositories
    - Runs in the background at regular intervals (default: every 3 minutes)
    - Keeps you informed about remote changes without manual fetching
    - Helps prevent merge conflicts by keeping you aware of upstream changes
- `"gitlens.hovers.currentLine.over": "line"`
    - Controls when the GitLens hover annotation appears
    - "line" setting shows git blame information when hovering over the current line
    - Alternatives include "annotation" (hover over the gutter blame annotation) or "window" (entire viewport)
    - Provides quick access to commit information without cluttering the interface
- `"gitlens.codeLens.enabled": true`
    - Enables GitLens CodeLens feature
    - Shows authorship information above functions and classes
    - Displays recent changes and number of authors
    - Makes it easy to track changes to specific code blocks

>To apply these settings:
>1. Open VSCode Settings (Ctrl+,)
>2. Click on the "Open Settings (JSON)" button in the top right
>3. Add these settings to your user or workspace settings
>4. Save the file to apply changes immediately

6. **Workspace Organization**:
   - Use the SCM view layout options to customize your review space
   - Toggle between inline and side-by-side diffs based on change complexity
   - Utilize the minimap for quick navigation through large files

This integrated approach using VSCode and its extensions provides a powerful environment for reviewing changes, with features that cater to both basic and advanced Git workflows. The visual tools and keyboard shortcuts make the review process more efficient and intuitive.

## Extras 2: Common Review Commands

```bash
# View specific file changes
git diff origin/main -- path/to/file

# See changed files list
git diff --stat origin/main

# Show last N commits
git log -n 5 origin/main

# See compact change summary
git whatchanged origin/main -n 5

# Check if pull will cause conflicts
git diff ...origin/main
```

Replace `main` with your branch name if different.

⚠️ If you spot problems:
```bash
# Abort pull if something looks wrong
git merge --abort

# Reset to previous state if already pulled
git reset --hard HEAD@{1}
```


**Edits:**

- 2024-03-06: Added sections on using PyCharm and VSCode features
- 2024-03-06: Added extras on vscode extensions and git commands for review