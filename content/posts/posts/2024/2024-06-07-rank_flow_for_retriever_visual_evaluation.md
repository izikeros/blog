---
Title: RankFlow plot for retriever visual evaluation
Slug: rankflow-plot-for-retriever-visual-evaluation
Date: 2024-07-08
Modified: 2024-07-08
Start: 2024-06-07
tags:
  - retriever
  - rag
  - visuallization
  - rag-evaluation
  - logging
  - struct-log
  - rankflow
  - observability
  - callback
Category: Machine Learning
Image: /images/head/rankflow_plot_head.jpg
banner: /images/head/rankflow_plot_head.jpg
Summary: RAG systems depend on high-quality retrieval to surface relevant information. Analyzing how document rankings evolve through multiple re-ranking steps is complex. This article explores ways to collect ranking data and visualize rank changes to optimize retriever effectiveness.
summary2: Retrieval-Augmented Generation systems rely heavily on effective retrieval. Tracking rank changes across multiple re-ranking stages is crucial but challenging. Visual analysis tools like rankflow charts can help AI professionals gain rapid insights into retriever performance.
summary3: The retriever is a critical component in RAG systems. Monitoring how document ranks shift across re-ranking phases provides valuable performance insights. We'll examine methods for tracking rank data and creating visual representations to streamline retriever analysis.
summary4: Effective retrieval is the cornerstone of RAG system performance. Tracing document rank changes through multiple re-ranking stages can be daunting. This piece look into techniques for gathering ranking data and generating visualizations to enhance retriever analysis.
summary5: 1. RAG systems live and die by the quality of their retrieval. Understanding rank evolution across re-ranking steps is key but often difficult. We'll explore approaches for capturing rank data and creating visual tools to accelerate retriever optimization.
prompt:
status: published
---


<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [TLDR](#tldr)
- [Introduction and problem statement](#introduction-and-problem-statement)
- [Inspiration - Rank flow visualization](#inspiration---rank-flow-visualization)
- [Tracking the rank changes in your RAG](#tracking-the-rank-changes-in-your-rag)
  - [Rank tracking using the structured logs](#rank-tracking-using-the-structured-logs)
  - [How to track with struct logs?](#how-to-track-with-struct-logs)
  - [Rank tracking using callbacks](#rank-tracking-using-callbacks)
  - [How to track retriever data with callbacks?](#how-to-track-retriever-data-with-callbacks)
- [Visualization](#visualization)
- [References](#references)

<!-- /MarkdownTOC -->

## TLDR

This article discusses the importance of tracking and visualizing rank changes in Retrieval-Augmented Generation (RAG) systems. It introduces the concept of rank flow visualization, which helps analyze how document rankings evolve through different stages of retrieval and re-ranking. The article outlines methods for collecting rank data using structured logging and callbacks, and presents a Python library called 'rankflow' for creating visual representations of these rank changes. This visualization technique enables AI professionals to quickly identify patterns and optimize their RAG systems, ultimately improving the quality of information retrieval and generation.
## Introduction and problem statement

Retrieval-Augmented Generation (RAG) systems are composed of two primary components: the **retriever** and the **answer generator**. The overall efficacy of RAG is largely contingent on the quality of the retriever, making it a critical area for optimization and analysis.

Advanced retrieval mechanisms often process numerous document fragments or nodes, which are initially ranked based on relevance. To enhance result quality, these nodes undergo **multiple re-ranking phases**, each aimed at surfacing the most pertinent information.

The re-ranking process can involve a variety of sophisticated techniques, including cross-encoders, bespoke re-ranking algorithms, and boosting systems. These methods serve to refine the rank of search results originating from diverse sources, such as traditional text search algorithms (e.g., BM25) and semantic search based on textual embeddings.

**Tracking the evolving ranks of these document nodes** across multiple processing stages within the retriever can be a complex and time-consuming endeavor. However, leveraging the human brain's innate capacity for visual information processing offers a solution. By employing appropriate visualization techniques, we can significantly streamline the analysis of node rank fluctuations throughout the various retriever stages.

This is where tools like rankflow chart (called also bump chart) come into play, offering a **visual representation of rank changes** that allows for rapid comprehension and insights into the retriever's performance. Such visualizations enable AI professionals to efficiently identify patterns, anomalies, and opportunities for optimization in their RAG systems, ultimately leading to more effective and reliable information retrieval.

In this article we focus on two aspects of visual analysis of rank changes: collecting data in retriever and generating graphical visualization like this:

![RankFlow Plot](/images/rankflow/rankflow_plot_full.jpg)

***Figure 1:** RankFlow chart illustrating rank changes in four steps of re-ranking. You can track the given node's rank history visually. For example, Document 4, after hybrid search, initially had a rank of 4. Then, after the Cross-encoder surfaced, it was re-ranked to 1. The Graph re-ranker subsequently placed it at rank 6, and finally, the Booster changed its rank to 0.*

## Inspiration - Rank flow visualization

When we started searching information about the tool that could help us to visualize how the ranks are changing, we found [RankFlow](https://labs.polsys.net/tools/rankflow/) that can do, more or less, the visualization type we were looking for.

<svg height="300" version="1.1" width="630" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="overflow: hidden; position: relative; top: -0.0546875px;"><path fill="url('#4130-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M433.5,122Q401.5,122,369.74,206T305.5,290L305.5,239Q337.5,239,369.26,155T433.5,71L433.5,122" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4120-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M293.5,290Q261.5,290,229.5,290T165.5,290L165.5,239Q197.5,239,229.5,239T293.5,239L293.5,290" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4110-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M153.5,290Q121.5,290,89.5,290T25.5,290L25.5,239Q57.5,239,89.5,239T153.5,239L153.5,290" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4100-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M433.5,290Q401.5,290,369.18,178T305.5,66L305.5,15Q337.5,15,369.82,127T433.5,239L433.5,290" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4090-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M293.5,66Q261.5,66,229.5,66T165.5,66L165.5,15Q197.5,15,229.5,15T293.5,15L293.5,66" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4080-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M153.5,66Q121.5,66,89.74,150T25.5,234L25.5,183Q57.5,183,89.26,99T153.5,15L153.5,66" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4070-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M433.5,66Q401.5,66,369.74,150T305.5,234L305.5,183Q337.5,183,369.26,99T433.5,15L433.5,66" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4060-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M293.5,234Q261.5,234,229.5,234T165.5,234L165.5,183Q197.5,183,229.5,183T293.5,183L293.5,234" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4050-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M153.5,234Q121.5,234,89.42,206T25.5,178L25.5,127Q57.5,127,89.58,155T153.5,183L153.5,234" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4040-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M433.5,234Q401.5,234,369.42,206T305.5,178L305.5,127Q337.5,127,369.58,155T433.5,183L433.5,234" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4030-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M293.5,178Q261.5,178,229.5,178T165.5,178L165.5,127Q197.5,127,229.5,127T293.5,127L293.5,178" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4020-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M153.5,178Q121.5,178,89.42,150T25.5,122L25.5,71Q57.5,71,89.58,99T153.5,127L153.5,178" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4010-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M433.5,178Q401.5,178,369.42,150T305.5,122L305.5,71Q337.5,71,369.58,99T433.5,127L433.5,178" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#4000-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M293.5,122Q261.5,122,229.5,122T165.5,122L165.5,71Q197.5,71,229.5,71T293.5,71L293.5,122" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><path fill="url('#3990-rgb_200_0_55_-rgb_200_0_55_')" stroke="#ffffff" d="M153.5,122Q121.5,122,89.42,94T25.5,66L25.5,15Q57.5,15,89.58,43T153.5,71L153.5,122" stroke-width="1px" opacity="1" fill-opacity="1" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0.35; fill-opacity: 1;"></path><desc style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Created with Raphaël 2.1.2</desc><defs style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><linearGradient id="3990-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4000-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4010-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4020-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4030-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4040-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4050-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4060-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4070-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4080-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4090-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4100-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4110-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4120-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient><linearGradient id="4130-rgb_200_0_55_-rgb_200_0_55_" x1="0" y1="0" x2="1" y2="0" gradientTransform="matrix(1,0,0,1,0,0)" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><stop offset="0%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop><stop offset="100%" stop-color="#c80037" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></stop></linearGradient></defs><path fill="none" stroke="#000000" d="M8.5,300.5L8.5,0.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><text x="3" y="291" text-anchor="end" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: end; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">0</tspan></text><text x="3" y="20" text-anchor="end" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: end; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">5</tspan></text><text x="13" y="5" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Step_1</tspan></text><rect x="13.5" y="15.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="13.5" y="71.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="13.5" y="127.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="13.5" y="183.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="13.5" y="239.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="153" y="5" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Step_2</tspan></text><rect x="153.5" y="15.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="153.5" y="71.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="153.5" y="127.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="153.5" y="183.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="153.5" y="239.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="293" y="5" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Step_3</tspan></text><rect x="293.5" y="15.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="293.5" y="71.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="293.5" y="127.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="293.5" y="183.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="293.5" y="239.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="433" y="5" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Step_4</tspan></text><rect x="433.5" y="15.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="433.5" y="71.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="433.5" y="127.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="433.5" y="183.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="433.5" y="239.5" width="12" height="51" rx="0" ry="0" fill="#c80037" stroke="#000000" stroke-width="1px" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="27.5" y="41" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_1 (1)</tspan></text><text x="167.5" y="97" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_1 (1)</tspan></text><text x="307.5" y="97" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_1 (1)</tspan></text><text x="447.5" y="153" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_1 (1)</tspan></text><text x="27.5" y="97" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_12_3 (1)</tspan></text><text x="167.5" y="153" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_12_3 (1)</tspan></text><text x="307.5" y="153" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_12_3 (1)</tspan></text><text x="447.5" y="209" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_12_3 (1)</tspan></text><text x="27.5" y="153" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_2 (1)</tspan></text><text x="167.5" y="209" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_2 (1)</tspan></text><text x="307.5" y="209" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_2 (1)</tspan></text><text x="447.5" y="41" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_2 (1)</tspan></text><text x="27.5" y="209" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_3 (1)</tspan></text><text x="167.5" y="41" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_3 (1)</tspan></text><text x="307.5" y="41" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_3 (1)</tspan></text><text x="447.5" y="265" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_1_3 (1)</tspan></text><text x="27.5" y="265" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_1 (1)</tspan></text><text x="167.5" y="265" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_1 (1)</tspan></text><text x="307.5" y="265" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_1 (1)</tspan></text><text x="447.5" y="97" text-anchor="start" font-family="&quot;Arial&quot;" font-size="10px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: Arial; font-size: 10px;"><tspan dy="3.44775390625" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">doc_2_1 (1)</tspan></text></svg> |

You can create the Excel table that reflect rank of the documents on each step. Note that the RankFlow tool supports also column with values that is responsible for the width of the "ribbon". You can use it to e.g. visualize importance of given node, or how many information from this node was finally used in the generated answer (if you have this type of information at hand).

| Step_1   | val_1 | Step_2   | val_2 | Step_3   | val_3 | Step_4   | val_4 |
| -------- | ----- | -------- | ----- | -------- | ----- | -------- | ----- |
| doc_1_1  | 1     | doc_1_3  | 1     | doc_1_3  | 1     | doc_2_2  | 1     |
| doc_12_3 | 1     | doc_1_1  | 1     | doc_1_1  | 1     | doc_2_1  | 1     |
| doc_2_2  | 1     | doc_12_3 | 1     | doc_12_3 | 1     | doc_1_1  | 1     |
| doc_1_3  | 1     | doc_2_2  | 1     | doc_2_2  | 1     | doc_12_3 | 1     |
| doc_2_1  | 1     | doc_2_1  | 1     | doc_2_1  | 1     | doc_1_3  | 1     |

This tool was an appetiser to have something similar implemented in Python. Before going to visualization, let's spent some time on how to collect data required for this visual analysis.

## Tracking the rank changes in your RAG

This is a separate topic - depending on the architecture of your retriever. I envision two main approaches:

- using structured logging
- using callbacks
- using dedicated monitoring/[[2024-02-22-llm_observability_platforms|observability tools]]

Here, we will discuss only first two since they are pretty while skipping the specific observability tools.

### Rank tracking using the structured logs

> **What are the struct logs?**
Structured logs are a standardized format for logging data where information is organized into consistent, machine-readable fields rather than free-form text. **They typically use formats like JSON or key-value pairs**, making it easier to parse, search, and analyze log data programmatically. The benefits of using structured logs include improved log consistency, easier data extraction and analysis, better integration with log management tools, and enhanced ability to generate insights and troubleshoot issues in complex systems.

### How to track with struct logs?

[Struct log]() have the advantage over non-structured log that you can easily, and with more confidentiality, extract data from it without using sophisticated log parsers. In Python, you can use loguru to drop the rank information to the separate log sink after each step that involves some form of reranking and trace e.g. node (chunk) id, new rank, and "label" for the reranking step. In this way you will get a jsonlines log file with all the data you need to create visualization. You can read more about how to use struct logs with loguru in [loguru docs]() and [this]() article.

### Rank tracking using callbacks
>
> **What are the callbacks?**
Callbacks in programming are functions passed as arguments to other functions, which are then executed at specific points during the execution of the containing function. In the context of machine learning and deep learning frameworks, callbacks are often used to track and log various metrics, execute custom actions, or modify behavior during training or inference.

### How to track retriever data with callbacks?

Here is an example how you can use callbacks to track re-ranking info in dummy implementation of the retriever with some re-ranking steps.

```python
import json
from typing import List, Dict, Callable

class Document:
    def __init__(self, id: str, content: str, score: float = 0.0):
        self.id = id
        self.content = content
        self.score = score

class RankingTracker:
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.rankings = []

    def log_ranking(self, step: str, documents: List[Document]):
        ranking = [{"id": doc.id, "score": doc.score} for doc in documents]
        self.rankings.append({"step": step, "ranking": ranking})

    def flush(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.rankings, f, indent=2)

class Retriever:
    def get_relevant_documents(self, query: str) -> List[Document]:
        # Simulated retrieval
        return [
            Document("1", "Content 1", 0.8),
            Document("2", "Content 2", 0.7),
            Document("3", "Content 3", 0.6),
        ]

def cross_encoder_rerank(query: str, documents: List[Document]) -> List[Document]:
    # Simulated cross-encoder re-ranking
    for doc in documents:
        doc.score += 0.1  # Simulate score adjustment
    return sorted(documents, key=lambda x: x.score, reverse=True)

def custom_rerank(documents: List[Document]) -> List[Document]:
    # Simulated custom re-ranking
    for doc in documents:
        doc.score *= 1.2  # Simulate score adjustment
    return sorted(documents, key=lambda x: x.score, reverse=True)

def rag_retrieval(query: str, retriever: Retriever,
                  rerankers: List[Callable],
                  tracker: RankingTracker) -> List[Document]:
    # Initial retrieval
    docs = retriever.get_relevant_documents(query)
    tracker.log_ranking("initial_retrieval", docs)

    # Apply each re-ranker
    for i, reranker in enumerate(rerankers):
        docs = reranker(query, docs) if 'query' in reranker.__code__.co_varnames else reranker(docs)
        tracker.log_ranking(f"rerank_step_{i+1}", docs)

    return docs
```

In this code above:

1. We define a simple `Document` class to represent our documents.
2. The `RankingTracker` class is responsible for logging rankings at each step and writing them to a file.
3. We have a basic `Retriever` class that simulates initial document retrieval.
4. Two re-ranking functions are defined: `cross_encoder_rerank` and `custom_rerank`. These simulate different re-ranking strategies.
5. The `rag_retrieval` function orchestrates the entire process:
    - It first retrieves documents using the retriever.
    - Then it applies each re-ranker in sequence.
    - **After each step, it logs the current ranking using the tracker**.

Here is the usage, with steps:

- Initialize the tracker and retriever.
- Call `rag_retrieval` with the query, retriever, list of re-rankers, and tracker.
- Print the final rankings.
- Flush the tracked rankings to a file.

```python
# Usage
if __name__ == "__main__":
    tracker = RankingTracker("ranking_results.json")
    retriever = Retriever()

    query = "What is the capital of France?"

    final_docs = rag_retrieval(
        query,
        retriever,
        [cross_encoder_rerank, custom_rerank],
        tracker
    )

    # Print final rankings
    print("Final document rankings:")
    for doc in final_docs:
        print(f"ID: {doc.id}, Score: {doc.score}")

    # Save all rankings to file
    tracker.flush()
```

## Visualization

For the visualization part you can use small Python library [rankflow](https://pypi.org/project/rankflow/) (disclaimer: I'm the author) that is able to produce this type of visualization:
![RankFlow Plot](/images/rankflow/rankflow_plot_full.jpg)

First, install it with pip:

```sh
pip install rankflow
```

It can accept various input data formats, one, convenient for data scientists is pandas data frame.

```python
import pandas as pd
import matplotlib.pyplot as plt
from rankflow import RankFlow

data = {"Doc 1": [2, 1, 3, 2], "Doc 2": [1, 2, 1, 3], "Doc 3": [3, 3, 2, 1]}
df = pd.DataFrame(data, index=["Step_1", "Step_2", "Step_3", "Step_4"])
```

When the DataFrame is ready, then it is time to create RankFlow object and call `plot()` method.

```python
rf = RankFlow(df=df)
rf.plot()

# save the plot to png
plt.savefig("rankflow.png")

plt.show()
```

If you found this library useful, please star the [repo](https://github.com/izikeros/rankflow).

With plotting options you have also some alternatives that you can use or take inspiration to create you own, customized rankflow plot/bump chart. See the references for alternatives.

## References

- [How To Plot Bump Chart In R Finnstats - vrogue.co](https://www.vrogue.co/post/how-to-plot-bump-chart-in-r-finnstats)
- [GitHub - kartikay-bagla/bump-plot-python](https://github.com/kartikay-bagla/bump-plot-python)
- [Bumpy Charts - mplsoccer 1.2.4 documentation](https://mplsoccer.readthedocs.io/en/latest/gallery/bumpy_charts/plot_bumpy.html#sphx-glr-gallery-bumpy-charts-plot-bumpy-py)
- [Jupyter Notebook Viewer](https://nbviewer.org/gist/pascal-schetelat/8382651)
