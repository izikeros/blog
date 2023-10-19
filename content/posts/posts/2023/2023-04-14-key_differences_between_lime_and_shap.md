---
Category: Explainable AI
Date: '2023-04-14'
Image: /images/head/shap_lime_differences.jpg
Modified: '2023-04-14'
Slug: explaining-ai-the-key-differences-between-lime-and-shap-methods
Start: '2023-04-14'
Status: published
Summary: When it comes to explainable AI, LIME and SHAP are two popular methods for providing insights into the decisions made by machine learning models. What are the key differences between these methods? In this article, we will help you understand which method may be best for your specific use case.
Tags: xai, explainable-ai, lime, shap
Title: Explaining AI - The Key Differences Between LIME and SHAP Methods
banner: "/images/head/shap_lime_differences.jpg"
prompt: What are the key differences between LIME and SHAP
---

LIME and SHAP are both popular methods for explainable AI (XAI), but they differ in several key ways.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Model-agnostic vs model-specific](#model-agnostic-vs-model-specific)
- [Local vs global explanations](#local-vs-global-explanations)
- [Kernel-based vs game-theoretic approach](#kernel-based-vs-game-theoretic-approach)
- [Interpretability vs accuracy trade-off](#interpretability-vs-accuracy-trade-off)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="model-agnostic-vs-model-specific"></a>
## Model-agnostic vs model-specific

One of the main differences between LIME and SHAP is that LIME is model-agnostic, meaning it can be used to explain the decisions of any machine learning model, regardless of the algorithm used. In contrast, SHAP is a model-specific method that is designed to explain the decisions of tree-based models, such as decision trees, random forests, and gradient boosting machines.

<a id="local-vs-global-explanations"></a>
## Local vs global explanations

Another key difference between LIME and SHAP is the type of explanation they provide. LIME generates local explanations, meaning it explains the decision of a complex model for a specific instance or observation. In contrast, SHAP provides global explanations, meaning it explains the overall behavior of the model across all instances.

<a id="kernel-based-vs-game-theoretic-approach"></a>
## Kernel-based vs game-theoretic approach

LIME uses a kernel-based approach to explain the decisions of a complex model. It creates a local, interpretable model that approximates the behavior of the complex model around a specific instance. In contrast, SHAP uses a game-theoretic approach to explain the contribution of each feature to the final prediction. It assigns a "credit" score to each feature based on how much it contributes to the prediction.

<a id="interpretability-vs-accuracy-trade-off"></a>
## Interpretability vs accuracy trade-off

Finally, LIME and SHAP differ in their approach to the interpretability vs accuracy trade-off. LIME sacrifices some accuracy in order to provide more interpretable explanations. It creates a simpler model that may not be as accurate as the complex model, but is easier to understand. In contrast, SHAP aims to provide accurate explanations without sacrificing model accuracy. It uses a more sophisticated approach to explain the contribution of each feature, but this can be more difficult to understand for non-experts.

<a id="conclusion"></a>
## Conclusion

LIME and SHAP are both useful methods for XAI, but they differ in their approach to explaining the decisions of complex machine learning models. LIME is model-agnostic and provides local, interpretable explanations, while SHAP is model-specific and provides global explanations using a game-theoretic approach. The choice between LIME and SHAP depends on the specific needs of the user and the characteristics of the machine learning model being explained.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*