---
Category: note
Date: '2022-04-27'
Modified: '2023-07-12'
Slug: serve-http-files-with-python-server
Status: published
Tags: python, htttp, server, javascript
Title: Serve HTTP Files With Python Server
citation_needed: false
---
up::[[python]]

Sometimes there is a need to serve HTML page instead of just displaying it in the browser:

- share content with others (allowing download)
- serve HTTP document with javascript when javascript can't be read due to CORS limitations.

From the directory with the content you want to serve type in terminal:

```sh
python -m http.server 9000
```

Read more [here](https://www.askpython.com/python-modules/python-httpserver)
