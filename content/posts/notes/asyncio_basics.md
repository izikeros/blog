---
Category: note
Date: 2025-09-09
Modified: 2025-09-09
Slug: asyncio-basics-async-await-when-to-use
Status: published
Summary: Learn how `async`/`await` enables efficient concurrent programming by handling I/O waits without blocking, and discover various ways to run tasks concurrently, manage context managers, and handle timeouts.
ai_summary: true
Tags: python, asyncio, concurrency, async-await, io-bound, performance
Title: asyncio Basics - async/await and When to Actually Use Them
Series: Python async
---
X::[[python_features_worth_exploring]]

## Core Principle

`async`/`await` is Python's way of writing concurrent code that can handle multiple I/O operations without blocking. The key insight: while one task is waiting for something (network response, file read, database query), other tasks can run. This is **cooperative multitasking** - tasks voluntarily yield control during waits.

```python
import asyncio

async def fetch_data(url):
    # This function can be paused and resumed
    await asyncio.sleep(1)  # Simulating network delay
    return f"Data from {url}"

async def main():
    # Run three fetches concurrently
    results = await asyncio.gather(
        fetch_data("api.example.com/1"),
        fetch_data("api.example.com/2"),
        fetch_data("api.example.com/3")
    )
    print(results)

# Run the async code
asyncio.run(main())
```

This takes roughly 1 second total, not 3, because the waits happen concurrently.

**History:** `async`/`await` syntax was introduced in Python 3.5 via PEP 492. Earlier async code used `@asyncio.coroutine` and `yield from`, but `async`/`await` is cleaner and now standard.

## Useful Extensions

**Multiple ways to run concurrent tasks:**

```python
# gather - run multiple tasks, collect all results
results = await asyncio.gather(task1(), task2(), task3())

# create_task - start a task in the background
task = asyncio.create_task(long_running_operation())
# Do other stuff
result = await task  # Wait for it when you need the result

# as_completed - process results as they finish
for coro in asyncio.as_completed([task1(), task2(), task3()]):
    result = await coro
    print(f"Got result: {result}")
```

**Async context managers and iterators:**

```python
# Async context manager
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.text()

# Async iterator
async for item in async_generator():
    process(item)
```

**Timeouts and cancellation:**

```python
try:
    result = await asyncio.wait_for(slow_operation(), timeout=5.0)
except asyncio.TimeoutError:
    print("Operation took too long")

# Cancel a running task
task = asyncio.create_task(operation())
task.cancel()
```

## Specific Use Cases

**When async actually helps** - I/O-bound operations where you're waiting for external resources:

- HTTP requests to APIs (using `aiohttp` or `httpx`)
- Database queries (using `asyncpg`, `motor` for MongoDB)
- Reading/writing files (using `aiofiles`)
- WebSocket connections
- Microservice communication

**When async doesn't help** - CPU-bound work like calculations, data processing, or image manipulation. Async doesn't give you parallelism for compute work - for that you need `multiprocessing` or threads (and threads don't help much due to the GIL). Async is about doing other things while waiting, not doing multiple CPU-intensive things simultaneously.

**Real-world example where async shines:**

```python
# Without async: 10 API calls taking 1 second each = 10 seconds total
# With async: 10 API calls taking 1 second each = ~1 second total

async def fetch_user_data(user_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, uid) for uid in user_ids]
        return await asyncio.gather(*tasks)

async def fetch_user(session, user_id):
    async with session.get(f"api.example.com/users/{user_id}") as resp:
        return await resp.json()
```

## Nuances

**You can't mix sync and async freely** - once you go async, you need an async ecosystem. You can't `await` in a regular function, and you can't call regular blocking functions in async code without consequences:

```python
async def bad_example():
    # This blocks the entire event loop!
    time.sleep(5)  # Wrong - use await asyncio.sleep(5)
    
    # This also blocks everything
    requests.get(url)  # Wrong - use aiohttp or httpx async client

async def good_example():
    await asyncio.sleep(5)  # Non-blocking sleep
    async with aiohttp.ClientSession() as session:
        await session.get(url)  # Non-blocking HTTP
```

**Running blocking code when necessary** - sometimes you have to use a blocking library. Use `run_in_executor` to run it in a thread pool:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def use_blocking_library():
    loop = asyncio.get_event_loop()
    # Run blocking code in a thread
    result = await loop.run_in_executor(
        None,  # Use default executor
        blocking_function,
        arg1, arg2
    )
    return result
```

**The event loop is the engine** - `asyncio.run()` creates an event loop, runs your main coroutine, and cleans up. In older code you'll see manual loop management with `loop.run_until_complete()`, but `asyncio.run()` (added in Python 3.7) is simpler.

**Common mistake - forgetting await:**

```python
async def fetch_data():
    return "data"

async def main():
    result = fetch_data()  # Wrong! This is a coroutine object, not the result
    print(result)  # Prints: <coroutine object fetch_data at 0x...>
    
    result = await fetch_data()  # Correct
    print(result)  # Prints: data
```

**When NOT to use async** - if you're only doing one I/O operation at a time, regular synchronous code is simpler and just as fast. Async adds complexity (mental overhead, debugging difficulty, library compatibility) that's only worth it when you're doing multiple I/O operations concurrently. A script that makes one API call doesn't benefit from async. A web scraper hitting 100 URLs does.