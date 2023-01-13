---
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: bash-default-argument
tags: default-argument, bash
title: Bash - default argument for the script
---

See the example of `somecommand.sh`:

```bash
#!/usr/bin/env bash

ARG1=${1:-foo}
ARG2=${2:-bar}
ARG3=${3:-1}
ARG4=${4:-$(date)}

echo "$ARG1"
echo "$ARG2"
echo "$ARG3"
echo "$ARG4"
```

Here are some examples of how this works:

```
$ ./somecommand.sh
foo
bar
1
Thu Mar 29 10:03:20 ADT 2018

$ ./somecommand.sh ez
ez
bar
1
Thu Mar 29 10:03:40 ADT 2018
```

**Credits:** 
This solution is taken from [How to write a bash script that takes optional input arguments? - Stack Overflow](https://stackoverflow.com/a/33419280/3247880)

up::[[MOC_Shell_Bash_Zsh]]