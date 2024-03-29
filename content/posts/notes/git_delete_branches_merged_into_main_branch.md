---
Category: note
Date: '2021-12-16'
Modified: '2023-07-12'
Slug: git-delete-branches-merged-into-main-branch
Status: published
Tags: branch, delete, git, merged
Title: Git - Delete Branches That Are Merged Into the Main Branch
suggested_tags: branch, delete, git, merged
---

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [First - fetch and prune](#first---fetch-and-prune)
 	- [How Do I Clean Outdated Branches?](#how-do-i-clean-outdated-branches)
 	- [Does Git Remote Prune Origin Delete the Local Branch?](#does-git-remote-prune-origin-delete-the-local-branch)
- [Second - delete merged local branches](#second---delete-merged-local-branches)

<!-- /MarkdownTOC -->

When actively developing feature branches that are later merged into develop branch you might end up with a bunch of local branches that are not relevant anymore, and do not have their remote counterparts and it would be good to remove them locally.

<a id="first---fetch-and-prune"></a>

## First - fetch and prune

```sh
git fetch -p
```

`git fetch --prune` will connect to the remote and fetch the latest remote state before pruning. It is essentially a combination of commands:

```sh
git fetch --all && git remote prune
```

> NOTE: The generic `git prune` command is entirely different. it will delete locally detached commits.

Read more about it: [Git Cleanup: "git Remote Prune" Explained | by Maroun Maroun | Better Programming](https://betterprogramming.pub/git-cleanup-git-remote-prune-explained-679fadc53ba7)

<a id="how-do-i-clean-outdated-branches"></a>

### How Do I Clean Outdated Branches?

`git fetch --prune` is the best utility for cleaning outdated branches. It will connect to a shared remote repository remote and fetch all remote branch refs. It will then delete remote refs that are no longer in use on the remote repository.

<a id="does-git-remote-prune-origin-delete-the-local-branch"></a>

### Does Git Remote Prune Origin Delete the Local Branch?

No `git remote prune origin` will only delete the refs to remote branches that no longer exist. Git stores both local and remote refs. A repository will have `local/origin` and `remote/origin` ref collections. `git remote prune origin` will only prune the refs in `remote/origin`. This safely leaves local work in `local/origin.`
To remove local branches you need to use `git branch -d` or replace `-d` with `-D`.

**Credits:** Prune explanation comes from an excellent article on [Git Prune](https://www.atlassian.com/git/tutorials/git-prune)

If you want to have prune executed with every fetch operation, you can configure Git accordingly:

```sh
git config --global fetch.prune true
```

<a id="second---delete-merged-local-branches"></a>

## Second - delete merged local branches

```sh
git branch --merged origin/develop | grep -v develop | xargs git branch -d
```

`--merged origin/develop` - branches merged into remote develop
`grep -v develop` - for safety reasons: exclude develop from the list of branches to delete

Read more here:
<https://stackoverflow.com/questions/16590160/remove-branches-not-on-remote>

up:: [[MOC_Git]]]
