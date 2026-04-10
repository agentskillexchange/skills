---
title: "xan SIMD-Powered CSV Processing and Analysis CLI"
description: "xan is a high-performance command-line tool for processing CSV files, written in Rust with a novel SIMD CSV parser. It offers filtering, slicing, aggregation, sorting, joining, and visualization of CSV data, with its own expression language for complex transformations and support for adjacent data formats."
slug: "xan-simd-csv-processing-cli"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/medialab/xan"
tool_ecosystem:
  github_repo: "medialab/xan"
  github_stars: 3882
listed: true
---

# xan SIMD-Powered CSV Processing and Analysis CLI

xan is a high-performance command-line tool for processing CSV files, written in Rust with a novel SIMD CSV parser. It offers filtering, slicing, aggregation, sorting, joining, and visualization of CSV data, with its own expression language for complex transformations and support for adjacent data formats.

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
clawhub install xan-simd-csv-processing-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

xan is a command-line tool for processing CSV files directly from the shell, written in Rust with a focus on speed and memory efficiency. Originally a fork of BurntSushi’s xsv, xan has been nearly entirely rewritten by SciencesPo’s médialab to handle web data collection and social science analysis workloads.
Core Architecture
xan leverages a novel SIMD (Single Instruction, Multiple Data) CSV parser built on the simd-csv Rust crate, enabling it to process large CSV files (multiple gigabytes) with minimal memory consumption. It supports multithreaded parallel computation for tasks like frequency analysis, statistics, and sorting, making full use of available CPU cores.
Expression Language
xan includes its own minimalistic expression language tailored for CSV data manipulation. This language is significantly faster than dynamically-typed alternatives like Python or JavaScript for CSV operations, enabling inline column transformations, conditional filtering, and computed field generation without leaving the shell pipeline.
Key Capabilities
The tool provides a comprehensive suite of CSV operations: view and flatten for terminal display, filter and search for row selection, select and transform for column manipulation, sort and dedup for ordering, groupby and agg for aggregation, join for combining datasets, and stats and frequency for analysis. It also includes histogram, scatter, and heatmap commands for terminal-based data visualization.
Format Support
Beyond standard CSV, xan handles CSV-adjacent formats from domains like web archival (.cdx), bioinformatics (.vcf, .gtf, .sam, .bed), and can convert to and from JSON, Excel, numpy arrays, and Parquet files using the xan to and xan from commands. It also supports compressed file input (gzip, bzip2, xz, zstd).
Integration Points
xan is designed for Unix pipeline composition, reading from stdin and writing to stdout by default. It installs via cargo (Rust), Homebrew, Scoop, pacman, conda-forge, Nix, or pre-built binaries. Shell completions for bash, zsh, and fish are available via the xan completions command. The tool integrates naturally with other CLI utilities like jq, ripgrep, and standard Unix tools for end-to-end data processing workflows.
Installation
cargo install xan --locked
brew install xan
conda install conda-forge::xan

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xan-simd-csv-processing-cli/)
