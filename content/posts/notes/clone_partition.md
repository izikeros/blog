---
Category: note
Date: '2022-03-03'
Modified: '2023-07-12'
Slug: clone-partition-in-linux
Status: published
Summary: how to clone disk partition in Linux
Tags: Linux, dd, pv, partition, disk
Title: Clone Partition in Linux
citation_needed: false
---

## clone partition

```sh
dd if=infile | pv > outfile
```

## create a disk image

(from arch wiki: <https://wiki.archlinux.org/index.php/Dd#Disk_cloning_and_restore>)

```sh
dd if=/dev/sda conv=sync,noerror bs=64K | gzip -c  > /path/to/backup.img.gz
```

Finally, save extra information about the drive geometry necessary in order to interpret the partition table stored within the image. The most important of which is the cylinder size.

```sh
fdisk -l /dev/sda > /path/to/list_fdisk.info
```

## Restore system

To restore your system:

```sh
gunzip -c /path/to/backup.img.gz | dd of=/dev/sda
```

up::[[MOC_Linux]]
