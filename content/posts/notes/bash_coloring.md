---
Category: note
Date: '2022-05-12'
Modified: '2023-07-12'
Slug: bash-coloring
Status: published
Tags: bash, coloring, cli, tui
Title: Bash - Coloring Output
---

# Bash coloring

```sh
# Text color variables
txtund=$(tput sgr 0 1)          # Underline
txtbld=$(tput bold)             # Bold
bldred=${txtbld}$(tput setaf 1) #  red
bldblu=${txtbld}$(tput setaf 4) #  blue
bldwht=${txtbld}$(tput setaf 7) #  7-gray, 15-white
bldorg=${txtbld}$(tput setaf 3) #  orange
txtrst=$(tput sgr0)             # Reset
info=${bldwht}*${txtrst}        # Feedback
pass=${bldblu}*${txtrst}
warn=${bldred}*${txtrst}
ques=${bldblu}?${txtrst}


st_clean="$bldwht\[clean \]$txtrst"
st_dirty="$bldred\[dirty \]$txtrst"
st_n_git="$bldorg\[not repo\]$txtrst"
```

*precise source unknown, found on Internet some time ago.*

up::[[MOC_Shell_Bash_Zsh]]
