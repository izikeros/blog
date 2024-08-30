---
Category: note
Date: '2022-08-08'
Modified: '2024-08-26'
Slug: install-photoprism-on-qnap-nas-using-docker-compose
Status: published
Summary: Instruction on how to install Photoprism on QNAP NAS using Docker Compose
Tags: nas, photoprism, Linux, photo-gallery, docker, docker-compose, qnap
Title: Install Photoprism on QNAP NAS Using Docker Compose
---
X:[[piwigo_photo_gallery]]

Photoprism is a modern, searchable, well organized web gallery of your photos and videos. At the moment of writing, the official documentation, does not contain a dedicated instructions on  how to install Photoprism on QNAP NAS. This article is meant to fill that gap.
Installation described here was done on TS-251+ (Celeron J1900 4 Cores) but should be applicable to wide variety of other QNAP NAS models. There is also possibility to install photoprism using Container Station GUI and modified docker-compose file (see lower in the article).

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [What is the photoprism](#what-is-the-photoprism)
  - [Feature Overview](#feature-overview)
- [Installation on QNAP NAS from the CLI](#installation-on-qnap-nas-from-the-cli)
  - [Prerequisites](#prerequisites)
  - [login to your NAS server via SSH](#login-to-your-nas-server-via-ssh)
  - [Create photoprism directory](#create-photoprism-directory)
  - [Create `docker-compose.yml` file](#create-docker-composeyml-file)
  - [Create directories in `/share/Container/photoprism`](#create-directories-in-sharecontainerphotoprism)
  - [Run application in the container](#run-application-in-the-container)
    - [Using web-UI](#using-web-ui)
    - [Using CLI](#using-cli)
  - [Manual upgrading Photoprism to the latests version](#manual-upgrading-photoprism-to-the-latests-version)
  - [Adding new content](#adding-new-content)
  - [Performance tuning](#performance-tuning)
- [Installation using Container Station GUI](#installation-using-container-station-gui)
- [References](#references)
- [Updates](#updates)

<!-- /MarkdownTOC -->


<a id="what-is-the-photoprism"></a>
## What is the photoprism

from the photoprism website:

>PhotoPrism® is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way. You can run it at home, on a private server, or in the cloud.

![Screenshot](https://docs.photoprism.app/img/preview.jpg)


<a id="feature-overview"></a>
### Feature Overview
>
>- Browse [all your photos](https://docs.photoprism.app/user-guide/organize/browse/) and [videos](https://try.photoprism.app/videos) without worrying about [RAW conversion, duplicates or video formats](https://docs.photoprism.app/user-guide/settings/library/)
>- Easily find specific pictures using [powerful search filters](https://try.photoprism.app/browse?view=cards&q=flower%20color%3Ared)
>- Recognizes [the faces of your family and friends](https://try.photoprism.app/people)
>- [Automatic classification](https://try.photoprism.app/labels) of pictures based on their content and location
>- [Play Live Photos](https://try.photoprism.app/browse?view=cards&q=type%3Alive) by hovering over them in [albums](https://try.photoprism.app/albums) and search results
>- Since the [User Interface](https://try.photoprism.app/) is a  [Progressive Web App](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps), it provides a native app-like experience, and you can conveniently install it on the home screen of all major operating systems and mobile devices
>- Includes 4 high-resolution [World Maps](https://try.photoprism.app/places) to bring back the memories of your favorite trips
>- Metadata is extracted and merged from Exif, XMP, and other sources such as Google Photos
>- Many more image properties like [Colors](https://try.photoprism.app/browse?view=cards&q=color:red), [Chroma](https://try.photoprism.app/browse?view=cards&q=mono%3Atrue), and [Quality](https://try.photoprism.app/review) can be searched as well
>- Use  [PhotoSync](https://link.photoprism.app/photosync) to securely backup iOS and Android phones in the background
>- WebDAV clients such as Microsoft's Windows Explorer and Apple's Finder [can connect directly](https://docs.photoprism.app/user-guide/sync/webdav/) to PhotoPrism, allowing you to open, edit, and delete files from your computer as if they were local

> **NOTE:** I haven't found functionality to add other accounts than administrator. But in my case having only single user is perfectly fine.


<a id="installation-on-qnap-nas-from-the-cli"></a>
## Installation on QNAP NAS from the CLI


<a id="prerequisites"></a>
### Prerequisites

This instruction assumes that you are familiar with using command line interface (CLI).

- ensure you have installed Container Station which is providing Docker on QNAP NAS
- ensure that you have docker in the path


<a id="login-to-your-nas-server-via-ssh"></a>
### login to your NAS server via SSH

from the terminal or use e.g. `putty` if working on Windows


<a id="create-photoprism-directory"></a>
### Create photoprism directory

```sh
mkdir /share/Container/photoprism
cd photoprism
```


<a id="create-docker-composeyml-file"></a>
### Create `docker-compose.yml` file

download `docker-compose.yml` from the link provided in [official documentation](https://docs.photoprism.app/getting-started/docker-compose/) :

```sh
wget https://dl.photoprism.app/docker/docker-compose.yml
```

You can try to use this docker file (compatible with v3 format)
```yaml
version: '3.8'

services:
  photoprism:
    image: photoprism/photoprism:latest
    stop_grace_period: 10s
    # restart: unless-stopped
    depends_on:
      - mariadb
    security_opt:
      - seccomp:unconfined
      - apparmor:unconfined
    ports:
      - "2342:2342"
    environment:
      PHOTOPRISM_ADMIN_USER: "admin"
      PHOTOPRISM_ADMIN_PASSWORD: "insecure"
      PHOTOPRISM_AUTH_MODE: "password"
      PHOTOPRISM_SITE_URL: "http://localhost:2342/"
      PHOTOPRISM_DISABLE_TLS: "false"
      PHOTOPRISM_DEFAULT_TLS: "true"
      PHOTOPRISM_ORIGINALS_LIMIT: 5000
      PHOTOPRISM_HTTP_COMPRESSION: "gzip"
      PHOTOPRISM_LOG_LEVEL: "info"
      PHOTOPRISM_READONLY: "false"
      PHOTOPRISM_EXPERIMENTAL: "false"
      PHOTOPRISM_DISABLE_CHOWN: "false"
      PHOTOPRISM_DISABLE_WEBDAV: "false"
      PHOTOPRISM_DISABLE_SETTINGS: "false"
      PHOTOPRISM_DISABLE_TENSORFLOW: "false"
      PHOTOPRISM_DISABLE_FACES: "false"
      PHOTOPRISM_DISABLE_CLASSIFICATION: "false"
      PHOTOPRISM_DISABLE_VECTORS: "false"
      PHOTOPRISM_DISABLE_RAW: "false"
      PHOTOPRISM_RAW_PRESETS: "false"
      PHOTOPRISM_SIDECAR_YAML: "true"
      PHOTOPRISM_BACKUP_ALBUMS: "true"
      PHOTOPRISM_BACKUP_DATABASE: "true"
      PHOTOPRISM_BACKUP_SCHEDULE: "daily"
      PHOTOPRISM_INDEX_SCHEDULE: ""
      PHOTOPRISM_AUTO_INDEX: 300
      PHOTOPRISM_AUTO_IMPORT: -1
      PHOTOPRISM_DETECT_NSFW: "false"
      PHOTOPRISM_UPLOAD_NSFW: "true"
      PHOTOPRISM_DATABASE_DRIVER: "mysql"
      PHOTOPRISM_DATABASE_SERVER: "mariadb:3306"
      PHOTOPRISM_DATABASE_NAME: "photoprism"
      PHOTOPRISM_DATABASE_USER: "photoprism"
      PHOTOPRISM_DATABASE_PASSWORD: "insecure"
      PHOTOPRISM_SITE_CAPTION: "AI-Powered Photos App"
      PHOTOPRISM_SITE_DESCRIPTION: ""
      PHOTOPRISM_SITE_AUTHOR: ""
    working_dir: "/photoprism"
    volumes:
      - "~/Pictures:/photoprism/originals"
      - "./storage:/photoprism/storage"

  mariadb:
    image: mariadb:11
    restart: unless-stopped
    stop_grace_period: 5s
    security_opt:
      - seccomp:unconfined
      - apparmor:unconfined
    command:
      - --innodb-buffer-pool-size=512M
      - --transaction-isolation=READ-COMMITTED
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
      - --max-connections=512
      - --innodb-rollback-on-timeout=OFF
      - --innodb-lock-wait-timeout=120
    volumes:
      - "./database:/var/lib/mysql"
    environment:
      MARIADB_AUTO_UPGRADE: "1"
      MARIADB_INITDB_SKIP_TZINFO: "1"
      MARIADB_DATABASE: "photoprism"
      MARIADB_USER: "photoprism"
      MARIADB_PASSWORD: "insecure"
      MARIADB_ROOT_PASSWORD: "insecure"

  watchtower:
    image: containrrr/watchtower
    restart: unless-stopped
    profiles:
      - update
    environment:
      WATCHTOWER_CLEANUP: "true"
      WATCHTOWER_POLL_INTERVAL: 7200
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "~/.docker/config.json:/config.json"

```

Assuming that you keep your original photos in `/share/Container/photos` modify  volume mount for `photoprism/originals`. To do that, edit `volumes` part of the photoprism service in `docker-compose.yml` file you just downloaded and provide proper mapping for the `/photoprism/originals`.

```yaml
volumes:
  # "/host/folder:/photoprism/folder"                 # Example
  - "/share/Container/photos:/photoprism/originals" # Original media files

```

> **NOTE:** Other things you might want to modify in the `docker-compose.yml` are:
>
> - default password for the user admin (default is: `insecure`)
> - number of workers
> - disable Tensorflow (used for categorization of photos and face detection)
>
> For changing number of workers and disabling TensorFlow see the "Performance tuning" section bellow.


<a id="create-directories-in-sharecontainerphotoprism"></a>
### Create directories in `/share/Container/photoprism`

```sh
mkdir /share/Container/photoprism/database
mkdir /share/Container/photoprism/import
mkdir /share/Container/photoprism/originals
mkdir /share/Container/photoprism/storage
```


<a id="run-application-in-the-container"></a>
### Run application in the container

Start the container. Pulling images might take few minutes depending on your Internet connection speed.

```sh
docker-compose up -d
```

> **NOTE**: From July 2023 Compose V1 invoked as `docker-compose` stopped receiving updates. It’s also no longer available in new releases of Docker Desktop. Compose V2 was announced in 2020, is written in Go, and is invoked as `docker compose`.

after that, Photoprism should be available under:

```
http://<YOUR-NAS-IP>:2342
```

You need to login as administrator with default password for the first time, after login remember to change that password in settings.
![img](/images/photoprism/photoprism_change_password.png)


<a id="using-web-ui"></a>
#### Using web-UI

Now, you can trigger indexing your photos and videos using web-UI or from CLI.
![img](/images/photoprism/photoprism_indexing.png)


<a id="using-cli"></a>
#### Using CLI

```sh
docker exec -ti photoprism photoprism index
```

<a id="manual-upgrading-photoprism-to-the-latests-version"></a>
### Manual upgrading Photoprism to the latests version

```sh
cd /share/Container/photoprism/
docker stop photoprism
docker pull photoprism/photoprism:latest
docker-compose up -d
```

For automated updates check [Watchtower](https://containrrr.dev/watchtower/)


<a id="adding-new-content"></a>
### Adding new content

- use upload via webDAV
- manually upload new pictures and videos to `/share/Container/photoprism/import` and manually trigger import using CLI:

```sh
docker exec photoprism photoprism import
```

You can also consider automating import by adding `import` do the cron (e.g. every midnight)


<a id="performance-tuning"></a>
### Performance tuning

If you are experiencing performance problems you can reduce number of workers (from documentation):
> Try [reducing the number of workers](https://docs.photoprism.app/getting-started/config-options/#index-workers) by setting `PHOTOPRISM_WORKERS` to a reasonably small value in `docker-compose.yml`, depending on the CPU performance and number of cores

or disable TensorFlow:

> As a last measure, you can [disable the use of TensorFlow](https://docs.photoprism.app/getting-started/config-options/#feature-flags) for image classification and facial recognition. You ca do it via web-UI settings, cli (`--disable-tensorflow` option) or set `PHOTOPRISM_DISABLE_TENSORFLOW` to `true` in `docker-compose.yml` and restart container.

**Credits:**
I was able to launch this service thanks to the instructions found on reddit [1] provided by [schol4stiker](https://www.reddit.com/user/schol4stiker/).

<a id="installation-using-container-station-gui"></a>
## Installation using Container Station GUI
I got message from one of the readers, that he realized, it was better to use Container Station to install Photoprism using its GUI. Open **Container Station > Applications > Create**

He named the application 'photoprism' and pasted the docker-compose file (first converted with Claude.ai to Docker Composer v3 format)

<a id="references"></a>
## References

1. [instruction from reddit](https://www.reddit.com/r/photoprism/comments/vph4ct/comment/ieobj8w/?utm_source=share&utm_medium=web2x&context=3)
2. [How to Setup PhotoPrism on a Synology NAS in 2022 - WunderTech](https://www.wundertech.net/how-to-setup-photoprism-on-a-synology-nas)

<a id="updates"></a>
## Updates

- 2023-08-11: add note about change in docker compose to v2. Thx Tom Berg.
- 2024-08-18: under volumes:    zdjecia was changed to photos, `/share/Multimedia/photos`  was changed to `/share/Container/`photos for documentation consistency.
- 2024-08-26: fixed process of manual update of docker images (stop should go before pull)
- 2024-08-26: fixed path in import section (for consistency)
