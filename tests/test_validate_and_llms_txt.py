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
Category: MLOps & LLMOps
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


def test_llms_txt_category_order_overrides_size(tmp_path):
    llms_txt._collect(
        SimpleNamespace(
            articles=[
                _article("A", "Big", 1),
                _article("B", "Big", 2),
                _article("C", "Small", 3),
            ]
        )
    )
    settings = {"SITENAME": "Blog", "LLMS_TXT_CATEGORY_ORDER": ["Small"]}
    llms_txt._write(SimpleNamespace(settings=settings, output_path=str(tmp_path)))
    out = (tmp_path / "llms.txt").read_text()
    assert out.index("## Small") < out.index("## Big")


def test_category_redirects_skip_live_and_write_old(tmp_path):
    import category_redirects

    live = SimpleNamespace(slug="new-cat")
    category_redirects._collect(SimpleNamespace(categories=[(live, [])]))
    settings = {
        "SITEURL": "https://example.com",
        "CATEGORY_REDIRECTS": {
            "old-cat": "category/new-cat.html",
            "new-cat": "categories.html",
        },
    }
    category_redirects._write(
        SimpleNamespace(settings=settings, output_path=str(tmp_path))
    )
    page = (tmp_path / "category" / "old-cat.html").read_text()
    assert 'url=https://example.com/category/new-cat.html"' in page
    assert not (tmp_path / "category" / "new-cat.html").exists()


def test_image_dimensions_reads_png_and_jpeg_headers(tmp_path):
    import struct
    from image_dimensions import read_image_size

    png = tmp_path / "a.png"
    png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\0\0\0\rIHDR" + struct.pack(">II", 640, 320) + b"\0" * 8)
    jpg = tmp_path / "b.jpg"
    # SOI, APP0 segment (skipped), SOF0 with height 90, width 160
    jpg.write_bytes(b"\xff\xd8\xff\xe0\x00\x04\0\0\xff\xc0\x00\x11\x08" + struct.pack(">HH", 90, 160) + b"\0" * 12)
    assert read_image_size(png) == (640, 320)
    assert read_image_size(jpg) == (160, 90)
    assert read_image_size(tmp_path / "missing.png") is None


def test_image_dimensions_resolves_only_local_files(tmp_path):
    from image_dimensions import resolve_local_image

    (tmp_path / "images").mkdir()
    (tmp_path / "images" / "x.jpg").write_bytes(b"")
    assert resolve_local_image("/images/x.jpg", tmp_path) == tmp_path / "images" / "x.jpg"
    assert resolve_local_image("images/x.jpg", tmp_path) == tmp_path / "images" / "x.jpg"
    assert resolve_local_image("https://site.com/images/x.jpg", tmp_path, "https://site.com") == tmp_path / "images" / "x.jpg"
    assert resolve_local_image("https://cdn.example.com/x.jpg", tmp_path) is None
    assert resolve_local_image("/images/nope.jpg", tmp_path) is None
