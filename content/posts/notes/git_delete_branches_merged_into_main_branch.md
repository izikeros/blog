---
category: note
date: '2021-12-16'
modified: '2022-02-17'
slug: git-delete-branches-merged-into-main-branch
status: published
suggested_tags: branch, delete, git, merged
tags: branch, delete, git, merged
title: Git - delete branches that are merged into main branch
---

```toc
```



When actively developing feature branches that are later merged into develop branch you might end up with a bunch of local branches that are not relevant anymore, and do not have their remote counterparts and it would be good to remove them locally.

## First - fetch and prune
```sh
$ git fetch -p
```
`git fetch --prune` will connect to the remote and fetch the latest remote state before pruning. It is essentially a combination of commands:
```sh
git fetch --all && git remote prune
```
> NOTE: The generic `git prune` command is entirely different. it will delete locally detached commits.

### How Do I Clean Outdated Branches?
`git fetch --prune` is the best utility for cleaning outdated branches. It will connect to a shared remote repository remote and fetch all remote branch refs. It will then delete remote refs that are no longer in use on the remote repository.

### Does Git Remote Prune Origin Delete the Local Branch?
No `git remote prune origin` will only delete the refs to remote branches that no longer exist. Git stores both local and remote refs. A repository will have `local/origin` and `remote/origin` ref collections. `git remote prune origin` will only prune the refs in `remote/origin`. This safely leaves local work in `local/origin.`
To remove local branches you need to use `git branch -d` or replace `-d` with `-D`.

**Credits:** Prune explanation comes from an excellent article on [Git Prune](https://www.atlassian.com/git/tutorials/git-prune)

## Second - delete merged local branches
```sh
$ git branch --merged origin/develop | grep -v develop | xargs git branch -d
```

`--merged origin/develop` - branches merged into remote develop
`grep -v develop` - for safety reasons: exclude develop from the list of branches to delete

Read more here:
https://stackoverflow.com/questions/16590160/remove-branches-not-on-remote
