---
Title: Threading vs Multiprocessing in Python - GIL Implications and Choosing the Right Tool 
Slug: threading-vs-multiprocessing-gil-implications 
Date: 2025-09-10 
Modified: 2025-09-10 
Status: published 
Tags: python, threading, multiprocessing, gil, concurrency, parallelism, performance 
Category: note
Series: Python async
---
X::[[python_features_worth_exploring]]

## Core Principle

Python has two built-in ways to run code concurrently: **threading** and **multiprocessing**. The critical difference comes down to the **Global Interpreter Lock (GIL)** - a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode at once. This means:

- **Threading** - multiple threads in one process, but only one thread executes Python code at a time due to the GIL. Good for I/O-bound tasks.
- **Multiprocessing** - separate processes with separate Python interpreters, each with its own GIL. True parallelism for CPU-bound tasks.

```python
import threading
import multiprocessing
import time

def cpu_bound_task(n):
    # Heavy computation
    return sum(i * i for i in range(n))

# Threading - doesn't help with CPU work
start = time.time()
threads = [threading.Thread(target=cpu_bound_task, args=(10_000_000,)) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threading: {time.time() - start:.2f}s")  # ~4 seconds on 4-core machine

# Multiprocessing - achieves true parallelism
start = time.time()
processes = [multiprocessing.Process(target=cpu_bound_task, args=(10_000_000,)) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()
print(f"Multiprocessing: {time.time() - start:.2f}s")  # ~1 second on 4-core machine
```

**History:** The GIL has been in CPython since the beginning. PEP 703 (approved in 2023) outlines a path to making the GIL optional in Python 3.13+, but it's still fundamental to understand for current Python versions.

## Useful Extensions

**Threading with ThreadPoolExecutor (simpler interface):**

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return len(response.content)

urls = ["http://example.com"] * 10

# Old way - manual thread management
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()

# Better way - thread pool handles everything
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_url, urls)
    print(list(results))
```

**Multiprocessing with ProcessPoolExecutor:**

```python
from concurrent.futures import ProcessPoolExecutor

def expensive_calculation(n):
    return sum(i * i for i in range(n))

numbers = [10_000_000] * 4

with ProcessPoolExecutor() as executor:
    results = executor.map(expensive_calculation, numbers)
    print(list(results))
```

**Sharing data between processes:**

```python
from multiprocessing import Process, Queue, Value, Array
import ctypes

# Queue - safe inter-process communication
def worker(queue):
    queue.put("Result from worker")

q = Queue()
p = Process(target=worker, args=(q,))
p.start()
print(q.get())
p.join()

# Shared memory with Value and Array
def increment_counter(counter, arr):
    counter.value += 1
    arr[0] += 10

counter = Value('i', 0)  # shared integer
arr = Array('i', [0, 1, 2])  # shared array

processes = [Process(target=increment_counter, args=(counter, arr)) for _ in range(5)]
for p in processes: p.start()
for p in processes: p.join()

print(f"Counter: {counter.value}")  # 5
print(f"Array: {list(arr)}")  # [50, 1, 2]
```

**Thread-safe operations with Lock:**

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:  # Only one thread can execute this block at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # 1,000,000 (correct with lock, random without)
```

## Specific Use Cases

**Use threading for I/O-bound tasks:**

- Making multiple HTTP requests (web scraping, API calls)
- Reading/writing multiple files
- Database queries where you're waiting for responses
- Network operations (socket communication)
- Any operation where you spend time waiting for external resources

The GIL doesn't matter here because threads release it during I/O operations. While one thread waits for network/disk, others can run.

**Use multiprocessing for CPU-bound tasks:**

- Image/video processing
- Data analysis and numerical computations
- Encryption/decryption
- Machine learning model training
- Parsing large files
- Any computation-heavy work where the CPU is the bottleneck

You need separate processes to get around the GIL and use multiple CPU cores effectively.

**Real-world example - web scraper:**

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def scrape_page(url):
    response = requests.get(url)
    # Process the page
    return extract_data(response.text)

urls = ["http://example.com/page1", "http://example.com/page2", ...]

# Threading is perfect here - lots of waiting for network responses
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scrape_page, urls))
```

**Real-world example - image processing:**

```python
from concurrent.futures import ProcessPoolExecutor
from PIL import Image

def process_image(filename):
    img = Image.open(filename)
    # CPU-intensive operations
    img = img.resize((800, 600))
    img = img.filter(ImageFilter.SHARPEN)
    img.save(f"processed_{filename}")
    return filename

images = ["img1.jpg", "img2.jpg", "img3.jpg", ...]

# Multiprocessing is needed - CPU-intensive work
with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_image, images))
```

## Nuances

**The GIL releases during I/O operations** - this is why threading works for I/O-bound tasks. When a thread calls a blocking I/O function (like `requests.get()` or `file.read()`), it releases the GIL so other threads can run. The GIL only prevents multiple threads from executing Python bytecode simultaneously.

**Multiprocessing has overhead** - creating processes is expensive (memory and startup time). Each process needs its own Python interpreter and memory space. For small tasks, this overhead can outweigh the benefits of parallelism:

```python
# Bad - overhead dominates
with ProcessPoolExecutor() as executor:
    results = executor.map(lambda x: x * 2, range(100))

# Good - task is substantial enough to justify processes
with ProcessPoolExecutor() as executor:
    results = executor.map(expensive_function, large_dataset)
```

**Data serialization between processes** - when you pass data to a process or get results back, Python uses `pickle` to serialize it. Large objects or objects that can't be pickled cause problems:

```python
# This won't work - lambda functions can't be pickled
with ProcessPoolExecutor() as executor:
    results = executor.map(lambda x: x * 2, numbers)  # Error

# This works - regular functions can be pickled
def multiply_by_two(x):
    return x * 2

with ProcessPoolExecutor() as executor:
    results = executor.map(multiply_by_two, numbers)  # Works
```

**Threading has less isolation** - all threads share the same memory space, which means bugs in one thread (like accessing shared data without locks) can corrupt data across the entire program. Processes are isolated - a crash in one process doesn't affect others.

**When neither helps** - if your program is both CPU and I/O bound, you might need a hybrid approach: processes for CPU work, each using threads for I/O. Or consider `asyncio` for I/O operations instead of threads if you're doing lots of concurrent I/O.

**Process pool size guidelines** - for CPU-bound work, use `os.cpu_count()` workers (one per CPU core). For I/O-bound work with threads, you can use many more (tens or hundreds) since threads spend most time waiting. Experiment to find the sweet spot.

```python
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# CPU-bound - match core count
with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = executor.map(cpu_intensive_func, data)

# I/O-bound - can use many more
with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(io_intensive_func, data)
```

**The simple decision tree:**

- Waiting for network/disk/external services? Use **threading** (or `asyncio`)
- Doing heavy calculations/data processing? Use **multiprocessing**
- Doing simple sequential work? Use **neither** - regular code is simpler