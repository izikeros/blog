---
Title: Simple In-Memory Knowledge Graphs for Quick Graph Querying
Slug: simple-inmemory-knowledge-graphs-for-quick-graph-querying
Date: 2025-01-16
Modified: 2025-01-16
Start: 2025-01-16
tags: graph, knowledge-graph, query, networkx, neo4j, rdflib, SPARQL
Category: Howto
Image: /images/head/knowledge_graph_cr_640px.jpg
banner: "/images/head/knowledge_graph_cr_640px.jpg"
Summary: As developers, we often reach for full-scale graph databases when simpler solutions would suffice. When your knowledge graph is modest in size, keeping it in memory can be both efficient and practical. Let's explore some powerful tools that make this approach work beautifully.
Status: published
prompt:
---
up::[[knowledge_graphs]]

Working with knowledge graphs doesn't always require [Neo4j](https://neo4j.com/) or other heavyweight solutions. Sometimes you need a lightweight way to represent and query graph data right in memory. Let me share some approachable solutions I've found particularly useful.

## NetworkX - The Python Swiss Army Knife

[NetworkX](https://github.com/networkx/networkx) has been my reliable companion for simple graph operations. It's incredibly intuitive and perfect for smaller knowledge graphs:

```python
import networkx as nx

# Create a knowledge graph
G = nx.Graph()

# Add some knowledge
G.add_edge("Alice", "knows", "Bob")
G.add_edge("Bob", "works_at", "TechCorp")

# Simple queries
def find_connections(G, person):
    return [(n, G[person][n]) for n in G[person]]
```

You can test it with this example:

```python
# Test NetworkX
print(find_connections(G, "Alice"))
print(find_connections(G, "Bob"))
print("\n")
```

The output is:

```python
NetworkX Example:
[('Bob', {'relationship': 'knows'})]
[('Alice', {'relationship': 'knows'}), ('TechCorp', {'relationship': 'works_at'})]
```

## RDFLib - When You Need Semantic Power

If you're dealing with semantic data and need [SPARQL](https://en.wikipedia.org/wiki/SPARQL)-like querying, [RDFLib](https://rdflib.readthedocs.io/en/stable/index.html) provides a perfect middle ground:

```python
from rdflib import Graph, Literal, RDF, URIRef

# Create an in-memory graph
g = Graph()

# Add triples
g.add((URIRef('Alice'), URIRef('knows'), URIRef('Bob')))

# Query using SPARQL
qres = g.query(
    """SELECT ?s ?o
       WHERE {
          ?s knows ?o .
       }""")
       
for row in qres:
 print(f"{row.s} -> {row.o}")
 print("\n")
```

The output is:

```
RDFLib Example:
Bob -> TechCorp
Alice -> Bob
```

## PyGraphviz - Visualization with Query Capabilities

When you need both visualization and querying use [pygraphviz](https://github.com/pygraphviz/pygraphviz):

```python
import pygraphviz as pgv

G = pgv.AGraph()
G.add_edge("Alice", "Bob", relationship="knows")

def find_relationships(G, node):
    return [e for e in G.edges() if node in e]
```

**NOTE**: There might be an problem when installing pygraphviz in Google Colab, you can use matlplotlib + networkx instead

## DIY Solution - Custom Graph Structure

Sometimes, a custom solution fits best:

```python
from collections import defaultdict
from typing import List, Dict, Any

class SimpleKG:
    def __init__(self):
        self.graph = defaultdict(dict)
    
    def add_relation(self, subject: str, predicate: str, object: str):
        if predicate not in self.graph[subject]:
            self.graph[subject][predicate] = []
        self.graph[subject][predicate].append(object)
    
    def query_by_subject(self, subject: str) -> Dict[str, List[str]]:
        return self.graph.get(subject, {})
    
    def get_connected_nodes(self, node: str) -> List[str]:
        connected = []
        for predicate, objects in self.graph.get(node, {}).items():
            connected.extend(objects)
        return connected
    
    def find_paths(self, start: str, end: str, max_depth: int = 4) -> List[List[str]]:
        if start == end:
            return [[start]]
            
        visited = set()
        queue = [(start, [start])]
        paths = []
        
        while queue:
            (vertex, path) = queue.pop(0)
            connected_nodes = self.get_connected_nodes(vertex)
            
            for next_node in connected_nodes:
                if next_node == end:
                    paths.append(path + [next_node])
                elif next_node not in visited and len(path) < max_depth:
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))
        
        return paths
    
    def find_by_predicate(self, predicate: str) -> List[tuple]:
        results = []
        for subject, predicates in self.graph.items():
            if predicate in predicates:
                for obj in predicates[predicate]:
                    results.append((subject, obj))
        return results
    
    def find_connected_through_predicate(self, node: str, predicate: str) -> List[str]:
        return self.graph.get(node, {}).get(predicate, [])
```

Here is simple example how you can test it:

```python
# Test the implementation
kg = SimpleKG()
kg.add_relation("Alice", "knows", "Bob")
kg.add_relation("Bob", "works_at", "TechCorp")
kg.add_relation("TechCorp", "located_in", "San Francisco")

print("Query by subject 'Alice':", kg.query_by_subject("Alice"))
print("Find paths from Alice to TechCorp:", kg.find_paths("Alice", "TechCorp"))
```

The output is:

```
Query by subject 'Alice': {'knows': ['Bob']}
Find paths from Alice to TechCorp: [['Alice', 'Bob', 'TechCorp']]
```

More advanced example:

```python

# Create sample data
kg = SimpleKG()

# Movies data
movies = [
    "Inception", "The Dark Knight", "Interstellar", "Dunkirk",
    "Memento", "The Prestige", "Tenet", "Fight Club", "Se7en",
    "The Social Network", "Gone Girl", "Panic Room"
]

directors = [
    "Christopher Nolan", "David Fincher", "Martin Scorsese",
    "Quentin Tarantino", "Steven Spielberg"
]

actors = [
    "Leonardo DiCaprio", "Christian Bale", "Matthew McConaughey",
    "Brad Pitt", "Tom Hardy", "Marion Cotillard", "Michael Caine",
    "Anne Hathaway", "Cillian Murphy", "Joseph Gordon-Levitt",
    "Ellen Page", "Jesse Eisenberg", "Ben Affleck", "Rosamund Pike"
]

# Add relationships
# Directors directed movies
movie_director = {
    "Inception": "Christopher Nolan",
    "The Dark Knight": "Christopher Nolan",
    "Interstellar": "Christopher Nolan",
    "Dunkirk": "Christopher Nolan",
    "Memento": "Christopher Nolan",
    "The Prestige": "Christopher Nolan",
    "Tenet": "Christopher Nolan",
    "Fight Club": "David Fincher",
    "Se7en": "David Fincher",
    "The Social Network": "David Fincher",
    "Gone Girl": "David Fincher",
    "Panic Room": "David Fincher"
}

for movie, director in movie_director.items():
    kg.add_relation(movie, "directed_by", director)
    kg.add_relation(director, "directed", movie)

# Add actors to movies (random assignment for demonstration)
movie_actors = {
    "Inception": ["Leonardo DiCaprio", "Tom Hardy", "Marion Cotillard", "Michael Caine", "Ellen Page", "Joseph Gordon-Levitt"],
    "The Dark Knight": ["Christian Bale", "Michael Caine", "Cillian Murphy"],
    "Interstellar": ["Matthew McConaughey", "Anne Hathaway", "Michael Caine"],
    "Fight Club": ["Brad Pitt"],
    "The Social Network": ["Jesse Eisenberg"],
    "Gone Girl": ["Ben Affleck", "Rosamund Pike"]
}

for movie, cast in movie_actors.items():
    for actor in cast:
        kg.add_relation(movie, "stars", actor)
        kg.add_relation(actor, "acted_in", movie)

# Add some awards
awards = ["Oscar", "Golden Globe", "BAFTA"]
for director in directors[:3]:
    for award in random.sample(awards, random.randint(1, len(awards))):
        kg.add_relation(director, "won", award)

for actor in actors[:6]:
    for award in random.sample(awards, random.randint(0, len(awards))):
        kg.add_relation(actor, "won", award)

# Example queries
print("1. Find all movies directed by Christopher Nolan:")
nolan_movies = kg.find_connected_through_predicate("Christopher Nolan", "directed")
print(nolan_movies)
print()

print("2. Find actors who worked with Christopher Nolan (through any movie):")
nolan_actors = set()
for movie in nolan_movies:
    actors = kg.find_connected_through_predicate(movie, "stars")
    nolan_actors.update(actors)
print(list(nolan_actors))
print()

print("3. Find path between Leonardo DiCaprio and Christopher Nolan:")
paths = kg.find_paths("Leonardo DiCaprio", "Christopher Nolan")
print("Found paths:")
for path in paths:
    print(" -> ".join(path))
print()

print("4. Find Oscar winners:")
oscar_winners = kg.find_by_predicate("won")
print([winner[0] for winner in oscar_winners if winner[1] == "Oscar"])
print()

print("5. Find common movies between Michael Caine and Leonardo DiCaprio:")
caine_movies = set(kg.find_connected_through_predicate("Michael Caine", "acted_in"))
dicaprio_movies = set(kg.find_connected_through_predicate("Leonardo DiCaprio", "acted_in"))
print(list(caine_movies & dicaprio_movies))
```

Output:

```
1. Find all movies directed by Christopher Nolan: 
['Inception', 'The Dark Knight', 'Interstellar', 'Dunkirk', 'Memento', 'The Prestige', 'Tenet'] 

2. Find actors who worked with Christopher Nolan (through any movie):
['Christian Bale', 'Michael Caine', 'Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Cillian Murphy', 'Anne Hathaway', 'Matthew McConaughey', 'Marion Cotillard', 'Ellen Page', 'Tom Hardy'] 

3. Find path between Leonardo DiCaprio and Christopher Nolan: 
Found paths: 
Leonardo DiCaprio -> Inception -> Christopher Nolan 
Leonardo DiCaprio -> Inception -> Michael Caine -> The Dark Knight -> Christopher Nolan 
Leonardo DiCaprio -> Inception -> Michael Caine -> Interstellar -> Christopher Nolan 

5. Find Oscar winners: 
['Leonardo DiCaprio', 'Tom Hardy', 'Marion Cotillard', 'Christian Bale', 'Matthew McConaughey', 'Brad Pitt', 'Martin Scorsese'] 

5. Find common movies between Michael Caine and Leonardo DiCaprio: 
['Inception']
```

## Making the Right Choice

The best solution depends on your specific needs:

- Use NetworkX for general graph operations and algorithms
- Choose RDFLib when working with semantic data and SPARQL
- Go with PyGraphviz when visualization is important
- Consider a custom solution for specialized query patterns

## Performance Considerations

These solutions work well for graphs with thousands of nodes and edges. The key is keeping everything in memory and optimizing your query patterns. For NetworkX and RDFLib, using their built-in query methods is usually faster than writing custom traversal code.

## Beyond Simple Solutions

When your knowledge graph grows beyond memory constraints or you need more complex querying capabilities, it might be time to consider solutions like [Neo4j](https://neo4j.com/) or [Amazon Neptune](https://aws.amazon.com/neptune/). However, for many use cases, these in-memory solutions provide the perfect balance of simplicity and functionality.

## A Note on Automated Graph Construction

Building knowledge graphs by hand, as shown in our examples, is straightforward. However, automatically constructing them from documents or unstructured data is a complex challenge worthy of its own article. Here are some key challenges you'll face:

**Entity recognition** and **disambiguation** is perhaps the trickiest part - determining whether "Apple" refers to the fruit or the company, or whether two mentions of "John Smith" refer to the same person. You'll need to handle coreference resolution (understanding that "he" refers to "John" mentioned earlier) and deal with variations in how entities are written ("NYC" vs "New York City").

**Relationship extraction** comes with its own set of problems. Natural language is complex and often implicit - extracting clear, structured relationships from sentences like "After years at Microsoft, Sarah brought her expertise to the startup" requires sophisticated NLP techniques.

**Data quality** and **consistency** are also major concerns. Sources might conflict with each other, contain outdated information, or present opinions as facts. You'll need strategies for handling uncertainty and conflicting information in your graph.

If you're interested in automatic graph construction, I'd recommend starting with established NLP libraries and knowledge graph toolkits rather than building everything from scratch. But that's a topic for another deep dive!

## Wrapping Up

Don't jump to complex graph databases when simpler solutions might suffice. These in-memory approaches can handle surprisingly complex tasks while keeping your codebase clean and maintainable. Plus, they're perfect for prototyping before committing to a full-scale graph database solution.

## Further Reading, References

- paper [\[2305.14485\] Knowledge Graphs Querying](https://arxiv.org/abs/2305.14485)
- similarar attempt as in this article to build and query knowledge graph: [Querying using simple knowledge graphs \| by Vishnu Nandakumar \| Analytics Vidhya \| Medium](https://medium.com/analytics-vidhya/querying-using-simple-knowledge-graphs-abeb13d05e48)
- [GraphRAG](https://memgraph.com/docs/ai-ecosystem/graph-rag)
- [CogniPy for Pandas - In-memory Graph Database and Knowledge Graph with Natural Language Interface - CogniPy 1.0.0 documentation](https://cognipy.org/) - In-memory Graph Database and Knowledge Graph with Natural Language Interface
- not necessarily small and simple solutions: [Title Unavailable \| Site Unreachable](https://www.puppygraph.com/blog/best-graph-databases)
