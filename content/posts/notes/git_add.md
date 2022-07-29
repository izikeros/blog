---
title: Git add - stage changes in various ways
date: 2021-10-12
status: published
tags: git
summary: various options to stage git files with `git add` command
slug: git-add
category: note
citation_needed: false
---

- `git add -A` stages **all changes**
- `git add .` stages new files and modifications, **without deletions** (on the current directory and its subdirectories).
- `git add -u` stages modifications and deletions, **without new files**

With git 2.0 `git add <path>` is the same as `git add -A <path>`.