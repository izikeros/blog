#!/usr/bin/env python
"""Pelican blog configuration file

Documentation: https://docs.getpelican.com/en/latest/settings.html
"""

from datetime import datetime
from nbconvert.preprocessors import RegexRemovePreprocessor, TagRemovePreprocessor
from traitlets.config import Config

# =============================================================================
# BASIC SETTINGS
# =============================================================================

AUTHOR = "Krystian Safjan"
SITENAME = "Krystian Safjan's Blog"
SITETITLE = SITENAME
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"

PATH = "content"
OUTPUT_PATH = "docs"

# =============================================================================
# ENVIRONMENT CONFIGURATION
# =============================================================================

IS_DEVELOPMENT = True

if IS_DEVELOPMENT:
    SITEURL = "http://127.0.0.1:8000"
    RELATIVE_URLS = False
    CACHE_CONTENT = False
    FEED_ALL_ATOM = None
    FEED_ALL_RSS = None
    CATEGORY_FEED_ATOM = None
else:
    SITEURL = "https://safjan.com"
    RELATIVE_URLS = False
    CACHE_CONTENT = False
    FEED_DOMAIN = "https://safjan.com"
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    FEED_ALL_RSS = "feeds/all.rss.xml"
    GOOGLE_ANALYTICS = "G-RM2PKDCCYM"

# =============================================================================
# THEME CONFIGURATION
# =============================================================================

MY_THEME = "flex"  # Options: flex | safi

THEME_CONFIG = {
    "flex": {
        "path": "pelican-themes/Flex",
        "theme_color_enable_user_override": True,
        "custom_css": "styles/custom.css",
    },
    "safi": {
        "path": "pelican-themes/safi_theme",
        "search_enabled": True,
        "dark_mode": True,
    },
}

THEME = THEME_CONFIG[MY_THEME]["path"]

# Theme-specific settings for Flex
if MY_THEME == "flex":
    SITELOGO = "/images/profile_new.jpg"
    SITESUBTITLE = (
        "Data Scientist | Researcher | Team Leader<br><br> working at "
        "Ernst &amp; Young and writing about <a "
        'href="/category/machine-learning.html">Data Science and Visualization</a>, '
        'on <a href="/category/machine-learning.html">Machine Learning, Deep Learning</a> '
        'and <a href="/tag/nlp/">NLP</a>. There are also some '
        '<a href="/category/howto.html">howto</a> posts on tools and workflows.'
    )
    DISPLAY_DATE_AFTER_TITLE = False
    DISPLAY_DATE_BEFORE_TITLE = True
    PROMO_BOX = True
    CUSTOM_CSS = THEME_CONFIG["flex"]["custom_css"]
    THEME_COLOR_ENABLE_USER_OVERRIDE = THEME_CONFIG["flex"]["theme_color_enable_user_override"]

# Theme-specific settings for Safi
elif MY_THEME == "safi":
    SAFI_SEARCH_ENABLED = THEME_CONFIG["safi"]["search_enabled"]
    SAFI_DARK_MODE = THEME_CONFIG["safi"]["dark_mode"]

# =============================================================================
# CONTENT AND LAYOUT
# =============================================================================

# Date formatting
DATE_FORMATS = {"en": "%Y-%m-%d"}
DEFAULT_DATE_FORMAT = "%B %d, %Y"

# Article display
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = False
DATE_FOR_ARTICLE_GROUPS = False
ENABLE_TOC = True  # Enable/disable Table of Contents generation

# Pagination and summaries
# DEFAULT_PAGINATION controls Pelican's internal pagination (set to match filtered page count)
# INDEX_ARTICLES_PER_PAGE controls visible articles per page (via exclude_category plugin)
# Formula: DEFAULT_PAGINATION = total_articles / (filtered_articles / INDEX_ARTICLES_PER_PAGE)
# With ~317 total, ~79 filtered, 10 per page = 8 pages needed, so 317/8 ≈ 40
DEFAULT_PAGINATION = 40
SUMMARY_MAX_LENGTH = 42
HOME_HIDE_TAGS = True

# Exclude categories from index (handled by exclude_category plugin)
INDEX_EXCLUDE_CATEGORIES = ['note']
INDEX_ARTICLES_PER_PAGE = 10

# Menu configuration
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ("Articles", "/archives.html"),
    ("Notes", "/til.html"),
    ("Categories", "/categories.html"),
    ("Resume", "/pdfs/Krystian_Safjan_resume_priv.pdf"),
)

DIRECT_TEMPLATES = ["index", "categories", "tags", "archives", "til"]

# =============================================================================
# URL AND SLUG CONFIGURATION
# =============================================================================

# Article URLs
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

# Page URLs
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Author URLs (disabled)
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = ""
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = ""

# Category URLs
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

# Tag URLs
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Default metadata
DEFAULT_METADATA = {"status": "draft"}

# =============================================================================
# SOCIAL MEDIA AND EXTERNAL LINKS
# =============================================================================

GITHUB_URL = "https://github.com/izikeros"
TWITTER_USERNAME = "izikeros"
TWITTER_CREATOR = "izikeros"

SOCIAL = (
    ("linkedin", "https://pl.linkedin.com/in/krystiansafjan"),
    ("github", "https://github.com/izikeros"),
    ("envelope", "mailto:ksafjan@gmail.com"),
    ("graduation-cap", "https://scholar.google.pl/citations?user=UlNJgMoAAAAJ"),
    ("rss", "/feeds/all.rss.xml"),
)

# =============================================================================
# STATIC FILES AND RESOURCES
# =============================================================================

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

# =============================================================================
# STYLING AND APPEARANCE
# =============================================================================

PYGMENTS_STYLE = "github"
TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ["style", "script", "title", "code", "pre"]

# =============================================================================
# FOOTER AND COPYRIGHT
# =============================================================================

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

# =============================================================================
# MARKDOWN AND MARKUP CONFIGURATION
# =============================================================================

MARKUP = ("md", "ipynb")

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "title": "",
            "toc_depth": "2-3",
            "permalink": False,
        },
        "markdown_mermaidjs": {},
    },
    "output_format": "html5",
}

USE_MERMAID = False
ADD_BIBTEX_NOTE = True
BIBTEX_JOURNAL = "Krystian's Safjan Blog"

# =============================================================================
# JUPYTER NOTEBOOK CONFIGURATION
# =============================================================================

IGNORE_FILES = [".ipynb_checkpoints"]

# Jupyter preprocessing configuration
c = Config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ("remove_output",)
c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)

IPYNB_PREPROCESSORS = [
    RegexRemovePreprocessor(patterns=[r"\s*\Z"]),  # Remove empty cells
    TagRemovePreprocessor(config=c),  # Remove tagged cells
]

# =============================================================================
# PLUGINS CONFIGURATION
# =============================================================================

PLUGIN_PATHS = ["./pelican-plugins"]

PLUGINS = [
    "exclude_category",
    "yaml_metadata",
    "seo_leo_enhancer",
]

# Other plugins (uncomment as needed):
# "featured_image", "render_math", "neighbors", "related_posts",
# "sitemap", "pelican_obsidian", "pelican_jupyter"

# =============================================================================
# SEO CONFIGURATION
# =============================================================================

SEO_REPORT = False
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = False
SEO_ARTICLES_LIMIT = 10
SEO_PAGES_LIMIT = 10

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

# =============================================================================
# THIRD-PARTY INTEGRATIONS
# =============================================================================

USE_GOOGLE_AUTO_ADS = True
USE_APPLAUSE = False

# Uncomment for production
# DISQUS_SITENAME = 'krystian-safjan'
