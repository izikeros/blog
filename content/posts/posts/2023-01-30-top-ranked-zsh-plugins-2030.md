---
Title: Top popular Zsh plugins on GitHub (2023)
slug: top-popular-zsh-plugins-on-github-2023
Date: 2023-01-30
modified: 2023-01-30
Start: 2023-01-30
Tags: zsh, scrapping, python, Linux
Category: Linux
Image: images/zsh/inside-work-tree.jpg
Summary: Explore the most popular Zsh plugins from the 2000+ options on the Awesome Zsh plugins GitHub project. See which ones have the highest number of stars from the Zsh community.
Status: published
---

> There is a series of articles dedicated to Zsh plugins: [2018](../top-popular-zsh-plugins-on-github/), [2019](../top-popular-zsh-plugins-on-github-2019/), [2021](../top-popular-zsh-plugins-on-github-2021/)

The collection [Awesome Zsh plugins](https://github.com/unixorn/awesome-zsh-plugins) of projects that can be useful for Zsh users grew substantially from the first, 2018 release of my article on Top-popular Zsh plugins - from 800+ to 2100+.  In this article, I'm listing top-popular tools that might be interesting for Zsh users and console users in general. As in previous year, I have divided them into four categories:

- **Tools** - general tools that are popular among console lovers, in most cases not limited to Zsh
- **Frameworks** - tools for managing Zsh configuration and plugins 
- **Prompts** - projects that help to configure shell prompts
- **Python tools** - tools that ease work with Python virtual environments

and added two new categories

- **Fuzzy finders** - tools for filtering lists, options, etc.
- **Docker/Containers/Kubernetes** - tools that helps to work with container technologies

Shortcuts to categories:
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Tools](#tools)
- [Frameworks](#frameworks)
- [Prompts](#prompts)
- [Python tools](#python-tools)
- [Fuzzy finders](#fuzzy-finders)
- [Docker/Containers](#dockercontainers)

<!-- /MarkdownTOC -->

<a id="tools"></a>
## Tools
| link                                                                            | description                                                                                                                                                                      | stars |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| [thefuck](https://github.com/nvbn/thefuck)                                      | Magnificent app which corrects your previous console command.                                                                                                                    | 75.5k |
| [fzf](https://github.com/junegunn/fzf)                                          | A command-line fuzzy finder                                                                                                                                                      | 49.5k |
| [bat](https://github.com/sharkdp/bat)                                           | A cat(1) clone with wings.                                                                                                                                                       | 39.3k |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp)                                      | A youtube-dl fork with additional features and fixes                                                                                                                             | 38.5k |
| [ripgrep](https://github.com/BurntSushi/ripgrep)                                | ripgrep recursively searches directories for a regex pattern while respecting your gitignore                                                                                     | 35.5k |
| [powerlevel10k](https://github.com/romkatv/powerlevel10k)                       | A Zsh theme                                                                                                                                                                      | 34.0k |
| [tmux](https://github.com/tmux/tmux)                                            | tmux source code                                                                                                                                                                 | 27.6k |
| [fd](https://github.com/sharkdp/fd)                                             | A simple, fast and user-friendly alternative to 'find'                                                                                                                           | 26.1k |
| [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)         | Fish-like autosuggestions for zsh                                                                                                                                                | 24.9k |
| [exa](https://github.com/ogham/exa)                                             | A modern replacement for ls                                                                                                                                                      | 20.5k |
| [asdf](https://github.com/asdf-vm/asdf)                                         | Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more                                                                                                 | 16.6k |
| [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) | Fish shell like syntax highlighting for Zsh.                                                                                                                                     | 16.2k |
| [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy)                      | Good-lookin' diffs. Actually… nah… The best-lookin' diffs.                                                                                                                       | 16.2k |
| [z](https://github.com/rupa/z)                                                  | z - jump around                                                                                                                                                                  | 15.0k |
| [autojump](https://github.com/wting/autojump)                                   | A cd command that learns - easily navigate directories from the command line                                                                                                     | 14.6k |
| [powerlevel9k](https://github.com/bhilburn/powerlevel9k)                        | Powerlevel9k was a tool for building a beautiful and highly functional CLI, customized for you. P9k had a substantial impact on CLI UX, and its legacy is now continued by P10k. | 13.4k |
| [ranger](https://github.com/ranger/ranger)                                      | A VIM-inspired filemanager for the console                                                                                                                                       | 12.8k |
| [navi](https://github.com/denisidoro/navi)                                      | An interactive cheatsheet tool for the command-line                                                                                                                              | 12.4k |
|[shellfirm](https://github.com/kaplanelad/shellfirm)               |Intercept any risky patterns (default or defined by you) and prompt you a small challenge for double verification                                                    |0.7k |                                                                                

Please find description of selected tools that were not described in previous years.

### navi
An interactive cheatsheet tool for the command-line.

[![Demo](https://camo.githubusercontent.com/d3cba877034f1c46a893a248355c1f923ce96906df8bd42c321f68923d09da29/68747470733a2f2f61736369696e656d612e6f72672f612f3430363436312e737667)](https://asciinema.org/a/406461)

**navi** allows you to browse through cheatsheets (that you may write yourself or download from maintainers) and execute commands. Suggested values for arguments are dynamically displayed in a list.

### shellfirm
`shellfirm` will intercept any risky patterns and immediately prompt a small challenge that will double verify your action, think of it as a captcha for your terminal.
![shellfirm example](https://github.com/kaplanelad/shellfirm/raw/main/docs/media/example.gif)

<a id="frameworks"></a>
## Frameworks
The top-3 Zsh frameworks in the ranking remains the same: Oh My Zsh, prezto and antigen.

|                                   link                                    |                                                                             description                                                                             |stars |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|[ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)                              |A delightful community-driven (with 2,100+ contributors) framework for managing your zsh configuration.                                                              |154.7k|
|[prezto](https://github.com/sorin-ionescu/prezto)                          |The configuration framework for Zsh                                                                                                                                  |13.2k |
|[antigen](https://github.com/zsh-users/antigen)                            |The plugin manager for zsh.                                                                                                                                          |7.5k  |
|[zplug](https://github.com/zplug/zplug)                                    | A next-generation plugin manager for zsh                                                                                                                            |5.3k  |
|[zimfw](https://github.com/zimfw/zimfw)                                    |Zim: Modular, customizable, and blazing fast Zsh framework                                                                                                           |3.0k  |
|[antibody](https://github.com/getantibody/antibody)                        |The fastest shell plugin manager.                                                                                                                                    |1.7k  |
|[zinit](https://github.com/zdharma-continuum/zinit)                        | Flexible and fast ZSH plugin manager                                                                                                                                |1.6k  |
|[zgen](https://github.com/tarjoilija/zgen)                                 |A lightweight and simple plugin manager for ZSH                                                                                                                      |1.4k  |

Personally, I use zgen, which works well however, last commits to the repo of this projects are from 2018. There is continuation of the heritage of this plugin manager in the project called: [zgenom](https://github.com/jandamm/zgenom)
<a id="prompts"></a>
## Prompts
|                               link                                |                                                                             description                                                                             |stars|
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|[spaceship-prompt](https://github.com/denysdovhan/spaceship-prompt)| Minimalistic, powerful and extremely customizable Zsh prompt                                                                                                        |17.9k|
|[powerline](https://github.com/powerline/powerline)                |Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.|13.7k|
|[pure](https://github.com/sindresorhus/pure)                       |Pretty, minimal and fast ZSH prompt                                                                                                                                  |11.9k|
|[oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh)         |A blazing fast cross platform/shell prompt renderer                                                                                                                  |9.6k |
|[bash-git-prompt](https://github.com/magicmonty/bash-git-prompt)   |An informative and fancy bash prompt for Git users                                                                                                                   |6.4k |
|[powerline-shell](https://github.com/b-ryan/powerline-shell)       |A beautiful and useful prompt for your shell                                                                                                                         |6.0k |
|[liquidprompt](https://github.com/nojhan/liquidprompt)             |A full-featured & carefully designed adaptive prompt for Bash & Zsh                                                                                                  |4.3k |
|[oh-my-git](https://github.com/arialdomartini/oh-my-git)           |An opinionated git prompt for bash and zsh                                                                                                                           |3.6k |
|[kube-ps1](https://github.com/jonmosco/kube-ps1)                   |Kubernetes prompt info for bash and zsh                                                                                                                              |3.0k |
|[powerline-go](https://github.com/justjanne/powerline-go)          | A beautiful and useful low-latency prompt for your shell, written in go                                                                                             |2.6k |
|[zsh-git-prompt](https://github.com/olivierverdier/zsh-git-prompt) |Informative git prompt for zsh                                                                                                                                       |1.6k |
|[gitstatus](https://github.com/romkatv/gitstatus)                  |Git status for Bash and Zsh prompt                                                                                                                                   |1.4k |
|[geometry](https://github.com/geometry-zsh/geometry)               |geometry is a minimal, fully customizable and composable zsh prompt theme                                                                                            |0.9k |
|[typewritten](https://github.com/reobin/typewritten)               |A minimal, lightweight, informative zsh prompt theme                                                                                                                 |0.8k |
|[hyperzsh](https://github.com/tylerreckart/hyperzsh)               |Hyperminimal zsh prompt                                                                                                                                              |0.5k |
|[posh-git-sh](https://github.com/lyze/posh-git-sh)                 |Bash/ZSH version of the posh-git command prompt                                                                                                                      |0.4k |

<a id="python-tools"></a>
## Python tools
Since I work a lot in Python environment - this category will be bit longer than it normally should be.

|                                          link                                           |                                                                                    description                                                                                     |stars|
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|[pyenv](https://github.com/pyenv/pyenv)                                                  |Simple Python version management                                                                                                                                                    |30.4k|
|[pip-tools](https://github.com/jazzband/pip-tools)                                       |A set of tools to keep your pinned Python dependencies fresh.                                                                                                                       |6.6k |
|[pipx](https://github.com/pypa/pipx)                                                     |Install and Run Python Applications in Isolated Environments                                                                                                                        |5.9k |
|[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)                            |a pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)                                                                                                                      |5.3k |
|[pew](https://github.com/berdario/pew)                                                   |A tool to manage multiple virtual environments written in pure python                                                                                                               |1.1k |
|[virtualfish](https://github.com/adambrenecki/virtualfish)                               |Fish shell tool for managing Python virtual environments                                                                                                                            |1.0k |
|[zsh-autoswitch-virtualenv](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv)| ZSH plugin to automatically switch python virtualenvs (including pipenv and poetry) as you move between directories                                                                |0.4k |
|[shtab](https://github.com/iterative/shtab)                                              |Automagic shell tab completion for Python CLI applications                                                                                                                       |0.2k |
|[zpy](https://github.com/AndydeCleyre/zpy)                                               |Zsh helpers for Python venvs, with pip-tools                                                                                                                                        |40   |
|[project](https://github.com/gko/project)                                                |Create node, rust, python or ruby project locally and on github (private or public)                                                                                             |19   |
|[virtualz](https://github.com/aperezdc/virtualz)                                         |Virtualfish-alike Python virtualenv wrapper for Zsh                                                                                                                                 |9    |
|[zargparse](https://github.com/ctil/zargparse)                                           |A tool for generating zsh completion files for python command line tools that use argparse                                                                                          |9    |
|[one-key-linux-setup](https://github.com/miracleyoo/one-key-linux-setup)                 |Scripts which aims to initialize and configure a linux system quickly. Mainly include update, zsh, oh-my-zsh, zsh plugins, python, and so on. Continue to update and welcome issues.|7    |
|[zsh-activate-py-environment](https://github.com/se-jaeger/zsh-activate-py-environment)  |ZSH plugin that automagically detects and activates your python environments (poetry, virtualenv, conda) while traversing directories.                                              |7    |



<a id="fuzzy-finders"></a>
## Fuzzy finders
| link                                                                        | description                                                                               | stars |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----- |
| [fzf](https://github.com/junegunn/fzf)                                      | A command-line fuzzy finder                                                               | 49.5k |
| [peco](https://github.com/peco/peco)                                        | Simplistic interactive filtering tool                                                     | 7.2k  |
| [skim](https://github.com/lotabout/skim)                                    | Fuzzy Finder in rust!                                                                     | 3.8k  |
| [percol](https://github.com/mooz/percol)                                    | adds flavor of interactive filtering to the traditional pipe concept of UNIX shell        | 3.2k  |
| [fzy](https://github.com/jhawthorn/fzy)                                     | A simple, fast fuzzy finder for the terminal                                              | 2.7k  |
| [enhancd](https://github.com/b4b4r07/enhancd)                               | A next-generation cd command with your interactive filter                                 | 2.3k  |
| [fz](https://github.com/changyuheng/fz)                                     | Cli shell plugin, the missing fuzzy tab completion feature for the z jump around command. | 0.4k  |

Note other, less popular tools in that category:
[pmy](https://github.com/relastle/pmy), [zeno.zsh](https://github.com/yuki-yano/zeno.zsh), [fzf-zsh-completions](https://github.com/chitoku-k/fzf-zsh-completions),[fzshell](https://github.com/mnowotnik/fzshell),[zsh-fzy](https://github.com/aperezdc/zsh-fzy),[zsh-history-filter](https://github.com/MichaelAquilina/zsh-history-filter),[zsh-fzf-pass](https://github.com/smeagol74/zsh-fzf-pass),[zsh-plugin-fd](https://github.com/aubreypwd/zsh-plugin-fd),[zsh-fuzzy-wd](https://github.com/spodin/zsh-fuzzy-wd), [qwy](https://github.com/Ryooooooga/qwy)

<a id="dockercontainers"></a>
## Docker/Containers
Not mentioned in the ranking below but worth checking is [k9s](https://github.com/derailed/k9s) (19.4k stars).

|                                         link                                          |                                         description                                         |stars|
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----|
|[kubectx](https://github.com/ahmetb/kubectx)                                   |Faster way to switch between clusters and namespaces in kubectl                                                                                                                 |14.6k|
|[ctop](https://github.com/bcicen/ctop)                                                 |Top-like interface for container metrics                                                     |13.9k|
|[zsh-in-docker](https://github.com/deluan/zsh-in-docker)                               |Install Zsh, Oh-My-Zsh and plugins inside a Docker container with one line!                  |0.6k |
|[fzf-zsh-completions](https://github.com/chitoku-k/fzf-zsh-completions)                |Fuzzy completions for fzf and Zsh (git, kubectl, docker, ...)                                |90 |
|[docker-zsh-completion](https://github.com/greymd/docker-zsh-completion)               |Zsh completion for docker and docker-compose.                                                |40 |
|[docker-compose-zsh-plugin](https://github.com/sroze/docker-compose-zsh-plugin)        |ZSH plugin that display status of project containers                                         |45 |




### K9s
[K9s](https://github.com/derailed/k9s) provides a curses based terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with observed resources.
![k9s](https://golangexample.com/content/images/2019/02/screen_po.png)