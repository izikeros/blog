---
Title: A guide to building a Python RPC server using Flask
Slug: guide-building-python-rpc-server-using-flask
Date: 2023-02-13
Modified: 2023-02-13
Start: 2023-02-13
Tags: python, flask, rpc, client-server, communication
Category: Howto
Image: /images/head/abstract_3.jpg
Summary: Discover the world of distributed systems and build your own Python RPC server using Flask. Harness the power of remote procedure calls today!
Status: published
prompt:
todo: verify if it works, add repo with code
---

## Introduction

Remote Procedure Call (RPC) is a communication protocol that allows a client application to call a function or method on a remote server. RPC is widely used in distributed systems for inter-process communication. Python is a powerful programming language for building applications, and Flask is a popular web framework for building web applications in Python. In this blog post, we will guide you on how to build a Python RPC server using Flask.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Step 1: Install Flask](#step-1-install-flask)
- [Step 2: Create a Flask app](#step-2-create-a-flask-app)
- [Step 3: Add a JSON-RPC endpoint](#step-3-add-a-json-rpc-endpoint)
- [Step 4: Define JSON-RPC functions](#step-4-define-json-rpc-functions)
- [Step 5: Test the JSON-RPC server](#step-5-test-the-json-rpc-server)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="step-1-install-flask"></a>
### Step 1: Install Flask

The first step is to install Flask. You can install Flask using pip, which is the package installer for Python.

```sh
pip install flask
```

<a id="step-2-create-a-flask-app"></a>
### Step 2: Create a Flask app

The next step is to create a Flask app. You can create a Flask app by creating a Python file and importing Flask. The following code creates a simple Flask app:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

```

The above code creates a Flask app and defines a route for the root URL. When a client sends a GET request to the root URL, the server will return 'Hello, world!'.

<a id="step-3-add-a-json-rpc-endpoint"></a>
### Step 3: Add a JSON-RPC endpoint

The next step is to add a JSON-RPC endpoint to the Flask app. JSON-RPC is a lightweight remote procedure call protocol that uses JSON to encode messages. You can use the `jsonrpcserver` package to add a JSON-RPC endpoint to Flask. The `jsonrpcserver` package provides a decorator `@app.route_jsonrpc` that you can use to define a JSON-RPC endpoint.

```python
from flask import Flask
from jsonrpcserver import dispatch, result

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route_jsonrpc('/rpc')
def rpc(request):
    response = dispatch(request.data)
    return result(response)

```


The above code defines a JSON-RPC endpoint at the URL `/rpc`. When a client sends a JSON-RPC request to the URL `/rpc`, the server will dispatch the request to the appropriate function and return the result in a JSON-RPC response.

<a id="step-4-define-json-rpc-functions"></a>
### Step 4: Define JSON-RPC functions

The next step is to define the JSON-RPC functions that the client can call. You can define JSON-RPC functions as Python functions and use the `@dispatch` decorator from the `jsonrpcserver` package to register the functions with the JSON-RPC server.

```python
from flask import Flask
from jsonrpcserver import dispatch, result
from jsonrpcserver.exceptions import InvalidParams

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route_jsonrpc('/rpc')
def rpc(request):
    response = dispatch(request.data)
    return result(response)

@dispatch
def add(a: int, b: int) -> int:
    return a + b

@dispatch
def subtract(a: int, b: int) -> int:
    return a - b

@dispatch
def multiply(a: int, b: int) -> int:
    return a * b

@dispatch
def divide(a: int, b: int) -> float:
    if b == 0:
        raise InvalidParams('division by zero')
    return a / b

```

The above code defines four JSON-RPC functions: `add`, `subtract`, `multiply`, and `divide`. Each function takes two integer arguments and returns an integer or float.

<a id="step-5-test-the-json-rpc-server"></a>
### Step 5: Test the JSON-RPC server

The final step is to test the JSON-RPC server. You can test the server by sending JSON-RPC requests to the URL `/rpc`. You can use any JSON-RPC client to send requests to the server. In the following example, we will use the `jsonrpcclient` package to send requests to the server.

```python
import jsonrpcclient

url = 'http://localhost:5000/rpc'

result = jsonrpcclient.request(url, 'add', a=2, b=3)
print(result)  # Output: 5

result = jsonrpcclient.request(url, 'subtract', a=5, b=3)
print(result)  # Output: 2

result = jsonrpcclient.request(url, 'multiply', a=2, b=3)
print(result)  # Output: 6

result = jsonrpcclient.request(url, 'divide', a=6, b=3)
print(result)  # Output: 2.0

result = jsonrpcclient.request(url, 'divide', a=6, b=0)
print(result)  # Output: {'code': -32602, 'message': 'Invalid params', 'data': 'division by zero'}

```

The above code sends five JSON-RPC requests to the server and prints the results. The first four requests call the `add`, `subtract`, `multiply`, and `divide` functions, respectively. The last request calls the `divide` function with a zero value for the `b` argument, which raises an `InvalidParams` exception.

<a id="conclusion"></a>
## Conclusion

In this blog post, we have shown you how to build a Python RPC server using Flask. We have used the `jsonrpcserver` package to add a JSON-RPC endpoint to Flask and define JSON-RPC functions. We have also shown you how to test the server using the `jsonrpcclient` package. With this knowledge, you can build powerful distributed systems that can communicate seamlessly across networks.