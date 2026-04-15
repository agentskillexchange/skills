---
title: "Triage production log spikes and incidents from the terminal with lnav"
description: "Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform."
verification: listed
source: "https://github.com/tstack/lnav"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tstack/lnav"
  github_stars: 10159
---

# Triage production log spikes and incidents from the terminal with lnav

Use lnav when an agent needs to investigate raw log files during an incident instead of guessing from `tail` output. The agent can open mixed log sources, pivot on structured fields, jump straight to error bursts, and summarize what changed around the spike. The scope is terminal-first incident triage on existing logs, not generic observability hosting or log-platform administration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav/)
