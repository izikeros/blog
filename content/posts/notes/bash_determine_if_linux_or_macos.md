---
Category: note
Date: 2022-06-03
Modified: 2023-07-12
Slug: bash-determine-if-linux-or-macos
Status: published
Summary: Learn how to determine if a Bash script is running on Linux, macOS, or other systems using `uname` and conditional statements.
ai_summary: true
Tags:
  - bash
  - determine
  - Linux
  - macos
Title: Bash - Determine if Script Runs on Linux, macOS or Other System
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

if [ "$machine" == "Mac" ]; then
    # code for macOS platform        
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # code for GNU/Linux platform
fi
```

**Credits:**
The solution from [bash - How to check if running in Cygwin, Mac or Linux? - Stack Overflow](https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux)

up::[[MOC_Shell_Bash_Zsh]]
