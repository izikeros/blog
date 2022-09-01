---
title: Serve HTTP files with python server
date: 2022-04-27
modified:2022-04-27
status: published
tags: python, htttp, server, javascript
slug: serve-http-files-with-python-server
category: note
citation_needed: false
todo: 
---

Sometimes there is a need to serve HTML page instead of just displaying it in the browser:
- share content with others (allowing download)
- serve HTTP document with javascript when javascript can't be read due to CORS limitations.


From the directory with the content you want to serve type in terminal:

```sh
python -m http.server 9000
```

Read more [here](https://www.askpython.com/python-modules/python-httpserver) 