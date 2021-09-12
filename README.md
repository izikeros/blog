# Blog
This is repository with my blog [safjan.com](http://safjan.com). It is created using Pelican - static site generator written in Python.

# Maintenance

## setup environment with pipenv

go to blog directory
```sh
cd ~/blog
```

create virtual env if none exist:
```sh
pipenv --python 3.9
```

install packages from Pipfile:
```sh
pipenv install "pelican[markdown]"
```

## activate environment

Go to the directory containing the blog and activate Pipenv virtual envitonment with

```bash
pipenv shell
```

## upgrade environment

To upgrade packages that are upgradable

```bash
pipenv upgrade
```

## install plugins and themes

### under linux
clone plugins to separate directory (e.g. ~/bulk)
```
git clone --recursive https://github.com/getpelican/pelican-plugins
```

Update submodules
```
git submodule update --recursive --remote
```

then:

* create pelican-plugins directory in blog
* symlink required plugins

## generate version to be published
```sh
make publish
```
It uses `pelicanconf.py` settings overwritten by `publishconf.py`.

## generate development preview
```sh
pelican -lr
```
or

```sh
make devserver
```


## Jupyter notebooks for content creation

### Hide prompt
add code as below to the notebook (e.g. last cell) and execute
```python
from IPython.core.display import HTML
HTML("<style>.prompt{display: None;</style>")
```

### Collapse cells
TODO


# TODO:
- [ ] 1. Normalize Yaml heading to articles and .nbdata files as well - write small python script for that job
- [ ] 2. Migrate to Pelican 4 style of plugins
- [ ] 3. write new about me as professional (do not reveal too much personal, private-life related facts)
- [ ] 4. add possibility to share the contents on social media using icons near the top of the article. Now: "Like this article? Share it with your friends!" - available
  - See themes:
    - https://github.com/mamcmanus/brutalist/tree/de551620221ec3f1958250adfaffbbc81e9b748c
- [ ] 5. add Last updated info (see: https://rasor.github.io/)
- [ ] 6. consider adding links to pages in sidebar: projects (tbd), publications (google scholar), cv (static), about me (already there)
- [ ] 7. add launch in binder to notebook-based articles (see: https://tobiasraabe.github.io/blog/numba-vectorize-and-guvectorize.html)
- [ ] 8. Add: "Krystian Safjan's Blog" (large font-size), and line below few job titles (Data Scientist | Team Leader | Researcher) (see: https://jackmckew.dev/)
- [ ] 9. Add What do You think for quick feedback from readers (see: https://jackmckew.dev/)
- [ ] 10. Move sidebar HTML to separate HTML files the is being included


## Customization examples:

### Theme customization, monokai for code blocks
https://cassiobotaro.dev/post/ordenando-dicionario-por-valores/
https://github.com/cassiobotaro/cassiobotaro.github.io
(author now moved blog to Hugo)

### Other style of using notebooks (probably)
https://dvatvani.github.io/whatsapp-analysis.html#whatsapp-analysis

(no code cells visible, article contains link to github repo with notebook and instructions)

# Problems with Pelican
## 1. Using outdated plugin for jupyter notebook conversion.

I'm using [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) plugin. This plugin is replaced by newer: [pelican-jupyter](https://github.com/danielfrg/pelican-jupyter). The old one works with: pinned `pelican==4.5.4`,  `nbconvert==5.6.0`, `notebook==5.6.0` and `python_version = "3.7"` - otherwise blog is not rendered correctly (for details run: `pelican -lr --debug`)

> Solution: I would need to migrate to the new system of plugins and their configuration (see TODO #2). Perhaps would be good to give a try on a toy-blog site (new minimal environment)? Helper instructions might be found here: https://janakiev.com/blog/pelican-jupyter/

See: https://github.com/danielfrg/pelican-jupyter/issues/126

Author of this plugin is not using Pelican for blogging anymore: https://github.com/danielfrg/pelican-jupyter/issues/126#issuecomment-715472746

## 2. Modifications to Flex theme

It is now very difficult to use recent updates to Flex theme since my version of Flex diverged. Perhaps with merging tool some changes could be applied. I think, that biggest problems were with Font Awesome (different version and my mods to styling social).

> Solution: try to extract my changes as patches
