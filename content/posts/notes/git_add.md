---
Category: note
Date: '2021-10-12'
Modified: '2023-07-12'
Slug: git-add
Status: published
Summary: various options to stage git files with `git add` command
Tags: git
Title: Git Add - Stage Changes in Various Ways
citation_needed: false
---


- `git add -A` stages **all changes**
- `git add .` stages new files and modifications, **without deletions** (on the current directory and its subdirectories).
- `git add -u` stages modifications and deletions, **without new files**

With git 2.0 `git add <path>` is the same as `git add -A <path>`.

up:: [[MOC_Git]]]