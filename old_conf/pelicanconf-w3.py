#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Krystian Safjan'
SITENAME = u'Krystian Safjan\'s blog'
# SITESUBTITLE = u'with love for data science'
SITEURL = 'https://samael500.github.io'
KEYWORDS = u'Krystian Safjan personal blog'

PATH = 'content'

# languages settings
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = u'en'


#THEME = '../my-w3-personal-blog'
THEME = "/home/bulk/blogs/pelican-blog/pelican-themes/my-w3-personal-blog"


"""
ARCHIVES_TEXT = u'Аrchive'
ARTICLESCATEGORY_TEXT = u'A'
ARTICLESTAG_TEXT = u'Статьи с тегом'
AUTHOR_TEXT = u'Автор'
AUTHORS_TEXT = u'Авторы'
CATEGORIES_TEXT = u'Категории'
CATEGORY_TEXT = u'Категория'
TAGS_TEXT = u'Теги'
COMMENTS_TEXT = u'Комментарии'
CONTENT_TEXT = u'Содержимое'
FIRST_TEXT = u'первая'
LAST_TEXT = u'последняя'
READMORE_TEXT = u'далее...'
"""

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
SOCIAL = (
    # 3247880
    ('<i class="fa-li fa fa-stack-overflow"></i> Stack', 'https://stackoverflow.com/users/3247880'),
    ('<i class="fa-li fa fa-linkedin"></i> Linkedin', 'https://www.linkedin.com/in/krystiansafjan'),
    ('<i class="fa-li fa fa-envelope"></i> Gmail', 'mailto:gmail.com'),
    ('<i class="fa-li fa fa-github"></i> Github', 'https://github.com/izikeros'),
)

#
SHARETHIS_PUB_KEY = ''

TAG_CLOUD_STEPS = True

# TWITTER_USERNAME = 'samael500'
# GITHUB_URL = 'https://github.com/izikeros'
GOOGLE_CUSTOM_SEARCH = '006263355362628034990:cuxoisonrno'


DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10

# url and path settings
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

CACHE_CONTENT = False
# STATIC_PATHS = ['icons', 'media', 'extra', 'emojify', 'stuff', ]
STATIC_PATHS = ['images', 'data', 'pdf' ]

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


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './pelican-plugins'
PLUGINS = ['ipynb.markup']

