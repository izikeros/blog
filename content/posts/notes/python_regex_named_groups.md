---
Category: note
Date: '2023-04-19'
Modified: '2023-07-12'
Slug: python-regex-named-groups
Status: published
Tags: python, regex
Title: Python Regex Named Groups
---
up::[[MOC_Python]]

In Python regex, `match.groupdict()` is a method that returns a dictionary containing all the named groups of a regular expression match.

When you use named capturing groups in a regular expression using the `(?P<name>...)` syntax, you can access the captured text using the `groupdict()` method on the match object returned by `re.match()` or `re.search()`. The keys of the dictionary correspond to the group names, and the values are the captured text for each group.

Here's an example:

```python
import re

pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
text = 'Today is 2023-04-19'

match = re.search(pattern, text)

if match:
    print(match.groupdict())

```

Output:

```python
{'year': '2023', 'month': '04', 'day': '19'}
```

In the above example, the regular expression pattern matches a date string in the format 'yyyy-mm-dd', and each part of the date is captured using named groups. The `groupdict()` method returns a dictionary with keys 'year', 'month', and 'day', and their corresponding captured values.