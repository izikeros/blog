---
title: What is inside kaggle-python docker image?
date: '2018-03-26T15:01:34+01:0'
tags: kaggle, docker
Category: Posts
image: /images/img1.jpg
Summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Status: draft
---

How the kaggle image has grown?

* plot number of packages time evolution (static plot)
* show time evolution (gource or other animation) (spacecowb0y/gource_to_git.sh)

What is inside kaggle-python docker image?

    * classification (categories)
        - extract pip installs and add oneliner comment with description
        - do the same with github packages (second approximation)

    * size of packages (brutto: package + dependencies, netto: package)


    * propose to remove large and less-starred packages (remove_score=size/stars)