---
Title: Understanding the Language Server Protocol through a Minimal Working Example
Slug: language-server-protocol-minimal-example
Date: 2025-10-16
Modified: 2025-10-16
Status: published
Tags: language-server-protocol, vscode, lsp, developer-tools, editors, programming
Category: note
llm: https://chatgpt.com/c/68f0c9b0-b1b8-8328-ae36-d30546f7276b
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

## How It Works: Building a Minimal Language Server

Let’s make a minimal working example. You’ll build a simple server in Python that recognizes `.foo` files and warns you if they contain the word “bad”.

### 1. Project structure

```
minimal-lsp/
├── server.py
├── package.json
├── client/
│   └── extension.js
```

We’ll create a **Python LSP server** and a **VS Code extension** to connect to it.

### 2. Install required tools

```bash
pip install pygls
```

[`pygls`](https://github.com/openlawlibrary/pygls) is a Python library that helps you implement language servers that follow the protocol.

### 3. Write the server

`server.py`

```python
from pygls.server import LanguageServer
from pygls.lsp.types import (Diagnostic, DiagnosticSeverity, Position, Range, PublishDiagnosticsParams)

server = LanguageServer("minimal-server", "v0.1")

@server.feature("textDocument/didOpen")
async def did_open(ls: LanguageServer, params):
    """Check file content when it's opened."""
    text = ls.workspace.get_document(params.text_document.uri).source
    diagnostics = []

    # Very simple rule: warn if file contains 'bad'
    if "bad" in text:
        start = text.find("bad")
        end = start + 3
        diagnostics.append(
            Diagnostic(
                range=Range(
                    start=Position(line=0, character=start),
                    end=Position(line=0, character=end),
                ),
                message="Found forbidden word 'bad'",
                severity=DiagnosticSeverity.Warning,
            )
        )

    ls.publish_diagnostics(params.text_document.uri, diagnostics)

if __name__ == "__main__":
    server.start_io()  # communicate via stdin/stdout
```

This is a **complete LSP server** that listens to file open events and sends warnings back to the editor.


## Integrating It with VS Code

To connect VS Code with the Python server, we’ll write a minimal client extension.

`client/extension.js`

```javascript
const path = require("path");
const { workspace, window } = require("vscode");
const { LanguageClient, TransportKind } = require("vscode-languageclient/node");

let client;

function activate(context) {
  const serverModule = context.asAbsolutePath(path.join("..", "server.py"));
  const serverOptions = {
    command: "python",
    args: [serverModule],
    options: { cwd: context.extensionPath }
  };

  const clientOptions = {
    documentSelector: [{ scheme: "file", language: "foo" }],
  };

  client = new LanguageClient(
    "minimalServer",
    "Minimal Python LSP Server",
    serverOptions,
    clientOptions
  );

  client.start();
}

function deactivate() {
  if (!client) {
    return undefined;
  }
  return client.stop();
}

module.exports = { activate, deactivate };
```

`package.json`

```json
{
  "name": "foo-lsp-client",
  "displayName": "Foo Language Support",
  "activationEvents": ["onLanguage:foo"],
  "main": "./client/extension.js",
  "contributes": {
    "languages": [
      {
        "id": "foo",
        "extensions": [".foo"],
        "aliases": ["Foo"]
      }
    ]
  },
  "dependencies": {
    "vscode-languageclient": "^8.0.0"
  }
}
```

Run the extension using **VS Code’s “Run Extension”** command (F5 in a development window).  
Open a `.foo` file and type:

```
this is bad
```

You’ll immediately see a yellow squiggly warning appear. That’s your LSP server talking!


## Practical Scenarios: When and Why to Build Your Own LSP

You’d build or extend your own LSP when:

- You’re developing a **new language**, DSL, or config format.
- You want **custom analysis or linting** in VS Code or other editors.
- You need **language intelligence in a company-specific language** (for example, internal workflow scripts or YAML schemas).
- You want to unify features across editors (VS Code, Neovim, JetBrains) using the same logic.

But you **shouldn’t** build an LSP server when your needs are simple syntax highlighting — use a TextMate grammar or tree-sitter grammar instead.  
LSP is powerful but introduces complexity, especially around synchronization and state handling.

## Final Thoughts

LSP sits at the intersection of editor UX and language tooling. It’s not glamorous, but it’s foundational.

If you’re building developer tools, understanding how to speak this protocol is worth the effort. You can start small — like we did here — and gradually add capabilities such as completions, hover info, or go-to-definition.

At its best, an LSP server is an invisible companion: it listens quietly, responds precisely, and makes the editor feel alive.