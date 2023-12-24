---
Category: note
Date: '2023-04-14'
Modified: '2023-07-12'
Prompt: give me long blog post on in python how to convert heic and heif to jpeg and other popular formats. in the post give me full working code
Slug: convert-heic-and-heif-to-jpg-png-bmp-with-python
Status: published
Tags: python, heic, heif, pillow, pil, pyheic, convert, image-conversion, compression
Title: Convert HEIC and HEIF to Jpg, Png, BMP With Python
---
HEIF and HEIC image formats are gaining popularity due to their superior image quality and smaller file sizes compared to traditional formats like JPEG and PNG. However, they are not yet widely supported by all devices and software applications. In this blog post, we will explore how to convert HEIF and HEIC files to JPEG and other popular image formats using Python.

<!-- MarkdownTOC levels="2,3,4" autolink="true" autoanchor="true" -->

- [Tutorial](#tutorial)
  - [Use Pillow](#use-pillow)
    - [Step 1: Installing Required Libraries](#step-1-installing-required-libraries)
    - [Step 2: Converting HEIF and HEIC Files to JPEG](#step-2-converting-heif-and-heic-files-to-jpeg)
    - [Step 3: Converting HEIF and HEIC Files to Other Formats](#step-3-converting-heif-and-heic-files-to-other-formats)
    - [Step 4: Converting HEIF and HEIC Files in Bulk to JPEG](#step-4-converting-heif-and-heic-files-in-bulk-to-jpeg)
  - [Use pyheif library](#use-pyheif-library)
- [Summary](#summary)

<!-- /MarkdownTOC -->

<a id="tutorial"></a>

## Tutorial

Python provides several libraries for working with images, including Pillow, OpenCV, and PyImageSearch. For this tutorial, we will be using the Pillow library, which is a fork of the Python Imaging Library (PIL) and provides a simple and easy-to-use API for image processing.

<a id="use-pillow"></a>

### Use Pillow

<a id="step-1-installing-required-libraries"></a>

#### Step 1: Installing Required Libraries

Before we can begin converting HEIF and HEIC files, we need to make sure we have the necessary libraries installed. To install Pillow, open a terminal or command prompt and run the following command:

```
pip install Pillow
```

<a id="step-2-converting-heif-and-heic-files-to-jpeg"></a>

#### Step 2: Converting HEIF and HEIC Files to JPEG

To convert HEIF and HEIC files to JPEG, we can use the Pillow library's `Image` module. The `Image` module provides several methods for opening and saving images in different formats, including `JPEG`, `PNG`, and `BMP`.

Here is a Python code example that shows how to convert a single HEIF or HEIC file to JPEG:

```python
from PIL import Image

# Open HEIF or HEIC file
image = Image.open('example.heic')

# Convert to JPEG
image.convert('RGB').save('example.jpg')

```

In the code above, we first import the `Image` module from the Pillow library. We then use the `open()` method to open the HEIF or HEIC file and assign it to the `image` variable. We then use the `convert()` method to convert the image to the RGB color space, which is required for saving the image in JPEG format. Finally, we use the `save()` method to save the converted image as a JPEG file.

Note that in order to convert HEIF and HEIC files to JPEG using Pillow, we need to convert them to the RGB color space. This can result in a loss of some of the advanced features of HEIF and HEIC, such as support for high dynamic range (HDR) and wide color gamut (WCG).

If you want to convert multiple HEIF or HEIC files to JPEG, you can use a for loop to iterate over a list of file names:

```python
from PIL import Image
import os

# Get list of HEIF and HEIC files in directory
directory = '/path/to/directory'
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]

# Convert each file to JPEG
for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))

```

In the code above, we use the `os` library to get a list of HEIF and HEIC files in a directory. We then use a for loop to iterate over the list of file names, open each file using the `Image` module, convert it to RGB color space, and save it as a JPEG file with the same name as the original file.

<a id="step-3-converting-heif-and-heic-files-to-other-formats"></a>

#### Step 3: Converting HEIF and HEIC Files to Other Formats

In addition to converting HEIF and HEIC files to JPEG, we can also convert them to other popular formats like PNG and BMP using the Pillow library. Here is an example that shows how to convert a HEIF or HEIC file to PNG:

```python
from PIL import Image  # Open HEIF or HEIC

HEIC file image = Image.open('example.heic')

# Convert to PNG
image.save('example.png')
```

In the code above, we use the `save()` method to save the opened HEIF or HEIC file as a PNG file.  Similarly, we can convert HEIF and HEIC files to BMP format using the `save()` method with the `'BMP'` argument:  

```python
from PIL import Image # Open HEIF or HEIC file 

image = Image.open('example.heic') 

# Convert to BMP 
image.save('example.bmp')
```

<a id="step-4-converting-heif-and-heic-files-in-bulk-to-jpeg"></a>

#### Step 4: Converting HEIF and HEIC Files in Bulk to JPEG

If you have a large number of HEIF and HEIC files that you need to convert to JPEG, you can use the following Python script:

```python
from PIL import Image
import os

# Get list of HEIF and HEIC files in directory
directory = '/path/to/directory'
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]

# Create output directory if it does not exist
if not os.path.exists(os.path.join(directory, 'output')):
    os.makedirs(os.path.join(directory, 'output'))

# Convert each file to JPEG
for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, 'output', os.path.splitext(filename)[0] + '.jpg'))

```

In the code above, we use the `os` library to get a list of HEIF and HEIC files in a directory. We then create an output directory if it does not already exist. Finally, we use a for loop to iterate over the list of file names, open each file using the `Image` module, convert it to RGB color space, and save it as a JPEG file in the output directory with the same name as the original file.

<a id="use-pyheif-library"></a>

### Use pyheif library

Here is an example of how to use the `pyheif` library to convert HEIF and HEIC files to JPEG:

```python
import pyheif
from PIL import Image

# Open HEIF or HEIC file
heif_file = pyheif.read("example.heic")

# Extract the image data
image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)

# Save as JPEG
image.save('example.jpg')

```

In the code above, we use the `pyheif` library to read in the HEIF or HEIC file, then use the `frombytes()` method of the `PIL.Image` module to create a PIL image object from the extracted image data. Finally, we use the `save()` method to save the image as a JPEG file.

To convert multiple HEIF and HEIC files in bulk using `pyheif`, you can use the following code:

```python
import pyheif
from PIL import Image
import os

# Get list of HEIF and HEIC files in directory
directory = '/path/to/directory'
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]

# Create output directory if it does not exist
if not os.path.exists(os.path.join(directory, 'output')):
    os.makedirs(os.path.join(directory, 'output'))

# Convert each file to JPEG
for filename in files:
    heif_file = pyheif.read(os.path.join(directory, filename))
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
    image.save(os.path.join(directory, 'output', os.path.splitext(filename)[0] + '.jpg'))

```

In this code, we use the same approach to get a list of HEIF and HEIC files in a directory and create an output directory if it does not already exist. Then, we use a for loop to iterate over the list of file names, read in each HEIF or HEIC file using `pyheif`, create a PIL image object from the extracted image data, and save it as a JPEG file in the output directory with the same name as the original file.

Using the `pyheif` library to convert HEIF and HEIC files to JPEG is a simple and effective way to handle image file format conversions in Python.

<a id="summary"></a>

## Summary

In this blog post, we explored how to convert HEIF and HEIC files to JPEG and other popular image formats using Python and the Pillow and pyheif libraries. We covered how to convert a single file as well as multiple files in bulk. With this knowledge, you can easily convert HEIF and HEIC files to more widely supported formats, enabling you to use them on any device or software application that supports images.

X::[[heic_and_heif_formats_for_image_and_video]]
up::[[MOC_Python]]
