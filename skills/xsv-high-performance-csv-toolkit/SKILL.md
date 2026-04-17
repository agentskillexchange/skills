---
title: "xsv High-Performance CSV Toolkit"
description: "xsv is a high-performance command-line toolkit for working with CSV data, written in Rust by Andrew Gallant (the creator of ripgrep). It provides a suite of subcommands for common CSV operations: cat (concatenation), count, fixlengths, flatten, fmt (formatting), frequency, headers, index, input, join, partition, sample, reverse, search, select, shuffle, slice, sort, split, stats, and table display.\nWhat makes xsv stand out is its raw speed. By leveraging Rust and the csv crate (also authored by Gallant), xsv can process multi-gigabyte CSV files in seconds. The indexing feature creates a secondary index that allows random access into a CSV file, enabling fast slicing, sampling, and counting operations on large datasets without reading the entire file into memory.\nThe tool supports powerful join operations between CSV files using inner, outer, left, right, and cross joins. Its frequency command generates frequency tables for column values, and the stats command computes summary statistics including mean, median, mode, standard deviation, min, max, and cardinality. The search subcommand supports regex filtering across columns, and select allows column selection and reordering using column names or indices.\nxsv excels as a building block in Unix-style data pipelines. You can chain multiple xsv commands together, or combine them with tools like jq, sort, and awk. It reads from stdin and writes to stdout by default, making it easy to integrate into shell scripts and automation workflows. With over 10,700 GitHub stars, xsv is one of the most popular data processing CLI tools. It is dual-licensed under MIT and the Unlicense.\nInstallation is available via cargo install xsv, Homebrew, and prebuilt binaries on the GitHub releases page for Linux, macOS, and Windows. While the repository is now archived, xsv remains widely used and its successor project qsv continues active development with additional features."
verification: security_reviewed
source: "https://github.com/BurntSushi/xsv"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "BurntSushi/xsv"
  github_stars: 10758
---

# xsv High-Performance CSV Toolkit

xsv is a high-performance command-line toolkit for working with CSV data, written in Rust by Andrew Gallant (the creator of ripgrep). It provides a suite of subcommands for common CSV operations: cat (concatenation), count, fixlengths, flatten, fmt (formatting), frequency, headers, index, input, join, partition, sample, reverse, search, select, shuffle, slice, sort, split, stats, and table display.
What makes xsv stand out is its raw speed. By leveraging Rust and the csv crate (also authored by Gallant), xsv can process multi-gigabyte CSV files in seconds. The indexing feature creates a secondary index that allows random access into a CSV file, enabling fast slicing, sampling, and counting operations on large datasets without reading the entire file into memory.
The tool supports powerful join operations between CSV files using inner, outer, left, right, and cross joins. Its frequency command generates frequency tables for column values, and the stats command computes summary statistics including mean, median, mode, standard deviation, min, max, and cardinality. The search subcommand supports regex filtering across columns, and select allows column selection and reordering using column names or indices.
xsv excels as a building block in Unix-style data pipelines. You can chain multiple xsv commands together, or combine them with tools like jq, sort, and awk. It reads from stdin and writes to stdout by default, making it easy to integrate into shell scripts and automation workflows. With over 10,700 GitHub stars, xsv is one of the most popular data processing CLI tools. It is dual-licensed under MIT and the Unlicense.
Installation is available via cargo install xsv, Homebrew, and prebuilt binaries on the GitHub releases page for Linux, macOS, and Windows. While the repository is now archived, xsv remains widely used and its successor project qsv continues active development with additional features.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/xsv-high-performance-csv-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/xsv-high-performance-csv-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xsv-high-performance-csv-toolkit/)
