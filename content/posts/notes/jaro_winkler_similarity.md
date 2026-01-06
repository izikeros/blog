---
Category: note
Date: 2023-08-29
Modified: 2023-08-29
Slug: jaro-winkler-similarity
Status: published
Summary: Learn about Jaro-Winkler similarity, a string-matching algorithm that emphasizes common prefixes and how to implement it in Python, providing better performance for strings with shared beginnings.
ai_summary: true
Tags:
  - nlp
  - text-similarity
  - string-similarity
  - similarity-metrics
  - jaccard
  - cosine-similarity
  - levenshtein
  - word-embeddings
  - soundex
Title: Jaro-Winkler Similarity
---
X::[[posts/notes/Tverski_similarity]]

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Jaro-Winkler Similarity](#jaro-winkler-similarity)
  - [Python Example:](#python-example)
  - [Valuable Properties of Jaro-Winkler Similarity:](#valuable-properties-of-jaro-winkler-similarity)
  - [Recommendations for Usage:](#recommendations-for-usage)
  - [Cases to Consider Alternatives:](#cases-to-consider-alternatives)

<!-- /MarkdownTOC -->

## Jaro-Winkler Similarity

Jaro-Winkler similarity is designed to compare two strings, giving more weight to the common prefix of the strings. The formula for Jaro-Winkler similarity is:

$$
JW(s1, s2) = J(s1, s2) + \frac{L \cdot p \cdot (1 - J(s1, s2))}{10}
$$

Where:

- $J(s1, s2)$ is the Jaro similarity between strings \(s1\) and \(s2\).
- $L$ is the length of the common prefix between the strings.
- $p$ is a constant scaling factor (typically 0.1) that increases the similarity for strings that share a common prefix.

The Jaro similarity $J(s1, s2)$ is calculated as:

$$
J(s1, s2) = \frac{m}{\max(\text{len}(s1), \text{len}(s2))}, \quad
$$
Where:

- $m$  is the number of matching characters

### Python Example

```python
def jaro_similarity(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    match_distance = max(len_s1, len_s2) // 2 - 1

    common_chars_s1 = []
    common_chars_s2 = []

    for i, char in enumerate(s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)

        if char in s2[start:end]:
            common_chars_s1.append(char)
            common_chars_s2.append(s2[start:end][s2[start:end].index(char)])

    m = len(common_chars_s1)
    if m == 0:
        return 0.0

    transpositions = sum(c1 != c2 for c1, c2 in zip(common_chars_s1, common_chars_s2)) // 2
    jaro_similarity = (m / len_s1 + m / len_s2 + (m - transpositions) / m) / 3
    return jaro_similarity


def jaro_winkler_similarity(s1, s2, p=0.1):
    jaro_sim = jaro_similarity(s1, s2)
    common_prefix_len = 0

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 == c2:
            common_prefix_len += 1
        else:
            break

    jaro_winkler_sim = jaro_sim + (common_prefix_len * p * (1 - jaro_sim))
    return jaro_winkler_sim
```

```python
string1 = "apple"
string2 = "applet"
jw_similarity = jaro_winkler_similarity(string1, string2)
print("Jaro-Winkler Similarity:", jw_similarity)
```

```
Jaro-Winkler Similarity: 0.9722222222222223
```

The Jaro-Winkler similarity metric possesses several valuable properties that make it suitable for specific use cases. However, it's important to note that no single similarity metric is universally best for all scenarios. Here are some valuable properties of the Jaro-Winkler metric, as well as recommendations for its usage and instances where other metrics might be more appropriate.
### Valuable Properties of Jaro-Winkler Similarity

1. **String Comparison with Common Prefix:** The Jaro-Winkler metric gives higher weight to common prefixes, making it effective for comparing strings that often have a prefix or abbreviation. This is particularly useful for names and addresses.

2. **Adjustable Scaling Factor:** The Jaro-Winkler metric allows for tuning the impact of the common prefix on the similarity score using the scaling factor $p$. This allows you to emphasize or de-emphasize the common prefix based on your needs.

3. **Simple to Understand and Implement:** The calculation of Jaro-Winkler similarity involves straightforward string matching and prefix length consideration, making it relatively easy to implement and understand.

### Recommendations for Usage

1. **Names and Addresses:** Jaro-Winkler similarity is highly recommended when comparing names, addresses, and other strings with common prefixes or abbreviations. It's often used in record linkage, deduplication, and fuzzy matching tasks in databases.

2. **Fuzzy String Matching:** When dealing with noisy or misspelled data, the Jaro-Winkler metric can be effective in finding approximate matches. It's suitable for scenarios where small typographical errors or variations are common.

3. **Short Texts:** Jaro-Winkler is well-suited for comparing short texts like product names, usernames, and titles, where the common prefix is an important aspect of similarity.

### Cases to Consider Alternatives

1. **Long Texts:** For comparing long texts or documents, **cosine similarity** or **Jaccard similarity** of term frequencies might be more appropriate, as they consider the distribution of terms across the entire text.

2. **Semantic Similarity:** If you're interested in capturing semantic meaning rather than character-level similarity, **word embeddings**-based metrics like cosine similarity between vector representations might be more suitable.

3. **Numerical Data:** For comparing numerical data, other similarity metrics such as **Euclidean distance**, **Manhattan distance**, or **Pearson correlation coefficient** might be more meaningful.

4. **Customized Weights:** If you have specific domain knowledge about feature importance, you might opt for a customized similarity metric that incorporates these weights effectively.

5. **Language-Specific Features:** If the text includes language-specific features, phonetic differences, or linguistic nuances, other specialized metrics like **Soundex** or **Levenshtein distance** might be considered.

## Examples

Here are some concrete pairs of strings that demonstrate the properties of the Jaro-Winkler similarity metric ($p$=0.2 if not stated differently):

**Common Prefix Emphasis:**

- String 1: "Michael"
- String 2: "Michelle"
- Jaro-Winkler similarity: 0.963

Explanation: The common prefix "Mich" contributes significantly to the similarity score in Jaro-Winkler, resulting in a high similarity even though the rest of the strings differ.

**Case Sensitivity and Scaling Factor:**

- String 1: "McDonald's"
- String 2: "Mcdonells"
- Jaro-Winkler similarity: 0.853

Explanation: The common prefix "Mcdon" is considered due to the case difference. The scaling factor can adjust the impact of this prefix on the similarity score.

**No Common Prefix:**

- String 1: "hello"
- String 2: "world"
- Jaro-Winkler similarity: 0.433

Explanation: Without a common prefix, the Jaro-Winkler similarity is low, even if the strings share some characters.

**Short vs. Long Strings:**

- String 1: "AI"
- String 2: "Artificial Intelligence"
- Jaro-Winkler similarity: 0.623
Explanation: The short string "AI" has a higher similarity to the beginning of "Artificial Intelligence" due to the common prefix "A".

**Typographical Errors:**

- String 1: "telephone"
- String 2: "telephne"
- Jaro-Winkler similarity: 0.967

Explanation: Despite the missing "o," the common prefix "teleph" contributes to a high Jaro-Winkler similarity score.

**Short and Noisy Data:**

- String 1: "abacus"
- String 2: "abaxus"
- Jaro-Winkler similarity: 0.956

Explanation: The similarity captures the similarity in the common prefix "aba" and penalizes the difference at the end.

**Significance of Scaling Factor:**

- String 1: "Thompson"
- String 2: "Thomson"
- Jaro-Winkler similarity with $p=0.1$: 0.975
- Jaro-Winkler similarity with $p=0.2$: 0.992

Explanation: The scaling factor $p$ affects the similarity score. A higher $p$ gives more emphasis to the common prefix, leading to a higher similarity.

These examples illustrate how the Jaro-Winkler similarity metric behaves based on different characteristics of input strings, such as common prefixes, case sensitivity, typos, length, and the scaling factor $p$.

## Summary

Jaro-Winkler similarity is highly valuable when dealing with short strings, names, and addresses, especially when common prefixes play a significant role. However, for longer texts, semantic similarity, numerical data, and specialized linguistic considerations, other metrics might be more appropriate. Always consider the specific characteristics of your data and the goals of your analysis when choosing a similarity metric.
