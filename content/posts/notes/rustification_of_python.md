---
Category: note
Date: 2023-03-06
Modified: 2023-07-12
Prompt: Give me long blog article on Rustification of python that highlight the trend that more and more python infrastucture and tools are based on Rust. Give me concrete examples. Finish with discusson of the future role of the Rust for the Python
Slug: rustification-of-python
Status: published
Tags:
  - rustification-of-python
  - python
  - rust
  - pyo3
  - maturin
  - tokenizers
  - performance
  - memory-safety
  - concurrent-programming
  - full-text-search
  - user-interface
  - standalone-applications
  - community
  - fragmentation
  - complexity
  - bugs
  - backlash
  - controversy
Title: Rustification of Python
---

Python has been one of the most popular programming languages for years now. It’s known for its simplicity, ease of use, and versatility. However, with the growing demand for high-performance applications, the limitations of Python have become more apparent. To address these limitations, the Python community has started to Rustify Python. Rust is a systems programming language that emphasizes safety, speed, and concurrency. It's becoming increasingly popular, and many Python infrastructure and tools are now being built using Rust.

In this article, we’ll explore the trend of Rustification of Python, provide some concrete examples, and discuss the future role of Rust in Python.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Rustification of Python](#rustification-of-python)
- [Concrete Examples](#concrete-examples)
 	- [PyO3 - use Rust as a Python extension module](#pyo3---use-rust-as-a-python-extension-module)
 	- [Maturin - build and publish Python packages with Rust extensions](#maturin---build-and-publish-python-packages-with-rust-extensions)
 	- [Tokenizers - tokenization of natural language texts](#tokenizers---tokenization-of-natural-language-texts)
 	- [Ruff - linter for python code](#ruff---linter-for-python-code)
 	- [huak - python package manager](#huak---python-package-manager)
 	- [Crossbeam - library for concurrent programming](#crossbeam---library-for-concurrent-programming)
 	- [Tantivy - full-text search engine](#tantivy---full-text-search-engine)
 	- [Cursive - building user interfaces](#cursive---building-user-interfaces)
 	- [PyOxidizer - standalone Python applications](#pyoxidizer---standalone-python-applications)
- [The Future Role of Rust in Python](#the-future-role-of-rust-in-python)
- [RustPython](#rustpython)
- [Drawbacks and controversies around the Rustification of Python](#drawbacks-and-controversies-around-the-rustification-of-python)
 	- [Increased complexity](#increased-complexity)
 	- [Fragmentation of the Python ecosystem](#fragmentation-of-the-python-ecosystem)
 	- [Potential for bugs in Rust code](#potential-for-bugs-in-rust-code)
 	- [Community backlash](#community-backlash)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="rustification-of-python"></a>

## Rustification of Python

Rustification of Python is the process of integrating Rust code into Python applications. The primary reason for Rustification is to improve performance and memory safety. Rust has been designed to be a safe and efficient language. Its memory safety features ensure that programs are free from memory errors like null pointers, buffer overflows, and data races. Rust’s performance, coupled with its safety, makes it an ideal language for building critical infrastructure and applications.

Over the years, Rust has gained significant popularity, and its adoption is increasing at an impressive rate. Many companies, including Dropbox, Microsoft, Mozilla, and Amazon, are using Rust in their infrastructure. The Python community has also embraced Rust and is using it to improve performance and safety in Python applications.

<a id="concrete-examples"></a>

## Concrete Examples

Let's look at some concrete examples of how Rust is being used to Rustify Python.

<a id="pyo3---use-rust-as-a-python-extension-module"></a>

### PyO3 - use Rust as a Python extension module

PyO3 is a Rust library that allows Rust to be used as a Python extension module. It allows Python developers to write performance-critical code in Rust and then expose it as a Python module. PyO3 is easy to use and has excellent documentation. It supports both Python 2 and 3.

Using PyO3, developers can write Rust code that can be called from Python. The Rust code can be compiled into a shared library, which can then be loaded into Python using the ctypes module. PyO3 makes it easy to write high-performance Python extensions in Rust.

**PyO3**: [https://github.com/PyO3/pyo3](https://github.com/PyO3/pyo3)

<a id="maturin---build-and-publish-python-packages-with-rust-extensions"></a>

### Maturin - build and publish Python packages with Rust extensions

Maturin is a Rust tool that makes it easy to build and publish Python packages with Rust extensions. It's designed to work with the Python packaging ecosystem and provides a simple command-line interface for building and publishing Rust extensions.

Maturin can be used to build Python wheels with Rust extensions, which can then be distributed through the Python Package Index (PyPI). Maturin also supports cross-compiling Rust extensions for different platforms.

**Maturin**: [https://github.com/PyO3/maturin](https://github.com/PyO3/maturin)

<a id="tokenizers---tokenization-of-natural-language-texts"></a>

### Tokenizers - tokenization of natural language texts

Tokenizers is a Python library that provides efficient tokenization of natural language texts. It's used by many natural language processing libraries, including Transformers, Hugging Face, and spaCy. Tokenizers uses Rust to implement its performance-critical parts, such as byte-level encoding and decoding.

By using Rust, Tokenizers can achieve high performance while ensuring memory safety. Tokenizers is written in Python, and Rust is used only for performance-critical parts.

**Tokenizers**: [https://github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers)
<a id="ruff---linter-for-python-code"></a>

### Ruff - linter for python code

Ruff is a linter for Python code that's written in Rust. It's designed to be faster and more efficient than traditional Python linters. Ruff uses the PyO3 library to interact with Python's AST (Abstract Syntax Tree), which makes it easy to write Rust code that can analyze Python code.

**Ruff**: [https://github.com/johnthagen/ruff](https://github.com/johnthagen/ruff)

<a id="huak---python-package-manager"></a>

### huak - python package manager

A Python package manager written in Rust. The [Cargo](https://github.com/rust-lang/cargo) for Python.
Huak ("hwok") aims to support a base workflow for developing Python packages and projects. The process is linear and purpose oriented, establishing better familiarization with the steps.

**huak:** <https://github.com/cnpryer/huak>

<a id="crossbeam---library-for-concurrent-programming"></a>

### Crossbeam - library for concurrent programming

Crossbeam is a Rust library for concurrent programming. It provides a set of data structures and synchronization primitives that make it easier to write high-performance, concurrent code. Crossbeam can be used in Python applications using the PyO3 library.

**Crossbeam**: [https://github.com/crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam)
<a id="tantivy---full-text-search-engine"></a>

### Tantivy - full-text search engine

Tantivy is a full-text search engine library that's written in Rust. It's designed to be fast, memory-efficient, and easy to use. Tantivy can be used in Python applications using the PyO3 library.

**Tantivy**: [https://github.com/tantivy-search/tantivy](https://github.com/tantivy-search/tantivy)
<a id="cursive---building-user-interfaces"></a>

### Cursive - building user interfaces

Cursive is a Rust library for building user interfaces. It provides a set of widgets and layout primitives that make it easy to create interactive UIs. Cursive can be used in Python applications using the PyO3 library.

**Cursive**: [https://github.com/gyscos/cursive](https://github.com/gyscos/cursive)

<a id="pyoxidizer---standalone-python-applications"></a>

### PyOxidizer - standalone Python applications

PyOxidizer is a Rust tool for building standalone Python applications. It allows Python developers to create a self-contained executable that includes the Python interpreter and all dependencies. PyOxidizer can be used to create Python applications that are easy to deploy and distribute.

**PyOxidizer**: [https://github.com/indygreg/PyOxidizer](https://github.com/indygreg/PyOxidizer)

These are just a few examples of Rust-based tools for Python developers. Rust's performance and memory safety make it a great language for building critical infrastructure and high-performance applications, and the PyO3 library makes it easy to integrate Rust code into Python applications. As Rust continues to gain popularity, we can expect to see more Rust-based tools and libraries for Python developers.

### Rye - alternative to pip/poetry/hatch/virtualenv/

[mitsuhiko/rye](https://github.com/mitsuhiko/rye) - It installs and manages Python installations, manages `pyproject.toml` files, installs and uninstalls dependencies, manages virtualenvs behind the scenes. It supports monorepos and global tool installations.

Rye: <https://github.com/mitsuhiko/rye>

<a id="the-future-role-of-rust-in-python"></a>

## The Future Role of Rust in Python

Rust has already made significant contributions to the Python ecosystem. Rust’s emphasis on performance and memory safety has made it an ideal language for building critical infrastructure and applications. Its adoption in the Python community is increasing at a rapid pace.

In the future, we can expect to see more Python infrastructure and tools being built using Rust. Rust's performance and memory safety features will be critical in building high-performance Python applications. We can also expect to see more Rust libraries being used in Python applications, like Tokenizers.

Furthermore, as Rust continues to gain popularity, we may see it becoming a first-class citizen in the Python ecosystem. We may see Python developers learning Rust to write performance-critical extensions for their Python applications. We may also see more Rust-specific tools and libraries being built for the Python ecosystem.

Rust’s popularity in the Python community has also led to the creation of Rust-based web frameworks, such as Tide and Rocket. These frameworks have the potential to compete with popular Python web frameworks like Django and Flask.

The Rustification of Python is not limited to performance-critical applications. Rust can also be used to build high-level abstractions that make it easier to write Python code. For example, the Rust-based library RustPython aims to create a Python interpreter entirely in Rust. This could lead to better performance and memory safety in Python programs.

Overall, Rustification of Python is an exciting trend that has the potential to revolutionize the Python ecosystem. By using Rust, Python developers can build high-performance, memory-safe applications that can scale to meet the demands of modern computing. Rust’s adoption in the Python community is a sign of its growing importance in the world of programming languages.

Rust is becoming an integral part of the Python ecosystem. Its emphasis on performance and memory safety has made it an ideal language for building critical infrastructure and applications. With the Rustification of Python, we can expect to see more high-performance, memory-safe Python applications being built. As Rust continues to gain popularity, it may even become a first-class citizen in the Python ecosystem.

<a id="rustpython"></a>

## RustPython

There are many implementations of Python, e.g.: [CPython](https://github.com/python/cpython) (C), [Jython](https://www.jython.org/) (Java), [IronPython](https://ironpython.net/) (.NET), [PyPy](https://www.pypy.org/) (Python). Using Jython or IronPython ease integration respectively with Java or .NET applications. It is the same case with Rust - Python interpreter can be implemented in Rust and such implementation already exists: [RustPython](https://rustpython.github.io/). Why Rust implementation of Python? RustPython can be embedded into Rust programs to use Python as a scripting language for your application, or it can be compiled to WebAssembly in order to run Python in the browser.

<a id="drawbacks-and-controversies-around-the-rustification-of-python"></a>

## Drawbacks and controversies around the Rustification of Python

While the Rustification of Python has many benefits, there are also some drawbacks and controversies surrounding the trend. Here are a few criticisms and controversies:

<a id="increased-complexity"></a>

### Increased complexity

One criticism of using Rust in Python applications is that it adds complexity to the codebase. Rust is a complex language with a steep learning curve, and integrating Rust code into a Python application requires developers to have knowledge of both languages.

<a id="fragmentation-of-the-python-ecosystem"></a>

### Fragmentation of the Python ecosystem

Another concern is that the Rustification of Python may lead to fragmentation of the Python ecosystem. As more and more tools and libraries are built in Rust, it may become more difficult for Python developers to find and use compatible libraries and tools.

<a id="potential-for-bugs-in-rust-code"></a>

### Potential for bugs in Rust code

While Rust is designed to be memory-safe, it's still possible to introduce bugs and errors in Rust code. This can be a concern if Rust code is tightly integrated with a Python application, as a bug in the Rust code could potentially crash the entire application.

<a id="community-backlash"></a>

### Community backlash

Finally, there has been some backlash in the Python community to the Rustification trend. Some developers feel that Rust is being hyped as a solution to all of Python's problems, and that it's being overhyped at the expense of other languages and tools.

Overall, while there are some concerns and criticisms of the Rustification of Python, it's clear that Rust has become an important language in the Python ecosystem. As more and more tools and libraries are built in Rust, it will be interesting to see how Python developers adopt and integrate Rust into their workflows.
<a id="references"></a>

## References

- **PyO3**: [https://github.com/PyO3/pyo3](https://github.com/PyO3/pyo3)
- **Maturin**: [https://github.com/PyO3/maturin](https://github.com/PyO3/maturin)
- **Tokenizers**: [https://github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers)
- **Ruff**: [https://github.com/johnthagen/ruff](https://github.com/johnthagen/ruff)
- **Crossbeam**: [https://github.com/crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam)
- **Tantivy**: [https://github.com/tantivy-search/tantivy](https://github.com/tantivy-search/tantivy)
- **Cursive**: [https://github.com/gyscos/cursive](https://github.com/gyscos/cursive)
- **PyOxidizer**: [https://github.com/indygreg/PyOxidizer](https://github.com/indygreg/PyOxidizer)
- **case-study: speed-up python with Rust**: <https://ohadravid.github.io/posts/2023-03-rusty-python/>

## Significant Revisions

- 2023-04-21: Add huak
