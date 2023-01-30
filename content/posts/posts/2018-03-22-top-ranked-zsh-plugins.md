---
Title: Top popular Zsh plugins on GitHub
Slug: top-popular-zsh-plugins-on-github
Date: 2018-03-22
modified: 2022-09-01
Start: 2018-03-22
Tags: zsh, scrapping, python, Linux
Category: Linux
Image: images/zsh/inside-work-tree.jpg
Summary: There is an exhaustive but curated list of Zsh plugins posted on GitHub project Awesome Zsh plugins. You can find there 800+ links to plugins, themes and Zsh plugin managers/frameworks. Even though it is a collection of awesome stuff the number is a bit high get orientation which plugins gained already good reputation from Zsh users community. In this post I will identify most popular plugins - those which have the highest number of stars.
Status: published
---

> **NOTE:** This article was written in 2018, for a more recent version of the ranking see: [2021](../top-popular-zsh-plugins-on-github-2021/). 
> There is a serie of articles dedicated to Zsh plugins: [2018](../top-popular-zsh-plugins-on-github/), [2019](../top-popular-zsh-plugins-on-github-2019/), [2021](../top-popular-zsh-plugins-on-github-2021/)

On the GitHub project [Awesome Zsh plugins](https://github.com/unixorn/awesome-zsh-plugins) you can find 800+ links to plugins, themes, and Zsh plugin managers/frameworks. Even though it is a collection of awesome stuff the number is a bit high get orientation which plugins gained already good reputation from the Zsh users community. This post aims at identifying the most popular plugins where popularity is measured by the number of stars that GitHub users added to the given plugin. For clarity, I will focus here only on plugins excluding frameworks and themes that are also listed on "Awesome Zsh plugins" website.

# What are Github stars?

Stars is the way how users can 'bookmark' projects - this can serve as an indication for others that a project successfully grabbed someone's attention. The `stargazers` statistics are available via [GithubAPI](https://developer.github.com/v4/)

# Top 20 most popular plugins as of March 2018

link                                                                               | description                                                                                                                                            | stars
------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -----
[autojump](https://github.com/wting/autojump)                                         | A cd command that learns - easily navigate directories from the command line. Install autojump-zsh for best results.                                   | 6524
[syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)           | Add syntax highlighting to your Zsh. Make sure you load this _before_ zsh-users/zsh-history-substring-search or they will both break.                  | 4851
[autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)                   | Fish-like fast/unobtrusive autosuggestions for Zsh.                                                                          | 4836
[blackbox](https://github.com/StackExchange/blackbox)                                 | Stack Exchange's toolkit for storing keys/credentials securely in a git repository.                                                                    | 4098
[git-flow-completion](https://github.com/bobthecow/git-flow-completion)               | Zsh completion support for git-flow.                                                                                                                   | 2031
[zsh-completions](https://github.com/zsh-users/zsh-completions)                       | A collection of extra completions for Zsh.                                                                                                             | 2003
[ansiweather](https://github.com/fcambus/ansiweather)                                 | Weather in your terminal, with ANSI colors and Unicode symbols.                                                                                        | 1342
[k](https://github.com/rimraf/k)                                                      | Directory listings for Zsh with git features.                                                                                                          | 898
[enhancd](https://github.com/b4b4r07/enhancd)                                         | A simple tool that provides enhanced `cd` command.                                                                                                     | 826
[git-secret](https://github.com/sobolevn/git-secret)                                  | A bash tool to store your private data inside a git repository.                                                                                        | 823
[history-substring-search](https://github.com/zsh-users/zsh-history-substring-search) | Needs to be loaded after zsh-syntax-highlighting, or they'll both break. You'll also need to bind keys to its functions, details are in the README.md. | 704
[sysadmin-util](https://github.com/skx/sysadmin-util)                                 | Steve Kemp's collection of tool scripts for sysadmins.                                                                                                 | 473
[histdb](https://github.com/larkery/zsh-histdb)                                       | Stores your history in an SQLite database.                                                                                                             | 426
[nvm](https://github.com/lukechilds/zsh-nvm)                                          | Zsh plugin for installing, updating, and loading nvm.                                                                                                  | 421
[zaw](https://github.com/zsh-users/zaw)                                               | Zsh anything.el-like widget.                                                                                                                           | 402
[gradle-completion](https://github.com/eriwen/gradle-completion)                      | Bash and Zsh completion support for gradle.                                                                                                            | 362

Below you can find a short description of the 10 most popular plugins

## 1. [autojump](https://github.com/wting/autojump)

autojump is a faster way to navigate your filesystem. It works by maintaining a database of the directories you use the most from the command line. Directories must be visited first before they can be jumped to. It can be an alternative for [z](https://github.com/rupa/z) or [fasd](https://github.com/clvv/fasd)

## 2. [syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

This package provides Fish shell-like syntax highlighting for the Zsh. It enables highlighting of commands whilst they are typed at a Zsh prompt into an interactive terminal. This helps in reviewing commands before running them, particularly in catching syntax errors.
Some examples:

Before: ![Screenshot #1.1](https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/images/before1-smaller.png)
<br>
After: ![Screenshot #1.2](https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/images/after1-smaller.png)

Before: ![Screenshot #3.1](https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/images/before3-smaller.png)
<br>
After: ![Screenshot #3.2](https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/images/after3-smaller.png)

## 3. [autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

This package provides Fish-like fast/unobtrusive autosuggestions for Zsh. It suggests commands as you type, based on command history.
Example:
<a href="https://asciinema.org/a/37390" target="_blank"><img src="https://asciinema.org/a/37390.png" width="400" /></a>

## 4. [blackbox](https://github.com/StackExchange/blackbox)

This package allows to safely store secrets in a VCS repo (i.e. Git, Mercurial, Subversion, or Perforce). These commands make it easy for you to Gnu Privacy Guard (GPG) to encrypt specific files in a repo, so they are "encrypted at rest" in your repository. However, the scripts make it easy to decrypt them when you need to view or edit them and decrypt them for use in production. Originally written for Puppet, BlackBox now works with any Git or Mercurial repository.

## 5. [git-flow-completion](https://github.com/bobthecow/git-flow-completion)

Bash, Zsh, and Fish completion support for [git-flow](http://github.com/nvie/gitflow).

This package provides support for completing:

* git-flow init and version
* feature, hotfix, and release branches
* remote feature, hotfix, and release branch names

## 6. [zsh-completions](https://github.com/zsh-users/zsh-completions)
This project aims at gathering/develop new completion scripts that are not available in Zsh yet.
Demo:

![zsh-completions-demo](https://raw.githubusercontent.com/supercrabtree/k/gh-pages/inside-work-tree.jpg)

## 7. [ansiweather](https://github.com/fcambus/ansiweather)

AnsiWeather is a Shell script for displaying the current weather conditions
in your terminal, with support for ANSI colors and Unicode symbols.

![AnsiWeather Screenshot](https://camo.githubusercontent.com/3e34f3781bf3109aa757104c8fa39c8e3ee95675/68747470733a2f2f7777772e63616d6275732e6e65742f66696c65732f616e7369776561746865722f616e7369776561746865722e706e67)

Weather data comes from the `OpenWeatherMap` free weather API.

## 8. [k](https://github.com/rimraf/k)

k is a Zsh script / plugin to make directory listings more readable, adding a bit of color and some git status information on files and directories.
![k](https://raw.githubusercontent.com/supercrabtree/k/gh-pages/inside-work-tree.jpg)

## 9. [enhancd](https://github.com/b4b4r07/enhancd)

The new `cd` command called "enhancd" enhanced the flexibility and usability for a user. enhancd will memorize all directories visited by a user and use it for the pathname resolution. If the log of enhancd has more than one directory path with the same name, enhancd will pass the candidate directories list to the filter within the `ENHANCD_FILTER` environment variable in order to narrow it down to one directory.

Thanks to this mechanism, the users can intuitively and easily change the directory they want to go to.

![enhancd-demo](https://raw.githubusercontent.com/b4b4r07/screenshots/master/enhancd/demo.gif)

## 10. [git-secret](https://github.com/sobolevn/git-secret)

`git-secret` is a bash tool to store your private data inside a git repo. It encrypts data, using `gpg`, the tracked files with the public keys of all the users that you trust. So every one of them can decrypt these files using only their personal secret key. Usage of private-public makes it easier for everyone to manage access rights. There are no passwords that change. When someone is out - just delete their public key, re-encrypt the files, and they won’t be able to decrypt secrets anymore.
[![git-secret terminal preview](https://asciinema.org/a/41811.png)](https://asciinema.org/a/41811?autoplay=1)

On the list there are 300+ projects that are falling into the scope of this research, you can get the complete dataset by downloading this CSV file: [CSV](/downloads/180322_results_sorted.csv).



*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
