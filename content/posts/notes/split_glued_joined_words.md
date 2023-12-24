---
Title: Split glued or joined words
Slug: split-glued-or-joined-words
Date: 2023-08-12
Modified: 2023-08-12
Status: published
Tags: nlp, text-preprocessing, split-text 
Category: note
---

up::[[MOC_Python]]

## wordninja package

![github stars shield](https://img.shields.io/github/stars/keredson/wordninja.svg?logo=github)

install [wordninja](https://github.com/keredson/wordninja) package: `pip install wordnija`

```python
>>> import wordninja
>>> wordninja.split('bettergood')
['better', 'good']
```

## wordsegment package

![github stars shield](https://img.shields.io/github/stars/grantjenks/python-wordsegment.svg?logo=github)

install the [wordsegment](https://github.com/grantjenks/python-wordsegment) package: `pip install wordsegment`.

use programatically:

```python
>>> from wordsegment import load, segment
>>> load()
>>> segment('thisisatest')
['this', 'is', 'a', 'test']
```

or from CLI

```bash
$ echo thisisatest | python -m wordsegment
this is a test
```

Solutions from: [string - How can I split multiple joined words? - Stack Overflow](https://stackoverflow.com/a/58010290)
