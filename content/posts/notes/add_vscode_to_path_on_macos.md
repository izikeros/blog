---
Title: Add VSCode to PATH
Slug: add-vscode-to-path
Date: 2023-07-21
Modified: 2023-07-21
Status: published
Tags: vscode, path, terminal, cli, bash, zsh
Category: note
---
If you get code command not found error but vscode  is installed:
```sh
> code
zsh: command not found: code
```

it means, that, `code` command is not in you system PATH. You need to add it.

To do that, follow these steps:

1. Launch Visual Studio Code.
    
2. Open the Command Palette by pressing `Cmd+Shift+P` (or `Ctrl+Shift+P` on Windows/Linux).
    
3. Type "shell command" in the Command Palette search bar.
    
4. You should see an option that says "Shell Command: Install 'code' command in PATH." Select it to add the `code` command to your system PATH.
    

After completing these steps, you should be able to open Visual Studio Code directly from the terminal using the `code` command.