---
category: note
date: '2022-05-12'
status: published
slug: bash-download-gist-from-github
tags: bash, download, gist, github
title: Bash - download gist from Github
---

## Download, output content to stdout

```sh
curl -L https://gist.githubusercontent.com/izikeros/937b05e81b5dca81d3daf309ea6bad20/raw/
```

## Download, save the output to file `my_file`
```
curl -L https://gist.githubusercontent.com/izikeros/937b05e81b5dca81d3daf309ea6bad20/raw/ -o my_file
```

```sh
# curl options to use
curl -LJO
```

### Options (excepts from the curl man page):
```
-L, --location
      (HTTP) If the server reports that the requested page has moved to a different location
      (indicated with a Location: header and a 3XX response code), this option will make curl
      redo the request on the new place.

-o, --output <file>
       Write output to <file> instead of stdout. If you are using {} or [] to fetch multiple
       documents, you should quote the URL and you can use '#' followed by a number in the
       <file> specifier. That variable will be replaced with the current string for the URL
       being fetched.

-O, --remote-name
      Write output to a local file named like the remote file we get. (Only the file part of
      the remote file is used, the path is cut off.

-J, --remote-header-name
       (HTTP) This option tells the -O, --remote-name option to use the server-specified
       Content-Disposition filename instead of extracting a filename from the URL.
```