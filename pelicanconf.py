#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# https://github.com/amitness/amitness.github.io/blob/source/pelicanconf.py
# https://github.com/alexandrevicenzi/blog
# https://github.com/garybake/blog
# https://github.com/cassiobotaro/cassiobotaro.github.io/blob/pelican/pelicanconf.py

from __future__ import unicode_literals

# Theme-specific settings
SITENAME = u'Krystian Safjan\'s blog'
DOMAIN = 'http://localhost:8000'
SITE_AUTHOR = 'Krystian Safjan'
AUTHOR = u'Krystian Safjan'

# Note under profile image
SITESUBTITLE = '<hr>Independent Data Science Consultant.</br>I blog about Machine Learning, Deep Learning and NLP.<hr>'

# Description thet goes to metadata
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR

INDEX_DESCRIPTION = 'A machine learning consultant with core expertise in Python and related technologies.'

SITELOGO = '/images/profile.jpg'
FAVICON = '/extra/favicon.ico'

ICONS_PATH = 'images/icons'

SITEURL = 'https://safjan.com'
SITEURL = ''
KEYWORDS = u'Krystian Safjan blog'

# Path to content directory to be processed by Pelican.
PATH = 'content'

# Where to output the generated files
OUTPUT_PATH = 'docs'

THEME = '/home/izix/blog/pelican-themes/Flex'
#THEME = 'pelican-themes/Flex'

THEME_COLOR = '#FF8000'

# languages settings
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'https://safjan.com'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Social widget
SOCIAL = (
    (
        'linkedin',
        'https://pl.linkedin.com/in/krystiansafjan'
    ),
        (
        'github',
        'https://github.com/izikeros'
    ),
    (
        'envelope-o',
        'mailto:ksafjan@gmail.com'
    ),
    (
        'mortar-board',
        'https://scholar.google.pl/citations?user=UlNJgMoAAAAJ'
    ),
    (
        'rss',
         '/feeds/all.rss.xml')
    # add Kaggle
    )

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
MENUITEMS = (('Home', '/index.html'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             #('Popular', '/tags.html'),
             )

DISQUS_SITENAME = 'krystian-safjan'
GOOGLE_ANALYTICS = 'UA-117080232-1'

#DEFAULT_PAGINATION = False
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 42

DISPLAY_PAGES_ON_MENU = True


# url and path settings
RELATIVE_URLS = False
CACHE_CONTENT = False

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

STATIC_PATHS = [
    'images',
    'downloads',
    'extra/robots.txt',
    'extra/favicon.ico'
]
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    'extra/favicon.ico': {'path': 'favicon.ico'}
#}

PLUGIN_PATHS = ['./pelican-plugins']
#PLUGIN_PATHS = ['C:/Users/safjan/projects/blog/pelican-plugins']

#PLUGINS = ['pelican-ipynb.markup', 'tag_cloud', 'neighbors','post_stats','related_posts','representative_image']
PLUGINS = [
        'pelican-ipynb.markup',
        'tag_cloud',
        'neighbors',
        'post_stats',
        'related_posts',
        'representative_image'
        ]
#PLUGINS = ['tag_cloud']

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
