---
title: xsv High-Performance CSV Toolkit
description: 'xsv is a high-performance command-line toolkit for working with CSV
  data, written in Rust by Andrew Gallant (the creator of ripgrep). It provides a
  suite of subcommands for common CSV operations: cat (concatenation), count, fixlengths,
  flatten, fmt (formatting), frequency, headers, index, input, join, partition, sample,
  reverse, search, select, shuffle, slice, sort, split, stats, and table display.
  What makes xsv stand out is its raw speed. By leveraging Rust and the csv crate
  (also authored by Gallant), xsv can process multi-gigabyte CSV files in seconds.
  The indexing feature creates a secondary index that allows random access into a
  CSV file, enabling fast slicing, sampling, and counting operations on large datasets
  without reading the entire file into memory. The tool supports powerful join operations
  between CSV files using inner, outer, left, right, and cross joins. Its frequency
  command generates frequency tables for column values, and the stats command computes
  summary statistics including mean, median, mode, standard deviation, min, max, and
  cardinality. The search subcommand supports regex filtering across columns, and
  select allows column selection and reordering using column names or indices. xsv
  excels as a building block in Unix-style data pipelines. You can chain multiple
  xsv commands together, or combine them with tools like jq, sort, and awk. It reads
  from stdin and writes to stdout by default, making it easy to integrate into shell
  scripts and automation workflows. With over 10,700 GitHub stars, xsv is one of the
  most popular data processing CLI tools. It is dual-licensed under MIT and the Unlicense.
  Installation is available via cargo install xsv, Homebrew, and prebuilt binaries
  on the GitHub releases page for Linux, macOS, and Windows. While the repository
  is now archived, xsv remains widely used and its successor project qsv continues
  active development with additional features.'
verification: security_reviewed
source: https://github.com/BurntSushi/xsv
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
tool_ecosystem:
  github_repo: BurntSushi/xsv
  github_stars: 10758
---

# xsv High-Performance CSV Toolkit

xsv is a high-performance command-line toolkit for working with CSV data, written in Rust by Andrew Gallant (the creator of ripgrep). It provides a suite of subcommands for common CSV operations: cat (concatenation), count, fixlengths, flatten, fmt (formatting), frequency, headers, index, input, join, partition, sample, reverse, search, select, shuffle, slice, sort, split, stats, and table display. What makes xsv stand out is its raw speed. By leveraging Rust and the csv crate (also authored by Gallant), xsv can process multi-gigabyte CSV files in seconds. The indexing feature creates a secondary index that allows random access into a CSV file, enabling fast slicing, sampling, and counting operations on large datasets without reading the entire file into memory. The tool supports powerful join operations between CSV files using inner, outer, left, right, and cross joins. Its frequency command generates frequency tables for column values, and the stats command computes summary statistics including mean, median, mode, standard deviation, min, max, and cardinality. The search subcommand supports regex filtering across columns, and select allows column selection and reordering using column names or indices. xsv excels as a building block in Unix-style data pipelines. You can chain multiple xsv commands together, or combine them with tools like jq, sort, and awk. It reads from stdin and writes to stdout by default, making it easy to integrate into shell scripts and automation workflows. With over 10,700 GitHub stars, xsv is one of the most popular data processing CLI tools. It is dual-licensed under MIT and the Unlicense. Installation is available via cargo install xsv, Homebrew, and prebuilt binaries on the GitHub releases page for Linux, macOS, and Windows. While the repository is now archived, xsv remains widely used and its successor project qsv continues active development with additional features.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xsv-high-performance-csv-toolkit/)
