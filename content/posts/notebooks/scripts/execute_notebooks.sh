#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=${1:-.}
ROOT_DIR=$(cd "$ROOT_DIR" && pwd)

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is not installed. Install it from https://astral.sh/uv" >&2
    exit 1
fi

# Find notebooks (skip .nbdata files and .ipynb_checkpoints folders)
NOTEBOOKS=()
while IFS= read -r nb; do
    NOTEBOOKS+=("$nb")
done < <(find "$ROOT_DIR" -type f -name '*.ipynb' \
    ! -name '*.nbdata' \
    ! -path '*/.ipynb_checkpoints/*' \
    ! -path '*/.venv/*' \
    | sort)

TOTAL=${#NOTEBOOKS[@]}

if [ "$TOTAL" -eq 0 ]; then
    echo "No notebooks found under $ROOT_DIR"
    exit 0
fi

echo "Discovered $TOTAL notebook(s) under $ROOT_DIR"
echo ""

FAILURES=0

for NB_PATH in "${NOTEBOOKS[@]}"; do
    NB_DIR=$(dirname "$NB_PATH")
    REL_PATH=${NB_PATH#"$ROOT_DIR/"}
    REL_PATH=${REL_PATH:-$(basename "$NB_PATH")}

    # Ensure environment for notebook directory
    "$SCRIPT_DIR/setup_env.sh" "$NB_DIR"

    echo "Executing $REL_PATH"

    if [ -f "$NB_DIR/pyproject.toml" ]; then
        UV_DIR="$NB_DIR"
    else
        UV_DIR="$ROOT_DIR"
    fi

    set +e
    uv run --directory "$UV_DIR" jupyter nbconvert --to notebook --execute --inplace \
        --ExecutePreprocessor.timeout=600 "$NB_PATH" 2>&1
    STATUS=$?
    set -e

    if [ $STATUS -eq 0 ]; then
        echo "✅ Success: $REL_PATH"
    else
        echo "❌ Failure: $REL_PATH" >&2
        FAILURES=$((FAILURES + 1))
    fi
    echo ""
done

echo "----------------------------------------"
echo "Total: $TOTAL | Passed: $((TOTAL - FAILURES)) | Failed: $FAILURES"

if [ $FAILURES -gt 0 ]; then
    exit 1
fi
