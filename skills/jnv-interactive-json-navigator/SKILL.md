---
title: jnv Interactive JSON Navigator and jq Filter Editor
description: jnv is an open-source interactive terminal tool for navigating JSON data
  and building jq filter expressions. Written in Rust, it combines a JSON viewer with
  a live filter editor, letting developers explore nested data structures and prototype
  jq queries without switching between tools or running commands repeatedly. The tool
  accepts JSON input from files or standard input and renders it with syntax highlighting
  in a navigable tree view. As the user types a jq filter expression in the editor
  pane, jnv evaluates it in real time and displays the filtered output immediately.
  This feedback loop makes it faster to develop correct jq queries compared to the
  traditional cycle of editing a command, running it, and inspecting the output. jnv
  uses jaq (a Rust reimplementation of jq) as its filter engine, which means no external
  jq installation is required. The auto-completion system supports identity expressions,
  object identifier-index access, and array indexing, suggesting valid paths based
  on the actual data structure. Users can copy either the current jq filter or the
  filtered JSON output to their clipboard with keyboard shortcuts. The interface supports
  multiple input formats including standard JSON files and JSON Lines (newline-delimited
  JSON). Configuration is handled through a TOML file where developers can customize
  the UI appearance, adjust debounce timing for filter evaluation, configure editor
  behavior, and remap keybindings to match their preferences. Installation is available
  through Homebrew, MacPorts, Nix, Conda, Cargo, and Docker. The tool also supports
  writing filtered results to stdout on exit via --write-to-stdout , making it usable
  as part of shell pipelines where a developer needs to interactively select the right
  jq expression before piping the result to another command.
verification: security_reviewed
source: https://github.com/ynqa/jnv
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
tool_ecosystem:
  github_repo: ynqa/jnv
  github_stars: 5979
---

# jnv Interactive JSON Navigator and jq Filter Editor

jnv is an open-source interactive terminal tool for navigating JSON data and building jq filter expressions. Written in Rust, it combines a JSON viewer with a live filter editor, letting developers explore nested data structures and prototype jq queries without switching between tools or running commands repeatedly. The tool accepts JSON input from files or standard input and renders it with syntax highlighting in a navigable tree view. As the user types a jq filter expression in the editor pane, jnv evaluates it in real time and displays the filtered output immediately. This feedback loop makes it faster to develop correct jq queries compared to the traditional cycle of editing a command, running it, and inspecting the output. jnv uses jaq (a Rust reimplementation of jq) as its filter engine, which means no external jq installation is required. The auto-completion system supports identity expressions, object identifier-index access, and array indexing, suggesting valid paths based on the actual data structure. Users can copy either the current jq filter or the filtered JSON output to their clipboard with keyboard shortcuts. The interface supports multiple input formats including standard JSON files and JSON Lines (newline-delimited JSON). Configuration is handled through a TOML file where developers can customize the UI appearance, adjust debounce timing for filter evaluation, configure editor behavior, and remap keybindings to match their preferences. Installation is available through Homebrew, MacPorts, Nix, Conda, Cargo, and Docker. The tool also supports writing filtered results to stdout on exit via --write-to-stdout , making it usable as part of shell pipelines where a developer needs to interactively select the right jq expression before piping the result to another command.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jnv-interactive-json-navigator/)
