---
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: git-delete-branch
tags: branch, delete, git
title: How to delete a Git branch locally and remotely?
---

delete branch locally
```sh
git branch -d localBranchName
```
use `-D` to force removing not fully-merged branches

delete branch remotely
```sh
git push origin --delete remoteBranchName
```

see also: 
[[git_delete_branches_merged_into_main_branch]]

### Helper -  list branches

All branches
```
git branch -a
```

Remote branches
```
git branch -r
```

up:: [[MOC_git]]]