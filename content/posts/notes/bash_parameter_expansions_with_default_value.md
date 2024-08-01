---
Title: Bash Parameter Expansion With Default Value
Slug: bash-parameter-expansion-with-default-value
Date: 2024-08-01
Modified: 2024-08-01
Status: published
tags: bash, parameter-expansion
Category: note
---

up::[[MOC_Shell_Bash_Zsh]]

## Bash parameter expansion with default value
Bash parameter expansion with default value is a useful feature for handling variables that may or may not be set. The syntax is:

```bash
${variable-default}
```

This expands to the value of `variable` if it's set and not null. If `variable` is unset or null, it expands to `default`. It's commonly used to provide fallback values for environment variables or function parameters, improving script robustness and readability.

A slight variation is `${variable:-default}`, which uses the default even if `variable` is set but empty.

## Examples

1. Basic usage:
```bash
echo ${USER-anonymous}
```
This prints the value of USER if set, otherwise "anonymous".

2. In a script:
```bash
#!/bin/bash
NAME=${1-"World"}
echo "Hello, $NAME!"
```
This script greets the first argument, defaulting to "World" if no argument is provided.

3. With environment variables:
```bash
BACKUP_DIR=${CUSTOM_BACKUP_DIR-"/var/backups"}
cp important_file.txt $BACKUP_DIR
```
This uses a custom backup directory if set, otherwise defaults to "/var/backups".

4. Function parameters:
```bash
function greet() {
    local greeting=${1-"Hello"}
    local name=${2-"Guest"}
    echo "$greeting, $name!"
}

greet                 # Output: Hello, Guest!
greet "Hi"            # Output: Hi, Guest!
greet "Hey" "Alice"   # Output: Hey, Alice!
```

5. Nested default values:
```bash
echo ${FOO-${BAR-"default"}}
```
This uses FOO if set, otherwise BAR if set, otherwise "default".

## Use cases
Here's a list of situations where bash parameter expansion with default values can be particularly useful:

1. **Script arguments**: Provide default values for optional command-line arguments.

2. **Configuration management**: Set default configuration values that can be overridden by environment variables.

3. **Function parameters**: Define default values for optional function parameters.

4. **Fallback paths**: Specify default file or directory paths when custom locations aren't provided.

5. **User customization**: Allow users to customize behavior through environment variables without modifying scripts.

6. **Default usernames**: Provide a default username when one isn't specified.

7. **API tokens**: Use a default or test API token when a custom one isn't provided.

8. **Temporary directories**: Set a default temp directory location that can be overridden.

9. **Logging levels**: Specify a default logging level that can be changed via an environment variable.

10. **Database connections**: Provide default database credentials that can be overridden for different environments.

11. **Default timeouts**: Set default timeout values for operations that can be customized.

12. **Fallback commands**: Use alternative commands if preferred ones aren't available on the system.

13. **Default language or locale settings**: Specify default language settings that can be overridden.

14. **Build environments**: Set default build flags or environments that can be customized.

15. **Default resource allocations**: Specify default CPU or memory allocations that can be adjusted.
