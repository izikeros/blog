---
Category: Howto
Date: '2019-01-17'
Image: /images/head/keras+tensorflow.jpg
Modified: '2019-02-08'
Start: '2019-01-17'
Status: published
Summary: Guide on how to install TensorFlow cpu-only version - the case for machines without GPU supporting CUDA. Step-by-step procedure starting from creating conda environment till testing if TensorFlow and Keras Works.
Tags: machine-learning, tensorflow, howto
Title: How to Install TensorFlow and Keras on Windows 10
---
> **EDIT 2021**: This post is partially depreciated by now since for TensorFlow 2.x CPU and GPU versions are integrated - there is no separate install and Keras is integrated with TensorFlow - no need to install separately unless you have good reasons for separate install.

Quick guide on how to install TensorFlow cpu-only version - the case for machines without GPU supporting CUDA.
<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Creating Conda environment for working with TensorFlow and Keras](#creating-conda-environment-for-working-with-tensorflow-and-keras)
- [Installing TensorFlow](#installing-tensorflow)
- [Installing Keras](#installing-keras)

<!-- /MarkdownTOC -->

<a id="creating-conda-environment-for-working-with-tensorflow-and-keras"></a>
# Creating Conda environment for working with TensorFlow and Keras
Open `anaconda prompt` (hit `Win+Q`, type anaconda) and create conda virtualenv:
```sh
conda create -n tf_windows python=3.6
```
this will create minimal environement

When the environment is created, activate it. After that the environment’s name will be added before the prompt.
```sh
activate tf_windows
```

<a id="installing-tensorflow"></a>
# Installing TensorFlow
Then install TensorFlow for CPU-only machines:
```text
(tf_windows)> pip install tensorflow
```
There can be few variants of the `tensorflow` package installation. If you need to run `pip` behind corporate proxy, add proxy information:
```text
(tf_windows)> pip --proxy="proxy_url:port" install tensorflow
```
If you need GPU-enabled version (and your machine supports it)
```text
(tf_windows)> pip install tensorflow-gpu
```

To test if installation was successful, you might want to do check:
```python
(tf_windows)>python
>>> import tensorflow as tf
>>> sess = tf.Session()
>>> print(sess.run(tf.constant('Hello world!')))
```
if everything was installed correctly, you should see:
```python
b'Hello world!''
```

On my machine I got warning when starting a new session:
```text
2019-01-17 07:09:01.477724: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
```
Don't get scared by that, TensorFlow works, the information displayed means that it isn't as fast as it could be.
In order to suppress this you will need to build TensorFlow from sources using appropriate flags (see [StackOverflow answer](https://stackoverflow.com/questions/41293077/how-to-compile-tensorflow-with-sse4-2-and-avx-instructions?rq=1)) for compilation otherwise you can ignore it.

<a id="installing-keras"></a>
# Installing Keras
The way that worked for me was:
```
(tf_windows)>conda install mingw libpython
(tf_windows)>pip install --upgrade keras
```
Using the `--upgrade` flag ensures that the latest version of Keras will be installed.

Perform the test if Keras was installed correctly

```python
>>> from keras import backend
Using TensorFlow backend.
>>> print(backend._BACKEND)
tensorflow
>>>
```



*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
