---
Category: note
Date: '2023-02-14'
Modified: '2023-07-12'
Slug: jupyter-duplicated-nbextensions-locations
Status: published
Tags: jupyter, jupyter-notebook, data-analysis, scientific-computing, nbextensions, customization, duplicates, diagnose, paths, per-user-directory, per-environment-directory, system-wide-directories, Anaconda, conda-package, jupyter_contrib_nbextensions
Title: Jupyte Notebook Duplicated Locations for Nbextensions
---

Jupyter notebooks are a great tool for data analysis and scientific computing, but they can also be customized and extended through the use of nbextensions. Nbextensions are additional pieces of code that can add new functionality, enhance existing features, and provide more customization options to Jupyter notebooks.

However, sometimes nbextensions can be duplicated or installed in multiple places, leading to conflicts and errors. In this article, we'll discuss how to manage and prevent duplicated nbextensions files, diagnose the current state of your nbextensions, and troubleshoot any issues that may arise.

Firstly, it's important to understand that nbextensions can be installed in multiple places on your system. When you run the command `jupyter --paths`, it will display all the directories where Jupyter notebooks can find nbextensions. These include the per-user directory (`~/.local/share/jupyter`), the per-environment (or per-python) directory (`/path/to/env/share/jupyter`), and one or more system-wide directories (`/usr/local/share/jupyter`, `/usr/share/jupyter`).

To control the Jupyter paths, you can use the `--user`, `--sys-prefix`, or `--system` flags when installing nbextensions. The `--user` flag installs the nbextension in the per-user directory, the `--sys-prefix` flag installs it in the per-environment directory, and the `--system` flag installs it in the system-wide directory.

If you're unsure which path to use, it's generally recommended to use the per-environment directory, especially if you're using Anaconda. This will ensure that any conda package installations will go there and won't conflict with other nbextensions.

Now, let's say you've installed an nbextension and have noticed that it's duplicated in multiple places. To fix this, you'll need to remove one of the installations. If you used the `jupyter_contrib_nbextensions` package to install the nbextension, you can run the command `jupyter contrib nbextensions uninstall --user` to remove the per-user installation, or `jupyter contrib nbextensions uninstall --sys-prefix` to remove the per-environment installation.

If you didn't use the `jupyter_contrib_nbextensions` package, you can uninstall each duplicated nbextension individually using the command `jupyter nbextension uninstall --user path/url path/url/entrypoint`. For example, to uninstall the `autosavetime` nbextension, you would run `jupyter nbextension uninstall --user autosavetime autosavetime/main`.

To diagnose the current state of your nbextensions, you can run the command `jupyter nbextension list`. This will display a list of all installed nbextensions and their paths. If you notice any duplicates, you can then proceed to remove one of the installations as described above.

In summary, managing and preventing duplicated nbextensions files in Jupyter notebooks is important to prevent conflicts and errors. By understanding how nbextensions are installed and using the appropriate flags, you can control where they're installed and avoid duplicates. And if you do encounter duplicates, you can use the `jupyter nbextension uninstall` command to remove them and ensure smooth operation of your Jupyter notebooks.

See also related GitHub issue: <https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/issues/25>

up::[[MOC_Jupyter_notebooks]]
