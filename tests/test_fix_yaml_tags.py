import sys
from pathlib import Path
from typing import Dict, Any

# Adjust path so we can import the plugin module (directory contains __init__.py)
ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "pelican-plugins"
if str(PLUGIN_DIR) not in sys.path:
    sys.path.insert(0, str(PLUGIN_DIR))

from fix_yaml_tags import normalize_tags  # type: ignore


class DummyContent:
    def __init__(self, metadata):
        self.metadata = metadata


def run_case(
    input_meta: Dict[str, Any], expected_meta: Dict[str, Any], description: str
):
    content = DummyContent(input_meta)
    normalize_tags(content)
    assert (
        content.metadata == expected_meta
    ), f"Failed: {description}. Got {content.metadata}, expected {expected_meta}"
    print(f"PASS: {description}")


def main():
    # 1. Already comma-separated string
    run_case({"tags": "one, two"}, {"tags": "one, two"}, "string unchanged")

    # 2. Capitalized key with string
    run_case(
        {"Tags": "one, two"}, {"tags": "one, two"}, "capitalized string normalized"
    )

    # 3. List with duplicates & whitespace
    run_case(
        {"tags": ["one", "two", "two", " three "]},
        {"tags": "one, two, three"},
        "list deduped and trimmed",
    )

    # 4. Capitalized key list
    run_case({"Tags": ["alpha", "beta"]}, {"tags": "alpha, beta"}, "capitalized list")

    # 5. Empty list removed
    run_case({"tags": []}, {}, "empty list removed")

    # 6. Non-string scalar coerced
    run_case({"Tags": 42}, {"tags": "42"}, "scalar coerced")

    # 7. List with empties and None
    run_case({"tags": ["", None, "x"]}, {"tags": "x"}, "skip empties and None")


if __name__ == "__main__":
    main()
