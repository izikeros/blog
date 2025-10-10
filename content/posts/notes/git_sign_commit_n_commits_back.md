---
Category: note
Date: 2023-02-28
Modified: 2023-07-12
Slug: git-sign-commit-n-commits-back
Status: published
Tags:
  - git
  - commit
Title: Git - Sign Commit That Is N Commits Back (Earlier)
---

## Example

To sign two specific commits that are respectively 4 and 5 commits back in Git, you can use the `git rebase` command with the `--exec` option to sign the commits as they are being rebased. Here are the steps:

1. Get the hash of the first (older) commit you want to sign by running `git log`.

2. Run `git rebase -i HEAD~5`.

3. This will open up a text editor with a list of the last 5 commits. Replace the word "pick" with "edit" for the first commit (5) you want to sign.

4. Save and close the file.

5. Git will now start the rebase process and stop at the first commit you want to sign.

6. Run `git commit --amend --no-edit -S`.

7. Enter your GPG key passphrase when prompted.

8. Run `git rebase --continue`.

9. Git will now continue the rebase process and stop at the second commit you want to sign.

10. Repeat steps 1-7 for the second commit.

11. Run `git rebase --continue`.

12. Git will now continue the rebase process and apply the signed commits.

13. Finally, you can run `git log` to confirm that the commits have been signed.

Note that rebasing can be a destructive operation, so it's important to make sure you have a backup of your repository before you start. Also, if the commits you want to sign have already been pushed to a remote repository, you'll need to force push the changes after rebasing, which can potentially cause problems for other users who have already pulled the changes. So, it's important to communicate with your team before using this approach.

X::[[git_sign_previous_commit]]
X::[[git_signing_commits]]
up::[[MOC_Git]]
