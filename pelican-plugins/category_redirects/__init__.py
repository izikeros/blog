"""
Category Redirects Plugin
=========================

Writes small HTML redirect pages for category URLs that no longer exist, so
old links and search results keep working after a taxonomy change.

Settings:
    CATEGORY_REDIRECTS: Mapping of old category slug to target path relative
        to SITEURL, e.g. {"machine-learning": "category/applied-ml.html"}.
        Each old slug is written to CATEGORY_SAVE_AS. Slugs that are still
        live categories are skipped.
"""

import html
import logging
import os

from pelican import signals

logger = logging.getLogger(__name__)

_live_slugs = set()

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
</head>
<body><p>This category has moved to <a href="{url}">{url}</a>.</p></body>
</html>
"""


def _collect(generator):
    _live_slugs.clear()
    _live_slugs.update(category.slug for category, _ in generator.categories)


def _write(pelican):
    settings = pelican.settings
    siteurl = settings.get("SITEURL", "").rstrip("/")
    save_as = settings.get("CATEGORY_SAVE_AS", "category/{slug}.html")
    written = 0
    for old, target in settings.get("CATEGORY_REDIRECTS", {}).items():
        if old in _live_slugs:
            logger.warning("category_redirects: %r is a live category, skipped", old)
            continue
        url = html.escape(f"{siteurl}/{target.lstrip('/')}", quote=True)
        path = os.path.join(pelican.output_path, save_as.format(slug=old))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(TEMPLATE.format(url=url))
        written += 1
    logger.info("category_redirects: wrote %d redirect pages", written)


def register():
    signals.article_generator_finalized.connect(_collect)
    signals.finalized.connect(_write)
