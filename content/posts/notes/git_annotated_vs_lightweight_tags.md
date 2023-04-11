---
Title: Git - annotated vs. lightweight tags
Slug: git-annotated-vs-lightweight-tags
Date: 2023-03-31
Modified: 2023-03-31
Status: published
Tags: git, tag
Category: note
prompt: Explain me, in git, what is the difference between annotated and lightweight tags. When to use each type? Give me long text.
---
In Git, tags are used to mark specific points in the history of a repository. They serve as a reference point for developers to easily identify and navigate to important milestones, such as releases or significant commits. There are two types of tags in Git: annotated tags and lightweight tags.

## Annotated tags
Annotated tags are more informative than lightweight tags. When creating an annotated tag, Git stores a full object in the repository that contains the tagger name, email, and date, a tagging message, and a SHA-1 checksum of the commit being tagged. Annotated tags are essentially Git objects that are separate from the commit objects they reference, whereas lightweight tags are simply pointers to specific commits.

The additional information stored in an annotated tag makes them useful for documenting significant events in the project's history. The tagging message can provide context about why the tag was created and what it represents. Additionally, annotated tags can be signed and verified to ensure their authenticity. Signed tags provide assurance that the tag was created by an authorized person and that the commit being tagged has not been tampered with.

**Example:**
```sh
git tag -a v1.2 -m "my version 1.4"
```

## Lightweight tags
Lightweight tags, on the other hand, are simply references to specific commits. They do not store any additional information beyond the tag name and the commit ID. Lightweight tags are useful for marking temporary or internal points in the repository history, such as to label a specific commit for testing or debugging purposes. Lightweight tags are created with the `git tag` command without the `-a` or `-m` options.

**Example:**
```sh
git tag v1.2
```

## When to use Annotated and when Lightweight tags?
So when should you use annotated tags versus lightweight tags? Annotated tags are ideal for marking significant events in the project's history, such as releases, milestones, or important changes. They are also useful for documenting the context and reasoning behind a particular tag. Lightweight tags, on the other hand, are useful for temporary or internal purposes, such as marking specific commits for debugging or testing purposes.

> In general, it is a good practice to **use annotated** tags for any **official releases** or **milestones**, as they provide a clear and detailed record of the project's progress. **Lightweight** tags can be used for more informal purposes, such as to **mark experimental** or **intermediate points** in the project's history.

up::[[MOC_Git]]
X::[[git_tags]]