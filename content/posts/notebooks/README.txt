================================================================================
NOTEBOOK ARTICLE WORKFLOW
================================================================================

This directory contains Jupyter notebook-based blog posts. Each notebook has
its own isolated virtual environment for reproducibility.

--------------------------------------------------------------------------------
1. CREATE NEW NOTEBOOK PROJECT
--------------------------------------------------------------------------------

Run the scaffolding script:

    ./scripts/new_notebook.sh <project_name> "Article Title"

Example:

    ./scripts/new_notebook.sh pandas_tips "10 Pandas Tips for Data Scientists"

This creates a new directory with:
    - pyproject.toml     (dependencies - only jupyter by default)
    - Makefile           (setup, run, execute, clean targets)
    - .gitignore         (ignores .venv and checkpoints)
    - <name>.ipynb       (starter notebook)
    - <name>.nbdata      (Pelican metadata - draft status)

--------------------------------------------------------------------------------
2. SET UP ENVIRONMENT
--------------------------------------------------------------------------------

    cd <project_name>
    make setup

This creates a .venv directory and installs dependencies from pyproject.toml.

--------------------------------------------------------------------------------
3. ADD DEPENDENCIES
--------------------------------------------------------------------------------

Edit pyproject.toml to add required packages:

    [project]
    dependencies = [
        "jupyter>=1.1.1",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
    ]

Then re-run:

    make setup

Or use uv directly:

    uv add pandas matplotlib

--------------------------------------------------------------------------------
4. DEVELOP NOTEBOOK
--------------------------------------------------------------------------------

Launch Jupyter:

    make run

Write your notebook content. Use cell tags for Pelican processing:
    - "remove_cell"    : removes entire cell from published article
    - "remove_input"   : removes code, keeps output
    - "remove_output"  : removes output, keeps code

--------------------------------------------------------------------------------
5. EXECUTE AND SAVE OUTPUTS
--------------------------------------------------------------------------------

Run all cells and save outputs in-place:

    make execute

This ensures reproducibility - outputs are stored in the .ipynb file.
Execution logs are saved to reports/logs/ directory.

--------------------------------------------------------------------------------
6. EDIT METADATA (.nbdata FILE)
--------------------------------------------------------------------------------

Edit the .nbdata file to set article metadata:

    ---
    Category: Data Science
    Date: '2026-01-07'
    Image: /images/head/your_image.jpg
    Modified: '2026-01-07'
    Slug: your-article-slug
    Status: draft                    <-- Change to 'published' when ready
    Summary: Your article summary for RSS and index pages
    Tags: python, pandas, tutorial
    Title: Your Article Title
    ---

Important fields:
    - Status: 'draft' (hidden) or 'published' (visible)
    - Slug: URL path (e.g., slug: my-article -> safjan.com/my-article/)
    - Image: header image path (relative to content/)
    - Tags: comma-separated list

--------------------------------------------------------------------------------
7. PREVIEW LOCALLY
--------------------------------------------------------------------------------

From the blog root directory:

    make devserver

Or:

    pelican --autoreload --listen

Visit http://127.0.0.1:8000 to preview. Draft articles appear in development.

--------------------------------------------------------------------------------
8. PUBLISH
--------------------------------------------------------------------------------

When ready to publish:

1. Set Status: published in .nbdata file
2. Update Modified date if needed
3. Generate site:

       make publish

4. Commit and push:

       git add <project_name>/
       git commit -m "Add article: Your Article Title"
       git push

--------------------------------------------------------------------------------
DIRECTORY STRUCTURE
--------------------------------------------------------------------------------

notebooks/
├── scripts/
│   ├── new_notebook.sh        # Scaffolding script
│   ├── setup_env.sh           # Environment setup helper
│   └── execute_notebooks.sh   # Batch notebook execution
├── test_notebook/             # Example project
│   ├── .venv/                 # Virtual environment (git-ignored)
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── Makefile
│   ├── .gitignore
│   ├── demo.ipynb
│   ├── demo.nbdata
│   └── reports/
└── <your_project>/
    └── ...

--------------------------------------------------------------------------------
MAKEFILE TARGETS
--------------------------------------------------------------------------------

    make setup     - Create .venv and install dependencies
    make run       - Launch Jupyter Notebook
    make execute   - Execute all notebooks and save outputs
    make clean     - Remove .venv and checkpoint files

--------------------------------------------------------------------------------
TIPS
--------------------------------------------------------------------------------

- Each notebook project has isolated dependencies - no conflicts
- The .venv directory is ignored by both git and Pelican
- Use uv for fast dependency management: uv add <package>
- Keep notebooks focused - one topic per notebook
- Test execution with 'make execute' before publishing
- Use meaningful slugs - they become permanent URLs

--------------------------------------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------------------------------------

Q: Pelican shows errors about .venv files
A: Ensure IGNORE_FILES includes ".venv" in pelicanconf.py

Q: Notebook won't execute
A: Check reports/logs/ for error details

Q: Dependencies not found when running notebook
A: Run 'make setup' or 'uv sync' to install dependencies

Q: Changes not showing in preview
A: Restart devserver or check Status is not 'draft'

================================================================================
