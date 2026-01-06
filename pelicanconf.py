#!/usr/bin/env python
"""
Pelican Configuration for Krystian Safjan's Blog
================================================

This configuration file controls all aspects of the blog generation.

Quick Start:
    - Set IS_DEVELOPMENT = True for local development (no feeds, no analytics)
    - Set IS_DEVELOPMENT = False before publishing to production

Key Customization Points:
    - PLUGINS: Enable/disable plugins in the PLUGINS list
    - FEED_UTM_PARAMS: Customize UTM tracking parameters for RSS/Atom feeds
    - INDEX_EXCLUDE_CATEGORIES: Categories to hide from main index

Documentation: https://docs.getpelican.com/en/latest/settings.html
"""

from datetime import datetime

# =============================================================================
# SITE IDENTITY
# =============================================================================

AUTHOR = "Krystian Safjan"
SITENAME = "Krystian Safjan's Blog"
SITETITLE = SITENAME  # Used in <title> tag, can differ from SITENAME
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"

# =============================================================================
# PATHS AND OUTPUT
# =============================================================================

PATH = "content"              # Source content directory
OUTPUT_PATH = "docs"          # Generated site output (GitHub Pages compatible)

# Files and directories to copy as-is to output
STATIC_PATHS = [
    "styles",      # Custom CSS
    "images",      # Article images and assets
    "pdfs",        # PDF files (resume, etc.)
    "zipfiles",    # Downloadable archives
    "robots.txt",  # Search engine directives
    ".nojekyll",   # Disable Jekyll processing on GitHub Pages
    "CNAME",       # Custom domain for GitHub Pages
    "ads.txt",     # Ads.txt for ad networks
    # Favicon files (generate at https://realfavicongenerator.net/)
    "favicon.ico",
    "apple-touch-icon.png",
    "favicon-32x32.png",
    "favicon-16x16.png",
    "site.webmanifest",
    # "safari-pinned-tab.svg",  # Optional: Safari pinned tabs
    # "browserconfig.xml",       # Optional: Windows tiles
]

# =============================================================================
# ENVIRONMENT CONFIGURATION (Development vs Production)
# =============================================================================
# Toggle this single variable to switch between dev and production settings

IS_DEVELOPMENT = True

if IS_DEVELOPMENT:
    # Local development settings
    SITEURL = "http://127.0.0.1:8000"
    RELATIVE_URLS = False
    CACHE_CONTENT = False
    # Disable feeds in development
    FEED_ALL_ATOM = None
    FEED_ALL_RSS = None
    CATEGORY_FEED_ATOM = None
else:
    # Production settings
    SITEURL = "https://safjan.com"
    RELATIVE_URLS = False
    CACHE_CONTENT = False
    # Enable feeds in production
    FEED_DOMAIN = "https://safjan.com"
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    FEED_ALL_RSS = "feeds/all.rss.xml"
    # Analytics (only in production)
    GOOGLE_ANALYTICS = "G-RM2PKDCCYM"

# =============================================================================
# FEEDS CONFIGURATION
# =============================================================================
# RSS/Atom feeds are only generated in production (IS_DEVELOPMENT = False)

# Maximum items in feed (None = unlimited)
FEED_MAX_ITEMS = 100

# UTM parameters added to feed links for Google Analytics tracking
# These help identify traffic coming from RSS readers
FEED_UTM_PARAMS = {
    'utm_source': 'rss',       # Traffic source identifier
    'utm_medium': 'feed',      # Marketing medium
    'utm_campaign': 'safjan-blog'  # Campaign name for tracking
}

# =============================================================================
# THEME CONFIGURATION (Flex theme)
# =============================================================================

THEME = "pelican-themes/Flex"

# Site branding
SITELOGO = "/images/profile_new.jpg"
SITESUBTITLE = (
    "Data Scientist | Researcher | Team Leader<br><br> working at "
    "Ernst &amp; Young and writing about <a "
    'href="/category/machine-learning.html">Data Science and Visualization</a>, '
    'on <a href="/category/machine-learning.html">Machine Learning, Deep Learning</a> '
    'and <a href="/tag/nlp/">NLP</a>. There are also some '
    '<a href="/category/howto.html">howto</a> posts on tools and workflows.'
)

# Theme display options
DISPLAY_DATE_BEFORE_TITLE = True   # Show date above article title
DISPLAY_DATE_AFTER_TITLE = False   # Don't show date below title
PROMO_BOX = True                   # Show promotional content box in sidebar
CUSTOM_CSS = "styles/custom.css"   # Path to custom stylesheet
THEME_COLOR_ENABLE_USER_OVERRIDE = True  # Allow dark/light mode toggle

# Code syntax highlighting theme (Pygments)
# Options: monokai, github, friendly, colorful, etc.
PYGMENTS_STYLE = "github"

# Favicon configuration
# Option 1: Simple favicon - set FAVICON = "/favicon.ico"
# Option 2: RealFaviconGenerator package (recommended for all platforms)
#   Generate at https://realfavicongenerator.net/ and place files in content/
RFG_FAVICONS = True                    # Enable full favicon package
RFG_THEME_COLOR = "#333333"            # Browser theme color (address bar, etc.)
# RFG_SAFARI_PINNED_TAB = "#5bbad5"    # Optional: Safari pinned tab icon color
# RFG_MSAPPLICATION_TILECOLOR = "#da532c"  # Optional: Windows tile color

# YouTube Auto-Embed
# Converts bare YouTube URLs and Obsidian vid code blocks to embedded players
# Supports: youtube.com/watch?v=, youtu.be/, and ```vid code fences
YOUTUBE_EMBED = True

# =============================================================================
# CONTENT DISPLAY
# =============================================================================

# Date formatting
DATE_FORMATS = {"en": "%Y-%m-%d"}      # Format: 2024-01-15
DEFAULT_DATE_FORMAT = "%B %d, %Y"       # Format: January 15, 2024

# Article metadata display
SHOW_ARTICLE_AUTHOR = False    # Hide author name (single-author blog)
SHOW_ARTICLE_CATEGORY = False  # Hide category in article header
SHOW_DATE_MODIFIED = False     # Hide "last modified" date
HOME_HIDE_TAGS = True          # Hide tags on home page article cards

# Table of Contents
ENABLE_TOC = False  # Disable automatic TOC generation

# Typography enhancement (smart quotes, etc.)
TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ["style", "script", "title", "code", "pre"]

# =============================================================================
# PAGINATION AND INDEX FILTERING
# =============================================================================
# The exclude_category plugin provides filtered, paginated article lists

# Categories to exclude from main index (articles still accessible directly)
INDEX_EXCLUDE_CATEGORIES = ['note']

# Number of articles per page on filtered index
INDEX_ARTICLES_PER_PAGE = 10

# Pelican's internal pagination setting
# Formula: total_articles / (filtered_articles / INDEX_ARTICLES_PER_PAGE)
# With ~317 total articles, ~79 filtered, 10/page = 8 pages → 317/8 ≈ 40
DEFAULT_PAGINATION = 40

# Auto-generated summary length (in words) when Summary not in frontmatter
SUMMARY_MAX_LENGTH = 42

# Default status for new articles without explicit Status in frontmatter
DEFAULT_METADATA = {"status": "draft"}

# =============================================================================
# NAVIGATION AND MENUS
# =============================================================================

MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False  # Don't auto-add pages to menu
USE_FOLDER_AS_CATEGORY = False  # Don't use folder structure for categories

# Main navigation menu items
MENUITEMS = (
    ("Articles", "/archives.html"),
    ("Notes", "/til.html"),
    ("Categories", "/categories.html"),
    ("Resume", "/pdfs/Krystian_Safjan_resume_priv.pdf"),
)

# Templates to generate (besides articles and pages)
DIRECT_TEMPLATES = ["index", "categories", "tags", "archives", "til"]

# =============================================================================
# URL PATTERNS
# =============================================================================
# Clean URLs without .html extension for articles and pages

# Article URLs: /article-slug/
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

# Page URLs: /page-slug/
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Category URLs: /category/category-name.html
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

# Tag URLs: /tag/tag-name/
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Author pages (disabled - single author blog)
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = ""      # Empty = don't generate
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = ""     # Empty = don't generate

# =============================================================================
# SOCIAL MEDIA AND LINKS
# =============================================================================

GITHUB_URL = "https://github.com/izikeros"
TWITTER_USERNAME = "izikeros"
TWITTER_CREATOR = "izikeros"  # For Twitter Cards

# Social links displayed in sidebar/footer
# Format: (icon-name, url) - icons from Font Awesome
SOCIAL = (
    ("linkedin", "https://pl.linkedin.com/in/krystiansafjan"),
    ("github", "https://github.com/izikeros"),
    ("envelope", "mailto:ksafjan@gmail.com"),
    ("graduation-cap", "https://scholar.google.pl/citations?user=UlNJgMoAAAAJ"),
    ("rss", "/feeds/all.rss.xml"),
)

# =============================================================================
# FOOTER AND COPYRIGHT
# =============================================================================

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR

# Creative Commons license configuration
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",  # Used to construct CC license URL
}

# =============================================================================
# MARKDOWN CONFIGURATION
# =============================================================================

# Supported markup formats
MARKUP = ("md", "ipynb")

# Markdown extension configuration
MARKDOWN = {
    "extension_configs": {
        # Syntax highlighting for code blocks
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        # Extra features: tables, fenced code, footnotes, etc.
        "markdown.extensions.extra": {},
        # Metadata in markdown files
        "markdown.extensions.meta": {},
        # Table of contents generation
        "markdown.extensions.toc": {
            "title": "",
            "toc_depth": "2-3",     # Include h2 and h3 only
            "permalink": False,     # No permalink anchors
        },
        # Mermaid.js diagram support
        "markdown_mermaidjs": {},
    },
    "output_format": "html5",
}

# Mermaid diagram rendering
USE_MERMAID = False

# BibTeX citation block at end of articles
ADD_BIBTEX_NOTE = True
BIBTEX_JOURNAL = "Krystian's Safjan Blog"

# =============================================================================
# JUPYTER NOTEBOOK CONFIGURATION
# =============================================================================
# Settings for rendering .ipynb files as blog posts

from nbconvert.preprocessors import RegexRemovePreprocessor, TagRemovePreprocessor
from traitlets.config import Config

# Ignore Jupyter checkpoint files
IGNORE_FILES = [".ipynb_checkpoints"]

# Notebook cell preprocessing - remove tagged cells
c = Config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)           # Remove entire cell
c.TagRemovePreprocessor.remove_all_outputs_tags = ("remove_output",)  # Remove cell output only
c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)         # Remove cell input only

IPYNB_PREPROCESSORS = [
    RegexRemovePreprocessor(patterns=[r"\s*\Z"]),  # Remove empty cells
    TagRemovePreprocessor(config=c),               # Remove tagged cells
]

# =============================================================================
# PLUGINS
# =============================================================================

PLUGIN_PATHS = ["./pelican-plugins"]

PLUGINS = [
    "exclude_category",   # Filter categories from index, provide pagination
    "yaml_metadata",      # Parse YAML frontmatter in markdown files
    "seo_leo_enhancer",   # Extract TL;DR, FAQ, HowTo from content markers
    "feed_utm",           # Add UTM tracking params to RSS/Atom feeds
    "obsidian",           # Obsidian wiki-links and hashtag support
]

# Additional plugins (uncomment to enable):
# PLUGINS += [
#     "featured_image",    # Extract featured image from article
#     "render_math",       # LaTeX math rendering
#     "neighbors",         # Previous/next article links
#     "related_posts",     # Related articles suggestions
#     "sitemap",           # Generate sitemap.xml
#     "pelican_jupyter",   # Enhanced Jupyter notebook support
# ]

# =============================================================================
# SEO AND SEARCH
# =============================================================================

# SEO plugin configuration
SEO_REPORT = False              # Don't generate SEO analysis report
SEO_ENHANCER = True             # Enable SEO meta tag generation
SEO_ENHANCER_OPEN_GRAPH = True  # Generate Open Graph tags (Facebook, LinkedIn)
SEO_ENHANCER_TWITTER_CARDS = False  # Twitter Cards (using custom implementation)
SEO_ARTICLES_LIMIT = 10         # Articles to include in SEO report
SEO_PAGES_LIMIT = 10            # Pages to include in SEO report

# Sitemap configuration (requires sitemap plugin)
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

# Robots meta tag for search engines
# Allows indexing with full snippets and image previews
ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"

# =============================================================================
# THIRD-PARTY INTEGRATIONS
# =============================================================================

# Google AdSense auto ads
USE_GOOGLE_AUTO_ADS = True

# Applause button (reader appreciation)
USE_APPLAUSE = False

# Disqus comments (disabled)
# DISQUS_SITENAME = 'krystian-safjan'
