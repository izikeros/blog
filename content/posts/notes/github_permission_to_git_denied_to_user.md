---
Category: note
Date: 2024-03-21
Modified: 2024-03-21
Slug: github-permission-to-repogit-denied-to-user
Status: published
Summary: Learn how to resolve 'Permission to repo.git denied' errors by managing SSH keys in Git for users dealing with multiple GitHub accounts. Discover the causes and solutions involving ssh-agent commands like `ssh-add -D` and key-specific removals.
ai_summary: true
Title: GitHub - Troubleshooting 'Permission to repo.git denied to user'
tags:
  - git
  - github
  - ssh
  - ssh-key
---
X::[[MOC_Git]]

When working with GitHub, you might encounter an issue that restricts you from executing a 'git push' operation due to permissions. This post will guide you through solving this problem and help you understand its causes.

Let's look at the issue in focus. You are trying to push to your repository:

```sh
git push origin main
```

However, the terminal returns an error that resembles:

```
ERROR: Permission to USER/REPO.git denied to USER.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

This issue often arises when you are operating two GitHub accounts interchangeably on the same machine and are using SSH keys for authorization.

One straightforward workaround, although not the most efficient, is to simply log out from the conflicting GitHub account, reboot the machine, and then attempt to push again. However, this method is a quick-fix and might not solve the underlying issue.

The root of this problem often lies within SSH authentication, particularly involving the 'ssh-agent'. The ssh-agent is a program that holds private keys used for public key authentication (RSA, DSA, ECDSA, Ed25519).

The solution is to clear all identities (SSH keys) stored by the ssh-agent:

```sh
ssh-add -D
```

The command `ssh-add -D` deletes all identities from the agent.

However, if you want to be more precise and remove specific keys, you can specify the file path of the key:

```sh
ssh-add -d ~/.ssh/id_rsa
ssh-add -d ~/.ssh/github
```

The above commands remove the id_rsa and github keys, respectively.

After cleaning up the stored keys, you can add the required SSH key back to the ssh-agent. This key should correspond to the GitHub account you intend to push to:

```sh
ssh-add ~/.ssh/github
```

By performing these steps, you can effectively manage your SSH keys and prevent conflicts when working with multiple GitHub accounts on the same machine.
