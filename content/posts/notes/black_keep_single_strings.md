---
category: note
date: '2022-05-12'
status: published
slug: black-keep-single-quotes-strings
tags: black, single-string, quotation-mark
title: Black - keep single quotes for strings
---

See: [Add --single-quote option · Issue #594 · psf/black · GitHub](https://github.com/psf/black/issues/594)

Currently, it requires everyone who uses single quotes to run black and then have a second tool (we use pre-commit double-quote-string-fixer) to ensure that single quotes are being used consistently.

From black documentation:
> If you are adopting *Black* in a large project with pre-existing string conventions (like the popular [“single quotes for data, double quotes for human-readable strings”](https://stackoverflow.com/a/56190)), you can pass `--skip-string-normalization` on the command line. This is meant as an adoption helper, avoid using this for new projects.