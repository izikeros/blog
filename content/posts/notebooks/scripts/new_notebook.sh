#!/usr/bin/env bash
#
# Create a new notebook project with reproducible environment setup
#
# Usage: ./new_notebook.sh <project_name> [notebook_title]
#
# Example:
#   ./new_notebook.sh my_analysis "My Data Analysis"

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
NOTEBOOKS_DIR=$(dirname "$SCRIPT_DIR")

if [ $# -lt 1 ]; then
    echo "Interactive mode - enter project details:"
    read -p "Project name (e.g., 2024-01-15-my_analysis): " PROJECT_NAME
    if [ -z "$PROJECT_NAME" ]; then
        echo "Error: Project name is required" >&2
        exit 1
    fi
    read -p "Article title [$PROJECT_NAME]: " NOTEBOOK_TITLE
    NOTEBOOK_TITLE=${NOTEBOOK_TITLE:-$PROJECT_NAME}
else
    PROJECT_NAME=$1
    NOTEBOOK_TITLE=${2:-$PROJECT_NAME}
fi
PROJECT_DIR="$NOTEBOOKS_DIR/$PROJECT_NAME"

if [ -d "$PROJECT_DIR" ]; then
    echo "Error: Directory '$PROJECT_DIR' already exists" >&2
    exit 1
fi

echo "Creating notebook project: $PROJECT_NAME"
mkdir -p "$PROJECT_DIR"

# Create pyproject.toml
cat > "$PROJECT_DIR/pyproject.toml" <<EOF
[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "Notebook project: $NOTEBOOK_TITLE"
requires-python = ">=3.10"
dependencies = [
    "jupyter>=1.1.1",
]

[tool.uv]
dev-dependencies = []
EOF

# Create Makefile
cat > "$PROJECT_DIR/Makefile" <<'EOF'
include ../scripts/notebook.mk
EOF

# Create .gitignore
cat > "$PROJECT_DIR/.gitignore" <<'EOF'
.venv
.ipynb_checkpoints
EOF

# Create starter notebook
SAFE_NAME=$(echo "$PROJECT_NAME" | tr '-' '_')
cat > "$PROJECT_DIR/$SAFE_NAME.ipynb" <<EOF
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $NOTEBOOK_TITLE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF

# Create .nbdata file for Pelican metadata
TODAY=$(date +%Y-%m-%d)
cat > "$PROJECT_DIR/$SAFE_NAME.nbdata" <<EOF
---
Category: Data Science
Date: '$TODAY'
Image: /images/head/abstract_1.jpg
Modified: '$TODAY'
Slug: $PROJECT_NAME
Status: draft
Summary: TODO - Add summary for $NOTEBOOK_TITLE
Tags: python, data-science, tutorial
Title: $NOTEBOOK_TITLE
---
EOF

echo "✅ Created notebook project at: $PROJECT_DIR"
echo ""
echo "Files created:"
echo "  - pyproject.toml (add dependencies here)"
echo "  - Makefile"
echo "  - .gitignore"
echo "  - $SAFE_NAME.ipynb"
echo "  - $SAFE_NAME.nbdata (Pelican metadata)"
echo ""
echo "Next steps:"
echo "  cd $PROJECT_DIR"
echo "  make setup        # Create venv and install dependencies"
echo "  make dev          # Open in VS Code"
echo "  make execute      # Execute notebook and save outputs"
