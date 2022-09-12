---
title: List unlinked (orphaned) notes in Obsidian
date: 2022-08-17
modified: 2022-08-17
status: published
tags: obsidian, dataview, orphaned-notes
slug: list-unlinked-orphaned-notes-obsidian
category: note
citation_needed: false
---

Here is how you can create dynamic list of unlinked notes (files) using dataview
<pre>
```dataview
LIST FROM ""
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
```
</pre>

Credits to [riddyrayes](https://forum.obsidian.md/u/riddyrayes/summary) for the solution posted on obsidian forum [Find orphan notes - Feature archive - Obsidian Forum](https://forum.obsidian.md/t/find-orphan-notes/817/15)
