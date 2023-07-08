---
Title: Software Versioning Schemes
Slug: software-versioning-schemes
Date: 2023-07-08
Modified: 2023-07-08
Status: published
Tags: versioning, semantic-versioning, semver, calver, calendar-versioning, zerover, 0ver
Category: note
todo: recommendations
---
X::[[MOC_Software_Development]]
X::[[software_project_conventions_branchning_commits]]


## Introduction
  
Software versioning schemes are essential in the world of programming, as they help developers, users, and collaborators keep track of various versions of a software product. A proper versioning scheme enables easy identification of the current release, the changes made in each version, and the compatibility of a version with previous ones. In this blog post, we will discuss some of the most popular versioning schemes used in the software industry, along with a few lesser-known but useful alternatives.  

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Semantic Versioning](#semantic-versioning)
- [Calendar Versioning \(CalVer\)](#calendar-versioning-calver)
- [ZeroVer: 0-based Versioning](#zerover-0-based-versioning)
- [Lesser-known Versioning Schemes](#lesser-known-versioning-schemes)
	- [Romantic Versioning](#romantic-versioning)
	- [Hash-based Versioning](#hash-based-versioning)
	- [Custom Versioning Schemes](#custom-versioning-schemes)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="semantic-versioning"></a>
## Semantic Versioning (SemVer)
  
Semantic versioning, also known as [SemVer](https://semver.org/), is a widely adopted versioning scheme that emphasizes the importance of clear and meaningful version numbers. In SemVer, a version number consists of three parts: MAJOR.MINOR.PATCH. Each part represents the following:  
  
- MAJOR version: incremented when you make incompatible API changes,  
- MINOR version: incremented when you add functionality in a backwards-compatible manner, and  
- PATCH version: incremented when you make backwards-compatible bug fixes.  
  
In addition to these three parts, SemVer allows for additional labels for pre-release and build metadata as extensions to the MAJOR.MINOR.PATCH format. This makes it easier for developers to communicate the scope of changes in each release and helps users understand if an update will break their existing setup or not.  
  
<a id="calendar-versioning-calver"></a>
## Calendar Versioning (CalVer)
  
Another popular versioning scheme is Calendar Versioning or [CalVer](https://calver.org/). CalVer uses a combination of the release date and a project-specific version number to create a unique identifier for each release. The format typically looks like this: YYYY.MM.DD.MICRO.  
  
The advantages of CalVer include its simplicity and the ability to quickly determine the age of a release. However, unlike SemVer, CalVer does not provide explicit information about API changes or compatibility between versions.  
  
<a id="zerover-0-based-versioning"></a>
## ZeroVer: 0-based Versioning (0ver)
  
ZeroVer, also known as [0ver](https://0ver.org/) is a unique and simple versioning scheme that asserts that your software's major version should never exceed the first and most important number in computing: zero.  This is in contrast to other versioning schemes like Semantic Versioning and Calendar Versioning.  
  
The rationale behind ZeroVer is that software is never truly "finished" and will always be subject to improvements, bug fixes, and new features. By keeping the major version at zero, developers acknowledge the ever-evolving nature of their software and avoid the pressures associated with "final" releases.  

> Note: in the `0ver` there is a zero in front of the name, do not confuse with capital letter O

<a id="lesser-known-versioning-schemes"></a>
## Lesser-known Versioning Schemes
  
In addition to the popular versioning schemes mentioned above, there are other lesser-known but equally useful alternatives. Some of these include:  
  
<a id="romantic-versioning"></a>
### Romantic Versioning
  
[Romantic Versioning](https://github.com/romversioning/romver) is a light-hearted, informal versioning scheme that uses popular culture references or personal milestones as version numbers. While not suitable for all projects, Romantic Versioning can be a fun way to engage users and make software updates more memorable.  

The Romantic Versioning specification was authored by [Daniel V from the Legacy Blog crew](http://blog.legacyteam.info/2015/12/romver-romantic-versioning/) in 2015. This open and public repository has the task of maintenance and visibility, cooperation with others.

See also: [sentimentalversioning.org](http://sentimentalversioning.org/)

<a id="hash-based-versioning"></a>
### Hash-based Versioning
  
[Hash-based Versioning](https://miniscruff.github.io/hashver/)is a versioning scheme that uses the unique hash of a particular commit in a version control system (such as Git) as the version number. This approach ensures that each release is directly tied to a specific point in the development history, making it easy to track and revert changes if needed.  
  
<a id="custom-versioning-schemes"></a>
### Custom Versioning Schemes
  
Some projects may benefit from a custom versioning scheme tailored to their specific needs. This could involve combining elements from various existing schemes or developing an entirely new approach. When creating a custom versioning scheme, it's essential to ensure that it is clear, consistent, and easy to understand for all stakeholders.  
  
<a id="conclusion"></a>
## Conclusion
  
Choosing the right versioning scheme for your software project is crucial for effective communication and collaboration among developers, users, and other stakeholders. While Semantic Versioning and Calendar Versioning are popular choices, alternative schemes like ZeroVer, Romantic Versioning, Hash-based Versioning, or even custom schemes can also be appropriate depending on your project's unique requirements. Ultimately, the ideal versioning scheme should be easy to understand, provide meaningful information about each release, and facilitate the management of software updates.