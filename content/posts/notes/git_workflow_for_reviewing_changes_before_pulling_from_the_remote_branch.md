---
Title: Efficient Workflow for Reviewing Changes in Git before Pulling from Remote Branch
Slug: git-workflow-reviewing-changes-before-pulling-remote-branch
Date: 2023-06-20
Modified: 2023-06-20
Status: published
Tags: git, workflow
Category: note
todo: add links
---


## Introduction

When working with Git, it is essential to have a streamlined workflow that ensures you **review the changes made by others** before pulling them into your local branch. This practice helps **prevent conflicts** and ensures that your local repository remains in sync with the remote branch. In this blog post, we will outline a few simple steps to check the changes introduced by others in the remote branch before performing a `git pull`.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Step 1: Fetch Remote Changes](#step-1-fetch-remote-changes)
- [Step 3: Review Changes](#step-3-review-changes)
- [Step 4: Resolve Conflicts \(if any\)](#step-4-resolve-conflicts-if-any)
- [Step 5: Pull Changes](#step-5-pull-changes)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="step-1-fetch-remote-changes"></a>

### Step 1: Fetch Remote Changes

Before reviewing any changes, it is crucial to fetch the latest updates from the remote repository. This step ensures that your local repository has the most up-to-date information. To fetch changes, run the following command:

```sh
git fetch
```

This command retrieves all the latest changes from the remote repository without automatically merging them into your local branch.

### Step 2: Inspect Remote Branch

After fetching the remote changes, you can inspect the remote branch to see the modifications made by others. This step helps you understand the nature and scope of the changes before merging them into your branch. To view the remote branch, use the following command:

```
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

If you prefer a more visual representation of changes, you can leverage Git GUI tools like GitKraken, Sourcetree, Git Cola or tig. These tools provide an intuitive interface that allows you to navigate through commits, inspect changes, and even visualize branching patterns.

##### tig

`tig test..master` - Show difference between two branches `test` and `master`

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

<a id="conclusion"></a>

## Conclusion

In this blog post, we discussed a streamlined workflow for reviewing changes in Git before pulling them from a remote branch. By following these steps, you can ensure that you have a clear understanding of the modifications introduced by others, address conflicts if necessary, and maintain a synchronized local repository. Adopting this workflow will help you avoid potential
