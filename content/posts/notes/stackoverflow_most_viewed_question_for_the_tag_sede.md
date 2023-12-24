---
Category: note
Date: '2023-02-13'
Modified: '2023-07-12'
Prompt: Give me few method on how to find most viewed questions with given tag on stackoverflow
Slug: stackoverflow-most-viewed-question-for-the-tag
Status: published
Tags: most-viewed-questions, stack-overflow, specific-tag, tag-search, search-tips, stackoverflow, sede
Title: How to Find Most Viewed Questions With Given Tag on Stackoverflow?
---



You can use the Stack Exchange Data Explorer (SEDE) to find the most viewed questions with a given tag on Stack Overflow. Here are a few steps you can follow:

1. Go to [https://data.stackexchange.com/stackoverflow/queries](https://data.stackexchange.com/stackoverflow/queries) and select "Stack Overflow" as the site.

2. Select "Compose Query" and write a query to find the most viewed questions with a given tag. For example, if you want to find the most viewed questions with the "python" tag, you can use the following query:

```sql
SELECT TOP 1000
    Id AS [Post Link],
    ViewCount,
    Score,
    CreationDate,
    Tags,
    Title
FROM Posts
WHERE Tags LIKE '%<python>%'
ORDER BY ViewCount DESC

```

This query will return the top 1000 questions with the "python" tag, sorted by view count.

3. Click "Run Query" to execute the query and see the results.

4. You can export the results as a CSV file or other formats by clicking "Export" at the top of the query results.

**NOTE:** SEDE is updated only once a week, so the data may not be up-to-date with the latest changes on Stack Overflow.

X::[[stack_exchange_data_explorer_sede]]
X::[[Explore_stack_overflow_by_using_SEDE]]
