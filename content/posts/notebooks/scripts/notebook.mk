.PHONY: help setup dev execute clean

NOTEBOOK_DIR := $(CURDIR)
SCRIPTS_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

help:
	@echo "  setup   - Install dependencies"
	@echo "  dev     - Open in VS Code"
	@echo "  execute - Run notebook and save outputs"
	@echo "  clean   - Remove .venv"

setup:
	@$(SCRIPTS_DIR)setup_env.sh $(NOTEBOOK_DIR)

dev: setup
	@code $(NOTEBOOK_DIR)

execute: setup
	@$(SCRIPTS_DIR)execute_notebooks.sh $(NOTEBOOK_DIR)

clean:
	@rm -rf $(NOTEBOOK_DIR)/.venv $(NOTEBOOK_DIR)/.ipynb_checkpoints
