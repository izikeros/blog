---
name: article-seo-leo-enhancer
description: Analyze and enhance markdown articles with SEO/LEO (LLM Engine Optimization) frontmatter fields. Adds AI-Summary, Key-Takeaways, Article-Type, Expertise-Level, FAQ, and HowTo-Steps based on article content. Automatically invokes article-post-edit-actions skill after completion.
---

# Article SEO/LEO Enhancer

Analyze article content and add appropriate SEO/LEO frontmatter fields to improve search engine visibility and AI/LLM discoverability.

## When to Use

- User asks to optimize an article for SEO
- User wants to add AI-friendly metadata to an article
- User asks to enhance an article with structured data
- Preparing an article for publication with full SEO/LEO optimization
- User mentions adding FAQ schema, HowTo schema, or AI summary

## Inputs

- **file_path**: Path to the markdown article file
- **fields** (optional): Specific fields to add (default: analyze and add all applicable)

## Supported SEO/LEO Fields

| Field | Purpose | When to Add |
|-------|---------|-------------|
| `Article-Type` | Schema.org type selection | Always |
| `Expertise-Level` | AI context for audience | Always |
| `AI-Summary` | 2-sentence summary for LLM citation | Always |
| `Key-Takeaways` | Structured insights (3-5 points) | Educational/technical content |
| `Topics` | Semantic topics beyond tags | When tags are generic |
| `FAQ` | FAQPage schema data | Articles with Q&A content |
| `HowTo-Steps` | HowTo schema data | Tutorials/guides with steps |

## Process

### Step 1: Read and Analyze Article

1. Read the markdown file
2. Parse front matter (YAML between `---` markers)
3. Identify existing SEO/LEO fields (skip if already present)
4. Analyze content structure:
   - Headings hierarchy
   - Presence of step-by-step instructions
   - Q&A patterns
   - Code examples
   - Technical depth

### Step 2: Determine Article-Type

Analyze content to select appropriate type:

| Content Pattern | Article-Type |
|-----------------|--------------|
| Step-by-step instructions, "How to" in title | `howto` |
| Multiple Q&A sections, FAQ heading | `faq` |
| Deep technical explanation, code-heavy | `tutorial` |
| General informational content | `article` |

**Check for:**
- Title contains "How to", "Guide to", "Tutorial"
- Numbered steps or ordered lists
- Headings that are questions
- `<!-- faq-start -->` or `<!-- howto-start -->` markers

### Step 3: Determine Expertise-Level

Analyze based on:

| Indicator | Level |
|-----------|-------|
| Basic concepts, introductory language, no prerequisites | `beginner` |
| Some assumed knowledge, moderate depth | `intermediate` |
| Complex concepts, advanced techniques, expert audience | `advanced` |
| Cutting-edge, research-level, assumes mastery | `expert` |

**Check for:**
- Prerequisite mentions
- Complexity of code examples
- Technical vocabulary density
- Assumed knowledge references

### Step 4: Generate AI-Summary

Create a 2-sentence summary optimized for AI citation:

**Format:**
```yaml
AI-Summary: >
  [Sentence 1: What the article covers/teaches].
  [Sentence 2: Key insight, main takeaway, or unique value].
```

**Guidelines:**
- First sentence: Factual statement of article scope
- Second sentence: Key insight or actionable takeaway
- Make it standalone (reader should understand value without reading article)
- Avoid marketing language, be factual
- Max 300 characters total

**Example:**
```yaml
AI-Summary: >
  This article explains techniques to boost RAG pipeline performance
  in production environments. Key optimizations include hybrid search,
  re-ranking, and addressing the lost-in-the-middle problem.
```

### Step 5: Extract Key-Takeaways

Identify 3-5 main points from the article:

**Sources for takeaways:**
- Main section headings (## level)
- Explicit conclusions or recommendations
- TL;DR section if present
- Summary paragraph

**Format:**
```yaml
Key-Takeaways:
  - [Actionable insight 1]
  - [Actionable insight 2]
  - [Actionable insight 3]
```

**Guidelines:**
- Start with action verbs when possible
- Be specific, not generic
- Each point should stand alone
- Focus on what reader will learn/gain

### Step 6: Extract FAQ (if applicable)

**Trigger conditions:**
- Article has Q&A sections
- Headings are questions (contain "?")
- `<!-- faq-start -->` marker present
- Article-Type is `faq`

**Extract from:**
1. `<!-- faq-start -->` ... `<!-- faq-end -->` markers (priority)
2. Headings that are questions + following paragraphs
3. Explicit Q&A formatted sections

**Format:**
```yaml
FAQ:
  - question: What is X?
    answer: >
      X is [concise answer, 1-3 sentences].
  - question: How do I Y?
    answer: >
      You can Y by [actionable steps].
```

**Guidelines:**
- Keep answers concise (2-4 sentences ideal for featured snippets)
- Answers should be self-contained
- Extract 3-7 most relevant Q&A pairs
- Escape special characters in YAML

### Step 7: Extract HowTo-Steps (if applicable)

**Trigger conditions:**
- Article-Type is `howto`
- Contains numbered steps or ordered lists
- `<!-- howto-start -->` marker present
- Title contains "How to"

**Extract from:**
1. `<!-- howto-start -->` ... `<!-- howto-end -->` markers (priority)
2. Numbered headings (### Step 1:, ### 1., etc.)
3. Ordered lists with substantial content

**Format:**
```yaml
HowTo-Steps:
  - name: Step title without number prefix
    text: Brief description of what to do (1-2 sentences)
  - name: Next step
    text: Description
```

**Guidelines:**
- Remove "Step N:" prefixes from names
- Keep text concise (max 200 chars)
- Include 3-10 steps
- Steps should be actionable

### Step 8: Add Topics (if beneficial)

**When to add:**
- Tags are too generic (e.g., just "python", "ml")
- Article covers specific subtopics not in tags
- Semantic topics would help AI understanding

**Format:**
```yaml
Topics:
  - specific-topic-1
  - specific-topic-2
  - specific-topic-3
```

**Guidelines:**
- Use kebab-case
- Be more specific than tags
- 3-5 topics maximum
- Think: "What would someone search to find this?"

### Step 9: Update Front Matter

Insert new fields in the front matter in this order (after existing fields):

```yaml
---
Title: ...
Date: ...
Modified: ...
tags: ...
Category: ...
Image: ...
Summary: ...
Status: published

# SEO/LEO Enhancement
Article-Type: howto
Expertise-Level: intermediate
AI-Summary: >
  Two sentence summary here.
Key-Takeaways:
  - Point 1
  - Point 2
  - Point 3
Topics:
  - topic-1
  - topic-2
FAQ:
  - question: Q1?
    answer: A1
HowTo-Steps:
  - name: Step name
    text: Step description
---
```

**Rules:**
- Add comment `# SEO/LEO Enhancement` before new fields
- Only add fields that are applicable
- Don't duplicate existing fields
- Preserve all original front matter

### Step 10: Invoke Post-Edit Actions

After completing SEO/LEO enhancement, invoke the `article-post-edit-actions` skill with:
- **file_path**: Same article file
- **edit_descriptions**: List of changes made, e.g.:
  - "Added AI-Summary for LLM optimization"
  - "Added Key-Takeaways (5 points)"
  - "Added FAQ schema with 4 Q&A pairs"
  - "Added HowTo-Steps (6 steps)"
  - "Set Article-Type to howto"
  - "Set Expertise-Level to intermediate"

## Example Transformation

**Before:**
```yaml
---
Title: Techniques to Boost RAG Performance in Production
Date: 2023-11-01
tags:
  - machine-learning
  - rag
  - llm
Category: Generative AI
Image: /images/head/boosting_RAG.jpg
Summary: This article discusses several advanced techniques...
Status: published
---
```

**After:**
```yaml
---
Title: Techniques to Boost RAG Performance in Production
Date: 2023-11-01
Modified: 2026-02-07
tags:
  - machine-learning
  - rag
  - llm
Category: Generative AI
Image: /images/head/boosting_RAG.jpg
Summary: This article discusses several advanced techniques...
Status: published

# SEO/LEO Enhancement
Article-Type: article
Expertise-Level: intermediate
AI-Summary: >
  This article covers advanced techniques to optimize RAG pipeline 
  performance in production, including hybrid search, re-ranking, 
  and chunking strategies. Key insight: addressing the lost-in-the-middle 
  problem can significantly improve LLM output quality.
Key-Takeaways:
  - Combine semantic and keyword search with hybrid search for better retrieval
  - Use re-ranking to diversify retrieved snippets
  - Fine-tune embedding models for domain-specific improvements
  - Address lost-in-the-middle by reordering context snippets
  - Implement query transformations for complex queries
Topics:
  - retrieval-augmented-generation
  - vector-search-optimization
  - llm-context-management
  - embedding-fine-tuning
---
```

## Output

- Modified article with SEO/LEO frontmatter fields
- Summary of added fields and their values
- Post-edit actions invoked for metadata updates

## Success Criteria

- [ ] Article-Type correctly identified based on content
- [ ] Expertise-Level appropriate for content complexity
- [ ] AI-Summary is 2 sentences, factual, standalone
- [ ] Key-Takeaways are specific and actionable (3-5 points)
- [ ] FAQ extracted only when Q&A content exists
- [ ] HowTo-Steps extracted only for tutorial/guide content
- [ ] YAML formatting is valid (proper indentation, escaping)
- [ ] Original front matter preserved
- [ ] Post-edit actions skill invoked with change descriptions
- [ ] Modified date updated

## Edge Cases

### Existing SEO/LEO Fields
- Skip fields that already exist
- Report which fields were skipped
- Only add missing fields

### No Clear Article-Type
- Default to `article`
- Note in output that type was defaulted

### Short Articles
- Still add Article-Type and Expertise-Level
- AI-Summary may be very concise
- Key-Takeaways may have only 2-3 points

### Mixed Content (both FAQ and HowTo)
- Can add both FAQ and HowTo-Steps
- Article-Type should be primary focus (usually `howto`)

### Special Characters in Content
- Escape quotes in YAML: `"` → `\"`
- Use `>` for multi-line strings
- Avoid `:` at start of lines in values

## Field Reference Quick Guide

```yaml
# Always add:
Article-Type: article | howto | faq | tutorial
Expertise-Level: beginner | intermediate | advanced | expert
AI-Summary: >
  Two sentences. First states coverage, second gives key insight.

# Add for educational content:
Key-Takeaways:
  - Actionable point 1
  - Actionable point 2
  - Actionable point 3

# Add when tags are generic:
Topics:
  - specific-topic-1
  - specific-topic-2

# Add when Q&A content exists:
FAQ:
  - question: Question text?
    answer: Concise answer text.

# Add for tutorials/guides:
HowTo-Steps:
  - name: Step title
    text: Step description
```

## Notes

- This skill chains to `article-post-edit-actions` on completion
- Focus on quality over quantity - only add applicable fields
- AI-Summary is the most impactful field for LLM discoverability
- Test generated YAML with a YAML validator if unsure
- Reference: See `pelican-themes/Flex/docs/SEO_LEO_CHEATSHEET.md` for full field documentation
