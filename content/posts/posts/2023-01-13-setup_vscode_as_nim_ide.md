---
Title: Setup VS Code as NIM IDE
Slug: vscode-as-nim-ide
Date: 2021-12-02
modified: 2023-01-13
Start: 2023-01-13
Tags: nim, ide, programming, vscode, debugging, nimrod
Category: Howto
Image: images/head/vscode-as-nim-ide.jpg
Summary: Learn how to set up VSCode as a Nim IDE from scratch. Includes instructions for downloading VSCode, installing the Nim extension, configuring settings, and debugging Nim code.
Status: published
prompt: Give me detailed instructions how to prepare vscode as NIM IDE starting from scratch (downloading vscode). Provide blog-post style answer with introduction and in the closing reference to related topics such as debugging in vscode and other. In the introduction - provide short info about the nim language.
---

## Introduction
[Nim](https://nim-lang.org/) is a statically-typed, imperative programming language that is designed to be efficient, expressive, and easy to learn. It is often compared to other programming languages like Python, C, and Go. One of the great things about Nim is that it can be used to create efficient command-line tools, web servers, and desktop applications.

In this tutorial, we will go over how to set up [Visual Studio Code](https://code.visualstudio.com/) (VS Code) as a Nim IDE (Integrated Development Environment) from scratch. This includes downloading VS Code, installing the Nim extension, and configuring the necessary settings for debugging and code completion.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Installation steps](#installation-steps)
	- [1. Download and Install VSCode](#1-download-and-install-vscode)
	- [2 Install the Nim Extension](#2-install-the-nim-extension)
	- [3. Configure the Settings](#3-configure-the-settings)
	- [4. Download Nim](#4-download-nim)
	- [5. Create a new Nim file](#5-create-a-new-nim-file)
	- [6. Debugging](#6-debugging)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="installation-steps"></a>
## Installation steps
<a id="1-download-and-install-vscode"></a>
### 1. Download and Install VSCode
The first step is to download and install VS Code. You can do this by visiting the VS Code website ([https://code.visualstudio.com/](https://code.visualstudio.com/)) and selecting the appropriate download for your operating system. Once the download is complete, simply follow the instructions to install VSCode on your computer.

<a id="2-install-the-nim-extension"></a>
### 2 Install the Nim Extension
Once VS Code is installed, open it and press <kbd>Ctrl+Shift+X</kbd> (<kbd>Cmd+Shift+X</kbd> on macOS) to open the Extensions pane. Search for `"Nim"` and select the "Nim" extension by "Konstantin Zaitsev" and click on the install button. This extension provides syntax highlighting, code completion, and other features for Nim development.

<a id="3-configure-the-settings"></a>
### 3. Configure the Settings
Now that the Nim extension is installed, you can configure the settings to make your Nim development experience even better. In VSCode, go to `File > Preferences > Settings` (`Code > Settings > Settings` on macOS) and search for "Nim". From here, you can configure settings such as the path to the Nim compiler, the formatting of the code, and the behavior of the code completion.

<a id="4-download-nim"></a>
### 4. Download Nim
You will also have to download the Nim compiler, which you can do from the official website ([https://nim-lang.org/install.html](https://nim-lang.org/install.html)). Once downloaded, you can add the bin path of the Nim compiler to your environment variable. On macOS, you can `brew install nim`. 
Check if Nim is installed with:
```sh
nim --version
```

you should see something like this:

```
Nim Compiler Version 1.6.10 [MacOSX: amd64]
Compiled at 2022-11-21
Copyright (c) 2006-2021 by Andreas Rumpf

active boot switches: -d:release -d:nimUseLinenoise
```

Now write and compile first program. Create text file `hello.nim` with content:
```nim
echo "Hello world!"
```

Then compile:
```nim
nim c hello.nim
```

output
```
Hint: used config file '/usr/local/Cellar/nim/1.6.10/nim/config/nim.cfg' [Conf]
Hint: used config file '/usr/local/Cellar/nim/1.6.10/nim/config/config.nims' [Conf]
.........................................................
CC: ../../usr/local/Cellar/nim/1.6.10/nim/lib/std/private/digitsutils.nim
CC: ../../usr/local/Cellar/nim/1.6.10/nim/lib/system/dollars.nim
CC: ../../usr/local/Cellar/nim/1.6.10/nim/lib/system/io.nim
CC: ../../usr/local/Cellar/nim/1.6.10/nim/lib/system.nim
CC: hello.nim
Hint:  [Link]
Hint: gc: refc; opt: none (DEBUG BUILD, `-d:release` generates faster code)
26644 lines; 0.776s; 31.555MiB peakmem; proj: /Users/krystian.safjan/hello.nim; out: /Users/krystian.safjan/hello [SuccessX]
```

Time to run it:
```sh
./hello
```
output:
```
Hello world!
```

<a id="5-create-a-new-nim-file"></a>
### 5. Create a new Nim file
Now that everything is set up in the system, you can create a new Nim file in VS Code by going to `File > New File` and then saving the file with a `.nim` file extension. You can now start writing Nim code, and use the features provided by the extension such as syntax highlighting, code completion, and debugging.

For example, create file `hello2.nim` with content:
```
echo "Hello world!!!"
```

and hit the Run button (triangle), and in the output window you should see:
```
[Running] nim compile --verbosity:0 --hints:off --run "/Users/krystian.safjan/hello2.nim"

Hello world!!!

  

[Done] exited with code=0 in 0.959 seconds
```


<a id="6-debugging"></a>
### 6. Debugging
For the information on debugging in VS Code, you can refer to the official documentation [Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging) and guide specific for the Nim language: [A walkthrough for setting up debugging of Nim code in VSCode](https://github.com/jasonprogrammer/nim-debug-example)

<a id="conclusion"></a>
## Conclusion
In conclusion, setting up VSCode as a Nim IDE is relatively easy, and provides a great development experience. The Nim extension provides a wide range of features that make Nim development much more efficient and enjoyable. 


## References
- [Editor Support · nim-lang/Nim Wiki · GitHub](https://github.com/nim-lang/Nim/wiki/Editor-Support)
- [A walkthrough for setting up debugging of Nim code in VSCode](https://github.com/jasonprogrammer/nim-debug-example)

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*

**Credits:**

Heading photo from [Unsplash](https://unsplash.com/photos/w7ZyuGYNpRQ) by [Kevin Ku](https://unsplash.com/@ikukevk)
