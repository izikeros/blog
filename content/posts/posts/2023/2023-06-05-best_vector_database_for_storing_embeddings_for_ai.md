---
Title: The best vector databases for storing embeddings
Slug: the-best-vector-databases-for-storing-embeddings
Date: 2023-06-05
Modified: 2023-06-05
Start: 2023-06-05
Tags: machine-learning, python, embeddings, vectordb, database, transformers
Category: Machine Learning
Image: /images/head/vectordb.jpg
banner: "/images/head/vectordb.jpg"
Summary: Delve into the World of Vector Databases Fueling NLP's Transformative Journey.
Status: published
prompt: see chatGPT prompts
prompt1: explain what vector databases are, and why there is demand for them when other types of databases exits and they are battlefield tested (like postgres)
---
## Best Vector Databases for Storing Embeddings in NLP

As natural language processing (NLP) continues to advance, the need for efficient storage and retrieval of vector representations, or embeddings, has become paramount. Vector databases are purpose-built databases that excel in storing and querying high-dimensional vector data, such as word embeddings or document representations. This article explores the best vector databases available, their unique features, and the crucial parameters that differentiate them.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [What vector databases are, and why there is demand for them?](#what-vector-databases-are-and-why-there-is-demand-for-them)
	- [Chroma](#chroma)
	- [DeepsetAI](#deepsetai)
	- [Faiss by Facebook](#faiss-by-facebook)
	- [Milvus](#milvus)
	- [pgvector](#pgvector)
	- [Pinecone](#pinecone)
	- [Supabase](#supabase)
	- [Qdrant](#qdrant)
	- [Vespa](#vespa)
	- [Weaviate](#weaviate)
	- [DeepLake](#deeplake)
	- [LANGCHAIN VectorStore](#langchain-vectorstore)
	- [Other Relevant Vector Databases](#other-relevant-vector-databases)
- [Related reading](#related-reading)

<!-- /MarkdownTOC -->

<a id="what-vector-databases-are-and-why-there-is-demand-for-them"></a>
## What vector databases are, and why there is demand for them?

Vector databases are specialized databases designed for efficient storage, retrieval, and manipulation of vector representations, particularly in the context of Natural Language Processing (NLP) and machine learning applications. They are optimized for handling high-dimensional embeddings that represent textual or numerical data in a vectorized format.

While traditional databases like PostgreSQL are versatile and battle-tested, they are not specifically optimized for vector operations. Vector databases, on the other hand, provide a set of features and optimizations tailored to the unique requirements of working with vector embeddings. Here are some reasons why vector databases are in demand despite the existence of other types of databases:

1. **Scalability**: Vector databases are built to handle large-scale datasets and can scale horizontally to accommodate growing data volumes. They distribute the storage and processing of vectors across multiple machines, enabling efficient handling of massive amounts of embedding data.
    
2. **Query Speed**: Vector databases employ advanced indexing structures and search algorithms, such as approximate nearest neighbor (ANN) search, to achieve fast and accurate similarity searches. These optimizations enable rapid retrieval of vectors based on their similarity to a given query vector.
    
3. **Accuracy of Search Results**: Vector databases focus on preserving the accuracy of similarity search results. They leverage techniques like space partitioning, dimensionality reduction, and quantization to ensure that similar vectors are efficiently identified, even in high-dimensional spaces.
    
4. **Flexibility**: Vector databases offer flexibility in terms of supported vector operations and indexing methods. They often provide a range of indexing algorithms, allowing users to choose the one that best suits their specific use case. Additionally, vector databases may support additional functionality like filtering, ranking, and semantic search.
    
5. **Data Persistence and Durability**: Vector databases prioritize data persistence and durability, ensuring that vector embeddings are reliably stored and protected against data loss. They often integrate with existing storage solutions or provide mechanisms for backup and replication.
    
6. **Storage Location**: Vector databases can be deployed either on-premises or in the cloud, providing flexibility in terms of infrastructure choices. Cloud-based vector databases offer the advantage of managed services, offloading the operational overhead of maintaining and scaling the database infrastructure.
    
7. **Direct Library vs. Abstraction**: Vector databases come in two main forms: those that offer a direct library interface for integration into existing systems and those that provide a higher-level abstraction, such as RESTful APIs or query languages. This flexibility allows developers to choose the level of control and integration that best fits their requirements.
    

While traditional databases like PostgreSQL can handle various data types, including vectors, they may lack the specialized optimizations and features provided by vector databases. Vector databases excel in efficiently storing and querying high-dimensional embeddings, enabling faster similarity search and supporting specific vector-related operations. By leveraging these optimizations, vector databases streamline the development and deployment of NLP and machine learning applications.

<a id="chroma"></a>
### Chroma

![github stars shield](https://img.shields.io/github/stars/chroma-core/chroma?logo=github)
![chroma logo](https://user-images.githubusercontent.com/891664/227103090-6624bf7d-9524-4e05-9d2c-c28d5d451481.png)
[Chroma](https://www.trychroma.com/) is an open-source vector database developed by Chroma.ai. It focuses on scalability, providing robust support for storing and querying large-scale embedding datasets efficiently. Chroma offers a distributed architecture with horizontal scalability, enabling it to handle massive volumes of vector data. It leverages Apache Cassandra for high availability and fault tolerance, ensuring data persistence and durability.

One unique aspect of Chroma is its flexible indexing system. It supports multiple indexing strategies, such as approximate nearest neighbors (ANN) algorithms like HNSW and IVFPQ, enabling fast and accurate similarity searches. Chroma also provides comprehensive Python and RESTful APIs, making it easily integratable into NLP pipelines. With its emphasis on scalability and speed, Chroma is an excellent choice for applications that require high-performance vector storage and retrieval.

<a id="deepsetai"></a>
### DeepsetAI Haystack

![github stars shield](https://img.shields.io/github/stars/deepset-ai/haystack?logo=github)

![haystack logo](images/vectordb/haystack.png)
DeepsetAI's [Haystack](https://haystack.deepset.ai/) is another popular vector database designed specifically for NLP applications. It offers a range of features tailored to support end-to-end development of search systems using embeddings. Haystack integrates well with popular transformer models like BERT, allowing users to extract embeddings directly from pre-trained models. It leverages Elasticsearch as its underlying storage engine, providing powerful indexing and querying capabilities.

Haystack stands out with its intuitive query language, which supports complex semantic searches and filtering based on various parameters. Additionally, it offers a modular pipeline architecture for preprocessing, embedding extraction, and querying, making it highly customizable and adaptable to different NLP use cases. With its user-friendly interface and comprehensive functionality, DeepsetAI's Haystack is an excellent choice for developers seeking a flexible and feature-rich vector database for NLP.

<a id="faiss-by-facebook"></a>
### Faiss by Facebook

![github stars shield](https://img.shields.io/github/stars/facebookresearch/faiss?logo=github)

Faiss, developed by Facebook AI Research, is a widely-used vector database renowned for its high-performance similarity search capabilities. It provides a range of indexing methods optimized for efficient retrieval of nearest neighbors, including IVF (Inverted File) and HNSW (Hierarchical Navigable Small World). Faiss also supports GPU acceleration, enabling fast computation on large-scale embeddings.

One of Faiss' notable features is its support for multi-index search, which combines different indexing methods to improve search accuracy and speed. Additionally, Faiss offers a Python interface, making it easy to integrate with existing NLP pipelines and frameworks. With its focus on search performance and versatility, Faiss is a go-to choice for projects demanding fast and accurate similarity search over vast embedding collections.

<a id="milvus"></a>
### Milvus

![github stars shield](https://img.shields.io/github/stars/milvus-io/milvus?logo=github)

Milvus is an open-source vector database developed by Zilliz, designed for efficient storage and retrieval of large-scale embeddings. It provides high scalability and supports distributed deployment across multiple machines, making it suitable for handling massive NLP datasets. Milvus integrates with popular ANN libraries like Faiss, Annoy, and NMSLIB, offering flexible indexing options to achieve high search accuracy.

One key feature of Milvus is its GPU support, leveraging NVIDIA GPUs for accelerated computation. This makes Milvus an excellent choice for deep learning applications that require fast vector search and similarity calculations. Furthermore, Milvus provides a user-friendly WebUI and supports multiple programming languages, simplifying development and deployment processes. With its focus on scalability and GPU acceleration, Milvus is an ideal vector database for large-scale NLP projects.

<a id="pgvector"></a>
### pgvector

![github stars shield](https://img.shields.io/github/stars/ankane/pgvector?logo=github)

pgvector is a vector database built on top of PostgreSQL, a popular open-source relational database. It leverages the powerful indexing capabilities of PostgreSQL's extension system to provide efficient storage and retrieval of vector embeddings. pgvector supports both CPU and GPU inference, enabling high-performance vector operations.

One key advantage of pgvector is its seamless integration with the broader PostgreSQL ecosystem. Users can leverage the rich functionality of PostgreSQL, such as ACID compliance and support for complex queries, while benefiting from vector-specific operations. pgvector provides a PostgreSQL extension that extends the SQL syntax to handle vector operations and offers a Python library for easy integration. With its compatibility with PostgreSQL and efficient vector storage, pgvector is a reliable choice for NLP applications that require a seamless SQL integration.

<a id="pinecone"></a>
### Pinecone

Pinecone is a managed vector database built for handling large-scale embeddings in real-time applications. It focuses on low-latency search and high-throughput indexing, making it suitable for latency-sensitive NLP use cases. Pinecone's cloud-native infrastructure handles indexing, storage, and query serving, allowing developers to focus on building their applications.

Pinecone offers a RESTful API and client libraries for various programming languages, simplifying integration with different NLP frameworks. It supports dynamic indexing, allowing incremental updates to embeddings without rebuilding the entire index. Pinecone also provides advanced features like vector similarity search, filtering, and result ranking. With its emphasis on real-time performance and ease of use, Pinecone is an excellent choice for developers seeking a fully managed vector database for NLP applications.

<a id="supabase"></a>
### Supabase

![github stars shield](https://img.shields.io/github/stars/supabase/supabase?logo=github)

Supabase, known for its open-source data platform, offers a scalable vector storage solution designed for fast and efficient retrieval of embeddings. Supabase leverages PostgreSQL as its underlying storage engine, ensuring data durability and compatibility with standard SQL queries. It provides a range of features such as indexing, querying, and filtering, optimized for vector data.

One distinctive aspect of Supabase is its real-time capabilities, enabled by its integration with PostgREST and PostgreSQL's logical decoding feature. This allows developers to build real-time applications that can react to changes in vector data. Supabase also provides a user-friendly interface and client libraries for various programming languages, making it accessible to developers with different skill sets. With its combination of vector storage and real-time capabilities, Supabase is an excellent choice for NLP projects that require both scalability and real-time updates.

<a id="qdrant"></a>
### Qdrant

![github stars shield](https://img.shields.io/github/stars/qdrant/qdrant?logo=github)

Qdrant is an open-source vector database designed for similarity search and efficient storage of high-dimensional embeddings. It leverages an approximate nearest neighbor (ANN) algorithm based on Hierarchical Navigable Small World (HNSW) graphs, enabling fast and accurate similarity searches. Qdrant supports both CPU and GPU inference, allowing users to leverage hardware acceleration for faster computations.

One notable feature of Qdrant is its RESTful API, which provides a user-friendly interface for indexing, searching, and managing vector data. Qdrant also offers flexible query options, allowing users to specify search parameters and control the trade-off between accuracy and speed. With its focus on efficient similarity search and user-friendly API, Qdrant is a powerful vector database for various NLP applications.

<a id="vespa"></a>
### Vespa

![github stars shield](https://img.shields.io/github/stars/vespa-engine/vespa?logo=github)

![](https://vespa.ai/assets/vespa-logo.png)

[Vespa](https://vespa.ai/) is an open-source big data processing and serving engine developed by Verizon Media. It provides a distributed, scalable, and high-performance infrastructure for storing and querying vector embeddings. Vespa utilizes an inverted index structure combined with approximate nearest neighbor (ANN) search algorithms for efficient and accurate similarity searches.

One of Vespa's key features is its built-in ranking framework, allowing developers to define custom ranking models and apply complex ranking algorithms to search results. Vespa also supports real-time updates, making it suitable for dynamic embedding datasets. Additionally, Vespa provides a query language and a user-friendly WebUI for managing and monitoring the vector database. With its focus on distributed processing and advanced ranking capabilities, Vespa is a powerful tool for NLP applications that require complex ranking models and real-time updates.

<a id="weaviate"></a>
### Weaviate

![github stars shield](https://img.shields.io/github/stars/semi-technologies/weaviate?logo=github)

[Weaviate](https://weaviate.io/) is an open-source knowledge graph and vector search engine that excels in handling high-dimensional embeddings. It combines the power of graph databases and vector search to provide efficient storage, retrieval, and exploration of vector data. Weaviate offers powerful indexing methods, including approximate nearest neighbor (ANN) algorithms like HNSW, for fast and accurate similarity searches.

One unique aspect of Weaviate is its focus on semantics and contextual relationships. It allows users to define custom schema and relationships between entities, enabling complex queries that go beyond simple vector similarity. Weaviate also provides a RESTful API, client libraries, and a user-friendly WebUI for easy integration and management. With its combination of graph database features and vector search capabilities, Weaviate is an excellent choice for NLP applications that require semantic understanding and exploration of embeddings.

<a id="deeplake"></a>
### DeepLake

![github stars shield](https://img.shields.io/github/stars/activeloopai/deeplake?logo=github)

![](https://camo.githubusercontent.com/d0c805affb06f5ea9ba767de06b77a04de54a7ef433fad08b2729d5e6b11112c/68747470733a2f2f692e706f7374696d672e63632f72736a63576333532f646565706c616b652d6c6f676f2e706e67)
[DeepLake](https://www.activeloop.ai/) is an open-source vector database designed for efficient storage and retrieval of embeddings. It focuses on scalability and speed, making it suitable for handling large-scale NLP datasets. DeepLake provides a distributed architecture with built-in support for horizontal scalability, allowing users to handle massive volumes of vector data.

One unique feature of DeepLake is its support for distributed vector indexing and querying. It leverages an ANN algorithm based on the Product Quantization (PQ) method, enabling fast and accurate similarity searches. DeepLake also provides a RESTful API for easy integration with NLP pipelines and frameworks. With its emphasis on scalability and distributed processing, DeepLake is a robust vector database for demanding NLP applications.

<a id="langchain-vectorstore"></a>
### LangChain VectorStore

![github stars shield](https://img.shields.io/github/stars/hwchase17/langchain?logo=github)

LangChain [VectorStore](https://docs.langchain.com/docs/components/indexing/vectorstore) is an open-source vector database optimized for multilingual NLP applications. It focuses on efficient storage and retrieval of embeddings across multiple languages. VectorStore supports various indexing methods, including approximate nearest neighbor (ANN) algorithms like HNSW and Annoy, for fast similarity searches.

One distinguishing feature of VectorStore is its language-specific indexing and retrieval capabilities. It provides language-specific tokenization and indexing strategies to optimize search accuracy for different languages. VectorStore also offers a RESTful API and client libraries for easy integration with NLP pipelines. With its multilingual support and language-specific indexing, VectorStore is an excellent choice for projects that deal with embeddings across multiple languages.

<a id="other-relevant-vector-databases"></a>
### Other Relevant Vector Databases

While the above tools represent some of the best vector databases available for storing embeddings in NLP, there are other notable options worth exploring:

- Annoy: ![github stars shield](https://img.shields.io/github/stars/spotify/annoy?logo=github) Annoy is a lightweight C++ library for approximate nearest neighbor (ANN) search, offering efficient indexing and querying of high-dimensional embeddings.
- Elasticsearch: ![github stars shield](https://img.shields.io/github/stars/elastic/elasticsearch?logo=github) Elasticsearch is a popular distributed search and analytics engine that can be used to store and retrieve vector embeddings efficiently.
- Hnswlib: ![github stars shield](https://img.shields.io/github/stars/nmslib/hnswlib?logo=github) Hnswlib is a C++ library for efficient approximate nearest neighbor (ANN) search, providing high-performance indexing and retrieval of embeddings.
- NMSLIB: ![github stars shield](https://img.shields.io/github/stars/nmslib/nmslib?logo=github) NMSLIB is an open-source library for similarity search, offering a range of indexing methods and data structures for efficient storage and retrieval of embeddings.

These vector databases provide additional options and features that may suit specific requirements or preferences. Exploring these alternatives can help developers find the best fit for their NLP projects.


| Tool             | Scalability | Query Speed | Search Accuracy | Flexibility | Persistence | Storage Location |
|------------------|-------------|-------------|-----------------|-------------|--------------|------------------|
| Chroma           | High        | High        | High            | High        | Yes          | Local/Cloud      
| DeepsetAI        | High        | High        | High            | High        | Yes          | Local/Cloud      
| Faiss            | High        | High        | High            | Medium      | No           | Local/Cloud     
| Milvus           | High        | High        | High            | High        | Yes          | Local/Cloud     
| pgvector         | Medium      | Medium      | High            | High        | Yes          | Local           
| Pinecone         | High        | High        | High            | High        | Yes          | Cloud           
| Supabase         | High        | High        | High            | High        | Yes          | Cloud            
| Qdrant           | High        | High        | High            | High        | Yes          | Local/Cloud      
| Vespa            | High        | High        | High            | High        | Yes          | Local/Cloud      
| Weaviate         | High        | High        | High            | High        | Yes          | Local/Cloud     
| DeepLake         | High        | High        | High            | High        | Yes          | Local/Cloud      
| LangChain VectorStore | High   | High        | High            | High        | Yes          | Local/Cloud     
| Annoy            | Medium      | Medium      | Medium          | Medium      | No           | Local/Cloud     
| Elasticsearch    | High        | High        | High            | High        | Yes          | Local/Cloud     
| Hnswlib           | High        | High        | High            | High        | No           | Local/Cloud     
| NMSLIB           | High        | High        | High            | High        | No           | Local/Cloud     


<a id="related-reading"></a>
## Related reading
1. [Riding the AI Wave with Vector Databases: How they work (and why VCs love them) - LunaBrain](https://lunabrain.com/blog/riding-the-ai-wave-with-vector-databases-how-they-work-and-why-vcs-love-them/)
2. [10 Best vector databases for building AI Apps with embeddings - HarishGarg.com](https://harishgarg.com/writing/best-vector-databases-for-ai-apps/)
3. [Vector Databases: Long-Term Memory for Artificial Intelligence - The New Stack](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/)
4. [Vector Databases as Memory for your AI Agents | by Ivan Campos | Sopmac AI | Apr, 2023 | Medium](https://medium.com/sopmac-ai/vector-databases-as-memory-for-your-ai-agents-986288530443)
5. [How vector databases can revolutionize our relationship with generative AI | VentureBeat](https://venturebeat.com/ai/how-vector-databases-can-revolutionize-our-relationship-with-generative-ai/)
6. [Vector databases provide new ways to enable search and data analytics.](https://www.forbes.com/sites/adrianbridgwater/2023/05/19/the-rise-of-vector-databases/)
7. [OpenAI’s Embeddings with Vector Database | Better Programming](https://betterprogramming.pub/openais-embedding-model-with-vector-database-b69014f04433)
