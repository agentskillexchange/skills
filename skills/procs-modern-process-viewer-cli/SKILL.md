---
title: "procs Modern Process Viewer CLI"
description: "A modern replacement for ps written in Rust. procs provides colorized, human-readable process listings with multi-column keyword search, TCP/UDP port display, Docker container names, and tree views."
slug: "procs-modern-process-viewer-cli"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/dalance/procs"
tool_ecosystem:
  github_repo: "dalance/procs"
  github_stars: 5994
---

# procs Modern Process Viewer CLI

A modern replacement for ps written in Rust. procs provides colorized, human-readable process listings with multi-column keyword search, TCP/UDP port display, Docker container names, and tree views.

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
clawhub install procs-modern-process-viewer-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

procs is a replacement for the ps command written in Rust by Daisuke Tanaka (dalance). With nearly 6,000 GitHub stars and published on crates.io, it reimagines process listing with colored output, automatic terminal background detection, and information columns that ps does not provide natively. The tool runs on Linux, macOS, Windows, and FreeBSD, making it a cross-platform process inspection utility.
The key advantage of procs over traditional ps is its default output format. Process lists are automatically colorized with human-readable formatting. The multi-column keyword search lets you type procs nginx to instantly filter processes by matching against both the USER and Command columns simultaneously. This is substantially more ergonomic than piping ps output through grep and trying to match column-aligned text.
procs provides several information columns that standard ps lacks. It can display the TCP and UDP ports each process is listening on, read and write throughput per process, Docker container names associated with each process, and detailed memory breakings including USS, PSS, and RSS. The tool also supports a tree view mode for visualizing parent-child process relationships and a watch mode that continuously refreshes the display like top.
Configuration is done via a TOML file that lets you define custom column sets, color schemes, and display preferences. For AI agents performing system diagnostics, container debugging, or resource monitoring, procs provides richer default output than ps without requiring complex flag combinations. The --sortd and --sorta flags allow sorting by any column in descending or ascending order. Installation is available via Homebrew, cargo, snap, pacman, dnf, scoop, and winget. The built-in pager support and configurable column widths make it suitable for both interactive use and automated process auditing workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/procs-modern-process-viewer-cli/)
