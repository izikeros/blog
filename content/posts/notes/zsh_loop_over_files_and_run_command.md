---
Category: note
Date: 2022-04-22
Modified: 2023-07-12
Slug: zsh-loop-over-files-and-run-command
Status: published
Summary: A one-line Zsh for loop that runs a command on each file in a directory.
ai_summary: true
Tags:
  - zsh
  - loop
Title: ZSH - Loop Over Files and Run Command
citation_needed: false
---
up::[[MOC_Shell_Bash_Zsh]]

```sh
for file in ~/folder/*; gpg $file
```

from: <https://quintussential.com/archive/2019/01/26/Looping-over-files-in-zsh/>
