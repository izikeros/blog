---
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: awk
tags: awk, gawk, mawk, snippet, software/alternatives, Linux
title: Awk
---

## Validate CSV number of fields:
```sh
awk 'BEGIN{FS=",";x=1}{x++}NF!=3{print "wrong number of fields:" NF " in line:" x; exit}' valid.csv
```

test data:
```sh
echo "a,b,c\n1,2,3\n11,12,13,14\n21,22,23" > invalid.csv
echo "a,b,c\n1,2,3\n11,12,13\n21,22,23" > valid.csv
```


Other scripts (inspiration)
```sh
awk 'BEGIN{FS=OFS=","} NF!=20{print "not enough fields"; exit}!($1~/^[0-9]$/) {print "1st field invalid"; exit}' file.csv
```


```sh
awk 'BEGIN{FS=","}!n{n=NF}n!=NF{failed=1;exit}END{exit !failed}'
```

Skip the first row, print comma separated
```sh
awk -F "^" 'NR>1 {print $1", "$2}' xaa
```


## display 80 columns from the first two rows
```sh
gawk -F',' 'NR<10 {for (i=1;i<=80;i++){printf "%d ", $i}print""}' file.txt
```

## transpose:
https://stackoverflow.com/questions/1729824/an-efficient-way-to-transpose-a-file-in-bash

## sum column
assuming column delimiter comma (`,`) and summing values in column #57
```sh
awk -F',' '{sum+=$57;} END{print sum;}' file.txt
```

## sum along rows
```sh
awk -F ',' '{sum=0; for (i=1; i<=NF; i++) { sum+= $i } print sum}' file.txt
```

> **NOTE:** 
> When the processing speed is critical, in many cases it is possible to replace AWK with a faster alternative MAWK - as in the famous example: [Command-line Tools can be 235x Faster than your Hadoop Cluster - Adam Drake](https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html) However, there is a warning that MAWK contains some bugs (not sure if fixed at the moment of writing).


## References
-   [Why Learn AWK?](https://blog.jpalardy.com/posts/why-learn-awk/) – great article by Jonathan Palardy conveying similar ideas
-   [Python vs. awk](https://pmitev.github.io/to-awk-or-not/Python_vs_awk/) – a remarkable case of replacing a 50 line Python script with 5 lines of AWK
-   [The AWK Programming Language](https://archive.org/download/pdfy-MgN0H1joIoDVoIC7/The_AWK_Programming_Language.pdf) – the book by the AWK creators, a must-read!