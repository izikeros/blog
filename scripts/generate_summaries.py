#!/usr/bin/env python3
"""
Generate Missing Summaries with Ollama

Scans markdown files for missing Summary frontmatter and generates
summaries using a local Ollama model.

Usage:
    python scripts/generate_summaries.py [--dry-run] [--limit N] [--model MODEL] [--verbose] [path]

Arguments:
    path        Path to scan (default: content/posts)
    --dry-run   Show what would be changed without modifying files
    --limit N   Process only N files (useful for testing)
    --model     Ollama model to use (default: qwen2.5:7b)
    --verbose   Show detailed output

Examples:
    python scripts/generate_summaries.py --dry-run
    python scripts/generate_summaries.py --limit 5
    python scripts/generate_summaries.py --model llama3.1:8b
    python scripts/generate_summaries.py content/posts/notes/
"""

import argparse
import re
import requests
import sys
from pathlib import Path

OLLAMA_API_URL = "http://localhost:11434/api/generate"

SUMMARY_PROMPT = """Generate a concise 1-2 sentence summary for this blog article.
The summary should be informative and describe what the reader will learn.
Do not use phrases like "This article" or "In this post".
Keep it under 200 characters.
Return ONLY the summary text, nothing else.

Title: {title}

Content:
{content}"""


def parse_frontmatter(content: str) -> tuple[dict | None, str, int, int]:
    """
    Parse YAML frontmatter from markdown content.
    
    Returns (frontmatter_dict, body, fm_start, fm_end) or (None, content, -1, -1) if no frontmatter.
    """
    import yaml
    
    # Match YAML frontmatter between --- markers
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return None, content, -1, -1
    
    try:
        fm_text = match.group(1)
        frontmatter = yaml.safe_load(fm_text)
        body = content[match.end():]
        return frontmatter, body, match.start(), match.end()
    except yaml.YAMLError:
        return None, content, -1, -1


def has_summary(frontmatter: dict | None) -> bool:
    """Check if frontmatter has a non-empty Summary field."""
    if not frontmatter:
        return False
    summary = frontmatter.get('Summary') or frontmatter.get('summary')
    return bool(summary and str(summary).strip())


def get_title(frontmatter: dict | None) -> str:
    """Extract title from frontmatter."""
    if not frontmatter:
        return "Untitled"
    return frontmatter.get('Title') or frontmatter.get('title') or "Untitled"


def generate_summary_ollama(title: str, content: str, model: str = "qwen2.5:7b") -> str | None:
    """
    Generate summary using Ollama API.
    
    Returns generated summary or None on error.
    """
    # Truncate content to ~2000 chars for context
    truncated_content = content[:2000]
    if len(content) > 2000:
        truncated_content += "..."
    
    prompt = SUMMARY_PROMPT.format(title=title, content=truncated_content)
    
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 100,
                }
            },
            timeout=60
        )
        response.raise_for_status()
        
        result = response.json()
        summary = result.get("response", "").strip()
        
        # Clean up summary - remove quotes if wrapped
        if summary.startswith('"') and summary.endswith('"'):
            summary = summary[1:-1]
        if summary.startswith("'") and summary.endswith("'"):
            summary = summary[1:-1]
        
        return summary if summary else None
        
    except requests.RequestException as e:
        print(f"  Error calling Ollama API: {e}")
        return None


def update_frontmatter_with_summary(content: str, summary: str) -> str:
    """
    Update markdown content with new Summary in frontmatter.
    Also adds ai_summary: true to indicate AI-generated summary.
    """
    import yaml
    
    # Parse existing frontmatter
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return content
    
    fm_text = match.group(1)
    body = content[match.end():]
    
    # Parse and update frontmatter
    try:
        frontmatter = yaml.safe_load(fm_text)
        if frontmatter is None:
            frontmatter = {}
    except yaml.YAMLError:
        return content
    
    # Add Summary and ai_summary flag
    frontmatter['Summary'] = summary
    frontmatter['ai_summary'] = True
    
    # Rebuild frontmatter preserving key order as much as possible
    # Put common keys first, then the rest
    key_order = ['Category', 'Date', 'Modified', 'Image', 'Slug', 'Status', 'Summary', 'ai_summary', 'Tags', 'Title']
    
    lines = []
    written_keys = set()
    
    # Write keys in preferred order
    for key in key_order:
        if key in frontmatter:
            value = frontmatter[key]
            lines.append(format_yaml_value(key, value))
            written_keys.add(key)
    
    # Write remaining keys
    for key, value in frontmatter.items():
        if key not in written_keys:
            lines.append(format_yaml_value(key, value))
    
    new_fm = '\n'.join(lines)
    return f"---\n{new_fm}\n---\n{body}"


def format_yaml_value(key: str, value) -> str:
    """Format a YAML key-value pair."""
    if value is None:
        return f"{key}: null"
    elif isinstance(value, bool):
        return f"{key}: {str(value).lower()}"
    elif isinstance(value, list):
        if not value:
            return f"{key}: []"
        items = '\n'.join(f"  - {item}" for item in value)
        return f"{key}:\n{items}"
    elif isinstance(value, str):
        # Check if value needs quoting
        if ':' in value or value.startswith('{') or value.startswith('[') or '\n' in value:
            # Use literal block for multiline, quotes for others
            if '\n' in value:
                indented = '\n'.join('  ' + line for line in value.split('\n'))
                return f"{key}: |\n{indented}"
            else:
                escaped = value.replace('"', '\\"')
                return f'{key}: "{escaped}"'
        return f"{key}: {value}"
    else:
        return f"{key}: {value}"


def process_file(filepath: Path, model: str, dry_run: bool = False, verbose: bool = False) -> tuple[bool, str | None]:
    """
    Process a single markdown file.
    
    Returns (was_modified, summary) or (False, None) if skipped/error.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return False, None
    
    frontmatter, body, _, _ = parse_frontmatter(content)
    
    if has_summary(frontmatter):
        if verbose:
            print(f"  Skipping (has summary): {filepath.name}")
        return False, None
    
    title = get_title(frontmatter)
    
    if verbose:
        print(f"  Generating summary for: {title}")
    
    if dry_run:
        print(f"  Would generate summary for: {filepath}")
        return True, "[DRY RUN - no summary generated]"
    
    # Generate summary with Ollama
    summary = generate_summary_ollama(title, body, model)
    
    if not summary:
        print(f"  Failed to generate summary for: {filepath}")
        return False, None
    
    # Update file with new summary
    new_content = update_frontmatter_with_summary(content, summary)
    
    try:
        filepath.write_text(new_content, encoding='utf-8')
        print(f"  Generated summary for: {filepath.name}")
        if verbose:
            print(f"    Summary: {summary[:100]}...")
        return True, summary
    except Exception as e:
        print(f"  Error writing {filepath}: {e}")
        return False, None


def scan_directory(path: Path, model: str, dry_run: bool = False, limit: int | None = None, verbose: bool = False) -> tuple[int, int, int]:
    """
    Scan directory for markdown files and generate missing summaries.
    
    Returns (files_scanned, files_needing_summary, files_processed).
    """
    files_scanned = 0
    files_needing_summary = 0
    files_processed = 0
    
    # Find all markdown files
    md_files = sorted(path.rglob('*.md'))
    
    print(f"Scanning {len(md_files)} markdown files in {path}...")
    
    # First pass: count files needing summary
    files_to_process = []
    for filepath in md_files:
        files_scanned += 1
        try:
            content = filepath.read_text(encoding='utf-8')
            frontmatter, _, _, _ = parse_frontmatter(content)
            if not has_summary(frontmatter):
                files_needing_summary += 1
                files_to_process.append(filepath)
        except Exception:
            continue
    
    print(f"Found {files_needing_summary} files missing summaries")
    
    if limit:
        files_to_process = files_to_process[:limit]
        print(f"Processing first {limit} files...")
    
    # Process files
    for filepath in files_to_process:
        modified, _ = process_file(filepath, model, dry_run, verbose)
        if modified:
            files_processed += 1
    
    return files_scanned, files_needing_summary, files_processed


def check_ollama_available(model: str) -> bool:
    """Check if Ollama is running and model is available."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        response.raise_for_status()
        models = response.json().get("models", [])
        model_names = [m["name"] for m in models]
        
        # Check exact match or prefix match (e.g., "qwen2.5:7b" matches "qwen2.5:7b")
        if model in model_names or any(m.startswith(model.split(':')[0]) for m in model_names):
            return True
        
        print(f"Model '{model}' not found. Available models:")
        for m in model_names[:10]:
            print(f"  - {m}")
        return False
        
    except requests.RequestException:
        print("Error: Cannot connect to Ollama. Make sure it's running (ollama serve)")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate missing article summaries using Ollama',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='content/posts',
        help='Path to scan (default: content/posts)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--limit', '-n',
        type=int,
        help='Process only N files (useful for testing)'
    )
    parser.add_argument(
        '--model', '-m',
        default='qwen2.5:7b',
        help='Ollama model to use (default: qwen2.5:7b)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )
    
    args = parser.parse_args()
    
    # Resolve path
    path = Path(args.path)
    if not path.is_absolute():
        script_dir = Path(__file__).parent.parent
        path = script_dir / args.path
        if not path.exists():
            path = Path(args.path)
    
    if not path.exists():
        print(f"Error: Path '{args.path}' does not exist")
        return 1
    
    # Check Ollama availability (skip in dry-run)
    if not args.dry_run:
        if not check_ollama_available(args.model):
            return 1
        print(f"Using model: {args.model}")
    
    if args.dry_run:
        print("DRY RUN - no files will be modified\n")
    
    files_scanned, files_needing, files_processed = scan_directory(
        path,
        model=args.model,
        dry_run=args.dry_run,
        limit=args.limit,
        verbose=args.verbose
    )
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Files scanned:          {files_scanned}")
    print(f"  Files needing summary:  {files_needing}")
    print(f"  Files processed:        {files_processed}")
    
    if args.dry_run and files_needing > 0:
        print(f"\nRun without --dry-run to generate summaries.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
