---
Category: note
Date: '2022-05-12'
Modified: '2023-07-12'
Slug: bash-continue-yes-no
Status: published
Tags: bash, bash-continue-yes-no, continue
Title: Bash - Continue, Yes or No
---

```sh
do_backup=y                      # In batch mode => Default is Yes
[[ -t 0 ]] &&                     # If TTY => Prompt the question
read -r -n 1 -p $'\e[1;32m
Continue with backup? (Y/n)\e[0m ' do_backup  # Store the answer in $do_xxxx
if [[ $do_backup =~ ^(y|Y|)$ ]]  # Do if 'y' or 'Y' or empty
then
 echo "doing backup"
fi
```

up::[[MOC_Shell_Bash_Zsh]]
