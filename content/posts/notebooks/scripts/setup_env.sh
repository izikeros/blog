#!/usr/bin/env bash

set -euo pipefail

TARGET_DIR=${1:-.}
TARGET_DIR=$(cd "$TARGET_DIR" && pwd)

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is not installed. Install it from https://astral.sh/uv" >&2
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: target directory '$TARGET_DIR' does not exist" >&2
    exit 1
fi

cd "$TARGET_DIR"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment in $TARGET_DIR/.venv"
    uv venv
fi

if [ -f "pyproject.toml" ]; then
    echo "Syncing dependencies in $TARGET_DIR"
    uv sync
else
    echo "Warning: No pyproject.toml found in $TARGET_DIR; created .venv without syncing dependencies." >&2
fi
