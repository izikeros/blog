---
Category: note
Date: '2021-09-14'
Modified: '2023-07-12'
Slug: git-autocommit-on-file-changes
Status: published
Summary: How to create automatically commits if any file in the watched folder was changed
Tags: git, autocommit, note-taking, notes, automatic, automation, git/autocommit
Title: Git - Autocommit on File Changes
citation_needed: false
---

> **Motivation:** I wanted to track the history of the changes introduced in my notes folder. Didn't want to create a commit, or redact the commit message after each change because typically during the day I made multiple edits in notes ad prefer to minimize time spent on managing my notes. I'm quickly jumping into the notes, adding something to existing notes, or creating new ones. Remembering to commit each change is too much overhead for me. I started to look for a solution that will monitor my notes folder, and, if anything changed, create a commit. I found several solutions that serve that purpose.

For reference see [making-git-auto-commit](https://stackoverflow.com/questions/420143/making-git-auto-commit) on StackOverflow.

My choice was **gitwatch** used as systemd service.

<!-- MarkdownTOC levels='1,2,3' autolink=True autoanchor=True -->

- [gitwatch , active](#gitwatch--active)
  - [Notes for installation on Mac](#notes-for-installation-on-mac)
- [gwatch  low activity](#gwatch-low-activity)
- [etckeeper](#etckeeper)
- [git-etc github: ★4, low activity, created 9 years ago, last commit in 2014](#git-etc-github-%E2%98%854-low-activity-created-9-years-ago-last-commit-in-2014)
- [Git Powercommit](#git-powercommit)
- [git-wip](#git-wip)
- [inotify](#inotify)
- [watchman](#watchman)
- [inotify.sh](#inotifysh)

<!-- /MarkdownTOC -->

<a id="gitwatch--active"></a>

# [gitwatch](https://github.com/gitwatch/gitwatch) ![GitHub stars](https://img.shields.io/github/stars/gitwatch/gitwatch.svg?logo=github), active

A bash script to watch a file or folder and commit changes to a git repo

Justification for my choice:

- active with large community
- There is an AUR package for Archlinux
- does exactly what I want, nothing more
- can be used as daemon that starts on boot

```
Usage:
gitwatch [-s <secs>] [-d <fmt>] [-r <remote> [-b <branch>]]
          [-m <msg>] [-l|-L <lines>] <target>
```

<a id="notes-for-installation-on-mac"></a>

## Notes for installation on Mac

If running on OS X, you'll need to install the following Homebrew tools:

```sh
brew install fswatch
brew install coreutils
```

and

```sh
brew install gitwatch
```

1. If installed to a path other than `/usr/bin/gitwatch`, modify `gitwatch@.service` to suit. In my case, `gitwatch` was found in `/usr/local/bin/gitwatch`
2. Create dir if it does not exist and copy systemd service file with `mkdir -p "$HOME/.config/systemd/user" && cp gitwatch@.service $HOME/.config/systemd/user`
If you cannot find `gitwatch@.service` file take it from the GitHub repository.

3. Start and enable the service for a given path by running `systemctl --user --now enable gitwatch@$(systemd-escape "'-r url/to/repository' /path/to/folder").service`
On macOS you need to act differently

- take `.plist` file from the repo, and adjust it to your needs
- copy modified plist to `/Library/LaunchDaemons/`` with sudo
- note: if there is a proper `gitwatch` script path (I needed to change `gitwatch.sh` to `gitwatch`)

<a id="gwatch-low-activity"></a>

# [gwatch](https://github.com/jw0k/gwatch) ![GitHub stars](https://img.shields.io/github/stars/jw0k/gwatch.svg?logo=github) low activity

A program that watches a folder for file modifications and commits them to a git repository automatically

After `gwatch` is started it will watch a given folder and all of its subfolders (recursively) for changes. If a change occurs, a timer will be started (the 30s by default). After the timer expires, `gwatch` will create a new git commit with all the modifications. The timer is to prevent creating too many commits when there are a lot of modifications. In order for `gwatch` to successfully create commits, a git repository must be initialized in the watched folder.

<a id="etckeeper"></a>

# [etckeeper](http://joeyh.name/code/etckeeper/)
>
> NOTE: In my case, I didn't need to track permissions

`etckeeper` is a collection of tools to let `/etc` be stored in a git, mercurial, darcs, or bzr repository. It hooks into apt (and other package managers including yum and pacman-g2) to automatically commit changes made to `/etc` during package upgrades. It tracks file metadata that revision control systems do not normally support, but that is important for `/etc`, such as the permissions of `/etc/shadow`. It's quite modular and configurable, while also being simple to use if you understand the basics of working with revision control.

`etckeeper` now has a website at <http://etckeeper.branchable.com/>.

<a id="git-etc-github-%E2%98%854-low-activity-created-9-years-ago-last-commit-in-2014"></a>

# [git-etc](https://arcanis.me/projects/git-etc) github: ★4, low activity, created 9 years ago, last commit in 2014

A simple daemon that automatically creates a git repository in the given directory and creates a commit at the specified time interval.

Has GUI, has AUR package

<a id="git-powercommit"></a>

# [Git Powercommit](https://github.com/grwlf/git-powercommit)

Commit every changed submodule. Commit every changed regular file or folder, aggregating the files that share a folder into a single commit.

<a id="git-wip"></a>

# [git-wip](https://github.com/bartman/git-wip)

`git-wip` is a script that will manage Work In Progress (or WIP) branches. WIP branches are mostly thrown away but identify points of development between commits. The intent is to tie this script into your editor so that each time you save your file, the `git-wip` script captures that state in git. `git-wip` also helps you return to a previous state of development.

<a id="inotify"></a>

# [inotify](http://inotify.aiken.cz/?section=incron&page=about&lang=en)

This program is an "inotify cron" system. It consists of a daemon and a table manipulator. You can use it in a similar way as the regular cron. The difference is that the inotify cron handles filesystem events rather than time periods.

<a id="watchman"></a>

# [watchman](https://facebook.github.io/watchman/)

Watchman exists to watch files and record when they change. It can also trigger actions (such as rebuilding assets) when matching files change

<a id="inotifysh"></a>

# [inotify.sh](https://github.com/nzvincent/nzvincent-github/blob/master/inotify-tools/inotify.sh)

This script uses inotifywatch to monitor file status and trigger commands.
Designed for Ansible playbook, but you can use this for other development purposes.
To install e.g. `apt-get install -y inotify-tools`
see: <https://gist.github.com/darencard/5d42319abcb6ec32bebf6a00ecf99e86>

up:: [[MOC_Git]]]
