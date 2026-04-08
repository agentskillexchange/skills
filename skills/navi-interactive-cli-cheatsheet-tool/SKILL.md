---
title: navi Interactive CLI Cheatsheet Tool
description: navi is an interactive command-line cheatsheet tool created by Denis
  Isidoro. It allows users to browse through predefined cheatsheets of shell commands,
  select the one they need via fuzzy search, and interactively fill in argument placeholders
  before executing. Instead of memorizing arcane command flags or searching documentation,
  users type navi and immediately get access to organized, searchable command references
  with guided parameter input. The navi Interactive CLI Cheatsheet Tool skill enables
  agents to leverage navi for generating and executing complex shell commands correctly.
  Cheatsheets are written in a simple text format where each entry has a description,
  the command template with named placeholders, and optional argument suggestions
  (including dynamic suggestions from shell commands). For example, a cheatsheet entry
  might describe “Kill process by name” with the command kill -9 $(pgrep ) , where
  <process_name> is filled interactively from ps aux output. navi integrates deeply
  with the shell environment. It supports Bash, Zsh, and Fish shell widget integration,
  allowing users to press a keybinding (typically Ctrl+G) to invoke navi inline within
  their current terminal session. The selected command is inserted directly into the
  shell prompt for review before execution. navi also supports a “best match” mode
  for non-interactive use, a TLDR pages integration for pulling community cheatsheets,
  and path-based cheatsheet organization for team-shared command libraries. Community-maintained
  cheatsheet repositories cover common tools like git, docker, kubectl, aws, and hundreds
  of other CLI tools. Users can fork and customize these repositories or create private
  ones. navi is written in Rust for fast startup and low memory usage, distributed
  under the Apache-2.0 license, and installable via Homebrew, cargo, apt, nix, and
  other package managers. With over 16,000 GitHub stars and recent commits in March
  2026, navi is actively maintained and widely adopted as a developer productivity
  tool for reducing command-line friction.
verification: security_reviewed
source: https://github.com/denisidoro/navi
category:
- Developer Tools
framework:
- Claude Code
tool_ecosystem:
  github_repo: denisidoro/navi
  github_stars: 16941
---

# navi Interactive CLI Cheatsheet Tool

navi is an interactive command-line cheatsheet tool created by Denis Isidoro. It allows users to browse through predefined cheatsheets of shell commands, select the one they need via fuzzy search, and interactively fill in argument placeholders before executing. Instead of memorizing arcane command flags or searching documentation, users type navi and immediately get access to organized, searchable command references with guided parameter input. The navi Interactive CLI Cheatsheet Tool skill enables agents to leverage navi for generating and executing complex shell commands correctly. Cheatsheets are written in a simple text format where each entry has a description, the command template with named placeholders, and optional argument suggestions (including dynamic suggestions from shell commands). For example, a cheatsheet entry might describe “Kill process by name” with the command kill -9 $(pgrep ) , where <process_name> is filled interactively from ps aux output. navi integrates deeply with the shell environment. It supports Bash, Zsh, and Fish shell widget integration, allowing users to press a keybinding (typically Ctrl+G) to invoke navi inline within their current terminal session. The selected command is inserted directly into the shell prompt for review before execution. navi also supports a “best match” mode for non-interactive use, a TLDR pages integration for pulling community cheatsheets, and path-based cheatsheet organization for team-shared command libraries. Community-maintained cheatsheet repositories cover common tools like git, docker, kubectl, aws, and hundreds of other CLI tools. Users can fork and customize these repositories or create private ones. navi is written in Rust for fast startup and low memory usage, distributed under the Apache-2.0 license, and installable via Homebrew, cargo, apt, nix, and other package managers. With over 16,000 GitHub stars and recent commits in March 2026, navi is actively maintained and widely adopted as a developer productivity tool for reducing command-line friction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/navi-interactive-cli-cheatsheet-tool/)
