---
Title: Create Self-Hosted Python Package Repository - General Guide
Slug: Create Self-Hosted Python Package Repository
Date: 2023-08-12
Modified: 2023-08-12
Status: published
Tags: pypi, python, python-package, package-repository, artifactory, devpi
Category: note
---
X::[[lesser_known_python_package_repository_managers]]
X::[[python_packages_on_local_NAS]]
up::[[python]]

Creating a self-hosted Python package repository allows you to host and manage your own Python packages, making them accessible to your team or the public without relying on external services like PyPI. Here's a general guide on how to set up a self-hosted Python package repository.

```toc
style: bullet
min_depth: 2
max_depth: 6 
title: "**Contents**"
```

## General Guide

### Choose a Repository Manager

You need a repository manager to host and manage your Python packages. Two popular options are:

- **Devpi**: A powerful and customizable Python package repository server.
- **Artifactory**: A general-purpose repository manager that can host various types of packages, including Python.

### Set Up a Server

You will need a server to host your package repository. This could be a dedicated server, a cloud instance (AWS, GCP, Azure), or even a local machine if the repository is for internal use.

### Install and Configure the Repository Manager

#### Devpi

- Install Devpi using pip: `pip install devpi-server devpi-web`
- Configure Devpi: Follow the instructions in the [official documentation](https://devpi.net/docs/devpi/devpi/stable/+doc/quickstart-server.html).

#### Artifactory

Download and install Artifactory: Follow the instructions on the [Artifactory website](https://www.jfrog.com/confluence/display/JFROG/Installing+Artifactory).

### Create a Virtual Environment (optional but recommended)

Set up a Python virtual environment on your server to keep your package repository isolated from the system Python.

### Upload Packages

Once your repository manager is set up, use tools like `twine` to upload your Python packages. Make sure to specify your self-hosted repository URL.

### Accessing Packages

To use packages from your self-hosted repository, users can modify their `pip.conf` or `.pypirc` configuration file to include your repository's URL.

### Security and Access Control

Configure user authentication and access control to restrict who can upload and access packages in your repository.

### Maintenance and Backup

- Regularly back up your package repository data to prevent data loss.
- Keep your repository manager and server updated with security patches.

### Documentation

Provide clear documentation to your team on how to access, upload, and manage packages in your self-hosted repository.

## Artifactory vs. Devpi - pros & cons and setup instructions

Let's explore two popular free and open-source options for creating a self-hosted Python package repository: Devpi and Artifactory, along with their pros, cons, use cases, and a tutorial for setting up each.

### Option 1: Devpi

**Pros:**

- Designed specifically for Python package management.
- Provides features like caching, replication, and access control.
- Supports easy package versioning and management.

**Cons:**

- Limited support for non-Python packages.
- Web interface might not be as polished as other solutions.

**Use Cases:**

- Small to medium-sized teams working exclusively with Python.
- Projects where ease of setup and simple usage is preferred.

**Tutorial:**

1. **Install Devpi**:

```
pip install devpi-server devpi-web
```

2. **Create and Configure Devpi Server**:
   - Initialize a new Devpi server:

```
devpi-server --init
```

- Start the Devpi server:

```
devpi-server
```

3. **Create Users and Indexes**:
   - Create a user:

```
devpi use http://localhost:3141
devpi user -c <username>
```

- Create an index:

```
devpi index -c <indexname>
```

4. **Upload and Use Packages**:
   - Upload a package:

```
devpi upload
```

- Install a package from your Devpi index:

```
pip install -i http://localhost:3141/<username>/<indexname>/simple/ <package>
```

### Option 2: Artifactory

**Pros:**

- Versatile repository manager supporting multiple package types.
- Robust access control and security features.
- Highly configurable and scalable.

**Cons:**

- More complex setup compared to Devpi.
- Heavier resource requirements.

**Use Cases:**

- Large organizations with diverse technology stacks.
- Projects needing advanced access control and security features.

**Tutorial:**

1. **Install Artifactory**:
   - Follow the installation guide for [Artifactory Community Edition](https://www.jfrog.com/confluence/display/JFROG/Installing+Artifactory).

2. **Configure Artifactory**:
   - Access Artifactory's web interface and set up your repository.

3. **Create a Virtual Repository**:
   - Create a new virtual repository and include a "PyPI" remote repository as a source.

4. **Upload Packages**:
   - Use `twine` to upload your Python packages to your virtual repository:

```
twine upload --repository-url <Artifactory_URL>/<repository_name> dist/*
```

5. **Access and Use Packages**:
   - Configure your pip to use your Artifactory repository as an index:

```
pip config set global.index-url <Artifactory_URL>/<repository_name>/simple/
```

- Install packages as usual using pip.

## Closing thoughts

- Setting up a self-hosted Python package repository requires careful consideration of your team's needs and technical expertise. Choose the option that best aligns with your requirements and resources.
- Remember, setting up and maintaining a self-hosted package repository requires technical expertise and ongoing maintenance. If you're not experienced with server management and administration, consider starting with a simpler approach or seeking help from someone with relevant experience.
