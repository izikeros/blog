---
Category: note
Date: 2022-08-16
Modified: 2023-07-12
Slug: reading-csv-with-obsidian-dataview-dataviewjs
Status: published
Tags:
  - obsidian
  - obsidian/dataview
  - obsidian/dataviewjs
  - csv
Title: Reading CSV With Obsidian Dataview and Dataviewjs
citation_needed: false
---

The [obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin allows reading data from the notes in the vault and data files such as CSV. Both `dataview` and `dataviewjs` can be used for that purpose. I'm more fluent in using `dataview` therefore I will dedicate more space to this solution

## Reading with dataview

Assume, that you have a CSV file `my_data.csv` with contents:

```
eventDate;eventName
2022-01-02;Birthday
2022-01-07;Lake excursion
2022-01-12;River
2022-01-13;Sunrise
2022-01-13;Sunset
2022-01-16;Mountain Excursion
2022-01-21;Evening at home
```

Reading tabular data
You can read and display the contents of that file as a table using `dataview` code:

```
 ```dataview
 TABLE WITHOUT ID eventDate, eventName
 FROM csv("my_data.csv")
 ```
```

In this specific case, one column contains dates and you might want to display data in a specific format. In my case - I needed dates in `YYYY-MM-DD` format. You can do date formatting on reading using `dateformat`:

```
 ```dataview
 TABLE WITHOUT ID dateformat(eventDate, "yyyy-MM-dd") As eventDate, eventName
 FROM csv("my_data.csv")
 ```
```

## Reading with dataviewjs

For reading data from csv with dataviewjs you can use someting along this lines:

```
 ```dataviewjs
 const myData = await dv.io.csv("my_data.csv");
 dv.table(["eventDate", "eventName"], myData)
 ```
```

Reading CSV files with `dataviewjs` is also possible. From the [official documentation](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dviocsvpath-origin-file):

> Load a CSV from the given path (a link or string). Relative paths will be resolved relative to the optional origin file (defaulting to the current file if not provided). Return a dataview array, each element containing an object of the CSV values; if the file does not exist, return `undefined`.
>
> `await dv.io.csv("hello.csv") => [{ column1: ..., column2: ...}, ...]`

**References:**

- My post on obsidian forum where I got wide explanations and ideas on how to work with CSV data: [Find rows with date field matching date of daily note where the query is made - Help - Obsidian Forum](https://forum.obsidian.md/t/find-rows-with-date-field-matching-date-of-daily-note-where-the-query-is-made/41437)

**Credits:**

- [mnvwvnm](https://forum.obsidian.md/u/mnvwvnm/summary) and [scholarintraining](https://forum.obsidian.md/u/scholarintraining/summary) users from [obsidian forum](https://forum.obsidian.md) that helped me to understand how the reading CSV works and better understand dataview and dataviewjs.

up: [[obsidian]]
