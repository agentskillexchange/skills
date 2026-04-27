---
title: "Remote-control tmux sessions for interactive CLI agents"
description: "Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs."
verification: "security_reviewed"
source: "https://github.com/openclaw/skills/tree/main/skills/steipete/tmux"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/skills"
  github_stars: 4086
---

# Remote-control tmux sessions for interactive CLI agents

Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/remote-control-tmux-sessions-for-interactive-cli-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/remote-control-tmux-sessions-for-interactive-cli-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
