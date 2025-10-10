---
Title: Store Output of the Command Into Array in Bash
Slug: store-output-of-the-command-into-array-in-bash
Date: 2023-11-13
Modified: 2023-11-13
Status: published
tags:
  - bash
  - array
  - cli
  - script
Category: note
---
up::[[MOC_Shell_Bash_Zsh]]

Both `mapfile` and `read -a` can be used to store the output of a command or a list of values into an array. However, the `mapfile` command is generally preferred when reading lines from a file, while `read -a` is well-suited for reading space-separated values from a string.

Let's assume that we want to store all directories (top-level) that are located in projects forlder. In other words, keeping all projects (dir names) as array elements.

```bash
projects=("$HOME"/projects/*)

# Using 'find' command with '-print0' to handle directory names with special characters
while IFS= read -r -d $'\0' line; do
    projects+=("$line")
done < <(find "${projects[@]}" -maxdepth 0 -type d -print0)
```

In the provided code, the `read` command is used together with some parameters. Here is a brief explanation:

- `-a` : This option is used when we want to read from input and store it in an array. In the given code snippet, the input is obtained from a subshell command that lists directories (`ls -d ${projects[@]}`).

- `-r` : This option prevents backslash escapes from being interpreted. It helps you to read the strings "as is".

- `-d $'\0'` : This tells `read` to continue until it encounters a null byte (`\0`), which is the delimiter used by `find . -print0`.

So `read -r -d $'\0' line` reads input separated by null characters into the variable `line`. This is done inside a `while` loop, which continues to perform this reading operation for each directory returned by `find`, assigned to the `projects` array one by one.

The while loop structure `while IFS= read -r -d $'\0' line; do` is commonly used in shell scripting to read lines from a file (or in this case, results from a command substitution) in a safe manner that preserves whitespace and special characters.

`IFS=` is used to temporarily clear the Internal Field Separator variable, which is used by `read` to split the input line into separate fields. By clearing it, we ensure that `read` treats each line as a whole, even if it includes spaces.

In this script, the `find` command is used, ill-equipped with the `-print0` option to output names using a null character as a delimiter, which helps in dealing with directory names that include spaces or other special characters. The `-maxdepth 0` option ensures that only the directories (not their subdirectories) are listed. The `-type d` filter ensures that only directories are returned.

The `while` loop with `IFS= read -r -d $'\0'` handles the null delimited output from `find`. Within the loop, each line is appended to the `projects` array. Lastly, the elements of the `projects` array are added to the 'list' array.
