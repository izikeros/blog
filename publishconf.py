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
# Must match content/CNAME: www.safjan.com 301-redirects to the apex domain,
# so canonical URLs, sitemap and feeds must use the apex.
SITEURL = "https://safjan.com"
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
FEED_MAX_ITEMS = 30

# Disable unused feeds
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = 'krystian-safjan'
GOOGLE_ANALYTICS = "G-RM2PKDCCYM" # v3:"UA-117080232-1"   v4:"G-RM2PKDCCYM"
USE_APPLAUSE = False
DISPLAY_DATE_BEFORE_TITLE = (
    False  # display date in the list of articles (tags, categories)
)
