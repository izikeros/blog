---
Category: note
Date: '2022-05-12'
Modified: '2023-07-12'
Slug: chocolatey
Status: published
Tags: chocolatey, windows, packages, winget
Title: Chocolatey (Windows)
---

> **NOTE:** 
> there is already an official tool from Microsoft for downloading and upgrading software as packages: [[winget]]

## install
### Step 1 — Opening and Configuring PowerShell
Open Powershell as admin
```sh
cd ~
echo "type: RemoteSigned"
Set-ExecutionPolicy -Scope CurrentUser
```

type:
```sh
RemoteSigned
```
confirm with `Y`

Confirmation
```sh
$ Get-ExecutionPolicy -List
```
should give:
 ```
        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser    RemoteSigned
 LocalMachine       Undefined
```

### Step 2 — Installing the Package Manager Chocolatey
```sh
$script = New-Object Net.WebClient
$script.DownloadString("https://chocolatey.org/install.ps1")
iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
```

```sh
choco feature enable -n allowGlobalConfirmation
```

## List packages installed WITH CHOCO locally
```sh
choco list -l
```
or use shortcut `clist`

## List ALL software installed by choco or classical installer:
```sh
clist -li
```

## Upgrade (all) packages
```sh
choco upgrade all
```

## Install chocolatey gui:
```
choco install chocolateygui
```

# Packages
## manually:
dropbox
paint.net

## my packets
```sh
$ choco install Firefox GoogleChrome doublecmd fsviewer git greenshot SublimeText3 winscp sumatrapdf kitty ccleaner procmon conemu f.lux transmission 
choco install pycharm-community virtualbox vlc sandboxie winamp vscode meld partitionwizard ffmepg cmder defraggler
```

## other things to install
searchmyfiles, Album art downloader XUI, windirstat
