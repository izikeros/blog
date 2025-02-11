---
Title: Guide to Managing VS Code Keyboard Shortcuts
Slug: managing-vs-code-keyboard-shortcuts-a-complete-guide
Date: 2025-02-11
Modified: 2025-02-11
Status: published
Tags: vscode, keybindings, personalization, customization
Category: note
---

I've been using VS Code for years, and keyboard shortcuts can definitely get messy, especially when you have multiple extensions installed. Let me break this down for you.

The interesting thing about VS Code shortcuts is that they can indeed be context-dependent. This means the same keyboard combination might do different things depending on whether you're in a Python file, Jupyter notebook, or even the integrated terminal.

## How VS Code Handles Shortcuts

VS Code uses a system of "when clauses" to determine which shortcut should fire in a given context. Think of it like a priority system where the more specific context wins. For example:

- A shortcut that works only in Python files (when: "editorLangId == 'python'")
- A shortcut that works in any text editor (when: "editorFocus")
- A global shortcut that works everywhere


## Finding and Resolving Conflicts

Here's how you can investigate and fix shortcut conflicts:

1. Open the Keyboard Shortcuts editor:
   - Press Cmd+K Cmd+S (Mac) or Ctrl+K Ctrl+S (Windows/Linux)
   - Or go to Code > Preferences > Keyboard Shortcuts

2. Type Cmd+L (or whatever shortcut you're investigating) in the search bar. This will show you all commands using that combination.

3. Look for overlapping shortcuts. If you see multiple entries, that's your conflict!

## Fixing Conflicts

You have several options:

1. Change the shortcut for the command you use less frequently
2. Add a more specific "when" clause to make the shortcuts context-dependent
3. Disable one of the conflicting shortcuts

To modify a shortcut:
1. Find it in the Keyboard Shortcuts editor
2. Click the pencil icon
3. Press your new desired key combination
4. Press Enter to save

## Context Matters

Different shortcuts can be active in different contexts like:
- `editorFocus` (when text editor has focus)
- `terminalFocus` (when terminal is focused)
- `notebookEditorFocus` (in Jupyter notebooks)
- `editorLangId == 'python'` (in Python files specifically)

Want to see what context you're in? Try the "Developer: Toggle Keyboard Shortcuts Troubleshooting" command. It'll show you active contexts as you work.

## Pro Tips

1. Back up your custom shortcuts! They're stored in keybindings.json, which you can access through the Keyboard Shortcuts editor.

2. Use the "Show Conflicts" option in the Keyboard Shortcuts editor to quickly spot problematic bindings.

3. Extensions can add their own keybindings. Check their documentation or the Keyboard Shortcuts editor to see what they've added.


## References
- [Keyboard shortcuts for Visual Studio Code](https://code.visualstudio.com/docs/getstarted/keybindings)
- [How to Customize VS Code Keybindings: A Comprehensive Guide](https://toxigon.com/customizing-vs-code-keybindings)
- [trycatchdebug.net \| 522: Connection timed out](https://trycatchdebug.net/news/1472749/vscode-keybindings-guide)
