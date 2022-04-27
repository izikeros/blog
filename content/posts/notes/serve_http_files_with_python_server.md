---
title: Serve http files with python server
date: 2022-04-27
status: published
tags: python, htttp, server, javascript
summary: 
slug: serve-http-files-with-python-server
category: note
citation_needed: false
todo: 
---

Sometimes there is a need to serve html page instead of just displaying it in the browser:
- share content with other (allowing download)
- serve http document with javascript when javascript can't be readed due to CORS limitations.


From directory with the content you want to serve type in terminal:

```sh
python -m http.server 9000
```

Read more [here](https://www.askpython.com/python-modules/python-httpserver) 