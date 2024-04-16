---
Title: OSI Approved in license metadata for Python project
Slug: osi-approved-in-license-metadata-for-python-project
Date: 2024-04-16
Modified: 2024-04-16
Status: published
tags: license, pyproject, osi, open-source-initiative,
Category: note
---
When it comes to sharing and distributing Python projects, clarity about licensing is crucial. A license tells users what they can and cannot do with your code, impacting everything from contributions to commercial use. The `pyproject.toml` file, as outlined in [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/) and enhanced by subsequent PEPs, provides a standardized format for project metadata, including license information. By specifying an "OSI Approved" license in your `pyproject.toml`, you not only make your software's terms of use explicit but also ensure you’re adhering to the standards that have become the cornerstone of open-source software.

In this blog post, we'll dive into the `[project]` section of the `pyproject.toml` file, where you can define your project's license. We will explore the reasons why including an OSI Approved license in your Python project metadata is not just good practice but also a reflection of your commitment to the open-source community's values.

Join us as we unpack the benefits of explicit licensing, how it can save you and your users legal headaches, and why it's an essential component of any reputable Python project.

## OSI Approval
"OSI Approved" in the context of a license listed in a `pyproject.toml` file for a Python project indicates that the license under which the project is distributed has been approved by the Open Source Initiative (OSI).

The [Open Source Initiative](https://opensource.org/) is a non-profit organization that advocates for open-source software and maintains the Open Source Definition. A license that is OSI Approved means that it complies with this definition, which includes a set of criteria to ensure free redistribution, access to source code, and other important freedoms related to software usage and distribution.

Therefore, if a project's `pyproject.toml` specifies a license as "OSI Approved," it implies that the software can be freely used, modified, and shared under the terms that are consistent with the open-source movement, as validated by the OSI's review process. It's a mark of recognition that the software license adheres to open-source principles.

## Examples of OSI approved licenses
The Open Source Initiative (OSI) approves various licenses that comply with their Open Source Definition. Some of the most commonly used OSI approved licenses include:

1. MIT License
2. Apache License 2.0
3. GNU General Public License (GPL) 2.0 & 3.0
4. BSD Licenses (2-clause and 3-clause)
5. GNU Lesser General Public License (LGPL)
6. Mozilla Public License 2.0
7. Eclipse Public License
8. GNU Affero General Public License (AGPL)
9. Creative Commons Zero v1.0 Universal (CC0)
10. Artistic License 2.0

Each of these licenses has its own terms and conditions, varying in terms of how redistributions must credit

## Examples of  licenses without approval from OSI
There are several licenses that are not approved by the Open Source Initiative (OSI) either because they have not been submitted for approval, they discriminate against persons or groups, they discriminate against fields of endeavor, they are not technology-neutral, or for other reasons that conflict with the Open Source Definition. Some examples include:

* Various Creative Commons licenses (excluding CC0):
 
Licenses such as Creative Commons Attribution-NonCommercial (CC BY-NC), Creative Commons Attribution-NoDerivatives (CC BY-ND), and others are not OSI-approved because they impose restrictions on commercial use or the creation of derivative works, which goes against the Open Source Definition that requires the license to allow modifications and derived works.

* JSON License ("The Software shall be used for Good, not Evil"):
   
The JSON License includes a clause that specifies "The Software shall be used for Good, not Evil," which introduces a subjective and non-legal term. This clause can be interpreted in various ways and thus makes it non-free according to the open-source criteria, which insist on no discrimination against fields of endeavor.

* The Apple Public Source License 1.x:

The earlier versions of the Apple Public Source License were not approved by the OSI due to concerns about the license's compatibility and restrictions on the usage of the covered software. Apple addressed these issues in version 2.0, which was approved by the OSI.

* Badgeware Licenses (Original Attribution Assurance License, the Honest Public License, etc.):
   
These licenses require the display of a logo, badge, or attribution in a manner that the OSI considers overly burdensome and not in line with the Open Source Definition's requirements for free redistribution.

* Microsoft Limited Public License (Ms-LPL) and the Microsoft Reciprocal License (Ms-RL):
   
These licenses were specific to Windows and were not technology-neutral, making them incompatible with the OSI's requirement that open-source licenses must not restrict the software to run on a particular operating system or environment.

> **NOTE:** When using software under a specific license or choosing a license for your own work, checking the current OSI-approved list is advisable for the most up-to-date information.