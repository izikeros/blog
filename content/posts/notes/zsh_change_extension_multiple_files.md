---
title: Change extension for multiple files in Zsh
date: 2022-04-22
status: published
tags: zsh, shell, zmv
slug: change-extension-for-multiple-files-in-zsh
category: note
citation_needed: false
todo: 
---

In Zsh it is a bit easier to perform this because of using `zmv`. First, you need to load `zmv`. In zsh, run the following command once (or put them in your ~/.zshrc for the future):

```sh
autoload -U zmv
```

change all extensions from `.lis` to `.txt`
```sh
zmv '(*).lis' '$1.txt'
```

`^*.*` means all files except the ones matching `*.*`, it's a shortcut for `*~*.*` (both are zsh extensions to the traditional pattern syntax).

for all files set extension `.md`
```sh
zmv '^*.*' '$f.md'
```
Tip coming from: [unix.stackexchange](https://unix.stackexchange.com/a/68943). Credits to: [Gilles 'SO- stop being evil'](https://unix.stackexchange.com/users/885/gilles-so-stop-being-evil)