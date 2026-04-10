---
title: "mcfly Intelligent Shell History Search with Neural Network"
description: "mcfly is a Rust-based shell history search tool that uses a small neural network to prioritize commands based on context. It replaces Ctrl+R with an intelligent full-screen search interface that considers your current directory, recent commands, and command exit status."
slug: "mcfly-intelligent-shell-history-search"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/cantino/mcfly"
tool_ecosystem:
  github_repo: "cantino/mcfly"
  github_stars: 7657
---

# mcfly Intelligent Shell History Search with Neural Network

mcfly is a Rust-based shell history search tool that uses a small neural network to prioritize commands based on context. It replaces Ctrl+R with an intelligent full-screen search interface that considers your current directory, recent commands, and command exit status.

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
clawhub install mcfly-intelligent-shell-history-search
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
mcfly is a replacement for the default Ctrl+R shell history search, written in Rust. Unlike basic reverse-search or even tools like Atuin that focus on sync and storage, mcfly uses a small neural network trained on your usage patterns to intelligently rank and suggest commands based on the current context — your working directory, what commands you have run recently, and the historical exit status of commands.
Key Features
- Neural Network Ranking: mcfly prioritizes history results using a small neural network that considers the current working directory, the commands you have run recently, and whether commands succeeded or failed historically.
- Full-Screen Interface: A full-screen terminal UI replaces the single-line Ctrl+R interface, showing multiple candidates at once with syntax highlighting.
- Context-Aware Suggestions: Commands are ranked higher if they were previously run in the same directory or after the same preceding command, surfacing the most relevant history.
- Exit Status Tracking: mcfly tracks whether commands succeeded or failed, deprioritizing commands that historically produced errors.
- SQLite Backend: History is stored in a SQLite database, providing fast queries and durable storage beyond the default shell history file limits.
- Scrubbing Mode: Delete commands from history with a single keypress to remove sensitive entries like passwords accidentally typed in commands.
How It Works
An agent skill wrapping mcfly allows AI agents to intelligently search and suggest shell commands from the user’s history. Instead of generic command suggestions, the agent can query mcfly’s ranked results to find the most contextually appropriate command for the current situation — the right build command for the current project directory, the specific SSH command used previously, or the correct deployment script.
Technical Details
mcfly is written in Rust and installs as a single binary via cargo install mcfly, Homebrew, or system package managers. It supports Bash, Zsh, and Fish shells. The neural network model is lightweight and runs locally with no external API calls. mcfly is released under the MIT license with over 7,600 GitHub stars and active development. The SQLite database typically resides at ~/.mcfly/history.db.
Integration Points
- Shell initialization via eval/source for Bash, Zsh, and Fish
- SQLite database queryable for programmatic history analysis
- Environment variables for customizing behavior (MCFLY_RESULTS, MCFLY_FUZZY, MCFLY_KEY_SCHEME)
- Works alongside other shell enhancements without conflicts

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mcfly-intelligent-shell-history-search/)
