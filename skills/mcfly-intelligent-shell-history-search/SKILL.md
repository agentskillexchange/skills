---
name: "mcfly Intelligent Shell History Search with Neural Network"
slug: "mcfly-intelligent-shell-history-search"
description: "mcfly is a Rust-based shell history search tool that uses a small neural network to prioritize commands based on context. It replaces Ctrl+R with an intelligent full-screen search interface that considers your current directory, recent commands, and command exit status."
github_stars: 7657
verification: "security_reviewed"
source: "https://github.com/cantino/mcfly"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "cantino/mcfly"
  github_stars: 7657
---

# mcfly Intelligent Shell History Search with Neural Network

mcfly is a Rust-based shell history search tool that uses a small neural network to prioritize commands based on context. It replaces Ctrl+R with an intelligent full-screen search interface that considers your current directory, recent commands, and command exit status.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install mcfly
- brew uninstall mcfly
- Run git clone https://github.com/cantino/mcfly and cd mcfly
- Run cargo install --path .

Requirements and caveats from upstream:
- time units **must** accompany all time span values.

Basic usage or getting-started notes:
- in real time. The goal is for the command you want to run to always be one of the top suggestions.
- The directory where you ran the command. You're likely to run that command in the same directory in the future.
- How often you run the command.

- Source: https://github.com/cantino/mcfly
- Extracted from upstream docs: https://raw.githubusercontent.com/cantino/mcfly/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mcfly-intelligent-shell-history-search/)
