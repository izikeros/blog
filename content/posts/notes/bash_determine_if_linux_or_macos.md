---
category: note
date: '2022-06-03'
modified: '2022-06-03'
status: published
slug: bash-determine-if-linux-or-macos
tags: bash, determine, Linux, macos
title: Bash - determine if script runs on Linux, macOS or other system
---

```sh
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
echo ${machine}
```

**Credits:**
The solution from [bash - How to check if running in Cygwin, Mac or Linux? - Stack Overflow](https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux)