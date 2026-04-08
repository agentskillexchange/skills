---
title: duf Modern Disk Usage and Free Utility
description: 'Overview duf (Disk Usage/Free) is a modern replacement for the classic
  df command, written in Go. While df outputs raw, hard-to-read columns, duf presents
  filesystem information in a clean, colorful table with progress bars, grouped by
  device type (local, network, special/virtual), and with human-readable sizes by
  default. Key Features Beautiful Terminal Output: duf formats disk usage information
  in colorful tables with Unicode progress bars showing percentage used, making it
  immediately readable at a glance. Smart Grouping: Filesystems are automatically
  grouped into categories — local devices, network volumes, and FUSE/special mounts
  — reducing clutter from pseudo-filesystems. JSON Output: Full JSON output mode (
  duf --json ) for programmatic consumption, making it easy for agents and scripts
  to parse filesystem data. Filtering: Filter displayed filesystems by type, mount
  point, or device path. Show only specific filesystem types or hide types you do
  not care about. Sorting: Sort output by any column — size, used space, available
  space, usage percentage, filesystem type, or mount point. Cross-Platform: Works
  on Linux, macOS, Windows, FreeBSD, and other platforms with consistent output formatting.
  How It Works A skill wrapping duf enables AI agents to quickly assess disk space
  across all mounted volumes on a system. The agent invokes duf --json to get structured
  data about every filesystem, including total size, used space, available space,
  and mount points. This is essential for diagnostic runbooks, deployment checks,
  and system monitoring tasks where the agent needs to verify sufficient disk space
  before proceeding. Technical Details duf is written in Go and distributed as a single
  binary. It can be installed via Homebrew ( brew install duf ), package managers,
  or downloaded from GitHub releases. The tool reads filesystem information from the
  operating system’s mount tables. It is released under an open-source license with
  nearly 15,000 GitHub stars. The binary is small, fast, and has zero runtime dependencies.
  Integration Points JSON output for structured data parsing by agents and scripts
  Configurable columns and sort order via command-line flags Theme support for different
  terminal color schemes CI/CD integration for pre-deployment disk space checks'
verification: security_reviewed
source: https://github.com/muesli/duf
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: muesli/duf
  github_stars: 14916
---

# duf Modern Disk Usage and Free Utility

Overview duf (Disk Usage/Free) is a modern replacement for the classic df command, written in Go. While df outputs raw, hard-to-read columns, duf presents filesystem information in a clean, colorful table with progress bars, grouped by device type (local, network, special/virtual), and with human-readable sizes by default. Key Features Beautiful Terminal Output: duf formats disk usage information in colorful tables with Unicode progress bars showing percentage used, making it immediately readable at a glance. Smart Grouping: Filesystems are automatically grouped into categories — local devices, network volumes, and FUSE/special mounts — reducing clutter from pseudo-filesystems. JSON Output: Full JSON output mode ( duf --json ) for programmatic consumption, making it easy for agents and scripts to parse filesystem data. Filtering: Filter displayed filesystems by type, mount point, or device path. Show only specific filesystem types or hide types you do not care about. Sorting: Sort output by any column — size, used space, available space, usage percentage, filesystem type, or mount point. Cross-Platform: Works on Linux, macOS, Windows, FreeBSD, and other platforms with consistent output formatting. How It Works A skill wrapping duf enables AI agents to quickly assess disk space across all mounted volumes on a system. The agent invokes duf --json to get structured data about every filesystem, including total size, used space, available space, and mount points. This is essential for diagnostic runbooks, deployment checks, and system monitoring tasks where the agent needs to verify sufficient disk space before proceeding. Technical Details duf is written in Go and distributed as a single binary. It can be installed via Homebrew ( brew install duf ), package managers, or downloaded from GitHub releases. The tool reads filesystem information from the operating system’s mount tables. It is released under an open-source license with nearly 15,000 GitHub stars. The binary is small, fast, and has zero runtime dependencies. Integration Points JSON output for structured data parsing by agents and scripts Configurable columns and sort order via command-line flags Theme support for different terminal color schemes CI/CD integration for pre-deployment disk space checks

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/duf-modern-disk-usage-free-utility/)
