---
title: Append JSON data to file, save the traces
category: note
date: '2022-06-03'
modified: '2022-07-05'
status: published
slug: append-json-data-to-file-save-traces
tags: append-json, data, json, trace, jsonlines, python
---

## The JSON Lines standard
Sometimes there is a need to store data in JSON format but simultaneously append data to files when new data arrive. JSON format stores data, on the top level, like a dictionary or a list it is not trivial to append new data without reading the whole file.

For this appending use-case derivative format: [JSON Lines](https://jsonlines.org/) can be used.

JSON lines is also called newline-delimited JSON it is:
- is a convenient format for **storing structured data** that may be processed **one record at a time**
- works well with **unix-style text processing** tools and **shell pipelines**. [[cli tools for data science]]
- is an excellent format for **log files**
- is a flexible format for **passing messages between** cooperating **processes**.
use jsonlines

## Python package - `jsonlines`
There is [jsonlines](https://jsonlines.readthedocs.io/en/latest/) Python package that supports using jsonlines format. Install it with `pip install jsonlines` and use like in example below to read and write one JSON object per line:

```python
with jsonlines.open('input.jsonl') as reader:
    for obj in reader:
        ...

with jsonlines.open('output.jsonl', mode='w') as writer:
    writer.write(...)
```

## JSON Lines Better than CSV
The jsonlines format is sometimes considered better than CSV since:
- CSV has **no standard encoding**
- no standard **column separator**
- multiple **character escaping** standards.
- **String is the only type supported** for cell values, so some programs attempt to guess the correct types.

When compared to CSV JSON Lines allows for easy nesting of the data
```json
{"name": "Gilbert", "wins": [["straight", "7♣"], ["one pair", "10♥"]]}
{"name": "Alexa", "wins": [["two pair", "4♠"], ["two pair", "9♠"]]}
{"name": "May", "wins": []}
{"name": "Deloise", "wins": [["three of a kind", "5♣"]]}
```
JSON Lines handles tabular data cleanly and without ambiguity. Cells may use the standard JSON types.

You can use CLI tools to see complex, nested data structures:
```shell
$ grep pair winning_hands.jsonl | jq .
```

See also:
- [NDJSON](http://ndjson.org/) - Newline delimited JSON:
- [ndjson standard specification](https://github.com/ndjson/ndjson-spec)