"""
llms.txt Plugin
===============

Generates ``llms.txt`` (https://llmstxt.org) in the output root: a Markdown
index of the site for LLM-based tools and answer engines.

Articles are grouped by category (LLMS_TXT_CATEGORY_ORDER first, then
largest first; newest article first).
Categories in LLMS_TXT_OPTIONAL_CATEGORIES go under the spec's "## Optional".

Settings:
    LLMS_TXT_DESCRIPTION: One-paragraph site description (blockquote).
        Default: SITESUBTITLE with HTML stripped.
    LLMS_TXT_INTRO: Optional extra Markdown placed after the description.
    LLMS_TXT_OPTIONAL_CATEGORIES: Category names treated as optional.
        Default: INDEX_EXCLUDE_CATEGORIES.
    LLMS_TXT_CATEGORY_ORDER: Category names listed first, in this order.
        Default: [].
    LLMS_TXT_SUMMARY_MAX: Max characters of each summary. Default: 200.
"""

import html
import logging
import os
import re
from collections import defaultdict

from pelican import signals

logger = logging.getLogger(__name__)

_articles = []


def _plain(text, limit=None):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return text


def _collect(generator):
    _articles[:] = list(generator.articles)


def _link(siteurl, article, limit):
    url = f"{siteurl}/{article.url}"
    summary = _plain(getattr(article, "summary", ""), limit)
    line = f"- [{_plain(article.title)}]({url})"
    return f"{line}: {summary}" if summary else line


def _write(pelican):
    settings = pelican.settings
    siteurl = settings.get("SITEURL", "").rstrip("/")
    limit = settings.get("LLMS_TXT_SUMMARY_MAX", 200)
    optional = {
        c.lower()
        for c in settings.get(
            "LLMS_TXT_OPTIONAL_CATEGORIES",
            settings.get("INDEX_EXCLUDE_CATEGORIES", []),
        )
    }
    description = settings.get("LLMS_TXT_DESCRIPTION") or _plain(
        settings.get("SITESUBTITLE", "")
    )

    main, extra = defaultdict(list), defaultdict(list)
    for article in sorted(_articles, key=lambda a: a.date, reverse=True):
        name = article.category.name
        (extra if name.lower() in optional else main)[name].append(article)

    out = [f"# {settings.get('SITENAME', '')}", ""]
    if description:
        out += [f"> {description}", ""]
    intro = settings.get("LLMS_TXT_INTRO")
    if intro:
        out += [intro.strip(), ""]
    order = {c.lower(): i for i, c in enumerate(settings.get("LLMS_TXT_CATEGORY_ORDER", []))}
    for name in sorted(
        main, key=lambda n: (order.get(n.lower(), len(order)), -len(main[n]), n.lower())
    ):
        out += [f"## {name}", ""]
        out += [_link(siteurl, a, limit) for a in main[name]]
        out.append("")
    if extra:
        out += ["## Optional", ""]
        for name in sorted(extra):
            out += [_link(siteurl, a, limit) for a in extra[name]]
        out.append("")

    path = os.path.join(pelican.output_path, "llms.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    logger.info("llms_txt: wrote %s (%d articles)", path, len(_articles))


def register():
    signals.article_generator_finalized.connect(_collect)
    signals.finalized.connect(_write)
