# Blog
This is repository with my blog [safjan.com](http://safjan.com).

It is using Pelican - static site generator written in Python.

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
pipenv install pelican
```

## setup environment with conda
```sh
conda install -c conda-forge pelican typogrify
conda install ipython markdown nbconvert jupyter beautifulsoup4 pylint
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


## Jupyter notebooks
### Hide prompt
add code as below to the notebook (e.g. last cell) and execute
```python
from IPython.core.display import HTML
HTML("<style>.prompt{display: None;</style>")
```

### Collapse cells
TODO

## Activate environment
pipenv shell

## Upgrade environment
pipenv upgrade


## TODO:
- Normalize Yaml heading to articles and .nbdata files as well - write small python script for that job
- Migrate to Pelican 4 style of plugins
- write new about me as professional (do not reveal too much personal, private-life related facts)
- add possibility to share the contents on social media using icons near the top of the article. Now: "Like this article? Share it with your friends!" - available
  - See themes:
    - https://github.com/mamcmanus/brutalist/tree/de551620221ec3f1958250adfaffbbc81e9b748c
- add Last updated info (see: https://rasor.github.io/)
- consider adding links to pages in sidebar: projects (tbd), publications (google scholar), cv (static), about me (already there)
- add launch in binder to notebook-based articles (see: https://tobiasraabe.github.io/blog/numba-vectorize-and-guvectorize.html)
- Add: "Krystian Safjan's Blog" (large font-size), and line below few job titles (Data Scientist | Team Leader | Researcher) (see: https://jackmckew.dev/)
- Add What do You think for quick feedback from readers (see: https://jackmckew.dev/)
- Move sidebar HTML to separate HTML files the is being included


## Customization examples:

### Theme customization, monokai for code blocks
https://cassiobotaro.dev/post/ordenando-dicionario-por-valores/
https://github.com/cassiobotaro/cassiobotaro.github.io
(author moved blog to Hugo)

### Using notebooks (probably)
https://dvatvani.github.io/whatsapp-analysis.html#whatsapp-analysis