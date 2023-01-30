---
category: note
date: '2022-05-12'
modified: 2023-01-17
status: published
slug: git-delete-branch
tags: branch, delete, git
title: How to delete a Git branch locally and remotely?
---

## Introduction

Git is a powerful tool for version control, and it is widely used by developers to keep track of changes in their code. One of the key features of Git is the ability to create and manage branches, which allows developers to work on different versions of their code simultaneously. However, as the number of branches grows, it can become difficult to keep track of them all, and it may be necessary to delete some of them. In this article, we will explore how to delete a Git branch locally and remotely.

## Deleting a Branch Locally

To delete a branch locally in Git, you can use the `git branch -d` command followed by the name of the branch you wish to delete. For example, if you want to delete a branch named `localBranchName`, you would use the following command:


`git branch -d localBranchName`

It's important to note that this command will only delete the branch if it has already been fully merged into the main branch. If you want to force delete a branch that has not been fully merged, you can use the `-D` option instead of `-d`. For example:

`git branch -D localBranchName`

## Deleting a Branch Remotely

To delete a branch remotely in Git, you can use the `git push origin --delete` command followed by the name of the branch you wish to delete. For example, if you want to delete a branch named `remoteBranchName`, you would use the following command:

`git push origin --delete remoteBranchName`

It's also possible to delete branches that have been merged into the main branch using git command `git branch --merged` and `git branch -d branchName`. You can learn more about this by visiting [git_delete_branches_merged_into_main_branch](https://www.example.com/git_delete_branches_merged_into_main_branch)

## Helper - Listing Branches

To list all branches in your local repository, you can use the `git branch -a` command. This will show you both local and remote branches. To see only remote branches, you can use the `git branch -r` command.


## Reference - Git documentation
The official Git documentation on deleting branches can be found here: 
- [Git - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [Git - Remote Branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches)

This link provides detailed instructions and options for deleting branches in Git, including how to delete both local and remote branches, as well as how to force delete branches that have not been fully merged.

## Summary

In this article, we have covered how to delete a Git branch locally and remotely. Remember that it's important to be cautious when deleting branches, as this action cannot be undone. 

up:: [[MOC_Git]]