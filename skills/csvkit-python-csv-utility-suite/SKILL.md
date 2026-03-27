---
name: "csvkit Python CSV Utility Suite"
description: "csvkit is a suite of Python command-line utilities for converting to, working with, and analyzing CSV files. It includes tools for format conversion, querying CSV with SQL, data cleaning, filtering, sorting, and statistical analysis."
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/csvkit-python-csv-utility-suite/"
---

# csvkit Python CSV Utility Suite

csvkit is a suite of Python command-line utilities for converting to, working with, and analyzing CSV files. It includes tools for format conversion, querying CSV with SQL, data cleaning, filtering, sorting, and statistical analysis.

## Install

### Any Agent (npx)
```bash
npx skills add csvkit-python-csv-utility-suite
```

### Claude Code
```bash
npx skills add csvkit-python-csv-utility-suite --claude-code
```

### Cursor
```bash
npx skills add csvkit-python-csv-utility-suite --cursor
```

### Codex
```bash
npx skills add csvkit-python-csv-utility-suite --codex
```

### OpenClaw
```bash
clawhub install csvkit-python-csv-utility-suite
```

## Overview

csvkit is a suite of command-line tools built on Python for working with CSV files, created by the wireservice team. It provides a collection of utilities that each handle a specific CSV operation, following the Unix philosophy of small composable tools. The suite is installed via pip and works on any platform with Python 3.
The conversion tools handle getting data into CSV format. in2csv converts Excel, JSON, fixed-width, and other tabular formats to CSV. sql2csv executes SQL queries against databases and outputs the results as CSV. csvjson converts CSV back to JSON. These converters handle encoding issues, multi-sheet workbooks, and nested structures that often trip up manual conversion attempts.
The processing tools work with CSV data directly. csvcut selects and reorders columns by name or position. csvgrep filters rows using string matching or regular expressions. csvsort sorts by one or more columns with type-aware ordering. csvstack concatenates multiple CSV files with compatible schemas. csvformat converts between different CSV dialects (changing delimiters, quoting styles, or line endings). csvclean reports and fixes common CSV errors like inconsistent column counts.
The analysis tools help understand the data. csvstat generates descriptive statistics for each column including type detection, min/max, mean, and frequency distributions. csvlook renders CSV as a readable Markdown-style table in the terminal. csvsql can create SQL table definitions from CSV schemas, import data into databases, and execute SQL queries directly against CSV files using an in-memory SQLite database.
With over 6,000 GitHub stars and an MIT license, csvkit has been a standard tool for data journalists and analysts since 2011. It integrates naturally into shell pipelines and pairs well with other command-line data tools like jq, Miller, and xsv.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill csvkit-python-csv-utility-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill csvkit-python-csv-utility-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill csvkit-python-csv-utility-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill csvkit-python-csv-utility-suite -a codex
```

### OpenClaw

```bash
clawhub install csvkit-python-csv-utility-suite
```
