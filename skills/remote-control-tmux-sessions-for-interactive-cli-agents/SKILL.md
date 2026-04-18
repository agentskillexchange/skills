---
title: Remote-control tmux sessions for interactive CLI agents
description: Lets an agent drive existing tmux sessions by sending keystrokes and
  scraping pane output, which is exactly what you need for interactive CLIs that cannot
  be handled as one-shot shell commands. Use it for session supervision and intervention,
  not for general terminal automation or starting new background jobs.
verification: security_reviewed
source: https://github.com/openclaw/skills/tree/main/skills/steipete/tmux
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Remote-control tmux sessions for interactive CLI agents

Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/remote-control-tmux-sessions-for-interactive-cli-agents
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/remote-control-tmux-sessions-for-interactive-cli-agents` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
