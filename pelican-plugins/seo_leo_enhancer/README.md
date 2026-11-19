# SEO/LEO Enhancer Plugin

A Pelican plugin that enhances articles with SEO (Search Engine Optimization) and LEO (LLM Engine Optimization) features.

## Overview

This plugin automatically:
- **Extracts structured content** from markdown markers (TL;DR, FAQ, HowTo)
- **Calculates word count and reading time** (fallback when post_stats not available)
- **Provides speakable specifications** for voice search optimization
- **Supports frontmatter AND content markers** for flexibility

## Installation

1. Ensure the plugin is in your plugin path:
```
pelican-plugins/
└── seo_leo_enhancer/
    ├── __init__.py
    └── README.md
```

2. Add to your `pelicanconf.py`:
```python
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = [
    "yaml_metadata",      # Required for YAML frontmatter parsing
    "seo_leo_enhancer",   # This plugin
]
```

## Settings

```python
# Enable/disable the plugin (default: True)
SEO_LEO_ENABLED = True

# Reading speed for time calculation (default: 200 words per minute)
SEO_LEO_WORDS_PER_MINUTE = 200
```

---

## Content Markers

The plugin extracts content from HTML comment markers in your article body. This allows you to have content that's both **visible to readers** and **used for structured data**.

### TL;DR Section

Wrap your summary in markers - it will be extracted for:
- AI summary fallback (if `AI-Summary` frontmatter not set)
- Speakable schema for voice search
- Featured in AI search results

```markdown
## TL;DR

<!-- tldr-start -->
This article explains how to build a RAG pipeline in 6 steps. 
The key insight is that chunking strategy matters more than 
model selection. Start with LangChain for rapid prototyping.
<!-- tldr-end -->

## Introduction
...
```

**Best Practices:**
- Keep to 2-4 sentences
- Include the main takeaway
- Make it standalone (reader should understand article's value)

### FAQ Section

Wrap Q&A content - it will generate FAQPage schema:

```markdown
## Frequently Asked Questions

<!-- faq-start -->
### What is RAG?

RAG (Retrieval-Augmented Generation) combines document retrieval 
with LLM generation to provide accurate, sourced answers.

### Do I need a GPU?

No, you can use cloud APIs like OpenAI. Local models may 
benefit from GPU acceleration.
<!-- faq-end -->
```

**Rules:**
- Use `###` (H3) headers for questions
- Answer immediately follows the question
- Keep answers concise (2-4 sentences for featured snippets)

### HowTo Section

Wrap step-by-step content - it will generate HowTo schema:

```markdown
## Getting Started

<!-- howto-start -->
### Step 1: Set up environment

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 2: Install dependencies

```bash
pip install langchain chromadb
```
<!-- howto-end -->
```

**Rules:**
- Use `###` (H3) headers for step names
- "Step N:" prefix is optional (plugin removes it automatically)
- Include code examples where relevant

---

## Template Variables

The plugin adds `article.seo_leo` dict to each article:

| Variable | Type | Description |
|----------|------|-------------|
| `tldr` | string | Extracted TL;DR text (stripped of HTML) |
| `faq_from_content` | list | FAQ extracted from content markers |
| `howto_from_content` | list | HowTo steps from content markers |
| `word_count` | int | Word count (only if post_stats unavailable) |
| `reading_time` | int | Reading time in minutes |
| `speakable_selectors` | list | CSS selectors for speakable content |

### FAQ and HowTo Structure

```python
# faq_from_content
[
    {'question': 'What is RAG?', 'answer': 'RAG combines...'},
    {'question': 'Do I need a GPU?', 'answer': 'No, you can...'},
]

# howto_from_content  
[
    {'name': 'Set up environment', 'text': 'Create and activate...'},
    {'name': 'Install dependencies', 'text': 'pip install...'},
]
```

---

## Template Integration

### AI Summary with TL;DR Fallback

```jinja
{# Priority: ai-summary > tldr from content > summary #}
{% set ai_summary = article.metadata.get('ai-summary') %}
{% if not ai_summary and article.seo_leo and article.seo_leo.tldr %}
{% set ai_summary = article.seo_leo.tldr %}
{% endif %}
{% if not ai_summary %}
{% set ai_summary = article.summary|striptags|truncate(300) %}
{% endif %}
<meta name="ai:summary" content="{{ ai_summary }}">
```

### FAQ Schema with Content Fallback

```jinja
{% set faq_items = article.metadata.get('faq') %}
{% if not faq_items and article.seo_leo %}
{% set faq_items = article.seo_leo.faq_from_content %}
{% endif %}
{% if faq_items %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {% for item in faq_items %}
    {
      "@type": "Question",
      "name": "{{ item.question | escape }}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ item.answer | escape }}"
      }
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  ]
}
</script>
{% endif %}
```

### Word Count with Fallback

```jinja
{% if article.stats and article.stats.wc %}
<meta name="ai:word-count" content="{{ article.stats.wc }}">
{% elif article.seo_leo and article.seo_leo.word_count %}
<meta name="ai:word-count" content="{{ article.seo_leo.word_count }}">
{% endif %}
```

### Speakable Schema

```jinja
{% if article.seo_leo and article.seo_leo.speakable_selectors %}
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": {{ article.seo_leo.speakable_selectors | tojson }}
}
{% endif %}
```

---

## Priority Order

The plugin follows this priority for data sources:

1. **Frontmatter** always takes precedence
2. **Content markers** used as fallback
3. **Auto-calculation** for word count/reading time (when post_stats unavailable)

| Data | Priority 1 | Priority 2 | Priority 3 |
|------|-----------|-----------|-----------|
| Summary | `AI-Summary` frontmatter | `<!-- tldr -->` markers | `Summary` frontmatter |
| FAQ | `FAQ` frontmatter | `<!-- faq-start -->` markers | - |
| HowTo | `HowTo-Steps` frontmatter | `<!-- howto-start -->` markers | - |
| Word Count | `post_stats` plugin | `seo_leo_enhancer` calc | - |

---

## Combining with Frontmatter

You can use **both** frontmatter and content markers:

```yaml
---
Title: How to Use Docker
Article-Type: howto

# Frontmatter FAQ (used for schema)
FAQ:
  - question: What is Docker?
    answer: Docker is a containerization platform...

# No HowTo-Steps in frontmatter - will use content markers
---

## TL;DR

<!-- tldr-start -->
Docker simplifies deployment by packaging apps in containers...
<!-- tldr-end -->

## Steps

<!-- howto-start -->
### Install Docker
Download from docker.com...

### Create Dockerfile
Add your configuration...
<!-- howto-end -->

## FAQ

<!-- faq-start -->
### Additional question from content?
This won't be used since FAQ is in frontmatter.
<!-- faq-end -->
```

In this example:
- FAQ comes from frontmatter (priority)
- HowTo comes from content markers (no frontmatter defined)
- TL;DR comes from content markers

---

## Related Documentation

- [Article Writing Guide](../../pelican-themes/Flex/docs/ARTICLE_WRITING_GUIDE.md) - Complete guide for article authors
- [SEO/LEO Specification](../../pelican-themes/Flex/docs/SEO_LEO_SPEC.md) - Technical specification
