# Blog
This is repository with my blog [safjan.com](http://safjan.com).

It is using Pelican - static site generator written in Python.

## setup environment
go to blog directory
```
cd ~/blog
```

create virtual env if none exist:
```
pipenv --python 3.7
```

install packages from Pipfile:
```
pipenv install
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