#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Krystian Safjan'
SITENAME = u'Safjan\'s blog'
# SITESUBTITLE = u'Samael500'
SITEURL = '/'
#SITEURL = 'https://izikeros.github.com/blog'
KEYWORDS = u'Krystian Safjan personal blog'

# Path to content directory to be processed by Pelican.
PATH = 'content'

# Where to output the generated files
OUTPUT_PATH = 'docs'

# languages settings
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL

# Blogroll
"""
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)
"""
# Social widget
# Social widget
SOCIAL = (
    # 3247880
    ('<i class="fa-li fa fa-stack-overflow"></i> Stack', 'https://stackoverflow.com/users/3247880'),
    ('<i class="fa-li fa fa-linkedin"></i> Linkedin', 'https://www.linkedin.com/in/krystiansafjan'),
    ('<i class="fa-li fa fa-envelope"></i> Gmail', 'mailto:gmail.com'),
    ('<i class="fa-li fa fa-github"></i> Github', 'https://github.com/izikeros'),
)

# TWITTER_USERNAME = 'samael500'
GITHUB_URL = ''
GOOGLE_CUSTOM_SEARCH = '006263355362628034990:cuxoisonrno'

THEME = '/home/bulk/blogs/blog/pelican-themes/my-w3-personal-blog'

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 2

# url and path settings
RELATIVE_URLS = False
CACHE_CONTENT = False
#STATIC_PATHS = ['icons', 'media', 'extra', 'emojify', 'stuff', ]

# article
ARTICLE_URL = u'articles/{category}/{slug}/'
ARTICLE_SAVE_AS = u'articles/{category}/{slug}/index.html'

# page
PAGE_URL = u'{slug}/'
PAGE_SAVE_AS = u'{slug}/index.html'

# author
AUTHOR_URL = u'author/{slug}/'
AUTHOR_SAVE_AS = u'author/{slug}/index.html'

# authors
AUTHORS_URL = u'authors/'
AUTHORS_SAVE_AS = u'authors/index.html'

# category
CATEGORY_URL = u'category/{slug}.html'
CATEGORY_SAVE_AS = u'category/{slug}.html'

# tag
TAG_URL = u'tag/{slug}/'
TAG_SAVE_AS = u'tag/{slug}/index.html'

# Count of different font sizes in the tag cloud.
TAG_CLOUD_STEPS = 4

# Maximum number of tags in the cloud
TAG_CLOUD_MAX_ITEMS = 100
