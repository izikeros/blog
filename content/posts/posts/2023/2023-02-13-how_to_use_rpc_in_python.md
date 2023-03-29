---
Title: How to use RPC in python?
Slug: how-to-use-rpc-in-python
Date: 2023-02-13
Modified: 2023-02-13
Start: 2023-02-13
Tags: python, microservices, communication, rpc, rest, remote-procedure-call, xmlrpc, jsonrpc, distributed-computing, client-server, server, client, SimpleXMLRPCServer, ServerProxy, remote-communication, Flask
Category: Howto
Image: /images/head/abstract_1.jpg
Summary: Get Started with RPC - A Beginner's Guide to Building a Python RPC Server Using xmlrpc and jsonrpc.
Status: published
prompt:
---

[Remote Procedure Call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call) is a protocol that allows two different processes or applications to communicate with each other across different machines, even if they are using different programming languages. RPC is a popular technique used in distributed computing environments, where applications running on different systems need to communicate with each other to perform a task. In this blog post, we will explore how to use RPC in Python and provide an example of two instances communicating using RPC.

## Using RPC in Python
Python provides built-in support for RPC through the [xmlrpc](https://docs.python.org/3/library/xmlrpc.html) and [jsonrpc](https://json-rpc.readthedocs.io/en/latest/) libraries. These libraries allow Python applications to expose their functions as RPC services and also consume RPC services provided by other applications.

To use RPC in Python, you need to create a server that exposes a set of functions or methods that can be invoked by remote clients. You can then use a client application to connect to the server and call these functions remotely.

### Simple client-server
#### Server
Let's start with an example of a **simple server** that exposes a function to add two numbers:

```python
import xmlrpc.server

class MyServer:
    def add(self, a, b):
        return a + b

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MyServer())
server.serve_forever()

```

In the code above, we first define a class called `MyServer` that exposes a single method called add, which takes two arguments and returns their sum. We then create an instance of the `SimpleXMLRPCServer` class, passing in the host and port where the server should listen for incoming requests. We register an instance of the `MyServer` class with the server, which means that any requests received by the server will be forwarded to the methods of the `MyServer` class. Finally, we call the `serve_forever` method to start the server and listen for incoming requests.

#### Client
Now that we have a server running, let's create a **client application** that can connect to the server and call the add method remotely:

```python
import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")
result = server.add(2, 3)
print(result)

```

In the code above, we create an instance of the `ServerProxy` class, passing in the URL of the server we want to connect to. We then call the add method on the server object, passing in the two numbers we want to add. The result of the method call is returned to the client, which we print to the console.

That's it! We have successfully used RPC to call a method on a remote server from a client application.

### Example of Two Instances Communicating Using RPC 
Now let's explore an example of two instances communicating using RPC. In this example, we will create a server application that exposes a set of methods that can be called by a client application. The client application will then call these methods to perform a task.

First, let's create the server application:

```python
import xmlrpc.server

class MyServer:
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MyServer())
server.serve_forever()

```

In the code above, we create a class called `MyServer` that exposes two methods, square and cube, which calculate the square and cube of a number respectively. We then create an instance of the `SimpleXMLRPCServer` class and register an instance of the `MyServer` class with the server.

Next, let's create the client application:

```python
import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")
result = server.square(5)
print("The square of 5 is:", result)
result = server

```

In the client application code above, we create an instance of the `ServerProxy` class and connect to the server running on localhost at port `8000`. We then call the square method on the server object, passing in the number `5`. The result of the method call is returned to the client, which we print to the console. We then call the cube method on the server object, passing in the number `3`, and print the result to the console.

When we run the client application, we should see the following output:

```python
The square of 5 is: 25
The cube of 3 is: 27
```

As you can see, we have successfully used RPC to call methods on a remote server from a client application.

## Conclusion 
RPC is a powerful technique for building distributed applications, and Python provides built-in support for RPC through the xmlrpc and jsonrpc libraries. Using RPC in Python is straightforward and can be done with just a few lines of code. By following the examples provided in this blog post, you should now have a good understanding of how to use RPC in Python and how to create a server that exposes methods that can be called remotely by a client application.

You mig be interested in reading my ["Guide to building a Python RPC server using Flask"](./guide-building-python-rpc-server-using-flask)

## Further Reading
1.  The Python documentation on xmlrpc: [https://docs.python.org/3/library/xmlrpc.html](https://docs.python.org/3/library/xmlrpc.html)
2.  The Python documentation on jsonrpc: 
	[https://json-rpc.readthedocs.io/en/latest/](https://json-rpc.readthedocs.io/en/latest/)
1.  A tutorial on using XML-RPC in Python: [https://pymotw.com/2/xmlrpc.client/index.html](https://pymotw.com/2/xmlrpc.client/index.html)
4.  List of material on distributed systems:
	[https://github.com/theanalyst/awesome-distributed-systems](https://github.com/theanalyst/awesome-distributed-systems)
