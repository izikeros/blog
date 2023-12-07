---
Title: Databricks - key concepts
Slug: databricks-key-concepts
Date: 2023-12-04
Modified: 2023-12-04
Status: published
Category: note
tags: databricks, data-science, notebook, jupyter-notebook, dbfs, databricks-workspace, databricks-runtime, databricks-file-system, databricks-clusters, databricks-notebooks, databricks-jobs, databricks-tables
---
up::[[MOC_Databricks]]

<script type="module"> import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs'; mermaid.initialize({ startOnLoad: true }); </script>


<pre class="mermaid">
mindmap
Databricks
    Databricks Workspace
    Databricks Runtime
    Databricks File System (DBFS)
    Databricks Clusters
    Databricks Notebooks
    Databricks Jobs
    Databricks Tables
</pre>

Here are some of the key features and components of Databricks:
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Databricks Workspace](#databricks-workspace)
- [Databricks Runtime](#databricks-runtime)
- [Databricks File System \(DBFS\)](#databricks-file-system-dbfs)
- [Databricks Clusters](#databricks-clusters)
- [Databricks Notebooks](#databricks-notebooks)
- [Databricks Jobs](#databricks-jobs)
- [Databricks Tables](#databricks-tables)

<!-- /MarkdownTOC -->



<a id="databricks-workspace"></a>
## Databricks Workspace
This is the collaborative environment where you can write code, create visualizations, and share your work with others. It supports several languages including Python, SQL, R, and Scala. 
Read more: [Create and manage your Databricks workspaces | Databricks on AWS](https://docs.databricks.com/en/administration-guide/workspace/index.html#what-is-a-workspace)
    
<a id="databricks-runtime"></a>
## Databricks Runtime
This is the set of core components that run on the clusters in Databricks. It includes Apache Spark but also includes other enhancements maintained by Databricks like performance optimizations, security, and integration with other tools like Delta Lake and MLflow.
Read more: [What is Databricks Runtime?](https://www.databricks.com/glossary/what-is-databricks-runtime)

    
<a id="databricks-file-system-dbfs"></a>
## Databricks File System (DBFS)
This is a distributed file system installed on Databricks clusters. It allows you to store data and share it across all nodes in a cluster.
Read more: [What is the Databricks File System (DBFS)?](https://docs.databricks.com/en/dbfs/index.html)

    
<a id="databricks-clusters"></a>
## Databricks Clusters
These are the compute resources that run your code. You can create clusters of different sizes and types depending on your workload.
Read more: [Compute - Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/clusters/)

    
<a id="databricks-notebooks"></a>
## Databricks Notebooks
These are collaborative documents that contain code, visualizations, and text. They're great for exploratory data analysis, data science, and machine learning workflows.
Read more: [Introduction to Databricks notebooks](https://docs.databricks.com/en/notebooks/index.html)


<a id="databricks-jobs"></a>
## Databricks Jobs
These are the tasks or computations you run on Databricks. You can schedule jobs to run periodically, or run them on demand.
Read more: [Create and run Databricks Jobs](https://docs.databricks.com/en/workflows/jobs/create-run-jobs.html)
    
<a id="databricks-tables"></a>
## Databricks Tables
These are the structured data sources that you can query using SQL or data frame APIs in Python, R, and Scala.
Read more: [Delta Live Tables](https://www.databricks.com/product/delta-live-tables)

    