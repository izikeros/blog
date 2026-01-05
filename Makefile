PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/docs
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make format-html                    format HTML files with Prettier    '
	@echo '   make validate-html                  validate HTML (errors only)        '
	@echo '   make validate-html-strict           validate HTML (errors + warnings)  '
	@echo '   make fix-duplicate-ids              remove duplicate HTML IDs from md  '
	@echo '   make remove-anchor-ids              remove <a id> anchors from md      '
	@echo '   make generate-summaries             generate missing summaries (Ollama)'
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	echo "Cleaning output directory"
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

e2e:
	echo "Building blog for publish"
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
	npx pagefind --site "$(OUTPUTDIR)"
	echo "Updating repo (git add, commit, push)"
	git add "$(OUTPUTDIR)" && git commit -m "Blog content update" && git push
	echo "Blog regenerated, and pushed to remote."

venv:
	uv lock --upgrade && uv sync
	uv pip install "git+https://github.com/izikeros/pelican-obsidian"
	uv pip install "git+https://github.com/lextoumbourou/pelican-jupyter"

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -b 0.0.0.0

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
	npx pagefind --site "$(OUTPUTDIR)"
	# @$(MAKE) format-html
	# @$(MAKE) validate-html

format-html:
	@echo "Formatting HTML files with Prettier..."
	@find "$(OUTPUTDIR)" -name "*.html" -type f | xargs -P 4 npx prettier --write --parser html 2>/dev/null || true
	@echo "HTML formatting complete."

validate-html:
	@echo "Validating HTML files (errors only)..."
	@npx html-validate "$(OUTPUTDIR)/**/*.html" --formatter stylish 2>&1 | grep -v "warning" || echo "HTML validation completed."

validate-html-strict:
	@echo "Validating HTML files (errors + warnings)..."
	@npx html-validate "$(OUTPUTDIR)/**/*.html" --formatter stylish || echo "HTML validation completed with issues."

fix-duplicate-ids:
	@echo "Fixing duplicate HTML IDs in markdown files..."
	@$(PY) scripts/fix_duplicate_ids.py "$(INPUTDIR)/posts"

remove-anchor-ids:
	@echo "Removing <a id> anchor elements from markdown files..."
	@$(PY) scripts/remove_anchor_ids.py "$(INPUTDIR)/posts"

generate-summaries:
	@echo "Generating missing article summaries with Ollama..."
	@$(PY) scripts/generate_summaries.py "$(INPUTDIR)/posts"

push:
	git add . && git commit -m "Blog content update" && git push

.PHONY: html help clean regenerate e2e venv serve serve-global devserver publish push format-html validate-html validate-html-strict fix-duplicate-ids remove-anchor-ids generate-summaries
