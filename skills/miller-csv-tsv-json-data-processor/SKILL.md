---
title: "Miller CSV TSV JSON Data Processor"
description: "Miller (mlr) is a command-line tool for querying, shaping, and reformatting name-indexed data such as CSV, TSV, JSON, and JSON Lines. It combines the functionality of awk, sed, cut, join, and sort into a single tool purpose-built for structured data processing."
verification: security_reviewed
source: "https://github.com/johnkerl/miller"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "johnkerl/miller"
  github_stars: 9814
---

# Miller CSV TSV JSON Data Processor

Miller (mlr) is a command-line tool created by John Kerl that brings the power of awk, sed, cut, join, and sort to name-indexed data formats. Unlike traditional Unix text-processing tools that operate on positional fields, Miller works with key-value-pair data, making it natural and intuitive for processing CSV, TSV, JSON, JSON Lines, and positionally-indexed data.

The tool allows you to perform on-the-fly transformations: adding new fields derived from existing ones, dropping fields, sorting, statistical aggregation, pretty-printing, and format conversion. Its natural data structure is the insertion-ordered hash map, making it a perfect fit for working with structured tabular data from the command line.

Miller is written in Go and is designed for high performance. It supports streaming processing of large files, automatic type inference, and a rich expression language for data manipulation. You can chain operations using Miller verbs (head, sort, tac, uniq, group-by, join, stats1, etc.) to build complex data pipelines directly from the command line.

Key capabilities include format conversion between CSV, TSV, JSON, and JSON Lines; statistical aggregation with mean, median, percentiles, and more; record-level filtering with boolean expressions; field transformations with arithmetic and string functions; joins between multiple data files; and sampling from large datasets. Miller complements tools like R and Pandas by handling data cleaning and preparation directly in the shell.

The tool is available via package managers on Linux (apt, yum, snap), macOS (brew, port), and Windows (choco, winget, scoop). It has comprehensive documentation at miller.readthedocs.io and is dual-licensed under BSD-2-Clause. With over 9,000 GitHub stars, Miller is one of the most widely used command-line data processing tools in the ecosystem.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/miller-csv-tsv-json-data-processor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/miller-csv-tsv-json-data-processor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/miller-csv-tsv-json-data-processor/)
