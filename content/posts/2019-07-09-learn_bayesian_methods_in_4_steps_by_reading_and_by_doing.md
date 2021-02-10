---
title: Learn Bayesian methods in 4 steps - by reading and by doing
started: 2019-07-04
date: '2019-07-09'
tags: machine learning, statistics, probability, howto
Category: Howto
image: /images/learn_bayes/probab_distrib.png
status: Published
Summary: This post propose 4-steps path for learning Byesian methods. First step is goint through the book: "Bayesian methods for hackers", second, use complementary books for probability and statistics, third, read How to become a Bayesian in eight easy steps: An annotated reading list", and last, go throught the book full of exercises: "Think Bayes".
---
## Background
When reading this article you probably have some experience with machine learning models. You might have tried RandomForest, XGBoost, etc.. They are easy to use but it is difficult to understand how final predictions where done. This is sometime refereed as predictions out of black box. Of course, there are techniques that might help a bit e.g. extracting feature importance from the trained models. 

Bayesian methods are a great helper for understanding how actually reasoning was done. These methods provides probabilistic models that can describe the process that produced data we want to process. Besides accurate predictions we often need understanding of what is important in the process. Through understanding gain confidence in used models. We need the convenience when moving with machine learning from toy projects to real business applications. Bayesian can offer such understanding and convenience and that is why these methods are gaining attention.

In this blog post I will present 4 steps for Bayesian methods mastery. The rough estimate is that you will need to dedicate around 100 hours to complete this 4-steps path.

## 1. "Bayesian methods for hackers"  - free book in form of Jupyter notebooks with interactive content.

<img style="float: lefts;" src="/images/learn_bayes/bmh.jpg" width="25%" height="25%">

First chapter of "Bayesian methods for hackers" (BMH) will  introduce you to Bayesian way of thinking. Understand reducing uncertainty using observations. You will go through first example that is showing statistical modeling of texting rate. The following chapters explain, new techniques in details. New techniques are immediately applied to solving exemplary problems.

For myself, when progressing through the book, I felt that I need to refresh my statistical knowledge and started looking for the proper book. The math required to use these methods is already provided in the book. Yet, I needed better understanding of different random variable distributions.  This is something that I already learned years ago on university courses but i needed an refresher.

## 2. Probability and Statistics books that will help you learn/refresh math to build solid foundation.
My choice for complementary probability and statistics books was twofold:

* For light introduction, on college level: [Open Intro to statistics 4th edition](https://leanpub.com/openintro-statistics)  by D. Diez, M. Cetinkaya-Rundel, and Ch. Barr. According to my needs, Chapter 4 "Distributions of random variables" was pleasant to read.

* For deep dive: [Probability Theory: The Logic of Science: Principles and Elementary Applications"](http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf) by E. T. Jaynes. This book itself could be a subject of learning for hundreds of hours, but reading separate chapters or sections still should be fine.

## 3. "How to become a Bayesian in eight easy steps: An annotated reading list".
["How to become a Bayesian in eight easy steps: An annotated reading list"](https://psyarxiv.com/ph6sw) by Etz, Alexander, et al., is a paper, not target on Computer Scientists. Actually, it  originates from field of psychology but is written in domain-agnostic style, so reader from any discipline can enjoy reading this. The paper has survey style, and use classification of the covered papers in two dimensions: of difficulty (from easy to hard), and focus (from theoretical to practical). See Figure below, borrowed from the paper.

<img src="/images/learn_bayes/readinglist.png" width="45%" height="45%">

The main paper and references are rather light reading and I found it useful in building context for diving into  Bayesian analysis.

## 4. Exercises to develop Bayesian thinking: "Think Bayes" by Allen Downey.

<img style="float: left;" src="/images/learn_bayes/think_bayes_1.jpg" width="25%" height="25%">

Another great book to learn Bayesian thinking. It is divided to smaller units than BMH  what makes it easier to digest for readers that are quickly loosing attention when reading scientific stuff. When compared to BMH, it has much more examples. Crashing large number of cases is to me very good approach for training Bayesian intuition and learning methods.

Will you give a try to Bayesian methods? If you have proposal of alternative learning path - please share it in the comments.