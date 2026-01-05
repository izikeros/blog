#!/usr/bin/env python3
"""
Fix Duplicate HTML IDs in Markdown Files

Scans markdown files for duplicate HTML id attributes and removes duplicates,
keeping only the first occurrence of each id.

Usage:
    python scripts/fix_duplicate_ids.py [--dry-run] [--verbose] [path]

Arguments:
    path        Path to scan (default: content/posts)
    --dry-run   Show what would be changed without modifying files
    --verbose   Show detailed output for each file

Examples:
    python scripts/fix_duplicate_ids.py --dry-run
    python scripts/fix_duplicate_ids.py content/posts/posts/2023/
    python scripts/fix_duplicate_ids.py --verbose content/posts/notes/
"""

import argparse
import re
from collections import defaultdict
from pathlib import Path


def find_ids_in_content(content: str) -> list[tuple[int, str, str]]:
    """
    Find all HTML id attributes in content.
    
    Returns list of (position, full_match, id_value) tuples.
    """
    # Match id="value" or id='value' in HTML tags
    pattern = r'(id=["\']([^"\']+)["\'])'
    matches = []
    for match in re.finditer(pattern, content):
        matches.append((match.start(), match.group(1), match.group(2)))
    return matches


def find_duplicate_ids(content: str) -> dict[str, list[int]]:
    """
    Find duplicate IDs and their positions.
    
    Returns dict mapping id_value -> list of positions (excluding first occurrence).
    """
    id_positions = defaultdict(list)
    
    for pos, full_match, id_value in find_ids_in_content(content):
        id_positions[id_value].append(pos)
    
    # Return only duplicates (more than one occurrence), excluding first
    duplicates = {}
    for id_value, positions in id_positions.items():
        if len(positions) > 1:
            duplicates[id_value] = positions[1:]  # Skip first occurrence
    
    return duplicates


def remove_duplicate_ids(content: str, verbose: bool = False) -> tuple[str, int]:
    """
    Remove duplicate id attributes from content, keeping first occurrence.
    
    Returns (modified_content, count_of_removals).
    """
    duplicates = find_duplicate_ids(content)
    
    if not duplicates:
        return content, 0
    
    # Collect all positions to remove
    positions_to_remove = set()
    for id_value, positions in duplicates.items():
        positions_to_remove.update(positions)
        if verbose:
            print(f"    Duplicate id='{id_value}' found {len(positions) + 1} times, removing {len(positions)}")
    
    # Find all id matches and remove those at duplicate positions
    pattern = r'(id=["\'][^"\']+["\'])'
    
    def replace_if_duplicate(match):
        if match.start() in positions_to_remove:
            # Remove the id attribute (and any leading space)
            return ''
        return match.group(0)
    
    # First pass: mark positions
    all_matches = list(re.finditer(pattern, content))
    
    # Build new content by removing duplicates
    result = []
    last_end = 0
    removals = 0
    
    for match in all_matches:
        if match.start() in positions_to_remove:
            # Add content before this match, skip the id attribute
            # Also remove leading whitespace before id=
            start = match.start()
            # Look back for whitespace
            while start > last_end and content[start - 1] in ' \t':
                start -= 1
            result.append(content[last_end:start])
            last_end = match.end()
            removals += 1
        else:
            result.append(content[last_end:match.end()])
            last_end = match.end()
    
    result.append(content[last_end:])
    
    return ''.join(result), removals


def process_file(filepath: Path, dry_run: bool = False, verbose: bool = False) -> tuple[bool, int]:
    """
    Process a single markdown file.
    
    Returns (was_modified, removal_count).
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return False, 0
    
    new_content, removals = remove_duplicate_ids(content, verbose)
    
    if removals == 0:
        return False, 0
    
    if dry_run:
        print(f"  Would remove {removals} duplicate id(s) from {filepath}")
    else:
        try:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  Removed {removals} duplicate id(s) from {filepath}")
        except Exception as e:
            print(f"  Error writing {filepath}: {e}")
            return False, 0
    
    return True, removals


def scan_directory(path: Path, dry_run: bool = False, verbose: bool = False) -> tuple[int, int, int]:
    """
    Scan directory for markdown files and fix duplicate IDs.
    
    Returns (files_scanned, files_modified, total_removals).
    """
    files_scanned = 0
    files_modified = 0
    total_removals = 0
    
    # Find all markdown files
    md_files = list(path.rglob('*.md'))
    
    print(f"Scanning {len(md_files)} markdown files in {path}...")
    
    for filepath in sorted(md_files):
        files_scanned += 1
        
        if verbose:
            print(f"\nProcessing: {filepath}")
        
        modified, removals = process_file(filepath, dry_run, verbose)
        
        if modified:
            files_modified += 1
            total_removals += removals
    
    return files_scanned, files_modified, total_removals


def main():
    parser = argparse.ArgumentParser(
        description='Fix duplicate HTML IDs in markdown files',
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
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output for each file'
    )
    
    args = parser.parse_args()
    
    # Resolve path relative to script location or current directory
    path = Path(args.path)
    if not path.is_absolute():
        # Try relative to script's parent directory (blog root)
        script_dir = Path(__file__).parent.parent
        path = script_dir / args.path
        if not path.exists():
            # Try relative to current directory
            path = Path(args.path)
    
    if not path.exists():
        print(f"Error: Path '{args.path}' does not exist")
        return 1
    
    if args.dry_run:
        print("DRY RUN - no files will be modified\n")
    
    files_scanned, files_modified, total_removals = scan_directory(
        path, 
        dry_run=args.dry_run, 
        verbose=args.verbose
    )
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Files scanned:  {files_scanned}")
    print(f"  Files modified: {files_modified}")
    print(f"  IDs removed:    {total_removals}")
    
    if args.dry_run and files_modified > 0:
        print(f"\nRun without --dry-run to apply changes.")
    
    return 0


if __name__ == '__main__':
    exit(main())
