"""
Exclude Category Plugin
=======================

Provides pre-filtered, pre-paginated article lists for index templates.
Does NOT modify the main articles list to ensure all articles are rendered.

Settings:
    INDEX_EXCLUDE_CATEGORIES: List of category names to exclude from index.
                              Example: ['note', 'draft']
    INDEX_ARTICLES_PER_PAGE: Number of filtered articles per index page.
                             Default: 10

Template variables:
    index_article_pages: List of article lists, one per page
    index_total_pages: Total number of filtered index pages
    index_articles_count: Total count of filtered articles
    index_exclude_categories: Set of category names excluded
"""

import logging
from itertools import islice

from pelican import signals

logger = logging.getLogger(__name__)

try:
    from rich.console import Console
    console = Console()
except ImportError:
    console = None


def _batch(iterable, n):
    """Yield successive n-sized chunks from iterable."""
    it = iter(iterable)
    while chunk := list(islice(it, n)):
        yield chunk


def add_filtered_index_context(generator):
    """Create pre-filtered, paginated article lists for index template."""
    # Normalize to lowercase for case-insensitive matching
    excluded = {cat.lower() for cat in generator.settings.get('INDEX_EXCLUDE_CATEGORIES', [])}
    per_page = generator.settings.get('INDEX_ARTICLES_PER_PAGE', 10)
    
    # Filter articles for index (excluding specified categories, case-insensitive)
    index_articles = [
        a for a in generator.articles
        if a.category.name.lower() not in excluded
    ]
    
    # Create paginated batches
    article_pages = list(_batch(index_articles, per_page))
    
    # Add to context
    generator.context['index_article_pages'] = article_pages
    generator.context['index_total_pages'] = len(article_pages)
    generator.context['index_articles_count'] = len(index_articles)
    generator.context['index_exclude_categories'] = excluded
    
    # Count and log excluded articles
    if excluded:
        excluded_counts = {}
        for article in generator.articles:
            if article.category.name.lower() in excluded:
                excluded_counts[article.category.name] = excluded_counts.get(article.category.name, 0) + 1
        
        if excluded_counts:
            parts = [f"{count} {cat}{'s' if count != 1 else ''}" for cat, count in sorted(excluded_counts.items())]
            msg = f"Index: {len(index_articles)} articles in {len(article_pages)} pages ({per_page}/page), excluded {', '.join(parts)}"
            if console:
                console.print(msg)
            else:
                logger.warning(msg)


def register():
    signals.article_generator_finalized.connect(add_filtered_index_context)
