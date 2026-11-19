---
name: article-tag-enhancer
description: Analyze markdown article content and add missing relevant tags to frontmatter. Uses kebab-case format for multi-word tags (e.g., python-venv). Only adds tags that are clearly relevant and not already present. Automatically invokes article-post-edit-actions skill after completion.
---

# Article Tag Enhancer

Analyze article content and add missing relevant tags to improve discoverability and categorization.

## When to Use

- User asks to add tags to an article
- User wants to improve article discoverability
- Article has few or generic tags that don't cover the content well
- Preparing an article for publication with proper tagging

## Inputs

- **file_path**: Path to the markdown article file
- **max_new_tags** (optional): Maximum number of new tags to add (default: 5)

## Tag Format Rules

| Rule | Example |
|------|---------|
| All lowercase | `machine-learning` not `Machine-Learning` |
| Multi-word: kebab-case | `python-venv` not `python_venv` or `pythonvenv` |
| Single word: as-is | `python`, `docker`, `kubernetes` |
| Acronyms: lowercase | `llm`, `rag`, `api`, `cli` |
| Version numbers: with dash | `python-3`, `gpt-4` |

## Process

### Step 1: Read and Parse Article

1. Read the markdown file
2. Parse front matter (YAML between `---` markers)
3. Extract existing tags (may be list or comma-separated)
4. Store existing tags in normalized form (lowercase, trimmed)

### Step 2: Analyze Article Content

Extract tag candidates from:

**Title and Headings:**
- Article title
- All ## and ### headings
- Look for technology names, concepts, methodologies

**Content Analysis:**
- Code block languages (```python, ```bash, etc.)
- Library/framework mentions (pandas, langchain, fastapi)
- Concept mentions (embedding, vector-database, fine-tuning)
- Tool mentions (docker, kubernetes, git)
- Methodology mentions (rag, few-shot, zero-shot)

**Category Context:**
- Use category to inform relevant domain tags
- E.g., "Generative AI" category suggests LLM-related tags

### Step 3: Build Tag Candidates

**High-confidence indicators:**
- Mentioned 3+ times in content
- Appears in title or multiple headings
- Is a code block language
- Is a well-known technology/framework name

**Tag categories to consider:**

| Category | Examples |
|----------|----------|
| Languages | `python`, `javascript`, `rust`, `go` |
| Frameworks | `fastapi`, `flask`, `langchain`, `pytorch` |
| Concepts | `machine-learning`, `deep-learning`, `nlp` |
| Tools | `docker`, `kubernetes`, `git`, `vscode` |
| Methodologies | `rag`, `fine-tuning`, `prompt-engineering` |
| Domains | `data-science`, `web-development`, `devops` |
| Formats | `api`, `cli`, `rest`, `graphql` |

### Step 4: Filter Candidates

**Remove candidates that:**
- Already exist in tags (case-insensitive match)
- Are too generic (e.g., "code", "programming", "tutorial")
- Are too specific/obscure (mentioned only once in passing)
- Are variations of existing tags (e.g., don't add `ml` if `machine-learning` exists)

**Synonym/variation mapping:**
| If exists | Don't add |
|-----------|-----------|
| `machine-learning` | `ml`, `machinelearning` |
| `python` | `py`, `python3` |
| `javascript` | `js`, `node` |
| `llm` | `large-language-model` |
| `rag` | `retrieval-augmented-generation` |
| `api` | `rest-api`, `web-api` |

### Step 5: Rank and Select Tags

**Ranking criteria (in order):**
1. Frequency of mention in content
2. Presence in title or headings
3. Specificity (more specific = better)
4. Relevance to category

**Selection rules:**
- Maximum 5 new tags by default (configurable)
- Prefer specific over generic
- Ensure diversity (don't add 5 similar tags)
- Must be clearly relevant to article content

### Step 6: Format New Tags

Convert all candidates to proper format:

```
"Python Virtual Environment" → "python-virtual-environment"
"LangChain" → "langchain"
"RAG Pipeline" → "rag-pipeline"
"GPT-4" → "gpt-4"
"REST API" → "rest-api"
"t-SNE" → "t-sne"
```

**Formatting rules:**
1. Convert to lowercase
2. Replace spaces with hyphens
3. Remove special characters except hyphens
4. Collapse multiple hyphens to single
5. Trim leading/trailing hyphens

### Step 7: Update Front Matter

Add new tags to existing tags list:

**Before:**
```yaml
tags:
  - python
  - machine-learning
```

**After:**
```yaml
tags:
  - python
  - machine-learning
  - langchain
  - vector-database
  - embeddings
```

**Rules:**
- Append new tags after existing ones
- Maintain YAML list format
- Don't reorder existing tags
- Preserve any tag formatting style used

### Step 8: Invoke Post-Edit Actions

After adding tags, invoke the `article-post-edit-actions` skill with:
- **file_path**: Same article file
- **edit_descriptions**: 
  - "Added tags: tag1, tag2, tag3" (list all new tags)

## Example Transformation

**Article content excerpts:**
```markdown
Title: Techniques to Boost RAG Performance in Production
Category: Generative AI

...discusses hybrid search, re-ranking...
...using LangChain and ChromaDB...
...vector store optimization...
```

**Before:**
```yaml
tags:
  - machine-learning
  - rag
  - llm
```

**After:**
```yaml
tags:
  - machine-learning
  - rag
  - llm
  - langchain
  - chromadb
  - vector-database
  - hybrid-search
  - re-ranking
```

## Output

- Modified article with new tags added
- List of tags added with brief justification
- Post-edit actions invoked for metadata updates

## Success Criteria

- [ ] Only relevant tags added (clearly present in content)
- [ ] No duplicate tags (case-insensitive)
- [ ] Tags in correct kebab-case format
- [ ] Maximum tag limit respected
- [ ] Original tags preserved and unchanged
- [ ] YAML formatting valid
- [ ] Post-edit actions skill invoked
- [ ] Modified date updated

## Edge Cases

### No New Tags Needed
- If existing tags already cover content well, add none
- Report: "No additional tags needed - existing tags are comprehensive"

### Ambiguous Technology Names
- Only add if clearly used as technology (not generic word)
- E.g., "Flask" the framework vs "flask" the container
- Check context: code blocks, imports, documentation links

### Similar Existing Tags
- Don't add `vector-store` if `vector-database` exists
- Don't add `neural-network` if `deep-learning` exists
- Use judgment on semantic overlap

### Many Potential Tags
- Prioritize by relevance and specificity
- Better to add 3 highly relevant tags than 5 marginally relevant

### Tag Format Variations in Existing Tags
- Match the existing format style if possible
- If existing uses underscores, still use hyphens for new (standard format)

## Common Tag Patterns

### By Domain

**Machine Learning / AI:**
- `machine-learning`, `deep-learning`, `neural-network`
- `nlp`, `computer-vision`, `reinforcement-learning`
- `pytorch`, `tensorflow`, `scikit-learn`, `keras`

**LLM / Generative AI:**
- `llm`, `gpt`, `chatgpt`, `claude`
- `langchain`, `llamaindex`, `openai`
- `rag`, `prompt-engineering`, `fine-tuning`
- `embeddings`, `vector-database`, `semantic-search`

**Data Science:**
- `pandas`, `numpy`, `data-analysis`
- `visualization`, `matplotlib`, `plotly`
- `statistics`, `data-cleaning`, `eda`

**DevOps / Infrastructure:**
- `docker`, `kubernetes`, `aws`, `gcp`, `azure`
- `ci-cd`, `github-actions`, `terraform`
- `monitoring`, `logging`, `observability`

**Python Development:**
- `python`, `fastapi`, `flask`, `django`
- `async`, `typing`, `testing`, `pytest`
- `poetry`, `pip`, `virtual-environment`

### Technology Detection Hints

| Content Pattern | Suggested Tag |
|-----------------|---------------|
| `import langchain` | `langchain` |
| `from chromadb` | `chromadb` |
| `pip install X` | Consider `X` as tag |
| `docker run` | `docker` |
| `kubectl` commands | `kubernetes` |
| `.ipynb` mentions | `jupyter-notebook` |
| `async def` | `async` |
| `@pytest` | `pytest`, `testing` |

## Notes

- This skill chains to `article-post-edit-actions` on completion
- Quality over quantity - fewer relevant tags is better than many marginal ones
- Consider the blog's existing tag taxonomy when adding tags
- Tags improve both human navigation and SEO/AI discoverability
- When in doubt, don't add the tag
