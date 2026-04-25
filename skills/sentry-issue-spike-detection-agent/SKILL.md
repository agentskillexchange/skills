---
title: "Sentry Issue Spike Detection Agent"
description: "Analyzes Sentry project event streams via the Sentry Issues API to detect sudden spikes in error frequency. Computes rolling baselines and triggers alerts through configurable notification channels."
verification: "security_reviewed"
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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sentry-issue-spike-detection-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sentry-issue-spike-detection-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/)
