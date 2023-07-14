---
Title: Understanding the Differences Between Git Push Force and Git Push Force-With-Lease
Slug: understanding-the-differences-between-git-push-force-and-git-push-force-with-lease
Date: 2022-11-22
Modified: 2023-07-14
Status: published
Tags: git, git-push, git-push-force, git-push-force-with-lease, version-control, collaboration, commit-history, rebasing, squashing, git-commands
Category: note
Summary: Discover the differences between Git Push Force and Git Push Force-With-Lease, their common use cases, and lesser-known features to help you manage your codebase effectively and safely.
---
up::[[MOC_Git]]

In the world of version control, Git is a powerful and widely-used tool for managing and tracking changes in your codebase. It allows multiple developers to work on the same project simultaneously, without conflicts. But when it comes to pushing changes to a remote repository, you might encounter some challenges. In this article, we will explore two Git commands that can help you overcome these challenges: `git push --force` and `git push --force-with-lease`. We will discuss their differences, common use cases, and lesser-known but super useful aspects of each.

<!-- MarkdownTOC levels="2,3,4" autolink="true" autoanchor="true" -->

- [Git Push Force](#git-push-force)
	- [Use Cases](#use-cases)
		- [Undoing a mistaken push](#undoing-a-mistaken-push)
		- [Cleaning up messy commit history](#cleaning-up-messy-commit-history)
		- [Updating a feature branch](#updating-a-feature-branch)
- [Git Push Force-With-Lease](#git-push-force-with-lease)
	- [Use Cases](#use-cases-1)
		- [Collaborative work](#collaborative-work)
		- [Rebasing or squashing commits](#rebasing-or-squashing-commits)
		- [Updating a feature branch](#updating-a-feature-branch-1)
	- [Lesser-Known Useful Features](#lesser-known-useful-features)
		- [Lease reference](#lease-reference)
		- [Dry run](#dry-run)
- [Comparing Git Push Force and Git Push Force-With-Lease](#comparing-git-push-force-and-git-push-force-with-lease)
- [Related reading](#related-reading)

<!-- /MarkdownTOC -->

<a id="git-push-force"></a>
## Git Push Force

[`git push --force`](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force) is a command that allows you to overwrite the remote branch with your local branch, regardless of any conflicts or discrepancies between the two branches. This is a powerful command that should be used with caution, as it can result in lost commits and overwritten work.

<a id="use-cases"></a>
### Use Cases

<a id="undoing-a-mistaken-push"></a>
#### Undoing a mistaken push
If you accidentally pushed a commit with incorrect changes or to the wrong branch, you can use `git push --force` to overwrite the remote branch with the correct local branch.

<a id="cleaning-up-messy-commit-history"></a>
#### Cleaning up messy commit history
If you want to clean up a cluttered commit history by squashing or rewriting commits, you can use `git push --force` to push the updated history to the remote branch.

<a id="updating-a-feature-branch"></a>
#### Updating a feature branch
If you have a feature branch that has diverged significantly from the main branch, and you want to update it with the latest changes from the main branch, you can use `git push --force` to push the updated feature branch to the remote repository.

<a id="git-push-force-with-lease"></a>
## Git Push Force-With-Lease

[`git push --force-with-lease`](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-force-with-lease) is a safer alternative to `git push --force`. It allows you to push changes to the remote branch only if the remote branch is at the same commit as the one you have locally. If the remote branch has been updated by someone else, the push will be rejected, preventing accidental overwrites.
<a id="use-cases-1"></a>
### Use Cases

<a id="collaborative-work"></a>
#### Collaborative work
When working with a team, using `git push --force-with-lease` helps ensure that you do not accidentally overwrite someone else's work.

<a id="rebasing-or-squashing-commits"></a>
#### Rebasing or squashing commits
If you need to rebase or squash commits, using `git push --force-with-lease` is a safer option, as it ensures that you are not overwriting any new commits.

<a id="updating-a-feature-branch-1"></a>
#### Updating a feature branch
Similar to `git push --force`, you can use `git push --force-with-lease` to update a feature branch with the latest changes from the main branch. However, it is a safer option, as it ensures that you are not overwriting any new commits on the remote branch.

<a id="lesser-known-useful-features"></a>
### Lesser-Known Useful Features

<a id="lease-reference"></a>
#### Lease reference
`git push --force-with-lease` accepts an optional argument, the lease reference, which allows you to specify the expected commit of the remote branch. This adds an extra layer of safety by ensuring that the remote branch is at the exact commit you expect before pushing.

```bash
git push --force-with-lease=origin/main:<expected-commit>
```

<a id="dry-run"></a>
#### Dry run
By adding the `--dry-run` option, you can check if the push would succeed without actually pushing the changes. This can help you avoid potential conflicts and overwrites.

```bash
git push --force-with-lease --dry-run
```

<a id="comparing-git-push-force-and-git-push-force-with-lease"></a>
## Comparing Git Push Force and Git Push Force-With-Lease

| Command | Overwrites Remote Branch | Safety | Use Cases |
|---------|--------------------------|--------|-----------|
| `git push --force` | Yes | Low | Undoing a mistaken push, cleaning up messy commit history, updating a feature branch |
| `git push --force-with-lease` | No, only if the remote branch is at the same commit as the local branch | High | Collaborative work, rebasing or squashing commits, updating a feature branch with additional safety |


<a id="related-reading"></a>
## Related reading
Proper way to do git push force: [The Dark Side of the Force Push - Will Anderson](https://willi.am/blog/2014/08/12/the-dark-side-of-the-force-push/)