.PHONY: new help

help:
	@echo "Targets:"
	@echo "  make new         - Create new notebook project (interactive)"
	@echo "  make dev-<name>  - Open existing project in VS Code"

new:
	@./scripts/new_notebook.sh && \
	PROJECT=$$(ls -td */ | head -1) && \
	cd "$$PROJECT" && make dev

dev-%:
	@cd $* && make dev
