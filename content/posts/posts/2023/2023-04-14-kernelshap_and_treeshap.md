---
Category: Responsible AI
Date: 2023-04-14
Image: /images/head/treeshap_kernelshap.jpg
Modified: 2023-11-05
Slug: kernelshap-treeshap-two-most-popular-variations-of-the-shap-method
Start: 2023-04-14
Status: published
Summary: Making sense of AI's inner workings with KernelShap and TreeShap the powerfull tools for responsible AI.
Tags:
  - shap
  - xai
  - explainable-ai
Title: KernelShap and TreeShap - Two Most Popular Variations of the SHAP Method
banner: /images/head/treeshap_kernelshap.jpg
prompt:
---
## TLDR

The **original SHAP does not scale well** with high dimensions data due to its exponential complexity associated with Shapley value calculations. KernelSHAP and TreeSHAP are two specific implementations of the SHAP method, developed to address the shortcomings of the original framework and to optimize it for different types of machine learning models, but they achieve this in different ways.
**KernelSHAP** uses a model-agnostic method to interpret the impact of features in a model. This means it can provide explanations **for any model** but **at the cost of computational efficiency**, making it **less suitable for complex**, high-dimensional situations or when real-time explanations are needed. In contrast, **TreeSHAP** is designed specifically **for tree-based models** (like decision tree and random forests, or boosting machines). It is **computationally efficient**, exploits the tree structure for **faster calculations**, and thus, can handle **more complex scenarios**. Moreover, TreeSHAP guarantees consistency - a helpful property for feature attribution methods to ensure that if a model relies more on a feature, the attributed importance of that feature should not decrease. However, it can't be used for non-tree models.

## Introduction
  
Responsible AI is an approach to artificial intelligence that ensures fairness, transparency, and accountability in the development, deployment, and management of AI systems. In the era of increasing reliance on AI-driven decision-making, understanding and explaining the predictions made by these models is essential. The interpretability of AI models helps build trust, enables better decision-making, and allows us to mitigate biases.
  
Two popular methods for explaining AI models are KernelShap and TreeShap. These techniques are part of the SHAP (SHapley Additive exPlanations) family, which is based on cooperative game theory. In this blog post, we will look into the details of KernelShap and TreeShap, exploring their underlying principles, advantages, and use cases.

> **SHAP (SHapley Additive exPlanations)** is a game theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from game theory and their related extensions (see [papers](https://github.com/shap/shap#citations) for details and citations).
> *(from [SHAP documentation](https://shap.readthedocs.io/en/latest/index.html))*

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [TLDR](#tldr)
- [Introduction](#introduction)
- [KernelShap](#kernelshap)
 	- [Steps](#steps)
 	- [KernelShap advantages and limitations](#kernelshap-advantages-and-limitations)
- [TreeShap](#treeshap)
 	- [Steps](#steps-1)
 	- [TreeShap advantages and limitations](#treeshap-advantages-and-limitations)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="kernelshap"></a>

## KernelShap
  
KernelShap is a model-agnostic explanation method that provides interpretable explanations for any black-box model. It uses the concept of Shapley values from cooperative game theory to attribute feature importance to individual features in the context of a specific prediction.

The Shapley value for feature $i$ in a model $f$ can be calculated using the following formula:
  
$$ϕ_i(f) = \sum_{S ⊆ N \setminus {i}} \frac{|S|!(|N|-|S|-1)!}{|N|!} [f(S ∪ {i}) - f(S)]$$
  
Here, $S$ is a subset of features excluding $i$, and $N$ is the total number of features. The term $|S|!$ represents the factorial of the number of features in subset $S$, while $|N|-|S|-1!$ represents the factorial of the remaining features outside of the subset. The denominator $|N|!$ is the factorial of the total number of features.

Shapley values, in the context of AI, are used to distribute the contribution of each feature to the final prediction. It ensures that the contribution of each feature is fairly allocated in a way that is efficient, symmetric, and additive.
  
KernelShap approximates the Shapley values by solving a weighted linear regression problem. It samples instances from the feature space and estimates the Shapley values using the Lasso regression model. The Lasso model is a linear model with an L1 penalty term, which helps in feature selection and makes the explanation sparse.

Lasso (Least Absolute Shrinkage and Selection Operator) regression is a linear regression technique that includes an L1 penalty term to shrink the coefficients of less important features towards zero. This allows for both regularization and feature selection, resulting in a more interpretable and parsimonious model.
  
The equation for Lasso regression is given by:
  
$$L(\beta) = \sum_{i=1}^{n}(y_i - X_i\beta)^2 + \lambda\sum_{j=1}^{p}|\beta_j|$$
In this equation:

- $L(\beta)$ represents the objective function to be minimized,
- $y_i$ is the actual response (outcome) for the $i^{th}$ observation,
- $X_i$ is the feature vector for the $i^{th}$ observation,
- $\beta$ is the vector of coefficients to be estimated,
- $n$ is the total number of observations,
- $p$ is the total number of features,
- $\lambda$ is a non-negative regularization parameter, and
- $|\beta_j|$ is the absolute value of the $j^{th}$ coefficient.

The first term, $\sum_{i=1}{n}(y_i - X_i\beta)2$, is the sum of squared residuals, which represents the difference between the actual and predicted responses. Minimizing this term alone would result in an ordinary least squares regression.

The second term, $\lambda\sum_{j=1}^{p}|\beta_j|$, is the L1 penalty term that adds the absolute values of the coefficients multiplied by the regularization parameter $\lambda$. By increasing $\lambda$, the penalty term forces some coefficients to be exactly zero, effectively selecting a subset of features for the final model. The optimal value of $\lambda$ is usually determined through cross-validation.

<a id="steps"></a>

### Steps

The KernelShap algorithm involves the following steps:

1. Generate a dataset of binary-masked instances by randomly selecting feature combinations.
2. Compute the output of the black-box model for each instance.
3. Fit a weighted linear regression model on the generated dataset, where the weights are determined by the similarity between the instance and the instance of interest.
4. The coefficients of the linear regression model represent the approximate Shapley values.

<a id="kernelshap-advantages-and-limitations"></a>

### KernelShap advantages and limitations

KernelShap has several **advantages**:

- It can be applied to any black-box model, regardless of its architecture or training algorithm.
- It provides a unified measure of feature importance that is consistent across different models.
- It takes into account the interactions between features.

However, KernelShap also has some **limitations**:

- It can be computationally expensive, especially for high-dimensional data or complex models.
- It requires a large number of samples to provide accurate estimates of the Shapley values.

<a id="treeshap"></a>

## TreeShap

TreeShap is a model-specific explanation method designed for tree-based models, such as decision trees, random forests, and gradient boosting machines. Like KernelShap, it is based on Shapley values, but it exploits the structure of tree-based models to compute the values efficiently.

TreeShap **computes the exact Shapley values for each feature by recursively traversing the decision tree**, attributing contributions to each feature as it moves down the tree. It uses a dynamic programming approach to avoid redundant calculations and reduce the computational complexity.

<a id="steps-1"></a>

### Steps

The TreeShap algorithm involves the following steps:

1. Traverse the tree from the root to the leaf nodes, recording the decision path for the instance of interest.
2. Attribute contributions to each feature encountered along the path, taking into account the number of possible feature combinations and the probability of each combination.
3. Repeat the process for all trees in the ensemble, if applicable.
4. Average the contributions across all trees to obtain the final Shapley values.

<a id="treeshap-advantages-and-limitations"></a>

### TreeShap advantages and limitations

TreeShap has several advantages:

- It computes the exact Shapley values without the need for sampling or approximations.
- It is computationally efficient due to its dynamic programming approach.
- It is specifically designed for tree-based models, which are widely used in practice.

However, TreeShap is limited to tree-based models and cannot be applied to other types of models, such as deep learning or support vector machines.
<a id="conclusion"></a>

## Conclusion
  
KernelShap and TreeShap are powerful methods for explaining AI models in the context of responsible AI. Both techniques leverage the concept of Shapley values to provide interpretable and fair attributions of feature importance. While KernelShap is a model-agnostic approach that can be applied to any black-box model, TreeShap is tailored for tree-based models and offers exact Shapley values with computational efficiency.
  
Understanding and implementing these methods is crucial for AI practitioners who aim to build transparent, accountable, and trustworthy AI systems. By providing insights into the inner workings of AI models, KernelShap and TreeShap enable developers to identify potential biases, improve the decision-making process, and ultimately foster trust in AI-driven technologies.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*

**Edits:**

- 2023-11-05: Added TLDR section, minor edits
