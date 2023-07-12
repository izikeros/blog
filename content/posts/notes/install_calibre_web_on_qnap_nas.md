---
Category: note
Date: '2022-10-12'
Modified: '2023-07-12'
Slug: install-calibre-web-qnap-nas-tutorial
Status: published
Tags: calibre, calibre-web, docker
Title: Tutorial - Install Calibre Web on QNAP NAS
citation_needed: false
---
Calibre-Web is a web app providing a clean interface for browsing, reading, and downloading eBooks using a [Calibre](https://calibre-ebook.com/) database.

This tutorial shows how to install [calibre-web](https://github.com/janeczku/calibre-web) on QNAP-NAS. 

![main screen of calibre-web](https://github.com/janeczku/calibre-web/wiki/images/main_screen.png)

The installation described here was done on TS-251+ (Celeron J1900 4 Cores) but should be applicable to a wide variety of other QNAP NAS models.

> **Caution**: This is a simple setup assuming that service will be used only within the LAN by the trusted users and therefore access management, other networking, and security matters are not in the scope of this tutorial.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Software](#software)
- [Installation](#installation)
  - [Install service from Docker Container via Container Station](#install-service-from-docker-container-via-container-station)
  - [Configuration](#configuration)
    - [Environment](#environment)
    - [Shared Folders](#shared-folders)
    - [Network](#network)
    - [Device](#device)
  - [Create Container](#create-container)
  - [container initialization](#container-initialization)
  - [Caliber-web initial setup](#caliber-web-initial-setup)
- [Post installation](#post-installation)
  - [Change admin password](#change-admin-password)
  - [Library change](#library-change)
- [Alternatives](#alternatives)
- [Credits](#credits)

<!-- /MarkdownTOC -->

<a id="software"></a>
## Software
We will be using [dockerized version](https://hub.docker.com/r/linuxserver/calibre-web/) of [janeczku/calibre-web](https://github.com/janeczku/calibre-web) 

<a id="installation"></a>
## Installation
<a id="install-service-from-docker-container-via-container-station"></a>
### Install service from Docker Container via Container Station
- Search for the `calibre-web` docker image in the `Create` tab of the Container Station.
- The popup window for version selection should be displayed. Select `latest` unless you have good reason to use an older version. Click `Install`.
- You need to confirm your intent to install calibre-web on another popup window.

<a id="configuration"></a>
### Configuration
Before the service will be started you need to configure it properly to provide information about where your Calibre book library (or multiple libraries) is located, configure the IP where the service will be available, etc.

We are using the docker image from linuxserver, the configuration proposed in this tutorial is based on suggestions from [linuxserver/calibre-web](https://hub.docker.com/r/linuxserver/calibre-web/) on how to run the service using the docker command-line.

```bash
docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e DOCKER_MODS=linuxserver/mods:universal-calibre `#optional` \
  -e OAUTHLIB_RELAX_TOKEN_SCOPE=1 `#optional` \
  -p 8083:8083 \
  -v /path/to/data:/config \
  -v /path/to/calibre/library:/books \
  --restart unless-stopped \
  lscr.io/linuxserver/calibre-web:latest
```

The configuration is divided into sections. We will touch: `Environment`, `Shared folders` and `Network`

<a id="environment"></a>
#### Environment
Set the time zone that suits you the most.
![environment section of calibre-web container configuration](/images/calibre_web_qnap/calibreweb_environment.jpg)

my settings for env
```
PUID=1000
PGID=1000
TZ=Europe/London
DOCKER_MODS=linuxserver/calibre-web:calibre
```
<a id="shared-folders"></a>
#### Shared Folders
![shared section of calibre-web container configuration](/images/calibre_web_qnap/calibreweb_shared_folders.jpg)
I suggest to create directory `calibre` in `/share/Container` - it will be placeholder for configuration and libraries.

- create folder `/share/Container/calibre/config` - for configuration
- create folder `/share/Container/calibre/books` - as a folder that will contain one or more calibre libraries. If you have your Calibre library already on the NAS but in the different location you can use symbolic links pointing at your calibre libraries. Example of two libraries:
	- `/share/Container/calibre/books/fiction`
	- `/share/Container/calibre/books/cooking`

Inside of these folders you should see directories corresponding to author names and `metadata.db` file.

> **CAUTION:** QNAP's container station cannot change the shared folder settings using the Web GUI after the container is created.

I've created shared folder mappings:
```
/Container/calibre -> /calibre
/Container/calibre/config -> /config 
/Container/calibre/books/books_it -> /books_it
/Container/calibre/books/books_life -> /books_life
/Container/calibre/books/books_ml -> /books_ml
```

<a id="network"></a>
#### Network
Set the calibre-web container IP address to e.g. 192.168.1.230.

<a id="device"></a>
#### Device
no need to modify anything

<a id="create-container"></a>
### Create Container
When the customizations in configuration are done, press the "Create" button and the summary of settings will be displayed.
![summary - part 1 - of calibre-web container configuration](/images/calibre_web_qnap/calibreweb_summary_1.jpg)

![summary - part 2 - of calibre-web container configuration](/images/calibre_web_qnap/calibreweb_summary_1.jpg)

When creation starts, you will be redirected  to the creation screen of Container Station. While creating, you need to wait until the number (1 in the example below) near the top right of the Container Station window (right next to the IoT icon) disappears.
![status of calibre-web container configuration](/images/calibre_web_qnap/calibre_web_status.jpg)

<a id="container-initialization"></a>
### container initialization

In the example above, we have set auto-start in the creation panel, so when the container is created, it will start running. Initialization happens when the container is first run.

On the "Overview" tab of the container station, click the corresponding container name to display the status

Caliber-web is not yet accessible during initialization, so we have to wait.

If the following message is displayed, it seems that initialization is completed and access from the Web is possible.

```
INFO in web : Starting Calibre Web ...
INFO in server : Starting Gevent server
```
![calibre-web container initialization](/images/calibre_web_qnap/calibreweb_starting_container_console.jpg)
<a id="caliber-web-initial-setup"></a>
### Caliber-web initial setup

Once Caliber-web is available, access the container's server from a web browser.

In this example the IP address of the container is 192.168.1.230. The port number used by calibre-web has not changed, so it is 8083. In other words, access http://192.168.1.230:8083/.

When accessing for the first time, basic settings are required.

- Set e.g.  `/books_life` as the location of library database.

The setting is applied by pressing the "Save" button. Then, log-in using the "Login" button.

By default, as described in https://hub.docker.com/r/linuxserver/calibre-web/, log-in with username `admin` and password `admin123`.

If you can log in, you should be able to see the library you set during initialization.

<a id="post-installation"></a>
## Post installation

<a id="change-admin-password"></a>
### Change admin password

To change the admin user's password after logging in, click the lowercase username `admin` with the person icon in the upper right corner of the window to switch to the change profile screen. 

<a id="library-change"></a>
### Library change

- To change the library after logging in, select the circular icon "Admin" in the upper right (to the left of the upper-body icon, where admin in lowercase is your username).
- To change the library, select `Configuration -> Basic Configuration`.
- Here, change the library to e.g. `/books_it`.
- Press the "Submit" button to confirm your changes.
- Click the calibre-web icon on the upper left to display the library, and the changed library should be displayed.

<a id="alternatives"></a>
## Alternatives
- you can install calibre-web using docker-compose instead of using container station. This is not covered by this tutorial, see docker-compose file on [Docker Hub](https://hub.docker.com/r/linuxserver/calibre-web/)
- you can use other front-ends for accessing calibre via web. Examples are e.g.: 
	- [ seblucas/cops](https://github.com/seblucas/cops) -  Calibre OPDS (and HTML) PHP Server : web-based light alternative to "Calibre content server"/"Calibre2OPDS" to serve ebooks (epub, mobi, pdf, ...)


<a id="credits"></a>
## Credits
Article [Run Calibre-web on QNAP NAS](https://kunsen.net/2019/10/26/post-2468/) (in Japanese) helped me with my first setup of calibre web. This tutorial is heavily based on that article.

X::[[nas_qnap_photoprism]]