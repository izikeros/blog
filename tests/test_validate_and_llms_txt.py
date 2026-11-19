import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "pelican-plugins"))

import llms_txt  # noqa: E402
from validate_frontmatter import check_text  # noqa: E402

VALID = """---
Title: T
Date: 2024-01-02 10:00
Category: MLOps
Summary: S
---
body
"""


def test_valid_frontmatter_has_no_errors():
    assert check_text(VALID) == ([], [])


def test_missing_required_and_bad_date():
    text = "---\nTitle: T\nDate: not-a-date\nCategory: MLOps\n---\n"
    errors, _ = check_text(text)
    assert "missing Summary" in errors
    assert any(e.startswith("unparseable Date") for e in errors)


def test_duplicate_casing_is_error_and_lowercase_is_warning():
    errors, _ = check_text(VALID.replace("Summary: S", "Summary: S\nsummary: x"))
    assert any("duplicate key" in e for e in errors)
    _, warnings = check_text(VALID.replace("Summary:", "summary:"))
    assert warnings == ["use 'Summary' instead of 'summary'"]


def test_no_frontmatter():
    assert check_text("# just markdown\n")[0] == ["no YAML frontmatter block"]


def _article(title, category, day, summary="<p>Short &amp; sweet</p>"):
    from datetime import datetime

    return SimpleNamespace(
        title=title,
        url=f"{title.lower()}/",
        summary=summary,
        date=datetime(2024, 1, day),
        category=SimpleNamespace(name=category),
    )


def test_llms_txt_groups_and_marks_optional(tmp_path):
    llms_txt._collect(
        SimpleNamespace(
            articles=[
                _article("Old", "MLOps", 1),
                _article("New", "MLOps", 2),
                _article("Til", "note", 3),
            ]
        )
    )
    settings = {
        "SITENAME": "Blog",
        "SITEURL": "https://example.com/",
        "SITESUBTITLE": "Hello <b>world</b>",
        "INDEX_EXCLUDE_CATEGORIES": ["note"],
    }
    llms_txt._write(SimpleNamespace(settings=settings, output_path=str(tmp_path)))
    out = (tmp_path / "llms.txt").read_text()
    assert out.startswith("# Blog\n\n> Hello world\n")
    assert out.index("[New]") < out.index("[Old]") < out.index("## Optional")
    assert "- [New](https://example.com/new/): Short & sweet" in out
    assert out.index("## Optional") < out.index("[Til]")
