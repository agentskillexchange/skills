---
name: Sentry Issue Spike Detection Agent
description: Analyzes Sentry project event streams via the Sentry Issues API to detect
  sudden spikes in error frequency. Computes rolling baselines and triggers alerts
  through configurable notification channels.
category: Monitoring & Alerts
framework: Claude Agents
verification: security_reviewed
source: https://github.com/getsentry/sentry
tool_ecosystem:
  github_repo: getsentry/sentry
  github_stars: 43486
  tool: sentry
---
# Sentry Issue Spike Detection Agent
Analyzes Sentry project event streams via the Sentry Issues API to detect sudden spikes in error frequency. Computes rolling baselines and triggers alerts through configurable notification channels.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sentry-issue-spike-detection-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sentry-issue-spike-detection-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/)
