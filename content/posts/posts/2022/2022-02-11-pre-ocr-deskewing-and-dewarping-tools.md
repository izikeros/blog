---
Category: Machine Learning
Date: '2022-02-11'
Image: /images/head/dewarp_deskew.jpg
Modified: '2023-07-12'
Slug: tools-for-doc-deskewing-and-dewarping
Status: Published
Summary: Sometimes input for document processing tasks such as OCR, table detection or text segmentation can be scanned or photo taken from hand that do not have ideal perspective - is rotated or spatially distorted in some way (warped document). If you are looking for my recommendations go straight to the last section of this article "Summary and recommendations".
Tags: document-intelligence, document-processing, computer-vision, digital-image-processing, canny-edge-detector, hough-transform, deep-learning
Title: 15 Tools for Document Deskewing and Dewarping
citation_needed: false
todo: Add credits to all images, copy images instead of hot linking
---

Sometimes input for document processing tasks such as OCR, table detection, or text segmentation can be scan, or photo taken from hand that does not have an ideal perspective - is rotated or spatially distorted in some way (warped document).
If you are looking for my recommendations go straight to the last section of this article [Summary and recommendations](#summary-and-recommendations). This article was inspired by a list of OCR-related projects posted on the list [awesome-ocr](https://github.com/zacharywhitley/awesome-ocr). To give readers intuition about the popularity of the project - information about GitHub stars is added to each project (as of Feb 2022 - time of writing this article). To differentiate actively developed projects from ones that don't get commits anymore - the date of the last commit was added.



## The typical approach for deskewing

The deskewing is typically realized by using Canny Edge Detection and Hough Transform to determine the angle of rotation (skew) and then applying rotation in opposite direction.



## The typical approach for dewarping

Reconstruction of spatial (3D) structure of the document is typically done using the Deep Learning approach. 


## List of approaches presented in this article

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Dewarping](#dewarping)
	- [Page dewarp \(1.1k stars\)](#page-dewarp-11k-stars)
	- [MORAN \(579 stars\)](#moran-579-stars)
	- [DewarpNet \(291 stars\)](#dewarpnet-291-stars)
	- [Document Image Dewarping  - algorithm \(241 stars\)](#document-image-dewarping---algorithm-241-stars)
	- [Unproject Text \(104 stars\)](#unproject-text-104-stars)
	- [Docuwarp \(stars 83\)](#docuwarp-stars-83)
	- [Book content segmentation and dewarping \(under construction\) \(11 stars\)](#book-content-segmentation-and-dewarping-under-construction-11-stars)
- [Deskewing](#deskewing)
	- [Unpaper \(770 stars\)](#unpaper-770-stars)
	- [Alyn \(222 stars\)](#alyn-222-stars)
	- [Deskew \(211 stars\)](#deskew-211-stars)
	- [galfar/deskew \(102 stars\)](#galfardeskew-102-stars)
	- [Skew correction \(12 stars\)](#skew-correction-12-stars)
	- [Deskewing \(stars 8\)](#deskewing-stars-8)
	- [Text deskewing \(5 stars\)](#text-deskewing-5-stars)
- [Summary and recommendations](#summary-and-recommendations)
	- [What to use for Deskewing?](#what-to-use-for-deskewing)
	- [What to use for Unwarping and Deskewing?](#what-to-use-for-unwarping-and-deskewing)
	- [What to use for Document Segmentation](#what-to-use-for-document-segmentation)

<!-- /MarkdownTOC -->


<a id="dewarping"></a>
# Dewarping
<a id="page-dewarp-11k-stars"></a>
## Page dewarp ![github stars shield](https://img.shields.io/github/stars/mzucker/page_dewarp.svg?logo=github)
> Last commit: Oct 2016, but the reworked version is actively developed (last commit: 24 Jan 2022)

[page_dewarp](https://github.com/mzucker/page_dewarp) - Page dewarping and thresholding using a "cubic sheet" model

<img src="https://mzucker.github.io/images/page_dewarp/linguistics_thesis_a_before_after.png" alt="before and after dewarp" style="zoom:50%;" />

Read more here: [Page dewarping](https://mzucker.github.io/2016/08/15/page-dewarping.html)

>  NOTE: It is written in Python but using Python 2.

Since the original work of mzucker was written in Python 2 and not developed further there was the initiative to renovate the original scripts and there is [page-dewarp](https://github.com/lmmx/page-dewarp) which is also available on Pypi, and it is pip installable (`pip install page-dewarp`)

<a id="moran-579-stars"></a>
## MORAN ![github stars shield](https://img.shields.io/github/stars/Canjie-Luo/MORAN_v2.svg?logo=github)
>  Last commit: 30 Jul 2019

[MORAN_v2](https://github.com/Canjie-Luo/MORAN_v2)  - A Multi-Object Rectified Attention Network for Scene Text Recognition

![img](https://github.com/Canjie-Luo/MORAN_v2/raw/master/demo/MORAN_v2.gif)

Written in Python, using PyTorch
> NOTE: The project is only free for academic research purposes.

<a id="dewarpnet-291-stars"></a>
## DewarpNet ![github stars shield](https://img.shields.io/github/stars/cvlab-stonybrook/DewarpNet.svg?logo=github)
> Last commit: 6 Sep 2021

[DewarpNet](https://github.com/cvlab-stonybrook/DewarpNet) - This repository contains the codes for [**DewarpNet**](https://www3.cs.stonybrook.edu/~cvl/projects/dewarpnet/storage/paper.pdf) training.

[<img src="https://github.com/cvlab-stonybrook/DewarpNet/raw/master/dwnet.png" alt="img" style="zoom:50%;" />](https://github.com/cvlab-stonybrook/DewarpNet/blob/master/dwnet.png)

[DewarpNet project web page](https://sagniklp.github.io/dewarpnet-webpage/). Here is how the authors characterize their solution in the abstract of the paper:

> DewarpNet, a deep learning approach for document image unwarping from a single image. Our insight is that the 3D geometry of the document not only determines the warping of its texture but also causes the illumination effects. Therefore, our novelty resides on the explicit modeling of 3D shape for document paper in an end-to-end pipeline. 

[DewarpNet pre-trained models]( https://drive.google.com/file/d/1hJKCb4eF1AJih_dhZOJSF5VR-ZtRNaap/view) are available for download from Google Drive.



<a id="document-image-dewarping---algorithm-241-stars"></a>
## Document Image Dewarping  - algorithm ![github stars shield](https://img.shields.io/github/stars/xellows1305/Document-Image-Dewarping.svg?logo=github)
> Last commit: 30 Sep 2019

[Document-Image-Dewarping](https://github.com/xellows1305/Document-Image-Dewarping)- Document image dewarping is approached by using text lines and line segments. 

In this repository, there is **no public code** to use but just algorithm description and executable available for [download](http://ispl.synology.me:8480/sharing/uA2DTRA8U).

<a id="unproject-text-104-stars"></a>
## Unproject Text ![github stars shield](https://img.shields.io/github/stars/mzucker/unproject_text.svg?logo=github)
> Last commit: 13 Oct 2016

[unproject_text](https://github.com/mzucker/unproject_text) - **Perspective recovery of text using transformed ellipses**.

 It is not exactly dewarping but perspective correction which is why it was placed in the dewarping section.

Written in Python, it is pretty lightweight: using numpy, scipy, cv2,...

In a nutshell, letters are replaced with ellipses and the axes of ellipses are used to determine what affine transformation is needed to correct perspective:

<img src="https://mzucker.github.io/images/unproject_text/example0_ellipses.png" alt="contours with areas" style="zoom:50%;" />

Image source: repository owner's [writeup](https://mzucker.github.io/2016/10/11/unprojecting-text-with-ellipses.html)

More information about the method can be found in the [article](https://mzucker.github.io/2016/10/11/unprojecting-text-with-ellipses.html) and [paper by Carlos Merino-Gracia et al.](http://www.sciencedirect.com/science/article/pii/S0262885613001066) .

<a id="docuwarp-stars-83"></a>
## Docuwarp ![github stars shield](https://img.shields.io/github/stars/thomasjhuang/deep-learning-for-document-dewarping.svg?logo=github)
>  Last commit: 18 Oct 2021

[Docuwarp](https://github.com/thomasjhuang/deep-learning-for-document-dewarping) - An application of high-resolution **GANs to dewarp images** of perturbed documents.
This project is focused on dewarping document images through the usage of pix2pixHD, a GAN that is useful for the general image to image translation. The objective is to take images of documents that are warped, folded, crumpled, etc., and convert the image to a "dewarped" state by using pix2pixHD to train and perform inference.

Written in Python.

<a id="book-content-segmentation-and-dewarping-under-construction-11-stars"></a>
## Book content segmentation and dewarping (under construction)  ![github stars shield](https://img.shields.io/github/stars/RaymondMcGuire/BOOK-CONTENT-SEGMENTATION-AND-DEWARPING.svg?logo=github)
> Last update of code: 2018

[Book Content Segmentation and Dewarping](https://github.com/RaymondMcGuire/BOOK-CONTENT-SEGMENTATION-AND-DEWARPING) - Using **FCN (fully convolution network) to segment the image** into 3 parts (left page, right page, and background).

The segmentation demo is available here: https://raymondmgwx.github.io/?e=Project_BookContent&&theme=Image-Process-Content.

> NOTE: that Data Augment and Dewarp Algorithm are in TODO of this project.

<a id="deskewing"></a>
# Deskewing
<a id="unpaper-770-stars"></a>
## Unpaper  ![github stars shield](https://img.shields.io/github/stars/unpaper/unpaper.svg?logo=github)

> Last commit: 21 Jan 2022

[unpaper](https://github.com/unpaper/unpaper) is a **post-processing tool for scanned sheets of paper**, especially for book pages that have been scanned from previously created photocopies.

 The main purpose is to make scanned book pages better readable on screen after conversion to PDF. Additionally, unpaper might be useful to enhance the quality of scanned pages before performing optical character recognition (OCR).

**unpaper tries to clean scanned images by removing dark edges that appeared through scanning or copying on areas outside the actual page content** (e.g. dark areas between the left-hand side and the right-hand side of a double-sided book-page scan).

The program also tries to detect misaligned centering and rotation of pages and will **automatically straighten each page** by rotating it to the correct angle. This process is called "deskewing".

Written mostly in C.

<a id="alyn-222-stars"></a>
## Alyn  ![github stars shield](https://img.shields.io/github/stars/kakul/Alyn.svg?logo=github)
> Last commit: 14 Jun 2017

[Alyn](https://github.com/kakul/Alyn) - **Skew detection and correction** in images containing text. It uses Canny Edge Detection and  Hough Transform to determine skew.

How the Alyns' skew detection works:

- Converts the image to greyscale
- Performs Canny Edge Detection on the Image
- Calculates the Hough Transform values
- Determines the peaks
- Determines the deviation of each peaks from 45-degree angle
- Segregates the detected peaks into bins
- Chooses the probable skew angle using the value in the bins

Alyn is written in Python can be installed with pip (`pip install allyn`).

<a id="deskew-211-stars"></a>
## Deskew ![github stars shield](https://img.shields.io/github/stars/sbrunner/deskew.svg?logo=github)
> Last commit : 10 Feb 2022

[deskew](https://github.com/sbrunner/deskew) - Library used to **deskew a scanned document**. Skew detection and correction in images containing text
Written in Python, lightweight. Inspired by [Alyn](#alyn-222-stars).

<a id="galfardeskew-102-stars"></a>
## galfar/deskew ![github stars shield](https://img.shields.io/github/stars/galfar/deskew.svg?logo=github)
> Last commit: 6 Jan 2022

[galfar/deskew](https://github.com/galfar/deskew) - Deskew is a **command-line tool** for deskewing scanned text documents. It uses Hough transform to detect "text lines" in the image. As an output, you get an image rotated so that the lines are horizontal.

There are binaries built for these platforms: Win64, Win32, Linux 64bit, macOS, and Linux ARMv7. GUI frontend for this CLI tool is available as well (Windows, Linux, and macOS),

> NOTE: It is written in Pascal.

<a id="skew-correction-12-stars"></a>
## Skew correction ![github stars shield](https://img.shields.io/github/stars/prajwalmylar/skew_correction.svg?logo=github)
[skew_correction](https://github.com/prajwalmylar/skew_correction) - **Deskewing images** with slanted content by finding the deviation using Canny Edge Detection.


<a id="deskewing-stars-8"></a>
## Deskewing ![github stars shield](https://img.shields.io/github/stars/sauravbiswasiupr/deskewing.svg?logo=github)
> Last commit: 12 Jan 2014

[deskewing](https://github.com/sauravbiswasiupr/deskewing) - Contains code to **deskew images using MLPs, LSTMs and LLS transformations.**
Written in Python.

<a id="text-deskewing-5-stars"></a>
## Text deskewing ![github stars shield](https://img.shields.io/github/stars/dehaisea/text_deskewing.svg?logo=github)
> Last commit: 9 Mar 2018

[text_deskewing](https://github.com/dehaisea/text_deskewing) - **Rotate text images if they are not straight** for better text detection and recognition. Uses Canny Edge Detection and probabilistic Hough Transform.

It is written in Python and the repository does not contain a lot of code - it is easy to follow and learn how those simple techniques can be used to desk the text.

<a id="summary-and-recommendations"></a>
# Summary and recommendations

<a id="what-to-use-for-deskewing"></a>
## What to use for Deskewing?

- If you need to **deskew** and additionally **clean-up** document from scanning artifacts use: [unpaper](https://github.com/unpaper/unpaper)
- If you just need to **correct the rotation** of the document use: [Alyn](https://github.com/kakul/Alyn) or [deskew](https://github.com/sbrunner/deskew)
- If you want to **learn about using Edge Detection and Hough Transform** for document deskewing you might want to have look at: [text_deskewing](https://github.com/dehaisea/text_deskewing)

<a id="what-to-use-for-unwarping-and-deskewing"></a>
## What to use for Unwarping and Deskewing?

- For dewarping book pages that have **smooth bendings** consider using [page-dewarp](https://github.com/lmmx/page-dewarp) (renovated version of popular [page_dewarp](https://github.com/mzucker/page_dewarp). 
- For more complex dewarping including e.g. **folded pages** use Deep Learning-based solutions such as [DewarpNet](https://github.com/cvlab-stonybrook/DewarpNet) or [Docuwarp](https://github.com/thomasjhuang/deep-learning-for-document-dewarping). 
- If you are working with flat pages and you just need to **correct perspective** [unproject_text](https://github.com/mzucker/unproject_text) might be the right tool for you.
<a id="what-to-use-for-document-segmentation"></a>
## What to use for Document Segmentation

Document segmentation was not in the scope of this article. You can check [awesome-ocr](https://github.com/zacharywhitley/awesome-ocr) section on Document Segmentation

**References:**

- [awesome-ocr](https://github.com/zacharywhitley/awesome-ocr) - a rich collection of OCR-related projects and tools

**Credits:**

- The image used in the header of this article comes from the paper [DewarpNet: Single-Image Document Unwarping With Stacked 3D and 2D Regression Networks](https://www3.cs.stonybrook.edu/~cvl/projects/dewarpnet/storage/paper.pdf). *Sagnik Das, Ke Ma, Zhixin Shu, Dimitris Samaras, Roy Shilkrot*; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019, pp. 131-140
- All other images in the article come from the project owners or related sources (papers, articles)


*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
