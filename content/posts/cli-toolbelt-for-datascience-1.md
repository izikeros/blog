---
title: Data Science Command line Tools
started: 2019-07-04
date: 2019-08-23
tags: machine learning, linux
category: Posts
image: /images/head/cli_tools.jpg
status: published
summary: 
---

There are plenty of tools designed to ease life of Data Scientist. In this group, the special place has tools that are used from command line. They are special because are available for most operating systems and are designed with Unix philosophy in mind: they do one thing extremely well, they can be chained creating convenient workflows. This post 



![Diagram of cli tools for data science](/images/cli_tools_1/cli_tools.png)

## Textutils from GNU Coreutils
From my experience, I have benefit most from mastering the GNU Coreutils. This is the collection of: shellutils, fileutils and textutils - and in this post I will be discussing the latter one. 

*Table 1. Textutils - text processing tools, part of GNU Coreutils*

|         command | description                                                  |
| --------------: | ------------------------------------------------------------ |
|             cat | merge, print files to standard output                        |
|            comm | compare sorted files line by line; can find differences, unique lines for each compared files |
|          csplit | divide files into parts using context                        |
|             cut | remove sections from each line in file                       |
| expand/unexpand | convert tab into spaces / convert spaces to tabs             |
|             fmt | Simple text formatter                                        |
|            fold | fold each input line to fit given line length                |
|  head/tail/shuf | display starting lines of file / display file ending lines/get random lines from file |
|            join | join lines from two files on common fields                   |
|              nl | line numbering                                               |
|           paste | merge lines                                                  |
|            sort | sort lines of text file                                      |
|           split | divide file into parts                                       |
|             tac | merge, print in reverse order lines of files to standard output |
|                 |                                                              |
|              tr | translate or remove characters                               |
|            uniq | Remove duplicated lines from file                            |
|              wc | display number of characters, words and lines of given file  |

I will give a few examples of commands I use most often or ones that are exceptionally useful.

### comm
The `comm` command is very handy when comes to compare lists stored in separate files. For example you have list of samples used for experiment #1 in one file and list of samples used in experiment #2 in another file.
The `comm` command takes sorted files as input and calculate unique lines for FILE1 and for FILE2 and the result is represented respectively as `column 1` and `column 2`. Having unique lines in column 1 and 2, set of lines that appear in both files is calculated and result is represented by column 3. 


Columns description for `comm`:

|1|2|3|
|-|-|-|
|lines unique to FILE1|lines unique to FILE1|lines that appear in both files|

Having three columns calculated we can now suppress lines that appears in given column in order to get lines that fulfill desired condition.

Meaning of the numbers used as `comm` parameters:

* `-1`     suppress column 1 (lines unique to FILE1)
* `-2`     suppress column 2 (lines unique to FILE2)
* `-3`     suppress column 3 (lines that appear in both files)

See below three typical usages of `comm`:
```sh
# find lines only in file1
comm -23 file1 file2

# find lines only in file2
comm -13 file1 file2

# find lines common to both files
comm -12 file1 file2
```

### head
By default, `head` prints  the first 10 lines of each file provided as argument to standard output.  With more than one file, precede each with a header giving the file name. You can control how many lines is displayed with option `-n`:
```sh
head -n5 file.txt
```

You can also print all but last N lines by adding `-` sign. For example in order to have all lines but last one:
```sh
head -n -1 file.txt
```

### shuf
To quickly inspect content of dataset in text file you can use `head` which shows some filest lines of the file. If you would like to have more representative example of the content of the file, you can take random sample of lines from file with `shuf`:
```sh
shuf -n 5 file.txt
```

### sort
Here are options I often use for sort and unique operation:
```
-b, --ignore-leading-blanks
              ignore leading blanks

-u, --unique
              with -c, check for strict ordering; without -c, output only the first  of  an equal run

-f, --ignore-case
              fold lower case to upper case characters

-i, --ignore-nonprinting
              consider only printable characters
```

```sh
sort -bufi data.csv
```
### split
Sometimes there is a need to split dataset to smaller parts. E.g. when processing large files you can be hit by memory limitations or you want to speed up processing using parallel computing. To split file into N parts with equal number of lines, use: 
```sh
split -n l/N data.csv
```
e.g.
```sh
split -n l/10 data.csv
```
This will create serie of files named: `xaa, xab, xac,...`. The default pattern of  `split` for file naming is PREFIXaa, PREFIXab,...; default PREFIX is `x`. You can provide your own prefix e.g.
### tail
```sh
split l/10 data.csv part_
```
and this will result in having files `part_aa, part_ab,...`.  Suffixes doesn't have to be alphabetical: can be numeric (use switch `-d`) or even hex (use switch `-x`). What is particularly usefull - prefixes can be used to save resulting files in given location. Let's take an example `dataset.csv` file located in data directory, we want to split this file into parts and save results in `parts` directory as shown below:

```text
data
├── dataset.csv
└── parts
    ├── xaa
    ├── xab
    └── xac
```
To achieve this create parts directory and modify the prefix to `parts/x`:
```sh
split l/3 data.csv parts/x
```

Skipping header row can be done with tail
```
tail -n +2 file.txt
```
This syntax with usage of `+` sign might require explanation. Here is excerpt from the man page: 
> -n N means output the last N lines, instead of the last 10; or use +N to output lines starting with the Nth.

The usage of `+` sign can be considered as inverting the argument and telling tail to print everything but the first x-1 lines. Note that `tail -n +1` would print the whole file, `tail -n +2` everything but the first line, etc.

the alternative solution involves `sed`:
```sh
sed 1d file.txt
```

### uniq
used often with `sort` in a way:
```
cat file.txt | sort | uniq
```
If there are no special circumstances `cat` should be avoided:
```sh
sort file.txt | uniq
```
Moreover, `sort` has option `-u` which stands for *unique*. Therefore, to have unique lines it is sufficient to use:
```
sort -u file.txt
```

### wc
- count lines
```
wc -l data.csv
```
- count lines in multiple files at once
```
wc -l *.csv
```

For special task - counting lines in very large files one can consider using replacement: [Super-Fast Multi-Threaded Line Counter](https://github.com/crioux/turbo-linecount)
