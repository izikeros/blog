#!/usr/bin/env python3
"""
Verify that contexts in golden_dataset.json exist exactly in knowledge_base.json.

This script ensures data integrity for RAG evaluation by checking that all
context strings are verbatim quotes from the knowledge base documents.

Usage:
    python verify_dataset.py
    
Exit codes:
    0 - All contexts verified successfully
    1 - One or more contexts not found in knowledge base
"""

import json
import sys
from pathlib import Path


def load_json(filepath: str) -> list:
    """Load JSON file and return contents."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def verify_contexts(knowledge_base: list[str], dataset: list[dict]) -> list[str]:
    """
    Verify all contexts strings exist in knowledge base.
    
    Args:
        knowledge_base: List of knowledge base documents
        dataset: List of golden dataset items with contexts
        
    Returns:
        List of error messages for contexts not found
    """
    # Combine all knowledge base documents into one searchable string
    # Keep original structure to search within each document
    errors = []
    
    for i, item in enumerate(dataset, 1):
        question = item.get("question", "")[:50]
        contexts = item.get("contexts", [])
        
        if not contexts:
            errors.append(f"Q{i}: Missing contexts field")
            continue
            
        for j, ctx in enumerate(contexts):
            # Check if context exists in any knowledge base document
            found = False
            for doc in knowledge_base:
                if ctx in doc:
                    found = True
                    break
            
            if not found:
                # Show truncated context for readability
                ctx_preview = ctx[:60] + "..." if len(ctx) > 60 else ctx
                errors.append(f"Q{i} context[{j}]: '{ctx_preview}' NOT FOUND in knowledge base")
    
    return errors


def main():
    """Main verification function."""
    # Get script directory for relative paths
    script_dir = Path(__file__).parent
    
    kb_path = script_dir / "knowledge_base.json"
    dataset_path = script_dir / "golden_dataset.json"
    
    # Check files exist
    if not kb_path.exists():
        print(f"ERROR: Knowledge base not found: {kb_path}")
        sys.exit(1)
    if not dataset_path.exists():
        print(f"ERROR: Golden dataset not found: {dataset_path}")
        sys.exit(1)
    
    # Load data
    print(f"Loading knowledge base from: {kb_path}")
    knowledge_base = load_json(kb_path)
    print(f"  → {len(knowledge_base)} documents loaded")
    
    print(f"Loading golden dataset from: {dataset_path}")
    dataset = load_json(dataset_path)
    print(f"  → {len(dataset)} questions loaded")
    
    # Count total contexts
    total_contexts = sum(len(item.get("contexts", [])) for item in dataset)
    print(f"  → {total_contexts} contexts entries to verify")
    print()
    
    # Verify
    errors = verify_contexts(knowledge_base, dataset)
    
    if errors:
        print("=" * 60)
        print("VERIFICATION FAILED")
        print("=" * 60)
        print(f"\n{len(errors)} error(s) found:\n")
        for error in errors:
            print(f"  ✗ {error}")
        print()
        print("Fix: Ensure contexts strings are exact quotes from knowledge_base.json")
        sys.exit(1)
    else:
        print("=" * 60)
        print("VERIFICATION PASSED")
        print("=" * 60)
        print(f"\n✓ All {len(dataset)} questions have valid contexts")
        print(f"✓ All {total_contexts} context quotes found in knowledge base")
        sys.exit(0)


if __name__ == "__main__":
    main()
