---
Title: Don't Just Create Backups, Verify Them: How Restic Can Help?
Slug: verify-backups-restic-example
Date: 2023-01-15
Modified: 2023-01-25
Start: 2023-01-25
Tags: linux, backup, good-practices, restic
Category: Howto
Image: /images/head/verify_backups.jpg
banner: /images/head/verify_backups.jpg
Summary: Learn how to verify your backups with Restic, ensure completeness, integrity, and recoverability. Automate the process for peace of mind. Read now
Status: published
prompt:Give me long article on How to verify that each backup is done correctly. You can use restic as an exemplary tool of choice to make backups.
todo: add diagram
---

## Introduction
Creating regular backups of your data is an important step in protecting against data loss due to hardware failure, human error, or malicious attacks. However, it is not enough to simply create backups - it is also crucial to ensure that the backups are done correctly and can be successfully restored in the event of a disaster. In this article, we will discuss how to verify that backups created with the open-source backup tool Restic are done correctly.

## general principles of backup verification
Before diving into the specifics of Restic, it's important to understand the general principles of backup verification. When verifying backups, you should ensure that the following three elements are present:

1.  **Completeness**: The backup should contain all of the files and data that you expect it to contain.
2.  **Integrity**: The backup should be free from errors, such as corrupted files or missing data.
3.  **Recoverability**: The backup should be able to be restored to a usable state in the event of a disaster.

## How to verify backups created with Restic?
With these principles in mind, let's take a look at how to verify backups created with Restic.

### 1.  Verify completeness of backups
To ensure that your backups contain all of the files and data that you expect, you can use the Restic command `restic check`. This command will check the integrity of the data stored in the backup, as well as verify that all files are present and have the correct permissions. If there are any issues with the backup, Restic will print a message indicating the problem and the file that is affected.
    
### Verify integrity of backups
Another important aspect of backup verification is ensuring that the backup is free from errors, such as corrupted files or missing data. Restic provides the command `restic check --read-data` to verify the integrity of data stored in the backup. This command will read all files in the backup and compare their checksums to the original files. If the checksums do not match, this indicates that the file is corrupted or has been modified.
    
### 3.  Verify recoverability of backups
The most important aspect of backup verification is the ability to restore the data in the event of a disaster. To test the recoverability of a Restic backup, you can use the command `restic restore`. This command will allow you to specify a specific snapshot or set of files to restore. You can also specify a directory where the files should be restored. Once the restore is complete, you should carefully review the restored files to ensure that they are complete, accurate, and usable.
    
### 4.  Automate the process
It can be time-consuming to manually check backups for completeness, integrity and recoverability. To automate this process, you can schedule Restic's commands `restic check`, `restic check --read-data` and `restic restore` to run at specific intervals using a cron job or a task scheduler.
    

## Conclusion
Backup verification is an essential step in protecting your data. By using the open-source tool Restic and following the steps outlined in this article, you can ensure that your backups are done correctly and can be successfully restored in the event of a disaster. Remember to schedule the verification process to run at specific intervals and to regularly review the backups to ensure that they are complete, accurate, and usable.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*

**Credits:**

Heading image from [Unsplash](https://unsplash.com/photos/GNyjCePVRs8) by [benjamin lehman](https://unsplash.com/@benjaminlehman)