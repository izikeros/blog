#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)

# ---- Use the setting from pelicanconf.py
from pelicanconf import *

# --- But overwrite some of them
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://www.safjan.com"
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = 'krystian-safjan'
GOOGLE_ANALYTICS = "UA-117080232-1"
