---
title: "procs Modern Process Viewer CLI"
description: "A modern replacement for ps written in Rust. procs provides colorized, human-readable process listings with multi-column keyword search, TCP/UDP port display, Docker container names, and tree views."
verification: security_reviewed
source: "https://github.com/dalance/procs"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "dalance/procs"
  github_stars: 5994
---

# procs Modern Process Viewer CLI

procs is a replacement for the ps command written in Rust by Daisuke Tanaka (dalance). With nearly 6,000 GitHub stars and published on crates.io, it reimagines process listing with colored output, automatic terminal background detection, and information columns that ps does not provide natively. The tool runs on Linux, macOS, Windows, and FreeBSD, making it a cross-platform process inspection utility.

The key advantage of procs over traditional ps is its default output format. Process lists are automatically colorized with human-readable formatting. The multi-column keyword search lets you type procs nginx to instantly filter processes by matching against both the USER and Command columns simultaneously. This is substantially more ergonomic than piping ps output through grep and trying to match column-aligned text.

procs provides several information columns that standard ps lacks. It can display the TCP and UDP ports each process is listening on, read and write throughput per process, Docker container names associated with each process, and detailed memory breakings including USS, PSS, and RSS. The tool also supports a tree view mode for visualizing parent-child process relationships and a watch mode that continuously refreshes the display like top.

Configuration is done via a TOML file that lets you define custom column sets, color schemes, and display preferences. For AI agents performing system diagnostics, container debugging, or resource monitoring, procs provides richer default output than ps without requiring complex flag combinations. The --sortd and --sorta flags allow sorting by any column in descending or ascending order. Installation is available via Homebrew, cargo, snap, pacman, dnf, scoop, and winget. The built-in pager support and configurable column widths make it suitable for both interactive use and automated process auditing workflows.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/procs-modern-process-viewer-cli/)
