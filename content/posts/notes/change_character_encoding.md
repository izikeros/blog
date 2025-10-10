---
Category: note
Date: 2022-05-12
Modified: 2023-07-12
Slug: change-character-encoding
Status: published
Tags:
  - change
  - convert
  - text
  - character
  - encoding
  - iconv
  - utf-8
  - Linux
Title: Change the Character Encoding
---

convert file `iconv.src` from `iso-8859-1` to `utf-8` and save to `/tmp/iconv.out`

```sh
iconv -f iso-8859-1 -t utf-8 iconv.src -o /tmp/iconv.out
```

up::[[MOC_Shell_Bash_Zsh]]
