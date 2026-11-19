---
Summary: How to shorten the log level to a single character in Python logging by using the precision field, %(levelname).1s, in the formatter.
ai_summary: true
Title: Python logging - single character log level
Category: note
Date: 2022-05-27
Status: published
Slug: python-logging-single-character-log-level
Tags:
  - log-level
  - logging
  - python
---
You can use the precision field to set a maximum field width:

```python
formatter = logging.Formatter('%(levelname).1s %(message)s')
```

`.1` sets the field width to at most one character, truncating the level to the first character:

```
>>> for level in ('CRITICAL', 'ERROR', 'INFO', 'WARNING', 'DEBUG'):
...     print '%(level)-.1s %(message)s' % {'level': level, 'message': 'Hello world!'}
... 
C Hello world!
E Hello world!
I Hello world!
W Hello world!
D Hello world!
```

from: <https://stackoverflow.com/a/27453084/3247880>
