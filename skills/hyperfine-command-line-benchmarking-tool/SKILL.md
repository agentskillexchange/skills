---
title: "Hyperfine Command-Line Benchmarking Tool"
description: "Benchmark command-line programs with statistical rigor using Hyperfine. Performs warmup runs, detects outliers, exports results in JSON/CSV/Markdown, and supports parameterized benchmarks for comparison."
verification: "security_reviewed"
source: "https://github.com/sharkdp/hyperfine"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sharkdp/hyperfine"
  github_stars: 27797
---

# Hyperfine Command-Line Benchmarking Tool

The Hyperfine Command-Line Benchmarking Tool skill uses sharkdp/hyperfine, a command-line utility for benchmarking programs with statistical analysis. With over 23,000 GitHub stars, Hyperfine is the standard tool developers and agent workflows use to measure and compare the performance of CLI commands, scripts, and compiled programs.

Hyperfine runs a command multiple times, collects timing data, and reports the mean, standard deviation, median, min, and max execution times. It automatically detects statistical outliers and warns when results may be unreliable. Warmup runs can be configured with --warmup N to ensure caches are populated before measurement begins. A preparation command (--prepare) runs before each timing iteration, useful for clearing caches or resetting state to ensure fair measurement.

Comparative benchmarking is where Hyperfine shines. Running hyperfine 'fd pattern' 'find . -name pattern' benchmarks both commands and produces a side-by-side comparison showing which is faster and by what factor. Parameterized benchmarks use --parameter-scan or --parameter-list to sweep across values, producing a matrix of results—for example, benchmarking a compression tool across different block sizes or thread counts.

Results export to JSON, CSV, Markdown, and AsciiDoc formats. The included Python scripts in the repository generate visualizations: histograms of individual run times, whisker plots comparing multiple benchmarks, and bar charts with confidence intervals. The JSON output includes all individual timing samples, enabling custom post-processing and integration with dashboards or CI performance tracking.

Setup and cleanup commands bracket the entire benchmark session. The --shell flag controls which shell interprets commands (or --shell=none for direct execution without shell overhead). The --min-runs and --max-runs flags control sample size. Hyperfine is written in Rust, distributed via apt, brew, cargo, conda, and direct binary download, and dual-licensed under Apache 2.0 and MIT. For any agent that needs to measure performance—comparing tool versions, validating optimization work, or profiling build times—Hyperfine provides rigorous, reproducible measurements.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hyperfine-command-line-benchmarking-tool/)
