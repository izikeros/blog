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

