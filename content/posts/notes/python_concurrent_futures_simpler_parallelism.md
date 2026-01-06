---
Category: note
Date: 2025-09-21
Modified: 2025-09-21
Slug: concurrent-futures-simpler-parallelism
Status: published
Summary: Learn how to simplify parallel and concurrent programming in Python using `concurrent.futures`, including executors for managing threads and processes, and futures for handling task results.
ai_summary: true
Tags: python, concurrency, parallelism, threading, multiprocessing, performance
Title: Simpler Parallelism with concurrent.futures
Series: Python async
---
## The High-Level Approach

Introduced in Python 3.2 via PEP 3148, `concurrent.futures` gives you a unified interface for running code in parallel. Instead of wrestling with threads and processes directly, you get executors that handle the messy details. You submit tasks, get back futures, and collect results when they're ready.

The module provides two main executors: `ThreadPoolExecutor` for I/O-bound work and `ProcessPoolExecutor` for CPU-bound tasks. Both share the same API, which means you can swap them out with minimal code changes.

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return len(response.content)

urls = [
    'https://example.com',
    'https://python.org',
    'https://github.com'
]

# Context manager handles cleanup automatically
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_url, urls)
    
for url, size in zip(urls, results):
    print(f"{url}: {size} bytes")
```

The executor manages a pool of workers for you. You don't create threads manually or worry about joining them. The context manager ensures everything gets cleaned up properly, even if exceptions occur.

## Working with Futures

The real power shows up when you need more control than `map()` provides. The `submit()` method returns a Future object immediately, letting you track individual tasks and handle them independently.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def process_item(item):
    time.sleep(item['delay'])
    return item['id'], item['value'] * 2

items = [
    {'id': 1, 'value': 10, 'delay': 0.5},
    {'id': 2, 'value': 20, 'delay': 0.1},
    {'id': 3, 'value': 30, 'delay': 0.3}
]

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit all tasks, get futures back
    future_to_item = {
        executor.submit(process_item, item): item 
        for item in items
    }
    
    # Process results as they complete
    for future in as_completed(future_to_item):
        item = future_to_item[future]
        try:
            result_id, result_value = future.result()
            print(f"Item {result_id}: {result_value}")
        except Exception as e:
            print(f"Item {item['id']} failed: {e}")
```

The `as_completed()` function is particularly useful because it yields futures as soon as they finish, rather than in submission order. This means you can start processing early results while slower tasks are still running.

You can also wait for specific conditions using `wait()`:

```python
from concurrent.futures import wait, FIRST_COMPLETED, ALL_COMPLETED

# Submit multiple tasks
futures = [executor.submit(slow_function, i) for i in range(10)]

# Wait for the first one to finish
done, pending = wait(futures, return_when=FIRST_COMPLETED)
fastest_result = next(iter(done)).result()

# Cancel the rest if you only needed one result
for future in pending:
    future.cancel()
```

The Future objects themselves provide several useful methods. You can check if a task is done with `.done()`, cancel pending tasks with `.cancel()`, and attach callbacks with `.add_done_callback()` that fire when the task completes.

## When Each Executor Makes Sense

`ThreadPoolExecutor` works best for I/O-bound operations where your code spends time waiting. Network requests, file I/O, database queries—these are all good candidates. Python's Global Interpreter Lock (GIL) doesn't hurt you here because threads release the GIL during I/O operations.

```python
from concurrent.futures import ThreadPoolExecutor
import sqlite3

def query_database(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

databases = ['users.db', 'orders.db', 'inventory.db']
query = "SELECT COUNT(*) FROM main_table"

with ThreadPoolExecutor(max_workers=3) as executor:
    counts = executor.map(
        lambda db: query_database(db, query), 
        databases
    )
```

`ProcessPoolExecutor` is your choice for CPU-intensive work like data processing, image manipulation, or mathematical computations. Each process gets its own Python interpreter and memory space, bypassing the GIL completely.

```python
from concurrent.futures import ProcessPoolExecutor
import hashlib

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return filepath, hasher.hexdigest()

files = ['large_file1.bin', 'large_file2.bin', 'large_file3.bin']

with ProcessPoolExecutor(max_workers=4) as executor:
    for filepath, digest in executor.map(hash_file, files):
        print(f"{filepath}: {digest}")
```

Don't use `ProcessPoolExecutor` for quick tasks or when you're passing large amounts of data. Spawning processes and serializing data between them has significant overhead. If your tasks take less than 0.1 seconds, the overhead probably exceeds the benefit.

Avoid threads for pure CPU-bound work. The GIL means only one thread executes Python bytecode at a time, so you won't get parallel execution. You might even see slower performance due to context switching overhead.

## The Subtle Bits

The `max_workers` parameter matters more than you might think. Too few workers and you're not utilizing available resources. Too many and you waste memory while adding context-switching overhead. For I/O-bound work, you can often use more workers than CPU cores. For CPU-bound work, using more processes than cores typically doesn't help.

```python
import os
from concurrent.futures import ProcessPoolExecutor

# Good default for CPU-bound work
with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = executor.map(cpu_intensive_function, data)

# For I/O-bound work, you might go higher
with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(fetch_url, urls)
```

When using `ProcessPoolExecutor`, remember that arguments and return values must be picklable. This means you can't pass lambdas, local functions, or objects with unpicklable attributes. If you need to share configuration, consider using `functools.partial()`:

```python
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def process_with_config(item, config):
    # Use config dict to guide processing
    return item * config['multiplier']

config = {'multiplier': 3}
data = [1, 2, 3, 4, 5]

# Wrong - lambdas aren't picklable
# with ProcessPoolExecutor() as executor:
#     results = executor.map(lambda x: process_with_config(x, config), data)

# Right - use partial to bind the config argument
with ProcessPoolExecutor() as executor:
    process_func = partial(process_with_config, config=config)
    results = executor.map(process_func, data)
```

Exception handling requires attention because exceptions happen in worker threads or processes, not your main thread. Always wrap `.result()` calls in try-except blocks. If you use `map()`, exceptions won't raise until you iterate over the results.

```python
def might_fail(x):
    if x < 0:
        raise ValueError("Negative values not allowed")
    return x * 2

with ThreadPoolExecutor() as executor:
    results = executor.map(might_fail, [1, -2, 3])
    
    for value in results:
        try:
            print(value)  # Exception raises here, not during map()
        except ValueError as e:
            print(f"Error: {e}")
```

The executors don't automatically time out. If a task hangs, it'll block forever unless you specify a timeout:

```python
future = executor.submit(potentially_slow_function, arg)

try:
    result = future.result(timeout=5.0)  # Wait max 5 seconds
except TimeoutError:
    print("Function took too long")
    future.cancel()  # Won't stop already-running tasks
```

One common mistake is thinking `.cancel()` will stop running tasks. It only prevents pending tasks from starting. Once a task begins execution, cancellation doesn't interrupt it. If you need interruptible tasks, you'll need to implement that logic yourself, typically using threading events or multiprocessing shared values.

The module handles resource cleanup well through context managers, but if you don't use them, call `.shutdown(wait=True)` explicitly. This ensures all pending tasks complete and resources get released. Forgetting this can leave threads or processes hanging around.