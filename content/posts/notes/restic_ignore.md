---
Title: gitignore-style exclusion for restic
Slug: gitignore-style-exclusion-for-restic
Date: 2023-07-27
Modified: 2023-07-27
Status: published
Tags: restic, ignore, gitignore 
Category: note
---
X::[[my_system_for_backups]]
X::[[2023-01-25-how_to_verify_that_each_automated_backup_is_done_correctly]]

Restic is a popular backup tool that supports the use of `.gitignore`-style exclusion patterns to ignore certain files and directories during the backup process. This feature is useful when you want to exclude specific files or directories from being backed up, such as temporary files, caches, or build artifacts.

To use `ignore` with Restic, you can create a file called `.resticignore` in the root of your repository (where you run Restic). This file should contain the patterns for the files and directories you want to ignore, just like you would do with a `.gitignore` file.

Here's how you can use `ignore` in Restic:

1. Create a `.resticignore` file:
   Inside your project's root directory (or the directory you're backing up), create a file named `.resticignore`. You can use any text editor to create this file.

2. Add patterns to ignore:
   In the `.resticignore` file, list the files and directories you want to ignore during the backup. Each pattern should be on a separate line. You can use the same syntax as you would in a `.gitignore` file.

   For example, a simple `.resticignore` file might look like this:
   ```
   *.log
   temp/
   cache/
   build/
   ```

   The above example would ignore all files with the `.log` extension and the `temp`, `cache`, and `build` directories.

3. Run Restic backup with `--ignore-file` option:
   When running Restic to perform the backup, specify the `.resticignore` file using the `--ignore-file` option. This tells Restic to use the patterns in that file to exclude certain files and directories.

   Here's an example command:
   ```
   restic backup /path/to/your/data --ignore-file /path/to/.resticignore
   ```

   Replace `/path/to/your/data` with the actual path of the data you want to back up and `/path/to/.resticignore` with the path to your `.resticignore` file.

By using the `.resticignore` file, you can customize what gets backed up and what gets excluded. This can be particularly useful to avoid backing up large or unnecessary files, reducing storage space and backup time.