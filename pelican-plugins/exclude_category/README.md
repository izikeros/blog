# Exclude Category Plugin

A Pelican plugin that provides pre-filtered, pre-paginated article lists for index templates. This enables predictable pagination (e.g., exactly 10 articles per page) while excluding specific categories like notes or drafts from the main index.

## Features

- Excludes specified categories from index pages without removing them from the site
- Provides pre-paginated article lists for predictable page counts
- All articles are still rendered and accessible (category pages, direct URLs, etc.)
- Integrates with Pelican's existing pagination system

## Installation

1. Copy the `exclude_category` folder to your `pelican-plugins` directory
2. Add the plugin to your `pelicanconf.py`:

```python
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["exclude_category"]
```

## Configuration

Add these settings to your `pelicanconf.py`:

```python
# Categories to exclude from the index (required)
INDEX_EXCLUDE_CATEGORIES = ['note', 'draft']

# Number of filtered articles per index page (default: 10)
INDEX_ARTICLES_PER_PAGE = 10

# Pelican's pagination - set to ensure enough pages are generated
# Formula: DEFAULT_PAGINATION ≈ total_articles / desired_filtered_pages
DEFAULT_PAGINATION = 40
```

### Understanding DEFAULT_PAGINATION

Pelican generates index pages based on `DEFAULT_PAGINATION`. To ensure enough pages exist for your filtered articles:

- If you have 300 total articles, 80 non-note articles, and want 10 per page
- You need 8 filtered pages (80 / 10 = 8)
- Set `DEFAULT_PAGINATION = 300 / 8 ≈ 38` (round down)

## Template Variables

The plugin adds these variables to the Jinja2 context:

| Variable | Type | Description |
|----------|------|-------------|
| `index_article_pages` | `list[list[Article]]` | Pre-filtered articles grouped by page |
| `index_total_pages` | `int` | Total number of filtered pages |
| `index_articles_count` | `int` | Total count of filtered articles |
| `index_exclude_categories` | `set[str]` | Set of excluded category names |

## Template Usage

### index.html

```jinja
{# Get current page number (0-indexed) #}
{% set current_page_num = (articles_page.number if articles_page else 1) - 1 %}

{# Get filtered articles for this page #}
{% set page_articles = index_article_pages[current_page_num] if index_article_pages else [] %}

<div class="article-list">
{% for article in page_articles %}
    <article>
        <h2>{{ article.title }}</h2>
        <p>{{ article.summary }}</p>
    </article>
{% endfor %}
</div>
```

### Custom Pagination (pagination_filtered.html)

```jinja
{% if index_total_pages is defined and index_total_pages > 1 %}
    {% set current_page_num = (articles_page.number if articles_page else 1) - 1 %}
    
    <div class="pagination">
        {% if current_page_num < index_total_pages - 1 and articles_page.has_next() %}
            <a href="{{ SITEURL }}/{{ articles_next_page.url }}">← Older Posts</a>
        {% endif %}
        
        {% if current_page_num > 0 and articles_page.has_previous() %}
            <a href="{{ SITEURL }}/{{ articles_previous_page.url }}">Newer Posts →</a>
        {% endif %}
    </div>
{% endif %}
```

## How It Works

1. The plugin hooks into Pelican's `article_generator_finalized` signal
2. It filters `generator.articles` to exclude specified categories
3. The filtered list is split into pages of `INDEX_ARTICLES_PER_PAGE` articles
4. These pre-computed pages are added to the template context
5. Templates use `index_article_pages[page_number]` instead of `articles_page.object_list`

**Important**: The plugin does NOT modify `generator.articles`, so all articles (including excluded categories) are still rendered as individual pages and appear in their respective category listings.

## Output Example

When running Pelican, you'll see:

```
Index: 79 articles in 8 pages (10/page), excluded 238 notes
Done: Processed 317 articles, 2 drafts, 0 hidden articles...
```

## License

MIT License
