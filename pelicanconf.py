#!/usr/bin/env python

# Pelican documentation (latest)
# https://docs.getpelican.com/en/latest/settings.html#basic-settings
#
# Trying to apply literate configurations (https://leanpub.com/lit-config/read)


# --Elegant theme
# https://jackdewinter.github.io/


AUTHOR = 'Krystian Safjan'
SITENAME = "Krystian Safjan's blog"

MY_THEME = 'flex' # flex | elegant
IS_DEVELOPMENT = True
# ---- Development settings
if IS_DEVELOPMENT:
	SITEURL = ''
	RELATIVE_URLS = True
	CACHE_CONTENT = False
else:
	# TODO: keep only development config here, use publishconf.py to produce publication content
	SITEURL = 'https://safjan.com'
	RELATIVE_URLS = False
	CACHE_CONTENT = True
	# -------------- Third party ------
	DISQUS_SITENAME = 'krystian-safjan'
	GOOGLE_ANALYTICS = 'UA-117080232-1'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

GITHUB_URL = "https://github.com/izikeros"
# ---- Side ----
if MY_THEME == 'flex':
    # Note under profile image
    SITESUBTITLE = '<hr><p style="font-size:220%">Krystian Safjan\'s Blog</p><p>Data Scientist | Researcher | Team Leader</p></br></br>I\'m working at Nokia and writing about <a href="/category/data-science.html">Data Science and Visualization</a>, on <a href="/category/data-science.html">Machine Learning, Deep Learning</a> and <a href="/tag/nlp/">NLP</a>. There are also some <a href="/category/howto.html">howto</a> posts on tools and workflows.</li></ul><hr>'
    SITELOGO = '/images/profile_new.jpg'

# define landing page for elegant style
if MY_THEME == 'elegant':
    LANDING_PAGE_TITLE='Krystian Safjan'
    RECENT_ARTICLE_SUMMARY = True # Elegant
    FEATURED_IMAGE = True

# --------------- RSS and Social Media ------------
# Feed generation is usually not desired when developing
if IS_DEVELOPMENT:
	FEED_ALL_ATOM = None
	FEED_ALL_RSS = None
	CATEGORY_FEED_ATOM = None
else:	
	FEED_DOMAIN = 'https://safjan.com'
	FEED_ALL_ATOM = 'feeds/all.atom.xml'
	FEED_ALL_RSS = 'feeds/all.rss.xml'
# Social widget
# https://github.com/alexandrevicenzi/Flex/wiki/Flex-Menus
# How to modify mine glyphs?
#   - 
#   - 

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
        'envelope',
        'mailto:ksafjan@gmail.com'
    ),
    # (
    #     'mortar-board', #'mortar-board',
    #     'https://scholar.google.pl/citations?user=UlNJgMoAAAAJ'
    # ),
    (
        'rss',
         '/feeds/all.rss.xml')
    # add Kaggle
    )

LINKS = (
    # (
    #     'linkedin',
    #     'https://pl.linkedin.com/in/krystiansafjan'
    # ),
    #     (
    #     'github',
    #     'https://github.com/izikeros'
    # ),
    # (
    #     'email',
    #     'mailto:ksafjan@gmail.com'
    # ),
    # (
    #     'google scholar', #'mortar-board',
    #     'https://scholar.google.pl/citations?user=UlNJgMoAAAAJ'
    # ),
    # (
    #     'rss',
    #      '/feeds/all.rss.xml')
    # add Kaggle
    )
# --------------- Layout ---------------------
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
MENUITEMS = (('All Posts', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Resume','/pdfs/Krystian_Safjan_resume_priv.pdf'),
             )
HOME_HIDE_TAGS = True         # ??
DEFAULT_PAGINATION = 20
SUMMARY_MAX_LENGTH = 42
DISPLAY_PAGES_ON_MENU = True  # Display in sidebar links to articles located in 'pages'

from datetime import datetime
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True

#------- Footer ---------------------------
from datetime import datetime
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}



# ----------------- Resources ------------------
STATIC_PATHS = [
    'styles',
    'images',
    'robots.txt',
    'favicon.ico',
    '.nojekyll',
    'pdfs',
    'zipfiles']

# ----------- Theme, CSS and other styling
PYGMENTS_STYLE = "github" # github | monokai # FLEX
if MY_THEME == 'elegant':
    THEME = 'pelican-themes/elegant'   # flex | elegant
    # NOTE: style customization for elegant:
    # elegant/static/css/custom.css
elif MY_THEME == 'flex':
    THEME = 'pelican-themes/flex'   # flex | elegant
    # THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
    THEME_COLOR_ENABLE_USER_OVERRIDE = True
    USE_LESS = True
    CUSTOM_CSS = 'styles/custom.css'

TYPOGRIFY = True

# Where to output the generated files
OUTPUT_PATH = 'docs'

# -------------- Slugs and URLs --------------

# article
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# page
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

# authors
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

# category
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# tag
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'


# -------------- Plugins
IGNORE_FILES = [".ipynb_checkpoints"]
PLUGIN_PATHS = ['./pelican-plugins']

MARKUP = ("md", "ipynb")

if MY_THEME == 'flex':
    PLUGINS = [
            'pelican-ipynb.markup',
            'post_stats',
            'representative_image',
            'render_math',
            'neighbors',
            'related_posts',
            ]
elif MY_THEME == 'elegant':
    PLUGINS = [
            'pelican-ipynb.markup',
            'post_stats',
            'representative_image'
            ]

# ----- SEO -----------
SEO_REPORT = True 
SEO_ENHANCER = True 
SEO_ENHANCER_OPEN_GRAPH = False 