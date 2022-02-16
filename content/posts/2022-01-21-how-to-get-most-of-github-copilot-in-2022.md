---
title: How to get most of GitHub Copilot
date: 2022-01-25
status: Published
tags: github, coding, ai
summary: This post describes techniques that help to get most accurate suggestions from the GitHub Copilot "Your AI pair programmer". For those who never heard of Copilot there is short introduction, if you already know Copilot - you can jump directly to section 4: "How to get most of GitHub Copilot".
slug: how-to-get-most-of-github-copilot
category: Howto
citation_needed: false
todo:
Image: /images/head/copilot-warp-speed-head.jpg
---



## TLDR
To get accurate autosuggestion from Copilot you can:

1. **Modify signature** of received suggestion to one that capture all relevant inputs and wait for new suggestion.
2. **Write pseudocode**: describe steps for the function with complex business logic.
3. For functions with complex business logic **divide them into multiple smaller functions**. Purpose of smaller function is easier to describe with just function name or the comment/docstring.

## Outline:

1. What is GitHub Copilot?
2. How to get it?
3. How to use it?
4. How to get most of GitHub Copilot?



## 1. What is GitHub Copilot?
In brief: [GitHub Copilot](https://copilot.github.com/), gives suggestions for whole lines or entire functions right inside your editor as you type. Currently, there is support for Visual Studio Code, Neovim, and JetBrains IDEs like PyCharm and IntelliJ IDEA.
GitHub Copilot is powered by the OpenAI Codex AI system, and, as authors claimed, trained on public internet text and billions of lines of code.

The way how it is used is that human programmer provides comment with intention what code he/she would like to get, and as autocomplete suggestion gets whole functions of classes. GitHub Copilot uses not only exact comment test but also context of the code that is expected to be auto-generated.

![img](https://copilot.github.com/diagram.png)
Figure 1. Data exchange between GitHub Copilot service, OpenAI Codex Model and Private Code and IDE. Image from: copilot.github.com

## 2. How to get it?
Access to GitHub Copilot is limited to a small group of testers during the technical preview. You can sign up and join the wait-list to try it out [here](https://github.com/features/copilot/signup).

## 3. How to use it?
Provide a docstring, comment, function name, or the piece of code itself, GitHub Copilot will use the context you’ve provided and generate code as suggestion.

## 4. How to get most of GitHub Copilot?
After using the GitHub Copilot service for almost three months, I was amazed how useful suggestions from Copilot can be. Of course, it is not ideal - suggestions are not always meeting my expectations. Sometimes it took few attempts to formulate my expectations to get the code that was looking good to me.
What I learned by the time of writing this post, are the few simple rules that can increase accuracy of the suggestions. I will outline them below. I'm using three main strategies to communicate my expectations with the GitHub Copilot service:

### Simple case - write short comment

For the simple cases: just write  comment that describe behavior for the code that you want to get as suggestion.
As example - we want to get a function that will return paths to all images in given directory and sub-directories. We are interested only in images of given type (specified file extensions).

Here is first attempt to get code auto completion from GitHub copilot.

 ![img](../images/copilot/copilot_1.gif)

Figure 2. Autosuggestion obtained as auto-completion to comment describing behavior of the function.

The example above illustrate how we started with initial suggestion for the comment and how the suggested  comment was refined as suggestions were provided by Copilot. The first suggestion for the code was very near the expectation - one thing that is missing is the support for selecting file extensions of interest.

Let's try to modify function signature and add list of extensions (and type hints):
old signature was:

```python
def get_images_in_dir(directory):
```
new signature:
```python
def get_images_in_dir(directory: str, extensions: List[str]) -> list:
```

And this time resulting code that meet requirements:
```python
def get_images_in_dir(directory: str, extensions: List[str]) -> list:
    """
    Get list of images in a directory, recursively. Include extensions:
    .jpg, .png, cr2, etc.
    :param directory: str
    :param extensions: list
    :return: list
    """
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(tuple(extensions)):
                images.append(os.path.join(root, file))
    return images
```



Other examples of functions that short comment can sufficiently describe responsibility:

```
# get image of the day from bing (or Wikipedia/NASA/...)

# convert a list of dictionaries to a list of lists

# get information using public API from stocktwits
```



## Simple case - write function name

Starting with descriptive function name can work as well:
 ![img](../images/copilot/copilot_2.gif)





### More complex cases - write pseudocode

For the complex cases: write line of comment that describe behavior for the code that you want to get as suggestion.
Example:

Comment with purpose of the function and pseudocode describing elements of solution
```python
# Check if two nested lists have the same dictionaries
# pseudocode:
# 1. Check if two top-level lists have the same length
# 2. Check if each pair of lower-level lists have the same length
# 3. Check if each pair of lower-level lists have the same keys and values
```


Resulting code:
```python
def check_lists_equal_nested(list_1: list, list_2: list) -> bool:
    """
    Check if two nested lists have the same dictionaries
    :param list_1: list
    :param list_2: list
    :return: bool
    """
    # 1. Check if two top-level lists have the same length
    if len(list_1) != len(list_2):
        return False

    # 2. Check if each pair of lower-level lists have the same length
    for i in range(len(list_1)):
        if len(list_1[i]) != len(list_2[i]):
            return False

    # 3. Check if each pair of lower-level lists have the same keys and values
    for i in range(len(list_1)):
        for j in range(len(list_1[i])):
            if list_1[i][j] != list_2[i][j]:
                return False

    return True
```
 ![img](../images/copilot/copilot_1.gif)

## More complex cases - write pseudocode

For functions with complex business logic **divide them into multiple smaller functions**. Purpose of smaller function is easier to describe with just function name or the comment/docstring. This is well known rule (at least from ancient Greeks) allowing to break big problem into smaller that are much easier to address.

> **Divide et Impera!**
>
> *Divide and conquer!* : in politics and sociology, it is *a strategy of gaining and maintaining power by breaking up larger concentrations of power into pieces that individually have less power than the one implementing the strategy.* [wikipedia](https://en.wikipedia.org/wiki/Divide_and_rule)

This rule also works when applied to using GitHub Copilot, I will not go into details since the method is pretty obvious and if not one can easily find multiple texts on applying "Divide and conquer" applications to software engineering.



### My impressions after using Copilot

I have started using Copilot in November 2021. When I had copilot plugin enabled I put more attention to use meaningful function names expecting the reward in form of auto-suggested code that will fit my needs.

I found Copilot great for using python for automation tasks - many simple functions that somebody else for sure has written someday, but it is too expensive to search e.g. GitHub snippet or code. Copilot comes in handy as replacement of gists of basic functions for manipulating text, files, etc.



**Credits:**

warp speed image comes from [here](https://videohive.net/item/warp-speed-effect-v10/47100)
