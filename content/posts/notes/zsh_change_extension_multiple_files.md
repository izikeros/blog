---
Category: note
Date: '2022-04-22'
Modified: '2023-07-12'
Slug: change-extension-for-multiple-files-in-zsh
Status: published
Tags: zsh, shell, zmv
Title: Change Extension for Multiple Files in ZSH
citation_needed: false
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

X::[[MOC_Shell_Bash_Zsh]]