---
category: note
date: '2022-05-12'
status: published
slug: bash-base-name-without-extension
tags: base, basename, bash, extension, name
title: Bash base name (without extension)
---

## file base name (without extension)
```bash
i="movie.mp4"
echo ${basename ${i/.mp4}}
```


## Get the current directory name (without full path) in a Bash script

```bash
result=${PWD##*/}          # to assign to a variable

printf '%s\n' "${PWD##*/}" # to print to stdout
                           # ...more robust than echo for unusual names
                           #    (consider a directory named -e or -n)

printf '%q\n' "${PWD##*/}" # to print to stdout, quoted for use as shell input
                           # ...useful to make hidden characters readable.
```