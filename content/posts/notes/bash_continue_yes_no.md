---
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: bash-continue-yes-no
tags: bash, bash-continue-yes-no, continue
title: Bash - continue: yes or no
---

```sh
do_backup=y                      # In batch mode => Default is Yes
[[ -t 0 ]] &&                  	  # If TTY => Prompt the question
read -r -n 1 -p $'\e[1;32m
Continue with backup? (Y/n)\e[0m ' do_backup  # Store the answer in $do_xxxx
if [[ $do_backup =~ ^(y|Y|)$ ]]  # Do if 'y' or 'Y' or empty
then
	echo "doing backup"
fi
```
gist