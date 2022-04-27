---
title: Zsh loop over files and run command
date: 2022-04-22
status: published
tags: zsh, loop
summary: 
slug: zsh-loop-over-files-and-run-command
category: note
citation_needed: false
todo: 
---

```sh
for file in ~/folder/*; gpg $file
```
from: https://quintussential.com/archive/2019/01/26/Looping-over-files-in-zsh/