---
category: note
date: '2022-05-12'
modified: '2022-05-12'
status: published
slug: change-character-encoding
tags: change, convert, text, character, encoding, iconv, utf-8, Linux
title: Change the character encoding
---

convert file `iconv.src` from `iso-8859-1` to `utf-8` and save to `/tmp/iconv.out`
```sh
iconv -f iso-8859-1 -t utf-8 iconv.src -o /tmp/iconv.out
```

