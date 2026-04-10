---
title: "xsv High-Performance CSV Toolkit"
description: "xsv is a fast CSV command-line toolkit written in Rust by Andrew Gallant (BurntSushi). It provides indexing, slicing, analyzing, splitting, joining, searching, sampling, and statistics operations on CSV files with exceptional speed and memory efficiency."
slug: "xsv-high-performance-csv-toolkit"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/BurntSushi/xsv"
tool_ecosystem:
  github_repo: "BurntSushi/xsv"
  github_stars: 10758
listed: true
---

# xsv High-Performance CSV Toolkit

xsv is a fast CSV command-line toolkit written in Rust by Andrew Gallant (BurntSushi). It provides indexing, slicing, analyzing, splitting, joining, searching, sampling, and statistics operations on CSV files with exceptional speed and memory efficiency.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install xsv-high-performance-csv-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

xsv is a high-performance command-line toolkit for working with CSV data, written in Rust by Andrew Gallant (the creator of ripgrep). It provides a suite of subcommands for common CSV operations: cat (concatenation), count, fixlengths, flatten, fmt (formatting), frequency, headers, index, input, join, partition, sample, reverse, search, select, shuffle, slice, sort, split, stats, and table display.
What makes xsv stand out is its raw speed. By leveraging Rust and the csv crate (also authored by Gallant), xsv can process multi-gigabyte CSV files in seconds. The indexing feature creates a secondary index that allows random access into a CSV file, enabling fast slicing, sampling, and counting operations on large datasets without reading the entire file into memory.
The tool supports powerful join operations between CSV files using inner, outer, left, right, and cross joins. Its frequency command generates frequency tables for column values, and the stats command computes summary statistics including mean, median, mode, standard deviation, min, max, and cardinality. The search subcommand supports regex filtering across columns, and select allows column selection and reordering using column names or indices.
xsv excels as a building block in Unix-style data pipelines. You can chain multiple xsv commands together, or combine them with tools like jq, sort, and awk. It reads from stdin and writes to stdout by default, making it easy to integrate into shell scripts and automation workflows. With over 10,700 GitHub stars, xsv is one of the most popular data processing CLI tools. It is dual-licensed under MIT and the Unlicense.
Installation is available via cargo install xsv, Homebrew, and prebuilt binaries on the GitHub releases page for Linux, macOS, and Windows. While the repository is now archived, xsv remains widely used and its successor project qsv continues active development with additional features.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xsv-high-performance-csv-toolkit/)
