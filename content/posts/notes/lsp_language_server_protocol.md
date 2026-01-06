---
Category: note
Date: 2025-10-16
Modified: 2025-10-16
Slug: language-server-protocol-minimal-example
Status: published
Summary: Learn how the Language Server Protocol standardizes communication between code editors and language servers, enabling editors like VS Code to request features such as diagnostics and completions from a single server, simplifying development workflows.
ai_summary: true
Tags: language-server-protocol, vscode, lsp, developer-tools, editors, programming
Title: Understanding the Language Server Protocol through a Minimal Working Example
llm: "https://chatgpt.com/c/68f0c9b0-b1b8-8328-ae36-d30546f7276b"
---
## The Mental Model: What Is the Language Server Protocol

The **Language Server Protocol (LSP)** is one of those invisible technologies that quietly revolutionized the developer experience. It defines a **standard way for code editors (clients)** to communicate with **language-specific analysis engines (servers)**.  

Before LSP, every editor (VS Code, Vim, Sublime, Atom, etc.) had to build their own support for each programming language. That meant dozens of editors and dozens of languages — an explosion of duplicated work.  

LSP fixed that by saying: “Let’s agree on how editors talk to language tools.”  

Now, editors can speak a **common protocol** over JSON-RPC (a lightweight request-response format over stdin/stdout). A single server can work with many editors.

You can think of it like this:

```mermaid
graph TD
    A[VS Code Editor] -->|JSON-RPC: initialize, textDocument/didOpen| B[Language Server]
    B -->|diagnostics, hover info, completions| A
````

In short:

- The **editor** (client) sends notifications and requests: _“File opened”, “User typed this”, “What symbols are here?”_
- The **server** responds with diagnostics, completions, definitions, etc.

Once you get this model, the magic of modern editor intelligence starts to feel less mysterious.