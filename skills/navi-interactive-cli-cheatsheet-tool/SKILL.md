---
title: "navi Interactive CLI Cheatsheet Tool"
description: "An interactive cheatsheet tool for the command line that lets you browse through commands and fill in argument values. Written in Rust with fuzzy search, community-maintained cheatsheet repos, and shell integration."
slug: "navi-interactive-cli-cheatsheet-tool"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/denisidoro/navi"
tool_ecosystem:
  github_repo: "denisidoro/navi"
  github_stars: 16941
---

# navi Interactive CLI Cheatsheet Tool

An interactive cheatsheet tool for the command line that lets you browse through commands and fill in argument values. Written in Rust with fuzzy search, community-maintained cheatsheet repos, and shell integration.

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
clawhub install navi-interactive-cli-cheatsheet-tool
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

navi is an interactive command-line cheatsheet tool created by Denis Isidoro. It allows users to browse through predefined cheatsheets of shell commands, select the one they need via fuzzy search, and interactively fill in argument placeholders before executing. Instead of memorizing arcane command flags or searching documentation, users type navi and immediately get access to organized, searchable command references with guided parameter input.
The navi Interactive CLI Cheatsheet Tool skill enables agents to leverage navi for generating and executing complex shell commands correctly. Cheatsheets are written in a simple text format where each entry has a description, the command template with named placeholders, and optional argument suggestions (including dynamic suggestions from shell commands). For example, a cheatsheet entry might describe “Kill process by name” with the command kill -9 $(pgrep ), where <process_name> is filled interactively from ps aux output.
navi integrates deeply with the shell environment. It supports Bash, Zsh, and Fish shell widget integration, allowing users to press a keybinding (typically Ctrl+G) to invoke navi inline within their current terminal session. The selected command is inserted directly into the shell prompt for review before execution. navi also supports a “best match” mode for non-interactive use, a TLDR pages integration for pulling community cheatsheets, and path-based cheatsheet organization for team-shared command libraries.
Community-maintained cheatsheet repositories cover common tools like git, docker, kubectl, aws, and hundreds of other CLI tools. Users can fork and customize these repositories or create private ones. navi is written in Rust for fast startup and low memory usage, distributed under the Apache-2.0 license, and installable via Homebrew, cargo, apt, nix, and other package managers. With over 16,000 GitHub stars and recent commits in March 2026, navi is actively maintained and widely adopted as a developer productivity tool for reducing command-line friction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/navi-interactive-cli-cheatsheet-tool/)
