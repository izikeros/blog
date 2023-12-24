---
Category: note
Date: '2022-08-17'
Modified: '2023-07-12'
Slug: list-unlinked-orphaned-notes-obsidian
Status: published
Tags: obsidian, obsidian/dataview, orphaned-notes
Title: List Unlinked (Orphaned) Notes in Obsidian
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

up::[[obsidian]]
