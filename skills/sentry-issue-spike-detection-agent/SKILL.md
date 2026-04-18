---
title: "Sentry Issue Spike Detection Agent"
description: "Analyzes Sentry project event streams via the Sentry Issues API to detect sudden spikes in error frequency. Computes rolling baselines and triggers alerts through configurable notification channels."
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43486
---

# Sentry Issue Spike Detection Agent

The Sentry Issue Spike Detection Agent connects to your Sentry organization using the Sentry Web API and continuously monitors issue event frequency across projects. It fetches recent events via the /api/0/organizations/{org}/issues/ endpoint with statsperiod and query parameters, computing rolling averages and standard deviations over configurable windows. When event frequency exceeds the baseline by a configurable multiplier, the agent classifies it as a spike and generates a structured alert containing the issue title, stack trace summary, affected users count, and first/last seen timestamps. Alerts can be routed to Slack via the Slack Web API, email via SMTP, or custom webhooks. The agent also groups related spikes using Sentry’s issue grouping metadata and suppresses duplicate notifications within a cooldown period. It supports Sentry DSN-based project filtering and can query the Sentry Releases API to correlate spikes with recent deployments.

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
