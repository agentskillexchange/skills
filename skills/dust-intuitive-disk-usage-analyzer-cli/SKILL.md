---
title: "dust Intuitive Disk Usage Analyzer CLI"
description: "A more intuitive version of the du command, written in Rust. dust instantly visualizes which directories consume the most disk space using colored proportional bars and smart recursive depth."
slug: "dust-intuitive-disk-usage-analyzer-cli"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/bootandy/dust"
tool_ecosystem:
  github_repo: "bootandy/dust"
  github_stars: 11500
---

# dust Intuitive Disk Usage Analyzer CLI

A more intuitive version of the du command, written in Rust. dust instantly visualizes which directories consume the most disk space using colored proportional bars and smart recursive depth.

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
clawhub install dust-intuitive-disk-usage-analyzer-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

dust (du + rust) is a disk usage visualization tool created by Andy Boot that provides an instant, intuitive overview of which directories and files are consuming the most space. Published as du-dust on crates.io with over 11,000 GitHub stars, dust replaces the traditional du command with output that humans and agents can interpret at a glance, without needing to pipe through sort or head.
The tool automatically determines the optimal number of entries to display based on terminal height and recursively descends into directories to find the largest consumers. Its output uses proportional colored bars that visually indicate what percentage of the parent directory each entry occupies. The shading system uses different grays to show the tree hierarchy, so you can immediately see which subdirectories belong to which parent without needing to trace indentation levels.
For AI agents performing system maintenance, storage auditing, or cleanup tasks, dust provides actionable data without configuration. Running dust alone gives you the top space consumers in the current directory. The -d flag controls recursion depth, -D shows only directories, -F shows only files for finding the largest individual files, and -n controls how many entries to display. The -r flag reverses sort order for identifying the smallest entries, and -s shows apparent file size rather than disk usage.
dust is available across all major platforms: via cargo install, Homebrew, apt (snap), pacman, conda-forge, and direct binary downloads from GitHub releases. It supports both si units and binary prefixes, can filter to specific file extensions, and ignores hidden files by default. The tool prints at most one permission-denied warning, keeping output clean even when scanning directories with mixed access levels. For automated disk space triage, CI/CD artifact cleanup, or storage capacity planning, dust provides the fastest path from question to answer.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dust-intuitive-disk-usage-analyzer-cli/)
