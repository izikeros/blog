---
Category: note
Date: 2023-03-05
Modified: 2023-07-12
Slug: bash-script-with-arguments-implemented-as-functions
Status: published
Summary: Learn how to use functions and `eval` in a bash script to dynamically execute commands passed as arguments, creating flexible and reusable scripts.
ai_summary: true
Tags:
  - bash
  - eval
  - args
Title: Eval in Bash Script With Arguments Implemented as Functions
---
up::[[MOC_Shell_Bash_Zsh]]
minimal example of how you can use functions and `eval` in a bash script:

```sh
#!/bin/bash

hello () {
  echo "Hello, $1!"
}

eval "$1 World"

```

This script defines a function called `hello` that takes one argument and prints a greeting message with that argument. Then, it uses `eval` to execute the first argument passed to the script followed by the string "World" as the argument to the function.

For example, if you save this script as `greeting.sh` and run `./greeting.sh hello`, it will execute the `hello` function with "World" as its argument, and the output will be:

```
Hello, World!
```

You can modify this example to fit your needs by defining your own functions and passing arguments to them through `eval`.
