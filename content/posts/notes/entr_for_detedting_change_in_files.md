---
Title: entr - run arbitrary command when files change
Slug: entr-run-arbitrary-command-when-files-change
Date: 2024-01-01
Modified: 2024-01-01
Status: published
tags:
  - change
  - watch
  - watch-files
Category: note
---

`entr` is a UNIX utility which runs arbitrary commands when files change. It helps in automating tasks during development such as rebuilding projects, running tests, or syncing files.

Here's a simple usage example:

```
ls *.c | entr make
```

In the above example, `ls *.c` lists all C files in the directory. This list is piped (`|`) into `entr`. When any of these files changes, `entr` executes the `make` command.

Some key features of `entr` include:

- It frees up developers to focus on the code by automating rebuild tasks.
- It doesn't require a configuration file or a list of tasks to run. It just reruns the command you provide it each time a file changes.
- You can use it with any command that needs to operate on a file. This might be shell commands, like `ls` or `echo`, or any other CLI tool you have in your system.

Additional commands for `entr` include:

- `-r` : To restart a long running process like a server when a file changes.
- `-p` : Postpone execution until files are updated.
- `-s` : Evaluate the first argument using the interpreter specified by the SHELL environment variable.
- `-d` : Track directories recursively and include files that are created after the utility starts

Please note that `entr` requires a list of files as input. It does not discover files on its own, it expects to receive a list of files from stdin, which is usually supplied with command line utilities like `ls`, `find` or `git ls-files`.
