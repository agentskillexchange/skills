---
title: "qsv Blazing-Fast CSV Data Wrangling Toolkit"
description: "qsv is a high-performance command-line toolkit for querying, transforming, validating, and analyzing CSV and tabular data. Written in Rust, it provides over 50 commands for data wrangling tasks and supports Excel, Parquet, JSON, and other formats."
verification: security_reviewed
source: "https://github.com/dathere/qsv"
category:
  - "Data Extraction & Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "dathere/qsv"
  github_stars: 3569
---

# qsv Blazing-Fast CSV Data Wrangling Toolkit

What is qsv?
qsv is a blazing-fast, feature-rich command-line program for working with CSV and tabular data. It is a successor to the popular xsv tool, written in Rust for maximum performance. qsv provides over 50 commands for querying, slicing, sorting, analyzing, filtering, enriching, transforming, validating, joining, formatting, and converting data. Beyond CSV, it supports Excel, Parquet, Arrow, Avro, JSON, JSONL, and TSV formats.

The tool is designed for composability—commands can be piped together in Unix-style workflows. With Polars integration for multithreaded processing, qsv can count rows in a 15GB, 27-million-row dataset in under 12 seconds, or instantly with an index.

Key Commands and Features
Notable commands include apply for string, date, math, and NLP transformations (sentiment analysis, language detection, name gender guessing); join for inner, outer, and cross joins using hash indexes; validate for checking data against JSON Schema definitions; frequency for building column frequency tables with parallelism; sqlp for running SQL queries directly against CSV files via Polars; and luau for custom Lua scripting.

qsv also includes a describegpt command that uses LLMs to generate natural-language descriptions of datasets, and a chat command for conversational data exploration. The clipboard command allows direct input/output from the system clipboard for interactive workflows.

Installation and Output
Install via cargo install qsv, Homebrew, Scoop, or download pre-built binaries from GitHub releases. qsv outputs clean CSV, JSON, or formatted tables to stdout, making it trivially composable with other CLI tools and pipeline orchestration systems. It is published on crates.io, has over 3,500 GitHub stars, uses the Unlicense (public domain), and receives daily commits from active maintainers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/qsv-blazing-fast-csv-data-wrangling-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/qsv-blazing-fast-csv-data-wrangling-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/qsv-blazing-fast-csv-data-wrangling-toolkit/)
