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

PATH = "content"  # Source content directory
OUTPUT_PATH = "docs"  # Generated site output (GitHub Pages compatible)

# Files and directories to copy as-is to output
STATIC_PATHS = [
    "styles",  # Custom CSS
    "images",  # Article images and assets
    "pdfs",  # PDF files (resume, etc.)
    "zipfiles",  # Downloadable archives
    "robots.txt",  # Search engine and AI crawler directives
    ".nojekyll",  # Disable Jekyll processing on GitHub Pages
    "CNAME",  # Custom domain for GitHub Pages
    "ads.txt",  # Ads.txt for ad networks
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
    "utm_source": "rss",  # Traffic source identifier
    "utm_medium": "feed",  # Marketing medium
    "utm_campaign": "safjan-blog",  # Campaign name for tracking
}

# =============================================================================
# THEME CONFIGURATION (Flex theme)
# =============================================================================

THEME = "pelican-themes/Flex"

# Site branding
SITELOGO = "/images/profile_new.jpg"
# Plain text: also used in feeds and llms.txt
SITESUBTITLE = (
    "AI/ML technical leader · building LLM & RAG systems in enterprise · "
    "evaluation, LLMOps, engineering leadership"
)

# Theme display options
DISPLAY_DATE_BEFORE_TITLE = True  # Show date above article title
DISPLAY_DATE_AFTER_TITLE = False  # Don't show date below title
PROMO_BOX = True  # Show promotional content box in sidebar
CUSTOM_CSS = "styles/custom.css"  # Path to custom stylesheet
USE_GOOGLE_FONTS = False  # System font stack: no render-blocking third-party CSS
THEME_COLOR_ENABLE_USER_OVERRIDE = True  # Allow dark/light mode toggle

# Homepage blocks (first page only), see Flex README "Homepage"
START_HERE = [
    "the-real-cost-of-model-migration-what-swapping-llms-actually-requires",
    "version-your-vectors-index-versioning-as-the-missing-layer-in-rag",
    "techniques-to-boost-rag-performance-in-production",
    "ragas-mlflow-rag-evaluation-tutorial",
    "the-role-and-responsibilities-of-a-forward-deployed-engineer",
]
TOPIC_HUBS = [
    {"title": "RAG", "url": "/tag/rag/", "description": "Retrieval, indexing and RAG in production"},
    {"title": "Evaluation", "url": "/tag/evaluation/", "description": "Measuring LLM and retrieval quality"},
    {"title": "LLMOps & MLOps", "url": "/category/mlops.html", "description": "Shipping and operating models"},
    {"title": "Responsible AI", "url": "/category/responsible-ai.html", "description": "Risk, fairness and governance"},
    {"title": "Engineering", "url": "/category/software-development.html", "description": "Software practice and tooling"},
]

# Code syntax highlighting theme (Pygments)
# Options: monokai, github, friendly, colorful, etc.
PYGMENTS_STYLE = "github"
# PYGMENTS_STYLE_DARK = "monokai"  # Optional: different theme for dark mode

# Notebook syntax highlighting - use theme's pygments CSS for unified styling
IPYNB_SKIP_CSS = True  # Don't inject notebook's own pygments CSS (uses theme's instead)

# Favicon configuration
# Option 1: Simple favicon - set FAVICON = "/favicon.ico"
# Option 2: RealFaviconGenerator package (recommended for all platforms)
#   Generate at https://realfavicongenerator.net/ and place files in content/
RFG_FAVICONS = True  # Enable full favicon package
RFG_THEME_COLOR = "#333333"  # Browser theme color (address bar, etc.)
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
DATE_FORMATS = {"en": "%Y-%m-%d"}  # Format: 2024-01-15
DEFAULT_DATE_FORMAT = "%B %d, %Y"  # Format: January 15, 2024

# Article metadata display
SHOW_ARTICLE_AUTHOR = False  # Hide author name (single-author blog)
SHOW_ARTICLE_CATEGORY = False  # Hide category in article header
SHOW_DATE_MODIFIED = True  # Show "Updated" date when it differs from Date
HOME_HIDE_TAGS = True  # Hide tags on home page article cards

# Table of Contents
ENABLE_TOC = True  # Collapsible TOC on long posts without a manual TOC
TOC_MIN_HEADINGS = 5

# Author box at the end of articles (not on notes)
SHOW_AUTHOR_BOX = False
AUTHOR_BOX_ROLE = "AI/ML technical leader building LLM and RAG systems in enterprise."
AUTHOR_BOX_LINKS = [
    ("About", "/about/"),
    ("LinkedIn", "https://pl.linkedin.com/in/krystiansafjan"),
    ("GitHub", "https://github.com/izikeros"),
]

# Typography enhancement (smart quotes, etc.)
TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ["style", "script", "title", "code", "pre"]

# =============================================================================
# PAGINATION AND INDEX FILTERING
# =============================================================================
# The exclude_category plugin provides filtered, paginated article lists

# Categories to exclude from main index (articles still accessible directly)
INDEX_EXCLUDE_CATEGORIES = ["note"]

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
    ("About", "/about/"),
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
AUTHOR_SAVE_AS = ""  # Empty = don't generate
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = ""  # Empty = don't generate

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

# Supported markup formats (for pelican_jupyter plugin)
MARKUP = ("md", "ipynb")

# Markdown extension configuration
MARKDOWN = {
    "extension_configs": {
        # Syntax highlighting for code blocks
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        # Extra features: tables, fenced code, footnotes, etc.
        "markdown.extensions.extra": {},
        # !!! note / tradeoff / decision "Title" callout blocks
        "markdown.extensions.admonition": {},
        # Metadata in markdown files
        "markdown.extensions.meta": {},
        # Table of contents generation
        "markdown.extensions.toc": {
            "title": "",
            "toc_depth": "2-3",  # Include h2 and h3 only
            "permalink": False,  # No permalink anchors
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
from pelican_jupyter import markup as nb_markup
from traitlets.config import Config

# Ignore Jupyter checkpoint files and virtual environments
IGNORE_FILES = [".ipynb_checkpoints", ".venv"]

# Notebook cell preprocessing - remove tagged cells
c = Config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)  # Remove entire cell
c.TagRemovePreprocessor.remove_all_outputs_tags = (
    "remove_output",
)  # Remove cell output only
c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)  # Remove cell input only

IPYNB_PREPROCESSORS = [
    RegexRemovePreprocessor(patterns=[r"\s*\Z"]),  # Remove empty cells
    TagRemovePreprocessor(config=c),  # Remove tagged cells
]

# =============================================================================
# PLUGINS
# =============================================================================

PLUGIN_PATHS = ["./pelican-plugins"]

PLUGINS = [
    "exclude_category",  # Filter categories from index, provide pagination
    "yaml_metadata",  # Parse YAML frontmatter in markdown files
    "seo_leo_enhancer",  # Extract TL;DR, FAQ, HowTo from content markers
    "feed_utm",  # Add UTM tracking params to RSS/Atom feeds
    "obsidian",  # Obsidian wiki-links and hashtag support
    "pelican_ai_analyzer_bar",  # AI service buttons for article analysis
    "llms_txt",  # Generate /llms.txt index for LLM tools (llmstxt.org)
    "category_redirects",  # Redirect pages for removed category URLs
    "image_dimensions",  # width/height for Image metadata (no layout shift)
]

# Category taxonomy (2026-11): old category slug -> new location
CATEGORY_REDIRECTS = {
    "machine-learning": "category/applied-ml-data-science.html",
    "data-science": "category/applied-ml-data-science.html",
    "algorithmic-trading": "category/applied-ml-data-science.html",
    "generative-ai": "category/llm-engineering.html",
    "mlops": "category/mlops-llmops.html",
    "linux": "category/software-engineering-tools.html",
    "software-development": "category/software-engineering-tools.html",
    "howto": "categories.html",
    "exploring-new-ideas": "categories.html",
}

# Positioning topics first in llms.txt (remaining categories follow by size)
LLMS_TXT_CATEGORY_ORDER = [
    "LLM Engineering",
    "RAG & Retrieval",
    "Evaluation & Observability",
    "MLOps & LLMOps",
    "AI Engineering Leadership",
    "Responsible AI",
]

# llms.txt (see pelican-plugins/llms_txt); notes go to the "Optional" section
LLMS_TXT_DESCRIPTION = (
    "Practitioner notes by Krystian Safjan, AI/ML technical leader at EY, "
    "on building and operating LLM, RAG and ML systems in enterprise "
    "environments: evaluation, MLOps, model migration, agentic workflows "
    "and engineering leadership."
)
LLMS_TXT_INTRO = (
    "- [About the author](https://safjan.com/about/)\n"
    "- [Resume](https://safjan.com/pdfs/Krystian_Safjan_resume_priv.pdf)\n"
    "- [LinkedIn](https://pl.linkedin.com/in/krystiansafjan)\n"
    "- [GitHub](https://github.com/izikeros)\n"
    "- [Google Scholar](https://scholar.google.pl/citations?user=UlNJgMoAAAAJ)"
)

# Additional plugins (uncomment to enable):
PLUGINS += [
    #     "featured_image",    # Extract featured image from article (not needed, theme has native support for that)
    "render_math",  # LaTeX math rendering
    "neighbors",  # Previous/next article links
    "related_posts",  # Related articles suggestions
    "sitemap",  # Generate sitemap.xml
    nb_markup,  # Enhanced Jupyter notebook support (pelican_jupyter)
    "series",
]

# =============================================================================
# SEO AND SEARCH
# =============================================================================

# SEO plugin configuration
SEO_REPORT = False  # Don't generate SEO analysis report
SEO_ENHANCER = True  # Enable SEO meta tag generation
SEO_ENHANCER_OPEN_GRAPH = True  # Generate Open Graph tags (Facebook, LinkedIn)
SEO_ENHANCER_TWITTER_CARDS = True  # Twitter Cards (using custom implementation)
SEO_ARTICLES_LIMIT = 10  # Articles to include in SEO report
SEO_PAGES_LIMIT = 10  # Pages to include in SEO report

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
# AI ANALYZER BAR
# =============================================================================
# Adds buttons to analyze articles with AI services (ChatGPT, Perplexity, etc.)

AI_ANALYZER_BAR = {
    "enabled": True,
    "services": ["chatgpt", "perplexity", "claude", "gemini", "grok"],
    "position": "after_summary",
    "text": "Summarize and analyze this article with:",
    "exclude_categories": ["note"],
    "exclude_paths": [],
}

# =============================================================================
# THIRD-PARTY INTEGRATIONS
# =============================================================================

# Google AdSense auto ads
USE_GOOGLE_AUTO_ADS = False

# Applause button (reader appreciation)
USE_APPLAUSE = False

# Disqus comments (disabled)
# DISQUS_SITENAME = 'krystian-safjan'

# =============================================================================
# LINKEDIN FOLLOW BUTTON
# =============================================================================
# Displays a "Follow on LinkedIn" button in the sidebar below social icons

LINKEDIN_FOLLOW = True
LINKEDIN_FOLLOW_MEMBER = "krystiansafjan"
