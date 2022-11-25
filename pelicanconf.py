#!/usr/bin/env python

# Pelican documentation (latest)
# https://docs.getpelican.com/en/latest/settings.html#basic-settings
#
# Trying to apply literate configurations (https://leanpub.com/lit-config/read)


# --Elegant theme
# https://jackdewinter.github.io/


AUTHOR = "Krystian Safjan"
SITENAME = "Krystian Safjan's Blog"

MY_THEME = "flex"  # flex | elegant, NOTE: this is nit name of the folder in pelican themes - search below for `THEME =`
IS_DEVELOPMENT = True
USE_APPLAUSE = False
# ---- Development settings
if IS_DEVELOPMENT:
    SITEURL = ""
    RELATIVE_URLS = True
    CACHE_CONTENT = False
else:
    # TODO: keep only development config here, use publishconf.py to produce publication content
    SITEURL = "https://safjan.com"
    RELATIVE_URLS = False
    CACHE_CONTENT = True
    # -------------- Third party ------
    # DISQUS_SITENAME = 'krystian-safjan'
    GOOGLE_ANALYTICS = "G-RM2PKDCCYM" # v3:"UA-117080232-1"   v4:"G-RM2PKDCCYM"

PATH = "content"

TIMEZONE = "Europe/Warsaw"

DEFAULT_LANG = "en"

GITHUB_URL = "https://github.com/izikeros"
# ---- Side ----
if MY_THEME == "flex":
    # Note under profile image
    # SITESUBTITLE = '<p>Data Scientist | Researcher | Team Leader</p><br/><br/>I\'m working at Ernst ;amp& Young and writing about <a href="/category/data-science.html">Data Science and Visualization</a>, on <a href="/category/data-science.html">Machine Learning, Deep Learning</a> and <a href="/tag/nlp/">NLP</a>. There are also some <a href="/category/howto.html">howto</a> posts on tools and workflows.</li></ul><hr>'
    SITETITLE = SITENAME  # Used in Flex theme
    # Search for SITESUBTITLE usage in Flex/templates/base.html
    # SITESUBTITLE = 'Data Scientist | Researcher | Team Leader<br><br> working at ' \
    #                'Ernst &amp; Young and writing about <a ' \
    #                'href="/category/data-science.html">Data Science and Visualization</a>, ' \
    #                'on <a href="/category/data-science.html">Machine Learning, Deep Learning</a> ' \
    #                'and <a href="/tag/nlp/">NLP</a>. There are also some  ' \
    #                '<a href="/category/howto.html">howto</a> posts on tools and workflows.<hr>'

    SITESUBTITLE = 'Data Scientist | Researcher | Team Leader<br><br> working at ' \
                   'Ernst &amp; Young and writing about <a ' \
                   'href="/category/data-science.html">Data Science and Visualization</a>, ' \
                   'on <a href="/category/data-science.html">Machine Learning, Deep Learning</a> ' \
                   'and <a href="/tag/nlp/">NLP</a>. There are also some  ' \
                   '<a href="/category/howto.html">howto</a> posts on tools and workflows.'
    SITELOGO = "/images/profile_new.jpg"
    DISPLAY_DATE_AFTER_TITLE = (
        False  # display date in the list of articles (tags, categories)
    )

# define landing page for elegant style
if MY_THEME == "elegant":
    LANDING_PAGE_TITLE = "Krystian Safjan"
    RECENT_ARTICLE_SUMMARY = True  # Elegant
    FEATURED_IMAGE = True

# --------------- RSS and Social Media ------------
# Feed generation is usually not desired when developing
if IS_DEVELOPMENT:
    FEED_ALL_ATOM = None
    FEED_ALL_RSS = None
    CATEGORY_FEED_ATOM = None
else:
    FEED_DOMAIN = "https://safjan.com"
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    FEED_ALL_RSS = "feeds/all.rss.xml"
# Social widget
# https://github.com/alexandrevicenzi/Flex/wiki/Flex-Menus


SOCIAL = (
    ("linkedin", "https://pl.linkedin.com/in/krystiansafjan"),
    ("github", "https://github.com/izikeros"),
    ("envelope", "mailto:ksafjan@gmail.com"),
    (
        "graduation-cap",  #'mortar-board | newspaper' or 'graduation-cap'
        "https://scholar.google.pl/citations?user=UlNJgMoAAAAJ",
    ),
    ("rss", "/feeds/all.rss.xml")
    # add Kaggle
)
# https://fontawesome.com/v5.15/icons/graduation-cap?style=solid

# --------------- Layout ---------------------
# How main menu works: https://github.com/alexandrevicenzi/Flex/wiki/Flex-Menus
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
MENUITEMS = (
    ("Articles", "/archives.html"),
    ("Notes", "/til.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    ("Resume", "/pdfs/Krystian_Safjan_resume_priv.pdf"),
)


HOME_HIDE_TAGS = (
    True  # Shall the tags be hidden when displaying list of articles on home page?
)
DEFAULT_PAGINATION = 200
SUMMARY_MAX_LENGTH = 42
DISPLAY_PAGES_ON_MENU = False  # Display in sidebar links to articles located in 'pages'
DEFAULT_DATE_FORMAT = (
    "%B %d, %Y"  # '%B %d, %Y' -> December 29, 2021, '%Y-%m-%d' -> 2021-12-29
)


# Article heading
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = False

DATE_FOR_ARTICLE_GROUPS = False


DIRECT_TEMPLATES = ["index", "categories", "tags", "archives", "til"]
# DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives']

# ------- Footer ---------------------------
from datetime import datetime

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}


# ----------------- Resources ------------------
STATIC_PATHS = [
    "styles",
    "images",
    "robots.txt",
    "favicon.ico",
    ".nojekyll",
    "pdfs",
    "zipfiles",
    "CNAME",
    "ads.txt",
]

# ----------- Theme, CSS and other styling
PYGMENTS_STYLE = "github"  # github | monokai # FLEX
if MY_THEME == "elegant":
    THEME = "pelican-themes/elegant"  # flex | elegant
    # NOTE: style customization for elegant:
    # elegant/static/css/custom.css
elif MY_THEME == "flex":
    THEME = "pelican-themes/Flex"  # flex | elegant
    # THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
    THEME_COLOR_ENABLE_USER_OVERRIDE = False
    USE_LESS = False
    CUSTOM_CSS = "styles/custom.css"

TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ["style", "script", "title", "code", "pre"]

# Where to output the generated files
OUTPUT_PATH = "docs"

# -------------- Slugs and URLs --------------

# article
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

# page
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# author
AUTHOR_URL = "author/{slug}/"
# AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_SAVE_AS = ""

# authors
AUTHORS_URL = "authors/"
#AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_SAVE_AS = ""

# category
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

# tag
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

DEFAULT_METADATA = {
    "status": "draft",
}

# -------------- Plugins
IGNORE_FILES = [".ipynb_checkpoints"]
PLUGIN_PATHS = ["./pelican-plugins"]

MARKUP = ("md", "ipynb")

if MY_THEME == "flex":
    PLUGINS = [
        "pelican-ipynb.markup",
        # 'post_stats',
        "representative_image",
        "render_math",
        "neighbors",
        "related_posts",
        "share_post",
        "sitemap",
    ]
elif MY_THEME == "elegant":
    PLUGINS = ["pelican-ipynb.markup", "post_stats", "representative_image"]

# Preprocessing - remove empty cells and cells tagged with "remove_cell"
#  NOTE: Tag cells to remove with "remove_cell" (View -> Cell Toolbar -> Tags)
from nbconvert.preprocessors import (
    RegexRemovePreprocessor,
    TagRemovePreprocessor,
)
from traitlets.config import Config

c = Config()
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ("remove_output",)
c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)
c.TagRemovePreprocessor.enabled = True
IPYNB_PREPROCESSORS = [
    RegexRemovePreprocessor(
        patterns=["\s*\Z"]
    ),  # Remove empty cells (or cells with whitespaces only)
    TagRemovePreprocessor(config=c),
]  # Remove cells marked as 'remove_cell'

# ----- SEO -----------
SEO_REPORT = False
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True


SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.6,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    },
}
ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"

# The code for google ads is in templates/partials/google_automatic_ads.html
USE_GOOGLE_AUTO_ADS = True
