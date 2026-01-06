---
Category: note
Date: 2022-05-12
Modified: 2023-07-12
Slug: bash-base-name-without-extension
Status: published
Summary: Learn how to extract file base names without extensions and get the current directory name in Bash scripts using built-in commands.
ai_summary: true
Tags:
  - base
  - basename
  - bash
  - extension
  - name
  - bash/basename
Title: Bash - File Base Name (Without Extension)
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
