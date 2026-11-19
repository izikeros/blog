---
Title: time.time() vs time.perf_counter() in Python
Slug: timetime-vs-timeperfcounter-in-python
Date: 2026-07-21
Modified: 2026-07-21
Status: published
Tags: python, benchmarking, observability, time-measurement, time
Category: note
Summary: time.time() returns adjustable wall-clock time for timestamps and TTLs, while time.perf_counter() is a high-resolution monotonic clock for measuring elapsed time. When to use each and why mixing them up skews benchmarks.
---

Today I learned that `time.time()` and `time.perf_counter()` are not interchangeable, even though both return timestamps as floating-point seconds.

## `time.time()`

Returns the current wall-clock time as seconds since the Unix Epoch (`1970-01-01 00:00:00 UTC`).

```python
import time

now = time.time()
print(now)  # e.g. 1784611234.123456
```

### Use `time.time()` when

- You need the actual current date/time.
- Creating timestamps.
- Calculating expiration times (TTLs).
- Logging events.

### Caveat

The system clock can be adjusted (e.g. NTP sync, manual clock change). This means the value can jump forward or backward, making it unreliable for measuring elapsed durations.

## `time.perf_counter()`

Returns a high-resolution, monotonic performance counter. The reference point is undefined—only differences between two calls are meaningful.

```python
import time

start = time.perf_counter()

# code to measure
sum(range(1000000))

elapsed = time.perf_counter() - start
print(elapsed)
```

### Use `time.perf_counter()` when

- Benchmarking code.
- Measuring latency.
- Tracking execution time.
- Performance profiling.

### Advantages

- Monotonic (never goes backwards).
- Highest available timer resolution on the platform.
- Not affected by system clock changes.

## Quick Comparison

| Feature | `time.time()` | `time.perf_counter()` |
| --- | --- | --- |
| Current real-world time | ✅ | ❌ |
| Seconds since Unix epoch | ✅ | ❌ |
| High resolution | ❌ (platform-dependent) | ✅ |
| Monotonic | ❌ | ✅ |
| Safe for benchmarking | ❌ | ✅ |
| Affected by clock adjustments | ✅ | ❌ |

## Rule of Thumb

- **Need to know *what time it is*?** Use `time.time()`.
- **Need to know *how long something took*?** Use `time.perf_counter()`.

### Example

```python
import time

# Wrong for benchmarking
start = time.time()
do_work()
duration = time.time() - start

# Correct for benchmarking
start = time.perf_counter()
do_work()
duration = time.perf_counter() - start
```

**Takeaway:**

> `time.time()` answers **"What time is it?"**
>
> `time.perf_counter()` answers **"How much time passed?"**
