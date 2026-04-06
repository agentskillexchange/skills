---
name: xan SIMD-Powered CSV Processing and Analysis CLI
description: xan is a high-performance command-line tool for processing CSV files,
  written in Rust with a novel SIMD CSV parser. It offers filtering, slicing, aggregation,
  sorting, joining, and visualization of CSV data, with its own expression language
  for complex transformations and support for adjacent data formats.
category: "Data Extraction &amp; Transformation"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/medialab/xan"
tool_ecosystem:
  github_repo: "https://github.com/medialab/xan"
  github_stars: 3880
---
# xan SIMD-Powered CSV Processing and Analysis CLI

xan is a high-performance command-line tool for processing CSV files, written in Rust with a novel SIMD CSV parser. It offers filtering, slicing, aggregation, sorting, joining, and visualization of CSV data, with its own expression language for complex transformations and support for adjacent data formats.

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

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill xan-simd-csv-processing-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill xan-simd-csv-processing-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill xan-simd-csv-processing-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill xan-simd-csv-processing-cli -a codex
```

### OpenClaw

```bash
clawhub install xan-simd-csv-processing-cli
```


## Source

- [GitHub](https://github.com/medialab/xan)
