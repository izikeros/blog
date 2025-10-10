---
Title: MLOps Roadmap
Category: note
Date: 2023-01-14
Modified: 2023-07-12
Slug: mlops-roadmap
Status: published
tags:
  - mlops
  - learning
  - data-management
  - reproducibility
  - pipeline
  - model-life-cycle
  - model-tuning
  - canary-release
  - jenkins
  - ansible
---
Roadmap to become MLOps. The 6 points, ordered plan on things to learn.

**1.  Data Management**
Understand the data pipeline, data governance, and data quality.

**2.  Experimentation**
Learn about experimentation frameworks, version control, and reproducibility.

**3.  Model Development**
Understand model development life cycle, model training, and tuning.

**4.  Model Deployment**
Learn about model deployment, A/B testing, and canary releases.

**5.  Model Monitoring**
Understand how to monitor models in production, and how to detect and diagnose issues.

**6.  Automation**
Learn about automation tools, such as Jenkins and Ansible, to automate ML workflows.

<script type="module"> import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs'; mermaid.initialize({ startOnLoad: true }); </script>

<pre class="mermaid">
graph TD;
    Data_Management-->Experimentation;
    Experimentation-->Model_Development;
    Model_Development-->Model_Deployment;
    Model_Deployment-->Model_Monitoring;
    Model_Monitoring-->Automation;
</pre>

up::[[mlops]]
