---
Category: note
Date: '2023-01-17'
Modified: '2023-07-12'
Prompt: "Give markdown article with hyperlinks on 3 Pieces of Popular MLOps Advice to Ignore \u2014 and What to Do Instead. In the article discuss three advices for mlops that are false helpers or are not the best option nowadays. Propose alternative solution to each of these three."
Slug: pieces-of-popular mlops-advice-to-ignore-what-to-do-instead
Status: published
Summary: Discover 3 common MLOps advice to avoid and learn better alternatives to improve your machine learning operations. Learn to use modular, polyglot and multi-cloud approach.
Tags: mlops
Title: "3 Pieces of Popular MLOps Advice to Ignore \u2014 And What to Do Instead"
prompt2: the three pieces of the advice boils down to diversification. Can you give me other (other that diversification) three examples of popular yet harmful mlops advices?
---

As machine learning becomes more prevalent in the enterprise, MLOps (machine learning operations) is becoming an increasingly important field. However, not all advice out there is equally valuable, and some popular recommendations can actually harm your MLOps efforts. In this article, we'll discuss three pieces of popular MLOps advice that you should ignore, and what to do instead.

## 1. "Use a monolithic MLOps platform"

One piece of advice that is often given is to use a monolithic MLOps platform to manage all aspects of your machine learning pipeline. These platforms promise to provide a one-stop-shop for everything from data preparation to model deployment, but in reality, they can be inflexible and limit your ability to use the best tools for each specific task.

Instead of using a monolithic platform, consider using a modular approach to your MLOps. This means using a combination of different tools that are best suited for each specific task. For example, you might use a tool like [DVC](https://dvc.org/) for data versioning, [Kubeflow](https://www.kubeflow.org/) for model training and [Seldon](https://www.seldon.io/) for model deployment.

This approach allows you to use the best tools for each task and to easily swap out components as needed. It also makes it easier to maintain and upgrade your system.

## 2. "Use a single language for everything"

Another piece of advice that you may hear is to use a single programming language for all aspects of your MLOps pipeline. This is often given as a way to simplify development and reduce the number of engineers needed on a project.

However, in reality, using a single language can limit your ability to use the best tools for each task. For example, Python is a popular language for data science, but it might not be the best choice for deploying models to production.

Instead of using a single language, consider using a polyglot approach to your MLOps. This means using multiple languages for different tasks. For example, you might use Python for data preparation, Java for model training, and Go for model deployment. This allows you to use the best tools for each task and to leverage the strengths of different languages.

## 3. "Use a single cloud provider"

A third piece of advice that you may hear is to use a single cloud provider for all aspects of your MLOps pipeline. This is often given as a way to simplify management and reduce costs.

However, in reality, using a single cloud provider can limit your ability to take advantage of the best tools and services available. For example, a specific cloud provider might not have the best services for data storage or might have higher costs than other providers.

Instead of using a single cloud provider, consider using a multi-cloud approach to your MLOps. This means using multiple cloud providers for different tasks. For example, you might use AWS for data storage, GCP for model training and Azure for model deployment. This allows you to take advantage of the best tools and services available from each provider and to reduce vendor lock-in.

## Conclusion

While it may be tempting to follow popular MLOps advice, it's important to consider whether these recommendations are actually the best fit for your specific needs. By using a modular, polyglot, and multi-cloud approach, you can ensure that you're using the best tools for each task and building a more flexible, scalable, and cost-effective MLOps pipeline.

up::[[mlops]]
