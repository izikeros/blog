---
Category: note
Date: '2023-02-28'
Modified: '2023-07-12'
Slug: git-sign-previous-commit
Status: published
Tags: git, commit, commit-signing, gpg-key, ssh-key, gpg
Title: Git - Sign Previous Commit
---

To sign a previous commit in Git, you can use the `git commit --amend --no-edit -S` command. This command will sign the previous commit using your GPG key.

Here are the steps to sign a previous commit:

1. Get the hash of the commit you want to sign by running `git log`.
2. Run `git commit --amend --no-edit -S <commit hash>`.
3. This will open up your default text editor with the commit message for the specified commit. You can review and save the commit message.
4. After saving the commit message, Git will prompt you to enter your GPG key passphrase.
5. Once you enter your passphrase, Git will sign the commit using your GPG key.
6. Finally, you can run `git log` to confirm that the commit has been signed.

> **NOTE:** If you haven't set up a GPG key yet, you'll need to generate one and add it to your Git configuration before you can sign commits. You can find more information on how to do this in the Git documentation or in [[git_signing_commits]]

up::[[MOC_Git]]
X::[[git_sign_commit_n_commits_back]]
X::[[git_signing_commits]]
