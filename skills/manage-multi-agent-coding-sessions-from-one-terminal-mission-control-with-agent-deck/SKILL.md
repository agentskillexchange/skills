---
name: "Manage multi-agent coding sessions from one terminal mission control with Agent Deck"
slug: "manage-multi-agent-coding-sessions-from-one-terminal-mission-control-with-agent-deck"
description: "Use Agent Deck when an operator needs one keyboard-first terminal to monitor, switch, fork, sandbox, and organize many coding-agent sessions instead of juggling tabs, panes, and worktrees by hand."
github_stars: 2027
verification: "security_reviewed"
source: "https://github.com/asheshgoplani/agent-deck"
author: "Ashesh Goplani"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "asheshgoplani/agent-deck"
  github_stars: 2027
---

# Manage multi-agent coding sessions from one terminal mission control with Agent Deck

Use Agent Deck when an operator needs one keyboard-first terminal to monitor, switch, fork, sandbox, and organize many coding-agent sessions instead of juggling tabs, panes, and worktrees by hand.

## Prerequisites

Agent Deck, tmux-compatible terminal, one or more supported coding agents such as Claude Code, Codex, Gemini CLI, or OpenCode

## Installation

Use the upstream install or setup path that matches your environment:
- brew install asheshgoplani/tap/agent-deck
- go install github.com/asheshgoplani/agent-deck/cmd/agent-deck@latest
- git clone https://github.com/asheshgoplani/agent-deck.git && cd agent-deck && make install
- Homebrew install: run brew upgrade asheshgoplani/tap/agent-deck.

Requirements and caveats from upstream:
- **New worktree location** depends on the layout:
- ### Docker Sandbox
- Run sessions inside isolated Docker containers. The project directory is bind-mounted read-write, so agents work on your code while the rest of the system stays protected.

Basic usage or getting-started notes:
- [Features](#features) . [Conductor](#conductor) . [Install](#installation) . [Quick Start](#quick-start) . [Docs](#documentation) . [Discord](https://discord.gg/e4xSs6NBN8) . [FAQ](#faq)
- Agent Deck supports per-group CLAUDE_CONFIG_DIR and env_file overrides. Useful when a single profile hosts groups that should authenticate against different Claude accounts — for example, a personal profile hosting a...
- Running many sessions? Socket pooling shares MCP processes across all sessions via Unix sockets, reducing MCP memory usage by 85-90%. Connections auto-recover from MCP crashes in ~3 seconds via a reconnecting proxy. E...

- Source: https://github.com/asheshgoplani/agent-deck
- Extracted from upstream docs: https://raw.githubusercontent.com/asheshgoplani/agent-deck/HEAD/README.md

## Documentation

- https://github.com/asheshgoplani/agent-deck

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/manage-multi-agent-coding-sessions-from-one-terminal-mission-control-with-agent-deck/)
