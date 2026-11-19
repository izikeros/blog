#!/usr/bin/env python
"""Validate YAML frontmatter of Markdown posts (read-only).

Errors (exit code 1):
  - missing/unparseable frontmatter
  - missing required key: Title, Date, Category, Summary
  - unparseable Date/Modified
  - the same key present in two casings (e.g. Tags and tags)
Warnings (printed with --warnings, never fail):
  - lowercase variant of a canonical key (e.g. tags instead of Tags)
  - category not in the known list

Usage:
  python scripts/validate_frontmatter.py [PATH ...] [--warnings]
PATH may be files or directories
(default: content/posts/posts content/posts/notes). Hidden dirs are skipped.
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

REQUIRED = ["Title", "Date", "Category", "Summary"]
CANONICAL = REQUIRED + ["Modified", "Tags", "Slug", "Status", "Image", "Series"]
KNOWN_CATEGORIES = {
    "note",
    "LLM Engineering",
    "RAG & Retrieval",
    "Evaluation & Observability",
    "MLOps & LLMOps",
    "AI Engineering Leadership",
    "Responsible AI",
    "Applied ML & Data Science",
    "Software Engineering & Tools",
}
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.S)


def _valid_date(value):
    if isinstance(value, (date, datetime)):
        return True
    try:
        datetime.fromisoformat(str(value).strip().replace(" ", "T", 1))
        return True
    except ValueError:
        return False


def check_text(text):
    """Return (errors, warnings) for one file's text."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return ["no YAML frontmatter block"], []
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return [f"invalid YAML: {exc.__class__.__name__}"], []
    if not isinstance(meta, dict):
        return ["frontmatter is not a mapping"], []

    errors, warnings = [], []
    by_lower = {}
    for key in meta:
        by_lower.setdefault(str(key).lower(), []).append(key)
    for variants in by_lower.values():
        if len(variants) > 1:
            errors.append(f"duplicate key in different casing: {variants}")

    def get(name):
        for key in by_lower.get(name.lower(), []):
            return meta[key]
        return None

    for name in REQUIRED:
        if get(name) in (None, ""):
            errors.append(f"missing {name}")
    for name in ("Date", "Modified"):
        value = get(name)
        if value not in (None, "") and not _valid_date(value):
            errors.append(f"unparseable {name}: {value!r}")
    for name in CANONICAL:
        if name not in meta and name.lower() in meta:
            warnings.append(f"use '{name}' instead of '{name.lower()}'")
    category = get("Category")
    if category and category not in KNOWN_CATEGORIES:
        warnings.append(f"unknown Category: {category!r}")
    return errors, warnings


def iter_files(paths):
    for path in paths:
        p = Path(path)
        if p.is_dir():
            yield from sorted(p.rglob("*.md"))
        elif p.suffix == ".md":
            yield p


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", default=["content/posts/posts", "content/posts/notes"])
    parser.add_argument("--warnings", action="store_true", help="show warnings")
    args = parser.parse_args(argv)

    n_files = n_err = n_warn = 0
    for f in iter_files(args.paths):
        if any(part.startswith(".") for part in f.parts):
            continue
        n_files += 1
        errors, warnings = check_text(f.read_text(encoding="utf-8"))
        n_err += len(errors)
        n_warn += len(warnings)
        for msg in errors:
            print(f"ERROR {f}: {msg}")
        if args.warnings:
            for msg in warnings:
                print(f"WARN  {f}: {msg}")
    print(f"{n_files} files, {n_err} errors, {n_warn} warnings")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
