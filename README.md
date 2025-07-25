This is repository with blog [safjan.com](http://safjan.com). It is created using [Pelican](https://github.com/getpelican) - static site generator written in Python.

- [Quick start](#quick-start)
- [Maintenance](#maintenance)
  - [setup environment with pipenv](#setup-environment-with-pipenv)
  - [activate environment](#activate-environment)
  - [upgrade environment](#upgrade-environment)
  - [install plugins and themes](#install-plugins-and-themes)
    - [under Linux](#under-linux)
  - [generate version to be published](#generate-version-to-be-published)
  - [generate development preview](#generate-development-preview)
  - [Jupyter notebooks for content creation](#jupyter-notebooks-for-content-creation)
    - [Checklist for notebook-based content creation](#checklist-for-notebook-based-content-creation)
    - [Add badges that allows running notebooks in Google Colab or Binder](#add-badges-that-allows-running-notebooks-in-google-colab-or-binder)
    - [Figure and Table captions](#figure-and-table-captions)
    - [Hide prompt](#hide-prompt)
    - [Styling](#styling)
- [TODO](#todo)
  - [Customization examples](#customization-examples)
    - [Theme customization, monokai for code blocks](#theme-customization-monokai-for-code-blocks)
    - [Other style of using notebooks (probably)](#other-style-of-using-notebooks-probably)
- [Problems with Pelican](#problems-with-pelican)
  - [1. Using outdated plugin for jupyter notebook conversion](#1-using-outdated-plugin-for-jupyter-notebook-conversion)
  - [2. Modifications to Flex theme](#2-modifications-to-flex-theme)
  - [Black formatting](#black-formatting)
- [Using notes category](#using-notes-category)
- [Aside (sidebar)](#aside-sidebar)
- [New metadata](#new-metadata)

## Quick start

Activate virtual env (if already created)

```sh
source ~/.venv/bin/activate
```

Render content and refresh on modifications

```sh
pelican -lr
```

## Maintenance

### setup environment with pipenv

go to blog directory

```sh
cd ~/blog
```

create virtual env if none exist:
```
```sh
uv lock --upgrade && uv sync
uv pip install "git+https://github.com/izikeros/pelican-obsidian"
uv pip install "git+https://github.com/lextoumbourou/pelican-jupyter"
```

### activate environment

Go to the directory containing the blog and activate virtual environment with

```bash
z blog && source ~/.venv/bin/activate
```

### upgrade environment

To upgrade packages that are upgradable

```bash
pdm upgrade
```

### install plugins and themes

#### under Linux

clone plugins to separate directory (e.g. ~/bulk)

```sh
git clone --recursive https://github.com/getpelican/pelican-plugins
```

Update submodules

```
git submodule update --recursive --remote
```

then:

- create pelican-plugins directory in blog
- symlink required plugins

### generate version to be published

```sh
make publish
```

It uses `pelicanconf.py` settings overwritten by `publishconf.py`.

### generate development preview

```sh
pelican -lr
```

or

```sh
make devserver
```

### Jupyter notebooks for content creation

#### Checklist for notebook-based content creation

- [ ] skip notebook title header (title will be added by Pelican)
- [ ] short introductory text about purpose of the notebook. Can be the same text as `summary` in the front matter.
- [ ] links to launch notebook in "Colab" or "Binder"
- [ ] add table of contents if notebook has 5 o more headings
- [ ] figures has markdown captions
- [ ] use black to format cells
- [ ] keep lines short to avoid horizontal scroll (use ruler=80?) in jupyter
- [ ] provide styling by placing styling snippet in last cell
- [ ] Article is still valuable, has flow even if all code cells are hidden
- [ ] hide input of trivial cells (such as imports). In extreme - hide all code cells.
- [ ] have conclusion and lessons learned. If no conclusion then summary at least.

#### Add badges that allows running notebooks in Google Colab or Binder

After article intro put the snippet of markdown code. See below example for the notebook named `2018-04-05-whats_cooking_NLP.ipynb`

```markdown
[![Open In Colab](../images/badges/colab.svg)](https://colab.research.google.com/github/izikeros/blog/blob/master/content/posts/notebooks/2018-04-05-whats_cooking_NLP.ipynb)&nbsp;[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/izikeros/blog/master?labpath=content%2Fposts%2Fnotebooks%2F2018-04-05-whats_cooking_NLP.ipynb)
```

> Note: Ensure that notebook can run with all the data needed

#### Figure and Table captions

Use markdown cells. Examples of captions:

```mark
*Figure 2. Relations visualized as graph created from adjacency matrix*

*Table 1. Transition matrix - value in each matrix element $a_{ij}$ represents probability that the spy will move to country $j$ (the column) from country $i$ (the row).*
```

#### Hide prompt

add code as below to the notebook (e.g. last cell) and execute

```python
from IPython.core.display import HTML
HTML("<style>.prompt{display: None;</style>")
```

#### Styling

Add this cell to the end of notebook and execute to see the effect. Styling is not important when opening in Colab. There is `notebook_custom_style.css` applied to the notebook (I think this stylesheet is heavily based on one use in Bayesian methods for hackers).

> NOTE: this cell is not important for the article thus should be not visible in rendered article. Ensure that `remove_input` tag is added to the cell (`View->Cell toolbar->Tags`). There is `nbconvert` preprocessing applied that removes such cells. See `pelicanconf.py`

```python
# Ensure this cell has remove_input tag added (to hide it in blog post text)
try:
  import google.colab
  IN_COLAB = True
except:
    from IPython.core.display import HTML

    def css_styling():
        styles = open("../styles/notebook_custom_style.css", "r").read()
        return HTML(styles)

    css_styling()
```

## TODO

- [ ] Normalize `yaml` heading to articles and `.nbdata` files as well - write small python script for that job
- [ ] Prepare tool that will add `remove_input` tag to all code cells of the notebook (and will be able to revert it)
- [ ] Write new about me as professional (do not reveal too much personal, private-life related facts)
- [ ] Notes are note displayed on tag view - either enable tag view or disable `note` category
- [ ] Add Last updated info (see: <https://rasor.github.io/>)
- [ ] Consider adding links to pages in sidebar: projects (tbd), publications (google scholar), cv (static), about me (already there)
- [ ] Ensure dependencies that will allow running notebook in colab <https://github.com/weiji14/deepbedmap/issues/61>
- [ ] Add What do You think for quick feedback from readers (see: <https://jackmckew.dev/>)
- [ ] Move sidebar HTML to separate HTML files the is being included
- [ ] Remove `notes` from the list of categories
- [ ] Check for dead links
- [ ] Remove formatting cells from the end of notebook
- [x] Add BibTex note - how to cite given article
- [ ] Add collapsible section (collapsed by default) on significant revisions (see: <https://martinfowler.com/articles/2023-chatgpt-xu-hao.html>)

```
Significant Revisions
20 April 2023: Added material on context window
13 April 2023: Published
04 April 2023: Started drafting
```


- "Next post" in notes moves to next post which can be blog post or note. Implement different button ("Next note") and implement logic for that. Need separate list of notes for that purpose.
- Tag cells to remove with "remove_cell" (`View -> Cell Toolbar -> Tags`)
- in pelicanconf.py add code that uses preprocessing:

```python
from nbconvert.preprocessors import TagRemovePreprocessor
from traitlets.config import Config
c = Config()
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.enabled = True
IPYNB_PREPROCESSORS=[TagRemovePreprocessor(config=c)]
```

### Customization examples

#### Theme customization, monokai for code blocks
<https://cassiobotaro.dev/post/ordenando-dicionario-por-valores/>
<https://github.com/cassiobotaro/cassiobotaro.github.io>
(author now moved blog to Hugo)

#### Other style of using notebooks (probably)
<https://dvatvani.github.io/whatsapp-analysis.html#whatsapp-analysis>

(no code cells visible, article contains link to github repo with notebook and instructions)

## Problems with Pelican

### 1. Using outdated plugin for jupyter notebook conversion

I'm using [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) plugin. This plugin is replaced by newer: [pelican-jupyter](https://github.com/danielfrg/pelican-jupyter). The old one works with: pinned `pelican==4.5.4`,  `nbconvert==5.6.0`, `notebook==5.6.0` and `python_version = "3.7"` - otherwise blog is not rendered correctly (for details run: `pelican -lr --debug`)

> Solution: I would need to migrate to the new system of plugins and their configuration (see TODO #2). Perhaps would be good to give a try on a toy-blog site (new minimal environment)? Helper instructions might be found here: <https://janakiev.com/blog/pelican-jupyter/>

See: <https://github.com/danielfrg/pelican-jupyter/issues/126>

Author of this plugin is not using Pelican for blogging anymore: <https://github.com/danielfrg/pelican-jupyter/issues/126#issuecomment-715472746>

### 2. Modifications to Flex theme

It is now very difficult to use recent updates to Flex theme since my version of Flex diverged. Perhaps with merging tool some changes could be applied. I think, that biggest problems were with Font Awesome (different version and my mods to styling social).

> Solution: try to extract my changes as patches

### Black formatting

Use `black --ipynb .` in `posts` directory to format notebooks (requires black with jupyter dependencies installed: `pip install black[jupyter]`).

## Using notes category

- create article with category 'note'

- these notes are hidden in home page (filtering in index.template)

## Aside (sidebar)

- styling for social icons is defined in `custom.css`
- headline is hardcoded in `pelicanconf.py` in `SITESUBTITLE` variable
- social icons `style.less`

## New metadata

see my fork of Flex new metadata
