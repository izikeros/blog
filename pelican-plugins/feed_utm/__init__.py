"""
Feed UTM Plugin
===============

Adds UTM tracking parameters to article links in RSS/Atom feeds for
Google Analytics tracking.

Settings:
    FEED_UTM_PARAMS: Dictionary of UTM parameters to add to feed links.
                     Default: {'utm_source': 'rss', 'utm_medium': 'feed', 'utm_campaign': 'blog'}

Example output URL:
    https://example.com/article/?utm_source=rss&utm_medium=feed&utm_campaign=blog

Usage:
    Add 'feed_utm' to PLUGINS in pelicanconf.py

    Optionally customize:
        FEED_UTM_PARAMS = {
            'utm_source': 'rss',
            'utm_medium': 'feed',
            'utm_campaign': 'my-blog'
        }
"""

import logging
from urllib.parse import urlencode

from pelican import signals

logger = logging.getLogger(__name__)

DEFAULT_UTM_PARAMS = {
    'utm_source': 'rss',
    'utm_medium': 'feed',
    'utm_campaign': 'blog'
}


def add_utm_to_feed(context, feed):
    """Add UTM parameters to all feed item links."""
    utm_params = context.get('FEED_UTM_PARAMS', DEFAULT_UTM_PARAMS)
    
    if not utm_params:
        return
    
    utm_query = urlencode(utm_params)
    items_modified = 0
    
    for item in feed.items:
        link = item.get('link', '')
        if not link:
            continue
            
        # Add UTM params, handling existing query strings
        if '?' in link:
            item['link'] = f"{link}&{utm_query}"
        else:
            item['link'] = f"{link}?{utm_query}"
        items_modified += 1
    
    logger.debug(f"Added UTM parameters to {items_modified} feed items")


def register():
    """Register the plugin with Pelican."""
    signals.feed_generated.connect(add_utm_to_feed)
    logger.debug("Feed UTM plugin registered")
