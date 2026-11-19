"""
SEO/LEO Enhancer Plugin
=======================

Enhances articles with SEO and LLM Engine Optimization (LEO) features:
1. Extracts content from markdown markers (tldr, faq, howto)
2. Auto-calculates word count and reading time if not provided
3. Builds structured data for templates
4. Adds speakable specifications

Settings:
    SEO_LEO_ENABLED: Enable/disable the plugin (default: True)
    SEO_LEO_WORDS_PER_MINUTE: Reading speed for time calculation (default: 200)

Template variables added to each article:
    article.seo_leo: dict with extracted/calculated data
        - tldr: Extracted TL;DR text from content markers
        - faq_from_content: FAQ extracted from content markers
        - howto_from_content: HowTo steps extracted from content markers
        - word_count: Calculated word count (if not in stats)
        - reading_time: Calculated reading time in minutes
        - speakable_selectors: CSS selectors for speakable content
"""

import logging
import re
from html import unescape

from pelican import signals

logger = logging.getLogger(__name__)


def strip_html(text):
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)


def extract_section(content, start_marker, end_marker):
    """Extract content between HTML comment markers.
    
    Args:
        content: HTML content to search
        start_marker: Start marker name (e.g., 'tldr-start')
        end_marker: End marker name (e.g., 'tldr-end')
    
    Returns:
        Extracted text or None if not found
    """
    pattern = rf'<!--\s*{re.escape(start_marker)}\s*-->(.+?)<!--\s*{re.escape(end_marker)}\s*-->'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        extracted = match.group(1).strip()
        # Strip HTML tags and clean up
        text = strip_html(extracted)
        text = unescape(text)
        # Normalize whitespace
        text = ' '.join(text.split())
        return text
    return None


def extract_faq_from_content(content):
    """Extract FAQ from markdown H3 headers within faq markers.
    
    Expects format:
        <!-- faq-start -->
        ### Question 1?
        Answer to question 1.
        
        ### Question 2?
        Answer to question 2.
        <!-- faq-end -->
    
    Returns:
        List of dicts with 'question' and 'answer' keys, or None
    """
    faq_content = extract_section(content, 'faq-start', 'faq-end')
    if not faq_content:
        return None
    
    # For HTML content, look for h3 tags
    h3_pattern = r'<h3[^>]*>(.+?)</h3>\s*(.+?)(?=<h3|$)'
    matches = re.findall(h3_pattern, faq_content, re.DOTALL | re.IGNORECASE)
    
    if not matches:
        # Try markdown format (### headers)
        md_pattern = r'###\s+(.+?)\n\s*(.+?)(?=###|$)'
        matches = re.findall(md_pattern, faq_content, re.DOTALL)
    
    if not matches:
        return None
    
    faqs = []
    for question, answer in matches:
        q = strip_html(question).strip()
        a = strip_html(answer).strip()
        # Normalize whitespace
        a = ' '.join(a.split())
        if q and a:
            faqs.append({'question': q, 'answer': a})
    
    return faqs if faqs else None


def extract_howto_from_content(content):
    """Extract HowTo steps from markdown within howto markers.
    
    Expects format:
        <!-- howto-start -->
        ### Step 1: Install dependencies
        Run pip install...
        
        ### Step 2: Configure settings
        Edit config.py...
        <!-- howto-end -->
    
    Returns:
        List of dicts with 'name' and 'text' keys, or None
    """
    howto_content = extract_section(content, 'howto-start', 'howto-end')
    if not howto_content:
        return None
    
    # For HTML content, look for h3 tags
    h3_pattern = r'<h3[^>]*>(.+?)</h3>\s*(.+?)(?=<h3|$)'
    matches = re.findall(h3_pattern, howto_content, re.DOTALL | re.IGNORECASE)
    
    if not matches:
        # Try markdown format
        md_pattern = r'###\s+(.+?)\n\s*(.+?)(?=###|$)'
        matches = re.findall(md_pattern, howto_content, re.DOTALL)
    
    if not matches:
        return None
    
    steps = []
    for name, text in matches:
        n = strip_html(name).strip()
        t = strip_html(text).strip()
        t = ' '.join(t.split())
        if n and t:
            # Remove "Step N:" prefix if present
            n = re.sub(r'^Step\s+\d+[:\s]*', '', n, flags=re.IGNORECASE).strip()
            steps.append({'name': n, 'text': t})
    
    return steps if steps else None


def count_words(content):
    """Count words in content, excluding HTML tags."""
    text = strip_html(content)
    words = text.split()
    return len(words)


def enhance_article(article, settings):
    """Enhance a single article with SEO/LEO data."""
    if not settings.get('SEO_LEO_ENABLED', True):
        return
    
    words_per_minute = settings.get('SEO_LEO_WORDS_PER_MINUTE', 200)
    
    seo_leo = {}
    
    # Extract TL;DR from content markers
    tldr = extract_section(article.content, 'tldr-start', 'tldr-end')
    if tldr:
        seo_leo['tldr'] = tldr
    
    # Extract FAQ from content markers (if not in frontmatter)
    if not article.metadata.get('faq'):
        faq = extract_faq_from_content(article.content)
        if faq:
            seo_leo['faq_from_content'] = faq
    
    # Extract HowTo from content markers (if not in frontmatter)
    if not article.metadata.get('howto-steps'):
        howto = extract_howto_from_content(article.content)
        if howto:
            seo_leo['howto_from_content'] = howto
    
    # Calculate word count if not available from post_stats
    if not hasattr(article, 'stats') or not article.stats:
        word_count = count_words(article.content)
        seo_leo['word_count'] = word_count
        seo_leo['reading_time'] = max(1, word_count // words_per_minute)
    
    # Speakable selectors for voice search
    seo_leo['speakable_selectors'] = [
        'article h1',
        '.summary',
        '.tldr',
        'article > p:first-of-type'
    ]
    
    # Attach to article
    article.seo_leo = seo_leo


def enhance_articles(generator):
    """Process all articles through the SEO/LEO enhancer."""
    settings = generator.settings
    
    for article in generator.articles:
        enhance_article(article, settings)
    
    # Also process drafts if they exist
    if hasattr(generator, 'drafts'):
        for article in generator.drafts:
            enhance_article(article, settings)
    
    logger.debug(f"SEO/LEO Enhancer: Processed {len(generator.articles)} articles")


def register():
    signals.article_generator_finalized.connect(enhance_articles)
